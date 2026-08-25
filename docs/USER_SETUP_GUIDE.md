# Crypto Forge Labs — Personal Bot Setup Guide

This guide walks you through setting up your own personal copy of the Crypto Forge Labs trading bots. When you're done, you'll have three bots running on your own Hyperliquid account and sending alerts to your own email and optional Telegram account.

> **Project note:** Crypto Forge Labs is based on the upstream `aicodepathways/crypto-yall` project. This guide points users to the Crypto Forge Labs fork for setup.

---

## Two Ways to Do This Setup

### Option 1: AI-Assisted Setup (Recommended for Most People)

Don't want to read 90 minutes of instructions? Use an AI assistant to walk you through it interactively.

**See [AI_ASSISTED_SETUP.md](AI_ASSISTED_SETUP.md)** — it has a ready-to-paste prompt you give to ChatGPT, Claude, or any other AI assistant. The AI will then guide you step-by-step, ask you for one value at a time, and help debug if anything fails.

**Pros:**
- Faster (30-45 minutes vs 90)
- Personalized — AI answers your specific questions
- Catches mistakes as you go
- No need to read the entire guide upfront

**Cons:**
- You need access to ChatGPT, Claude, Gemini, or another AI assistant
- AI can occasionally get interface details wrong — verify critical steps against what you actually see on screen

### Option 2: Manual Setup (Read This Guide)

If you prefer to read everything yourself or want full control, keep reading below.

---

## Before You Start

**Time required:** ~90 minutes the first time. Most of it is clicking through web interfaces, not coding.

**Technical level:** You don't need to be a developer, but you need to be comfortable:
- Creating accounts on a few services
- Copying and pasting long strings of letters and numbers exactly
- Following click-by-click instructions carefully
- Not getting frustrated when something doesn't work on the first try

**You'll be creating accounts on:**
- GitHub (free)
- Hyperliquid (already done if you've connected a wallet there)
- Gmail (free, or use an existing account)

**You'll need:**
- A crypto wallet that already has some USDC on Arbitrum (for the testnet faucet activation; minimum $5)
- A phone for 2-factor authentication and Telegram
- ~30 minutes of uninterrupted focus

---

## What You're Setting Up

By the end of this guide, you'll have:

1. **A forked copy of the bot code** on your GitHub account
2. **Three trading bots** running on your Hyperliquid account:
   - Daily bot (checks once per day)
   - Intraday bot (checks once per hour)
   - Aggressive bot (checks every 30 minutes)
3. **Email alerts** to your inbox whenever a bot opens or closes a trade
4. **Optional Telegram alerts** to your phone
5. **A dashboard** showing positions and PnL (optional but recommended)
6. **Complete control** over your own bot — you can pause, restart, change capital, anything

You control your own accounts and credentials. Keep all private keys, passwords, seed phrases, and tokens private and store them only in services you trust.

---

## Part 1: Fork the Repository (5 minutes)

### Step 1.1: Create a GitHub account (if you don't have one)

1. Go to https://github.com/signup
2. Sign up with your email
3. Verify your email when prompted

### Step 1.2: Fork the Crypto Forge Labs repo

1. Sign in to GitHub
2. Visit https://github.com/Crypto-Forge-Labs/crypto-yall 3. Click the "**Fork**" button in the top right
4. On the next page, leave defaults and click "**Create fork**"
5. You'll be redirected to `https://github.com/<your-username>/crypto-yall`

**That's your personal copy.** From here on, when this guide says "your repo," it means this forked copy at `github.com/<your-username>/crypto-yall`.

### Step 1.3: Enable GitHub Actions on your fork

GitHub disables Actions on forks by default. You need to turn them on.

1. In your forked repo, click the "**Actions**" tab
2. You'll see a yellow banner saying "Workflows aren't being run on this forked repository"
3. Click the green "**I understand my workflows, go ahead and enable them**" button

---

## Part 2: Set Up Hyperliquid (15 minutes)

You need a Hyperliquid account with an API wallet that the bots can use to place trades.

### Step 2.1: Connect a wallet to Hyperliquid

If you've used Hyperliquid before, skip to Step 2.2.

1. Visit https://app.hyperliquid.xyz
2. Click "Connect Wallet" in the top right
3. Choose your wallet (Metamask, Rabby, Coinbase Wallet, etc.)
4. Sign the connection prompt

**Regional availability:** Before using Hyperliquid, make sure the service is available to you in your location and follow its current terms and regional restrictions.

### Step 2.2: Activate your account by depositing $5+ USDC

The testnet faucet requires you to have made at least one real deposit on mainnet first. This is Hyperliquid's anti-abuse measure.

1. Click "**Deposit**" on Hyperliquid
2. Choose "Arbitrum" as the source network
3. Send at least $5 USDC from your wallet to the Hyperliquid bridge address shown
4. Wait ~1 minute for confirmation
5. You'll see the balance appear

This $5 is real money but it stays in your Hyperliquid account and can be withdrawn later.

### Step 2.3: Get free testnet USDC

1. Visit https://app.hyperliquid-testnet.xyz/drip (note: **testnet** URL)
2. Connect the same wallet
3. Click "Claim" or "Drip"
4. You'll receive 1,000 mock USDC for testnet

**Note:** One claim per address ever. If you mess up, you can't claim again. The 1,000 mock USDC is plenty for the 2-week testnet phase.

### Step 2.4: Generate an API wallet on testnet

The API wallet is a trading-only key. It can place orders but cannot withdraw funds. This is the key the bot will use.

1. Visit https://app.hyperliquid-testnet.xyz/API
2. Connect your wallet
3. Click "Generate" next to API Wallets
4. Name it: "Crypto Forge Labs Bot"
5. **Copy the private key it shows you** (starts with `0x...`) — you'll only see this once. Save it somewhere secure right now, preferably in a trusted password manager. Do not paste it into an AI chat or public document.
6. Sign the authorization transaction (free on testnet)
7. **Copy your main account address** (top right of Hyperliquid, starts with `0x...`) — this is your wallet address, not the API wallet

**Save both of these somewhere safe:**

- **API wallet private key:** `0x...64 characters of hex...`
- **Main account address:** `0x...40 characters of hex...`

You'll need them in Part 6.

---

## Part 3: Set Up State Storage (10 minutes)

The bots remember what positions they own using GitHub Gists (a simple file-storage feature of GitHub).

### Step 3.1: Create a GitHub Personal Access Token

This token lets the bot read and write to your Gists.

1. Visit https://github.com/settings/tokens/new
2. Name: "Crypto Forge Labs Bot"
3. Expiration: 1 year (or "No expiration" if you'll remember to renew)
4. Scopes: check **only** the box that says "**gist**"
5. Scroll to the bottom and click "**Generate token**"
6. **Copy the token immediately** — starts with `ghp_...` — you'll never see it again

Save this somewhere safe.

### Step 3.2: Create 4 secret Gists

The bots store their state in 4 separate secret Gists. Secret Gists are unlisted, not truly private, so keep each Gist URL and ID private.

For each Gist:
1. Visit https://gist.github.com
2. **Filename:** use one of the names below
3. **Content:** type exactly `{}` (just two curly braces)
4. Click "**Create secret gist**" (NOT "Create public gist")
5. After creating, copy the URL — the ID is the long string after the last `/`
   - Example: `https://gist.github.com/yourname/abc123def456` → ID is `abc123def456`

**Create these 4 Gists:**

| Filename | What it's for | Save the Gist ID as |
|----------|---------------|---------------------|
| `signal_state.json` | Tracks signal changes (for alerts) | `GIST_ID` |
| `trading_state.json` | Daily bot state | `TRADING_GIST_ID` |
| `intraday_state.json` | Intraday Standard bot state | `INTRADAY_GIST_ID` |
| `aggressive_state.json` | Aggressive bot state | `AGGRESSIVE_GIST_ID` |

You should now have a saved list of 4 Gist IDs. Keep them in your notes.

---

## Part 4: Set Up Email Alerts (10 minutes)

The bots will send you an email every time they make a trade. You need a Gmail account with an "app password" for this.

### Step 4.1: Use an existing Gmail or create a new one

Either works. If you want to keep bot emails separate from your personal email, create a new Gmail. Otherwise, use your existing one.

### Step 4.2: Enable 2-Step Verification

Required to create app passwords.

1. Visit https://myaccount.google.com/security
2. Find "2-Step Verification"
3. If it's off, turn it on (you'll need your phone)

### Step 4.3: Create an app password

1. Visit https://myaccount.google.com/apppasswords
2. Name: "Crypto Forge Labs Bot"
3. Click "Create"
4. Google will show you a 16-character password. **Copy it immediately** — you can't see it again.
5. Save it somewhere safe

**Save:**
- **Gmail address:** the one you used (e.g., `you@gmail.com`)
- **App password:** the 16-character string Google generated

---

## Part 5: Set Up Telegram Alerts (Optional, 10 minutes)

Skip this section if you only want email alerts.

### Step 5.1: Install Telegram

If you don't have it: https://telegram.org/

### Step 5.2: Create your own bot via BotFather

1. In Telegram, search for `@BotFather`
2. Send it: `/newbot`
3. When asked for a name, type: "Crypto Forge Labs Bot"
4. When asked for a username, type something unique (ending in "bot"), like: "MyCryptoForgeBot"
5. BotFather will give you a token (long string of numbers and letters). **Copy it.**

### Step 5.3: Get your chat ID

1. Search for your new bot in Telegram (by the username you just set)
2. Tap "Start" or send it any message like "hello"
3. Open this URL in a browser, replacing `<YOUR_BOT_TOKEN>` with the token from Step 5.2:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
4. In the response, look for `"chat":{"id":` followed by a number. That number is your chat ID.

**Save:**
- **Telegram bot token:** the long string from BotFather
- **Telegram chat ID:** the number from the API response

---

## Part 6: Configure Your GitHub Secrets and Variables (20 minutes)

This is the longest section. You'll be entering all the values you collected into your forked repo's settings.

### Step 6.1: Add Secrets

Secrets are encrypted values your bot uses. They're hidden once you save them.

1. Go to `https://github.com/<your-username>/crypto-yall/settings/secrets/actions`
2. Click "**New repository secret**" for each secret below
3. For each: enter the name exactly as shown, then paste the value

| Secret Name | What to paste |
|-------------|---------------|
| `HL_PRIVATE_KEY` | Your API wallet private key from Step 2.4 (starts with `0x...`) |
| `HL_ACCOUNT_ADDRESS` | Your main account address from Step 2.4 (starts with `0x...`) |
| `GIST_TOKEN` | Your GitHub personal access token from Step 3.1 (starts with `ghp_...`) |
| `GIST_ID` | The ID of your `signal_state.json` Gist from Step 3.2 |
| `TRADING_GIST_ID` | The ID of your `trading_state.json` Gist from Step 3.2 |
| `INTRADAY_GIST_ID` | The ID of your `intraday_state.json` Gist from Step 3.2 |
| `AGGRESSIVE_GIST_ID` | The ID of your `aggressive_state.json` Gist from Step 3.2 |
| `GMAIL_USER` | Your Gmail address from Step 4.1 |
| `GMAIL_APP_PASSWORD` | The 16-character app password from Step 4.3 |
| `NOTIFY_EMAILS` | Comma-separated list of emails to receive alerts (just yours is fine: `you@example.com`) |
| `TELEGRAM_BOT_TOKEN` | Your bot token from Step 5.2 (or leave blank if skipping Telegram) |
| `TELEGRAM_CHAT_ID` | Your chat ID from Step 5.3 (or leave blank if skipping Telegram) |

Double-check every value. Even one extra space or missing character can cause the bot to fail. Never paste secret values into an AI chat.

### Step 6.2: Add Variables

Variables are settings you can see and change anytime (unlike secrets). They control how the bots behave.

1. Go to `https://github.com/<your-username>/crypto-yall/settings/variables/actions`
2. Click "**New repository variable**" for each variable below

| Variable Name | Value | What it does |
|---------------|-------|--------------|
| `HL_TESTNET` | `true` | Use testnet (fake money) instead of mainnet |
| `KILL_SWITCH` | `ON` | Daily bot enabled |
| `INTRADAY_KILL_SWITCH` | `ON` | Intraday bot enabled |
| `AGGRESSIVE_KILL_SWITCH` | `ON` | Aggressive bot enabled |
| `SEGREGATED_CAPITAL` | `1000` | Daily bot pretend capital (testnet only) |
| `INTRADAY_CAPITAL` | `500` | Intraday bot pretend capital |
| `AGGRESSIVE_CAPITAL` | `300` | Aggressive bot pretend capital |
| `DAILY_DD_PCT` | `5` | Daily bot drawdown halt threshold (%) |
| `INTRADAY_DD_PCT` | `5` | Intraday bot drawdown halt threshold (%) |
| `AGGRESSIVE_DD_PCT` | `3` | Aggressive bot drawdown halt threshold (%) |
| `MAX_POSITIONS` | `4` | Daily bot max concurrent positions |
| `INTRADAY_MAX_POSITIONS` | `2` | Intraday bot max concurrent positions |
| `AGGRESSIVE_MAX_POSITIONS` | `4` | Aggressive bot max concurrent positions |

---

## Part 7: First Run and Verification (10 minutes)

You're done with setup. Time to make sure it works.

### Step 7.1: Trigger the test trade workflow

This places a $10 BTC trade and immediately closes it. It proves the bot can connect to Hyperliquid and place orders.

1. Go to your forked repo's Actions tab: `https://github.com/<your-username>/crypto-yall/actions`
2. Click "**Test Trade**" in the left sidebar
3. Click the "**Run workflow**" dropdown on the right
4. Click the green "**Run workflow**" button
5. Wait ~1 minute, then click into the run that just appeared
6. Click "trade" in the job list
7. Look for these lines in the output:
   ```
   Account equity: $1000.00
   Placing test LONG: 0.00013 BTC @ market
   Open response: {'status': 'ok', ...}
   Position confirmed: ...
   Closing position…
   Close response: {'status': 'ok', ...}
   Final equity: ~$999.98
   ```

If you see these, **your bot is working**. Slight equity loss is just slippage on a $10 trade — totally normal.

### Step 7.2: If the test trade failed

Common errors:

| Error message | Cause | Fix |
|---------------|-------|-----|
| `User or API Wallet does not exist` | API wallet not authorized on testnet | Go back to Step 2.4, make sure you're on app.hyperliquid-**testnet**.xyz |
| `Account equity: $0.00` | Testnet not funded | Go back to Step 2.3, claim the faucet |
| `private key must be exactly 32 bytes` | Wrong value in `HL_PRIVATE_KEY` secret | Re-check; should start with `0x` followed by 64 hex characters |
| `Could not load state from Gist` | Gist ID wrong or token wrong | Re-check the IDs and the `GIST_TOKEN` |

### Step 7.3: Enable the scheduled bots

Once the test trade works, the actual bots will start running on their schedules:

- **Daily bot:** runs once per day at ~00:15 UTC (often delayed 30-60 minutes by GitHub)
- **Intraday bot:** runs every hour at :05
- **Aggressive bot:** runs every 30 minutes

You'll get email + Telegram alerts whenever they place a trade.

### Step 7.4: Trigger each bot manually for a fast first test

You don't have to wait for the schedules. Trigger each one once now:

1. Actions tab
2. Click "**Execute Trades**" → Run workflow → Run workflow
3. Wait 1 minute
4. Click "**Execute Intraday**" → Run workflow → Run workflow
5. Wait 1 minute
6. Click "**Execute Aggressive**" → Run workflow → Run workflow

If any of these succeed and you see "Decided on X trade(s)" in the output, you're fully live.

---

## Part 8: Daily Operations

### How to check on your bot

**Option A: GitHub Actions tab** — see if recent runs succeeded
Visit `https://github.com/<your-username>/crypto-yall/actions`

**Option B: View your Gists** — see current state
Visit your Gist URLs from Step 3.2

**Option C: Email/Telegram alerts** — passive monitoring
You'll get alerts on every trade. No alerts = market is quiet.

**Option D: Dashboard** (advanced, optional)
You can deploy your own Streamlit dashboard. See "Optional: Personal Dashboard" at the bottom of this guide.

### How to pause the bots

1. Go to `https://github.com/<your-username>/crypto-yall/settings/variables/actions`
2. Find `KILL_SWITCH`, `INTRADAY_KILL_SWITCH`, or `AGGRESSIVE_KILL_SWITCH`
3. Click to edit, change `ON` to `OFF`, save

The bot will skip its next scheduled run. To resume, change `OFF` back to `ON`.

### How to change capital allocation

Edit `SEGREGATED_CAPITAL`, `INTRADAY_CAPITAL`, or `AGGRESSIVE_CAPITAL` in the variables. Changes take effect on the next scheduled run.

---

## Part 9: Going to Mainnet (Real Money)

Only consider moving to real money after you have thoroughly tested the bot on testnet, understand its behavior and risks, and are comfortable with every control in this guide.

### Pre-mainnet checklist

- [ ] You've watched the bots place trades and understood the alerts
- [ ] You've successfully paused and resumed a bot
- [ ] You understand the worst-case scenario (you lose all the money you allocate)
- [ ] You have a specific dollar amount you can afford to lose entirely
- [ ] You've talked to a tax professional about the implications

### Going-live steps

1. **Generate a new API wallet on mainnet**
   - Same process as Step 2.4, but at https://app.hyperliquid.xyz/API (no testnet)
   - You can use the same address as the testnet one or generate fresh
   - Update `HL_PRIVATE_KEY` secret with the new mainnet key

2. **Bridge real USDC**
   - Bridge only an amount you can afford to lose to your mainnet account via app.hyperliquid.xyz/deposit
   - Distribute it however you want across the three bots (mentally — they share the account)

3. **Reset your state Gists**
   - For each of the 4 Gists, edit and replace contents with just `{}`
   - This wipes the testnet trade history so the bot starts fresh

4. **Tighten your safety settings**
   - `DAILY_DD_PCT` and `INTRADAY_DD_PCT`: change from 5 to 3
   - `AGGRESSIVE_DD_PCT`: change from 3 to 2
   - Capital variables: set to actual USDC amounts you bridged

5. **Flip the testnet flag**
   - Variable `HL_TESTNET`: change from `true` to `false`

6. **Watch the first 10 runs carefully**
   - Verify every trade alert matches what shows on Hyperliquid
   - Pause everything immediately if anything looks wrong

---

## Troubleshooting

### I'm not getting email alerts

1. Check the workflow's output (Actions tab → recent run → click "trade" job). Look for `Email sent to [...]` line.
2. Check your spam folder.
3. Verify `NOTIFY_EMAILS` secret has your address.
4. Verify `GMAIL_APP_PASSWORD` is correct — try regenerating it.

### A bot stopped running

1. Visit Actions tab.
2. Click on the latest run that failed (red X).
3. Click into the failing job and read the error.
4. Common fixes: re-check secrets, verify Hyperliquid account isn't drained.

### I see "0 trades executed this cycle" emails constantly

Normal in quiet markets. The bot is running but no signals are firing. Wait for market movement.

### "GitHub Actions disabled on this fork"

If you didn't enable Actions in Step 1.3, the bots won't run. Go back to that step.

### My GitHub Actions usage is running high

GitHub Actions limits and pricing can change, so check the current usage and billing information for your GitHub plan.

The Aggressive bot runs frequently and can use a large share of included Actions minutes.

Options:
- Reduce or pause the Aggressive bot schedule
- Review your repository visibility and GitHub's current Actions policy
- Review GitHub's current paid plan or Actions billing options if needed

Your repository secrets are not displayed publicly, but always review workflow code before enabling it.

### Something else is wrong

Use the troubleshooting guide and workflow logs first. If you still need help, provide:
- A screenshot of the error
- Which workflow failed
- When it started failing
- What you changed most recently (if anything)

Never include private keys, passwords, seed phrases, GitHub tokens, Gmail app passwords, or Telegram bot tokens in screenshots or support messages.

---

## Optional: Personal Dashboard

The dashboard is nice-to-have but not required. The bot works without it.

To set up your own:

1. Sign up at https://share.streamlit.io with your GitHub account
2. Click "New app"
3. Choose your forked `crypto-yall` repo
4. Branch: `main`
5. Main file path: `app.py`
6. Click "Advanced settings"
7. Add these secrets:
   ```toml
   GIST_TOKEN = "your_github_pat_from_step_3.1"
   TRADING_GIST_ID = "your_trading_gist_id"
   INTRADAY_GIST_ID = "your_intraday_gist_id"
   AGGRESSIVE_GIST_ID = "your_aggressive_gist_id"
   ```
8. Click "Deploy"

After ~2 minutes you'll have your own dashboard URL. Bookmark it.

---

## Important Disclaimers

- This is software that places real trades with real money on a leveraged perpetual futures exchange.
- You can lose all of your bridged capital, and (with leverage) potentially get liquidated below your initial deposit if you don't manage risk.
- Past performance on testnet does not guarantee future performance on mainnet.
- This guide and project documentation do not provide investment advice or guarantee trading results.
- You are solely responsible for your own trades, your own taxes, and your own decisions.
- Don't use money you can't afford to lose entirely.

---

## Summary Checklist

Use this to verify you've completed everything:

- [ ] Part 1: Forked the repo, enabled Actions
- [ ] Part 2: Connected Hyperliquid wallet, activated mainnet with $5+ USDC, claimed testnet faucet, generated API wallet on testnet
- [ ] Part 3: Created GitHub PAT, created 4 secret Gists
- [ ] Part 4: Set up Gmail app password
- [ ] Part 5: (optional) Created Telegram bot, got chat ID
- [ ] Part 6: Added all 12 secrets and 13 variables
- [ ] Part 7: Test trade succeeded
- [ ] Part 7: Manually triggered all 3 bot workflows
- [ ] You're getting alerts on email (and Telegram if enabled)
- [ ] You know how to pause via kill switches

Welcome to Crypto Forge Labs. Test carefully and manage risk.