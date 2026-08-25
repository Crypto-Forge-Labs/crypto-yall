# Troubleshooting Guide (For Non-Technical Users)

Things sometimes go wrong. This guide shows you how to identify common problems and recover safely without guessing.

> **Project note:** Crypto Forge Labs is based on the upstream `aicodepathways/crypto-yall` project. This troubleshooting guide assumes you are running your own fork, your own Hyperliquid account, and your own credentials.

---

## Step 1: When Something Looks Wrong

Before changing settings:

1. Check which bot or workflow is affected.
2. Open the latest GitHub Actions run and read the error message.
3. Check Hyperliquid directly to confirm your actual positions and account equity.
4. If you are unsure what is happening, set the affected bot's kill switch to **OFF** before making other changes.

Avoid:
- Trying random fixes
- Posting private keys, passwords, seed phrases, or tokens in screenshots or chats
- Editing Gist contents unless you understand what the change will do
- Assuming a dashboard is more authoritative than Hyperliquid itself

The exchange is the source of truth for actual positions and account equity.

---

## Common Issue 1: "I Stopped Getting Trade Alerts"

### Possible cause A: The market is quiet

The bots only place trades when their strategy conditions are met.

A quiet period can last hours or days. No trade alerts does **not** automatically mean the bot is broken.

### How to verify

1. Open your GitHub Actions page:
   `https://github.com/<your-username>/crypto-yall/actions`
2. Check the latest runs:
   - Daily bot: **Execute Trades**
   - Intraday bot: **Execute Intraday**
   - Aggressive bot: **Execute Aggressive**
3. Look for green checkmarks on recent runs.
4. Open a run and confirm the job completed without an error.

Typical schedules:
- Daily: once per day
- Intraday: once per hour
- Aggressive: every 30 minutes

GitHub-hosted schedules are best-effort, so a run can occasionally be delayed.

### Possible cause B: A bot is paused

Check your GitHub Variables:

`https://github.com/<your-username>/crypto-yall/settings/variables/actions`

Look at:
- `KILL_SWITCH`
- `INTRADAY_KILL_SWITCH`
- `AGGRESSIVE_KILL_SWITCH`

If one is `OFF`, that bot is paused.

### Possible cause C: Email is going to spam

1. Check your spam or junk folder.
2. Look for messages from the Gmail account you configured in `GMAIL_USER`.
3. Mark legitimate bot alerts as "Not spam".

If alerts still do not arrive, check:
- `GMAIL_USER`
- `GMAIL_APP_PASSWORD`
- `NOTIFY_EMAILS`

### Possible cause D: Telegram is not working

If you enabled Telegram:

1. Open your own Telegram bot.
2. Make sure you have not blocked it.
3. Send it a message such as `hello`.
4. Re-check your own:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`

Do not share the bot token in screenshots or chats.

### Possible cause E: GitHub Actions stopped running

1. Go to:
   `https://github.com/<your-username>/crypto-yall/actions`
2. Check whether recent scheduled runs are appearing.
3. If no runs are appearing, check:
   - Actions are enabled on the fork
   - The workflows still exist
   - Repository settings have not disabled Actions
   - Your current GitHub Actions usage and billing limits

---

## Common Issue 2: "I Got an Error Email or Failed Run"

### Error: "Daily drawdown triggered — halting today"

**What it means:** The bot reached its configured daily drawdown limit and stopped opening new trades for the rest of that day.

Default testnet thresholds:
- Daily: `5%`
- Intraday: `5%`
- Aggressive: `3%`

**What to do:** Review the affected bot's positions and recent trades. The bot is designed to resume on the next calendar day unless you keep it paused manually.

**If it keeps happening:** Leave the bot paused and review the strategy, capital setting, and recent market conditions before resuming.

---

### Error: "User or API Wallet does not exist" or "API Wallet does not exist"

**What it means:** Hyperliquid cannot use the API wallet in the environment the bot is currently pointing at.

Common causes:
- API wallet was not authorized on testnet
- API wallet was authorized on mainnet but the bot is using testnet
- API wallet was authorized on testnet but the bot is using mainnet
- The key was replaced or revoked

**What to do:**

1. Pause all affected bots.
2. Check `HL_TESTNET`.
3. If `HL_TESTNET = true`, verify the API wallet at:
   https://app.hyperliquid-testnet.xyz/API
4. If `HL_TESTNET = false`, verify the API wallet at:
   https://app.hyperliquid.xyz/API
5. Re-enter `HL_PRIVATE_KEY` only if you have confirmed which key belongs to the correct environment.

Never paste the private key into an AI chat or public issue.

---

### Error: "Account equity: $0.00"

**What it means:** The selected Hyperliquid environment has no usable account equity.

**On testnet:**
- Check that you claimed the testnet faucet using the same wallet.
- Confirm the bot is pointed at testnet.

**On mainnet:**
- Check your actual Hyperliquid balance directly before doing anything else.

Do not change `HL_TESTNET` merely to make an error disappear.

---

### Error: "private key must be exactly 32 bytes"

**What it means:** `HL_PRIVATE_KEY` is malformed.

**What to do:**

1. Open the GitHub Secrets page.
2. Re-enter `HL_PRIVATE_KEY` from your saved API wallet private key.
3. It should be `0x` followed by exactly 64 hexadecimal characters.
4. Make sure there are no spaces before or after it.

Do not show the value to anyone while troubleshooting.

---

### Error: "Insufficient balance"

**What it means:** Hyperliquid does not have enough available margin for the attempted order.

**What to do:**

1. Open Hyperliquid directly.
2. Check account equity and current open positions.
3. Review your capital variables:
   - `SEGREGATED_CAPITAL`
   - `INTRADAY_CAPITAL`
   - `AGGRESSIVE_CAPITAL`
4. Check whether another bot is already using margin.
5. Reduce sizing or pause bots if necessary.

Do not deposit additional real money simply to clear an error unless you have independently decided you are comfortable with the risk.

---

### Error: "CLIENT INIT FAILED"

**What it means:** The bot could not initialize its Hyperliquid client.

Possible causes:
- Temporary network/API problem
- Wrong or missing Hyperliquid credentials
- Wrong environment
- Malformed private key

**What to do:**

1. Open the failed GitHub Actions run.
2. Read the lines immediately before and after `CLIENT INIT FAILED`.
3. Check `HL_TESTNET`, `HL_PRIVATE_KEY`, and `HL_ACCOUNT_ADDRESS`.
4. If it appears to be a temporary network problem, wait for the next run.
5. If it repeats, keep the bot paused until the cause is identified.

---

### Error: "Could not load state from Gist"

**What it means:** The bot cannot read one of its state Gists.

Check:
- `GIST_TOKEN`
- `GIST_ID`
- `TRADING_GIST_ID`
- `INTRADAY_GIST_ID`
- `AGGRESSIVE_GIST_ID`

Also confirm:
- The Gists still exist
- The filenames are correct
- The GitHub token still has Gist access

Secret Gists are unlisted, not truly private. Keep their URLs and IDs private.

---

### Error: "Telegram error: 400" or "401"

**What it means:** Telegram rejected the request.

Common causes:
- Wrong bot token
- Wrong chat ID
- Bot was blocked
- Bot token was regenerated or revoked

**What to do:**

1. Confirm your own Telegram bot is still active.
2. Message the bot again.
3. Re-check `TELEGRAM_BOT_TOKEN`.
4. Re-check `TELEGRAM_CHAT_ID`.

Email alerts can continue working independently if Gmail is configured correctly.

---

### Error: "Email sent to []"

**What it means:** The bot has no valid notification recipients.

**What to do:**

1. Open your repository Secrets page.
2. Check `NOTIFY_EMAILS`.
3. Re-enter your intended email address or comma-separated recipient list.
4. Run a workflow again and check the output.

---

## Common Issue 3: "The Dashboard Shows No Data"

The dashboard is optional. The bot can operate without it.

### The live trading sections are missing

**Likely cause:** Your Streamlit deployment does not have the required Gist secrets.

Open your own Streamlit app settings and check:

```toml
GIST_TOKEN = "your_github_pat"
TRADING_GIST_ID = "YOUR_TRADING_GIST_ID"
INTRADAY_GIST_ID = "YOUR_INTRADAY_GIST_ID"
AGGRESSIVE_GIST_ID = "YOUR_AGGRESSIVE_GIST_ID"
```

Never put your actual token or secret values in the public repository.

### The dashboard shows stale data

Possible causes:
- Streamlit caching
- A bot has not run recently
- A Gist has not been updated
- The dashboard app was sleeping

Try:
1. Refresh the dashboard.
2. Check GitHub Actions directly.
3. Check the relevant Gist.
4. Reboot your own Streamlit app if necessary.

### The dashboard won't load

1. Check your Streamlit deployment status.
2. Check the app logs.
3. Confirm the repository and branch are correct.
4. Confirm `app.py` is still the configured main file.
5. Re-check your Streamlit secrets.

Remember: Hyperliquid itself is the source of truth for exchange positions.

---

## Common Issue 4: "The Bot Opened a Position But Hyperliquid Shows Something Different"

All three bots may share the same Hyperliquid account.

If two bots take opposite positions in the same asset, Hyperliquid can show the **net exchange position** rather than each bot's internal intended position separately.

Example:
- Daily bot: ETH long
- Aggressive bot: ETH short
- Hyperliquid: shows the net result

**What to do:**

1. Check the actual exchange position on Hyperliquid.
2. Check each bot's state Gist.
3. Review the most recent fills in GitHub Actions.
4. If the internal state no longer matches what actually exists on the exchange, pause the affected bots before changing state files.

Do not assume the dashboard's per-bot view is the same thing as the exchange's net position.

---

## Common Issue 5: "I Want to Stop the Bots Right Now"

### Emergency procedure

**Step 1: Stop new automated orders**

Go to:

`https://github.com/<your-username>/crypto-yall/settings/variables/actions`

Set all three to:

- `KILL_SWITCH = OFF`
- `INTRADAY_KILL_SWITCH = OFF`
- `AGGRESSIVE_KILL_SWITCH = OFF`

**Step 2: Review existing positions**

Open Hyperliquid and connect **your own wallet**.

The kill switches do not close existing exchange positions.

**Step 3: If you choose to exit**

Close the relevant positions manually on Hyperliquid.

Before closing, make sure you understand which positions are open and whether closing them will affect positions shared across multiple bots.

---

## Common Issue 6: "The Bot Made a Trade I Don't Understand"

Alerts and GitHub Actions logs may include a reason for the decision.

Examples:

- **"Sync to hold_long"** — the bot's state says it owns no position, while the strategy says it should be long, so it attempts to synchronize.
- **"SELL / EXIT signal"** — an exit condition fired.
- **"LIQUIDATE TO CASH signal"** — the Daily strategy moved to cash under its regime logic.
- **"ENTER SHORT signal"** — a short-entry condition fired.
- **"pyramid add #1"** — the Aggressive bot added to an existing position under its pyramiding rules.
- **"BUY signal"** — a long-entry condition fired.

If a trade does not make sense:

1. Check the workflow log for the exact reason.
2. Check the strategy signal.
3. Check Hyperliquid for the actual fill.
4. Pause that bot if you want time to investigate before another run.

---

## Common Issue 7: "I Accidentally Changed Something in GitHub"

### If you accidentally changed a variable

Compare the value with the setup guide.

Safe testnet defaults:

- `HL_TESTNET = true`
- `KILL_SWITCH = ON`
- `INTRADAY_KILL_SWITCH = ON`
- `AGGRESSIVE_KILL_SWITCH = ON`
- `SEGREGATED_CAPITAL = 1000`
- `INTRADAY_CAPITAL = 500`
- `AGGRESSIVE_CAPITAL = 300`
- `DAILY_DD_PCT = 5`
- `INTRADAY_DD_PCT = 5`
- `AGGRESSIVE_DD_PCT = 3`
- `MAX_POSITIONS = 4`
- `INTRADAY_MAX_POSITIONS = 2`
- `AGGRESSIVE_MAX_POSITIONS = 4`

If you are unsure, pause the affected bot before restoring values.

### If you accidentally changed a secret

GitHub does not show the saved secret value after it has been stored.

You will need to:
- Re-enter the value from your own secure notes, or
- Regenerate/recreate the credential if necessary

Never ask someone else to send you a copy of your private key or password.

### If you accidentally changed code

1. Pause all bots.
2. Open the repository's commit history.
3. Identify the commit that introduced the unwanted change.
4. Restore the affected file from a known-good version or revert the commit.
5. Review the change before resuming Actions.

If you are not comfortable reverting code, keep the bots paused until you can get help reviewing the repository history.

---

## When to Keep the Bots Paused

Keep the affected bot or all bots paused if:

- The same error happens repeatedly
- You cannot confirm which Hyperliquid environment is active
- You are unsure which API wallet key is configured
- Actual Hyperliquid positions do not match what you expected
- You accidentally changed code or state and do not know how to restore it
- You suspect a credential has been exposed
- You are preparing to change from testnet to mainnet

If a private key or token may have been exposed, revoke or replace it rather than continuing to use it.

---

## Safe Diagnostic Checklist

Before asking for help, collect:

- Approximate time the problem started
- Which bot is affected: Daily / Intraday / Aggressive
- Which workflow failed
- The exact error message
- Whether `HL_TESTNET` is `true` or `false`
- What Hyperliquid shows for positions and equity
- What you changed most recently
- A screenshot of the error with all secret values hidden

Do **not** include:
- Hyperliquid API private keys
- Wallet seed phrases
- GitHub tokens
- Gmail app passwords
- Telegram bot tokens
- Any other secret credential

---

## Quick Troubleshooting Reference

| Problem | First thing to check |
|---|---|
| No alerts | GitHub Actions recent runs |
| Bot paused | Kill switch Variables |
| API wallet error | Correct Hyperliquid environment and authorization |
| $0 equity | Correct environment and account funding |
| Private-key format error | `HL_PRIVATE_KEY` formatting |
| Gist state error | Gist IDs and `GIST_TOKEN` |
| No email | `NOTIFY_EMAILS` and Gmail app password |
| Telegram 400/401 | Bot token and chat ID |
| Dashboard empty | Streamlit Gist secrets |
| Unexpected position | Hyperliquid actual position + bot state |
| Need to stop | Set all three kill switches to `OFF` |

---

*Crypto Forge Labs troubleshooting guide — August 2026*
