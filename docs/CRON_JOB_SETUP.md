\
# Crypto Forge Labs — Render + cron-job.org Scheduler Setup

Crypto Forge Labs uses **Render** to host the bot trigger service and
**cron-job.org** to call the bot on a schedule.

GitHub remains the home of the code, but GitHub Actions is **not**
used for automatic scheduling. The existing Actions workflows remain
available as manual fallbacks.

## Websites to use

- **Render:** https://render.com
  - Hosts the Crypto Forge Labs Python service.
  - Stores the bot's environment variables and secrets.
  - Gives you an `onrender.com` URL.

- **cron-job.org:** https://cron-job.org
  - Sends scheduled HTTPS POST requests to your Render service.
  - This replaces the automatic GitHub Actions cron schedules.

- **Hyperliquid:** https://app.hyperliquid.xyz
  - Source of truth for real positions, account equity, and fills.

## 1. Deploy the service on Render

1. Sign in to **Render**.
2. Choose **New → Web Service**.
3. Connect your own fork of:
   `https://github.com/Crypto-Forge-Labs/crypto-yall`
4. Use:
   - Build command: `pip install -r requirements.txt`
   - Start command:
     `gunicorn cron_server:app --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 120`
5. Add your environment variables under **Render → Environment**.
6. Add a new secret named:
   `CRON_SECRET`
7. Give `CRON_SECRET` a long random value that only you know.
   Do not paste it into an AI chat or public document.
8. Deploy the service.
9. Open:
   `https://YOUR-SERVICE.onrender.com/health`
10. You should see a small JSON response showing the service is OK.

## 2. Environment variables on Render

The executor scripts read their settings from environment variables.
When Render runs the bot, the required values therefore need to exist
in **Render**, not only in GitHub Secrets/Variables.

### Secret values

- `HL_PRIVATE_KEY`
- `HL_ACCOUNT_ADDRESS`
- `GIST_TOKEN`
- `GIST_ID`
- `TRADING_GIST_ID`
- `INTRADAY_GIST_ID`
- `AGGRESSIVE_GIST_ID`
- `GMAIL_USER`
- `GMAIL_APP_PASSWORD`
- `NOTIFY_EMAILS`
- `TELEGRAM_BOT_TOKEN` (if used)
- `TELEGRAM_CHAT_ID` (if used)
- `CRON_SECRET`

### Normal configuration values

Recommended testnet starting values:

- `HL_TESTNET=true`
- `SEGREGATED_CAPITAL=1000`
- `INTRADAY_CAPITAL=500`
- `AGGRESSIVE_CAPITAL=300`
- `DAILY_DD_PCT=5`
- `INTRADAY_DD_PCT=5`
- `AGGRESSIVE_DD_PCT=3`
- `MAX_POSITIONS=4`
- `INTRADAY_MAX_POSITIONS=2`
- `AGGRESSIVE_MAX_POSITIONS=4`
- `KILL_SWITCH=ON`
- `INTRADAY_KILL_SWITCH=ON`
- `AGGRESSIVE_KILL_SWITCH=ON`

Start on testnet.

## 3. Create the cron jobs on cron-job.org

Sign in at:

`https://cron-job.org`

Each job should use:

- Request method: **POST**
- URL: your Render URL plus the endpoint below
- Custom header:
  - Name: `X-Cron-Secret`
  - Value: exactly the same value as your Render `CRON_SECRET`

Do not put the secret in the URL.

## 4. Schedules

These schedules preserve the cadence used by the original repository,
but the requests now come from cron-job.org instead of GitHub Actions.

| Job | Render endpoint | Schedule |
|---|---|---|
| Daily | `/run/daily` | Every day at **00:15 UTC** |
| Intraday | `/run/intraday` | Every hour at **:05 UTC** |
| Aggressive | `/run/aggressive` | Every **30 minutes** |
| Signal alerts | `/run/signals` | Every **6 hours** |

Example, if Render gives you:

`https://crypto-forge-scheduler.onrender.com`

then the Daily URL is:

`https://crypto-forge-scheduler.onrender.com/run/daily`

and the Aggressive URL is:

`https://crypto-forge-scheduler.onrender.com/run/aggressive`

## 5. Test one endpoint

Before enabling all cron jobs:

1. Keep the trading kill switches set to `OFF`.
2. Run one cron job manually from cron-job.org.
3. Open the Render logs.
4. Confirm the request returned **202 Accepted**.
5. Confirm the bot started in the Render logs.
6. Confirm no secret values or full wallet address were printed.
7. Only enable normal scheduling after the test is clean.

## 6. Important: avoid duplicate scheduling

Do **not** leave GitHub Actions schedules enabled at the same time as
cron-job.org.

In GitHub → Actions, keep these four workflows **Disabled** while
cron-job.org is running the scheduler:

- Execute Trades
- Execute Intraday
- Execute Aggressive
- Check Signals

The Test Trade workflow can remain available for manual testing.

## 7. Checking whether it is alive

Health check:

`https://YOUR-SERVICE.onrender.com/health`

Job status examples:

`https://YOUR-SERVICE.onrender.com/status/daily`

`https://YOUR-SERVICE.onrender.com/status/aggressive`

The status endpoints also require the `X-Cron-Secret` header.

## Security

- Never commit `CRON_SECRET` to GitHub.
- Never commit Hyperliquid private keys.
- Keep all credentials in Render's Environment settings.
- Use a different `CRON_SECRET` if you think the old one was exposed.
- Keep the three kill switches available as emergency controls.
- Hyperliquid itself is the source of truth for open positions.

---

*Crypto Forge Labs scheduler guide — August 2026*
