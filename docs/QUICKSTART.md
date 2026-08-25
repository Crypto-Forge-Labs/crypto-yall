# Quickstart Guide (For Non-Technical Users)

This guide is for everyday operation of your Crypto Forge Labs trading bots — checking status, pausing them, reviewing alerts, and handling common issues. No coding is required.

> **Project note:** Crypto Forge Labs is based on the upstream `aicodepathways/crypto-yall` project. This guide is written for users running their own fork and their own accounts.

---

## What You Need

- A web browser
- Access to your own forked GitHub repo: `https://github.com/<your-username>/crypto-yall`
- Access to your own Hyperliquid account
- Email alerts configured, and Telegram alerts if you chose to enable them
- Optional: your own Streamlit dashboard, if you deployed one

---

## How to Check on the Bots

### Option 1: GitHub Actions (recommended)

1. Open `https://github.com/<your-username>/crypto-yall/actions`
2. Look for the latest runs of:
   - **Execute Trades** — Daily bot
   - **Execute Intraday** — Intraday Standard bot
   - **Execute Aggressive** — Aggressive bot
3. A green checkmark means the workflow completed successfully.
4. A red X means the workflow failed. Click the failed run, then open the failed job to read the error.

Typical schedules:
- **Daily bot:** once per day, around 00:15 UTC
- **Intraday bot:** every hour at :05
- **Aggressive bot:** every 30 minutes

GitHub-hosted schedules are best-effort, so runs can be delayed.

### Option 2: Email and Telegram alerts

You receive notifications when the bots place trades or when certain errors occur.

A period with no trade alerts does **not** automatically mean something is wrong. In a quiet market, the bots may correctly decide that there are no trades to place.

### Option 3: Hyperliquid directly

Hyperliquid is the source of truth for actual positions, account equity, and PnL.

1. Visit https://app.hyperliquid.xyz for mainnet, or the appropriate Hyperliquid testnet URL when testing
2. Connect **your own wallet**
3. Review open positions and account equity

### Option 4: Your own dashboard (optional)

If you deployed the Streamlit dashboard for your fork, use the URL created for your own deployment.

The dashboard can show:
- Bot status
- Account equity
- Open positions
- Recent trades
- Current strategy signals

If the dashboard is missing trading sections or looks stale, check its Streamlit secrets and your Gist configuration.

---

## How to Pause a Bot

You might want to pause a bot if:
- The market is unusually volatile
- You want to investigate unexpected behaviour
- You are changing settings
- You simply do not want that bot opening new positions

### Step-by-step using GitHub

1. Go to `https://github.com/<your-username>/crypto-yall/settings/variables/actions`
2. Find the kill switch you want to change:
   - **KILL_SWITCH** → Daily bot
   - **INTRADAY_KILL_SWITCH** → Intraday Standard bot
   - **AGGRESSIVE_KILL_SWITCH** → Aggressive bot
3. Edit the variable
4. Change **ON** to **OFF**
5. Save the variable

The bot will skip new order placement while its kill switch is OFF.

**Important:** Existing Hyperliquid positions remain open. A kill switch does not automatically close an existing position.

### To resume

Change the relevant variable from **OFF** back to **ON**.

### To pause all three bots

Set all three kill switches to **OFF**.

---

## Emergency Stop

If you need to stop new automated orders immediately:

1. Set all three GitHub kill switches to **OFF**
2. Open Hyperliquid and review all current positions
3. If you want to exit existing positions, close them manually on Hyperliquid
4. Check the most recent GitHub Actions runs for errors or unexpected behaviour

**Important:** The GitHub kill switches prevent new automated orders. They do not close existing positions.

---

## How to Change Bot Capital Allocation

The capital variables control the sizing calculations used by each bot.

Go to:

`https://github.com/<your-username>/crypto-yall/settings/variables/actions`

The safe testnet defaults in the Crypto Forge Labs setup guide are:

- **SEGREGATED_CAPITAL** → Daily bot: `1000`
- **INTRADAY_CAPITAL** → Intraday Standard bot: `500`
- **AGGRESSIVE_CAPITAL** → Aggressive bot: `300`

Edit the variable, enter the new value, and save it. The change applies on the next run.

**Important:** These are sizing/accounting variables. They do not move money between accounts or limit the exchange balance by themselves. Do not set capital values higher than you understand or can safely support with your actual Hyperliquid balance and margin.

---

## Understanding the Alerts

Depending on which workflow generated the alert, an email or Telegram notification may include:

- **Asset** — BTC, ETH, SOL, etc.
- **Action** — for example `BUY`, `open_long`, `open_short`, `close`, or hold states
- **Mode** — Standard or Aggressive
- **Regime** — Bull, Bear, or Chop where applicable
- **Price** at the time of the signal or execution
- **Previous action** or previous state

Trade alerts are normally informational. If a fill has already occurred, the trade has already been placed by the bot.

Always use Hyperliquid itself to confirm the actual exchange position.

---

## What to Do If You Don't Get Alerts for a Long Time

Possible causes include:

1. **No trade signal fired** — this can be completely normal
2. **A bot is paused** — check the kill switch variables
3. **Email went to spam** — check your spam/junk folder
4. **Telegram is not configured correctly** — verify your own bot token and chat ID
5. **A workflow failed** — check the GitHub Actions tab
6. **GitHub Actions usage or repository settings changed** — check your current GitHub Actions status and plan limits

### Check whether the bots are still running

1. Open `https://github.com/<your-username>/crypto-yall/actions`
2. Check **Execute Aggressive** — normally scheduled every 30 minutes
3. Check **Execute Intraday** — normally scheduled hourly
4. Check **Execute Trades** — normally scheduled daily

Green checkmark = completed successfully.

Red X = open the failed run and read the failed job output.

---

## What to Do If You Get an Error or Failed Run

Common causes include:
- Hyperliquid rejected an order
- The API wallet is not authorized on the correct environment
- The account has insufficient margin
- A GitHub Secret or Gist ID is wrong
- The drawdown protection halted a bot
- The bot is intentionally paused

If the same error repeats:

1. Set the affected bot's kill switch to **OFF**
2. Read the latest GitHub Actions error log
3. Check your Hyperliquid account directly
4. Refer to `docs/TROUBLESHOOTING.md`
5. Re-check the relevant GitHub Secret or Variable

Never paste private keys, seed phrases, Gmail app passwords, GitHub tokens, or Telegram bot tokens into screenshots, issues, public chats, or support messages.

---

## Common Controls

### Pause Daily bot

`KILL_SWITCH = OFF`

### Pause Intraday bot

`INTRADAY_KILL_SWITCH = OFF`

### Pause Aggressive bot

`AGGRESSIVE_KILL_SWITCH = OFF`

### Resume a bot

Change its kill switch back to:

`ON`

### Switch to testnet

`HL_TESTNET = true`

### Mainnet warning

Do not switch `HL_TESTNET` to `false` until you have completed the mainnet checklist, authorized the correct mainnet API wallet, reviewed your capital settings, and understand the risks of leveraged perpetual futures trading.

---

## Quick Reference Card

| What you want to do | How |
|---------------------|-----|
| Check bot runs | `https://github.com/<your-username>/crypto-yall/actions` |
| Verify positions on exchange | https://app.hyperliquid.xyz |
| Pause Daily bot | `KILL_SWITCH = OFF` |
| Pause Intraday Standard | `INTRADAY_KILL_SWITCH = OFF` |
| Pause Aggressive | `AGGRESSIVE_KILL_SWITCH = OFF` |
| Resume any bot | Change its kill switch back to `ON` |
| Change bot sizing | Edit the relevant capital variable in GitHub Variables |
| See trade history | Use your Gists or your own deployed dashboard |
| Investigate a failure | Actions → failed run → failed job → logs |

---

## Security Reminder

Your setup should use your own:
- Hyperliquid wallet and API wallet
- GitHub Secrets and Variables
- GitHub Gists
- Gmail account/app password
- Telegram bot and chat ID, if enabled

Keep all private keys, passwords, seed phrases, and tokens out of the repository and out of AI chats. Store them only in the appropriate secret-management fields or a trusted password manager.

---

*Crypto Forge Labs quickstart guide — August 2026*
