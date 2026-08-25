import hmac
import os
import subprocess
import sys
import threading
from datetime import datetime, timezone

from flask import Flask, jsonify, request

app = Flask(__name__)

JOBS = {
    "daily": "hyperliquid_executor.py",
    "intraday": "intraday_executor.py",
    "aggressive": "aggressive_executor.py",
    "signals": "notifier.py",
    "test-trade": "test_trade.py",
}

locks = {name: threading.Lock() for name in JOBS}
status = {
    name: {
        "running": False,
        "last_started": None,
        "last_finished": None,
        "last_exit_code": None,
    }
    for name in JOBS
}


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def authorized():
    expected = os.environ.get("CRON_SECRET", "")
    supplied = request.headers.get("X-Cron-Secret", "")
    if not expected:
        return False
    return hmac.compare_digest(supplied, expected)


def run_job(name):
    lock = locks[name]
    if not lock.acquire(blocking=False):
        print(f"[{name}] skipped: job already running", flush=True)
        return

    try:
        status[name]["running"] = True
        status[name]["last_started"] = utc_now()
        print(f"[{name}] started at {status[name]['last_started']}", flush=True)

        result = subprocess.run(
            [sys.executable, JOBS[name]],
            env=os.environ.copy(),
            check=False,
            timeout=60 * 20,
        )

        status[name]["last_exit_code"] = result.returncode
        print(f"[{name}] finished with exit code {result.returncode}", flush=True)

    except subprocess.TimeoutExpired:
        status[name]["last_exit_code"] = 124
        print(f"[{name}] timed out after 20 minutes", flush=True)

    except Exception as exc:
        status[name]["last_exit_code"] = 1
        print(f"[{name}] failed: {exc}", flush=True)

    finally:
        status[name]["running"] = False
        status[name]["last_finished"] = utc_now()
        lock.release()


@app.get("/")
@app.get("/health")
def health():
    return jsonify(
        service="Crypto Forge Labs scheduler",
        status="ok",
        scheduler="cron-job.org",
    )


@app.post("/run/<name>")
def trigger(name):
    if name not in JOBS:
        return jsonify(error="Unknown job"), 404

    if not authorized():
        return jsonify(error="Unauthorized"), 401

    if locks[name].locked():
        return jsonify(
            status="already-running",
            job=name,
        ), 409

    thread = threading.Thread(
        target=run_job,
        args=(name,),
        daemon=True,
        name=f"crypto-forge-{name}",
    )
    thread.start()

    return jsonify(
        status="accepted",
        job=name,
        started=utc_now(),
    ), 202


@app.get("/status/<name>")
def job_status(name):
    if name not in JOBS:
        return jsonify(error="Unknown job"), 404

    if not authorized():
        return jsonify(error="Unauthorized"), 401

    return jsonify(job=name, **status[name])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
