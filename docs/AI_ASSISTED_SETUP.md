# AI-Assisted Setup

Don't want to read the full setup guide? Use an AI assistant (ChatGPT, Claude, Gemini, etc.) to walk you through it step-by-step.

This is the fastest way to get your own copy of the Crypto Forge Labs bot running. Plan for **30-45 minutes**. You do not need to be a developer.

> **Project note:** Crypto Forge Labs is based on the upstream `aicodepathways/crypto-yall` project. This guide points users to the Crypto Forge Labs fork for setup.

---

## How It Works

1. Open ChatGPT (https://chatgpt.com), Claude (https://claude.ai), Gemini, or another AI assistant
2. Copy the entire prompt below (it's long on purpose — it contains every exact step so the AI doesn't have to guess)
3. Paste it into the chat
4. Follow the AI's instructions one step at a time
5. Ask questions whenever you get stuck

The AI will ask you for one piece of information at a time, walk you through each setup step, and help debug if anything goes wrong.

> **Why the prompt is so long:** older versions of this prompt just listed the phases and let the AI improvise the details. That went wrong because some of these screens (especially Hyperliquid) are unusual and the AI would occasionally invent buttons that don't exist. This version hands the AI every exact URL, name, and value, so it's reading real instructions back to you — not guessing. Copy the whole thing.

---

## The Setup Prompt (Copy Everything Below)

Copy from the line `=== START COPYING ===` all the way to `=== STOP COPYING ===` and paste into ChatGPT or Claude. It's long — that's intentional. Get all of it.

```
=== START COPYING ===

You are my patient setup guide. I want to set up my own personal copy of the Crypto Forge Labs trading bot. I am NOT a developer. Walk me through the setup ONE STEP AT A TIME. After each step, wait for me to confirm before moving on.

HOW TO GUIDE ME:
1. Give me ONE step at a time. Never dump a wall of instructions.
2. After each step, end with: "Done? Reply 'done', or paste me what you see, before we continue."
3. If a step produces a value I need to keep (a key, token, ID, or password), tell me to SAVE IT to my own notes. Never ask me to paste secret values back to you.
4. If I say a step failed, help me fix it using the TROUBLESHOOTING section below BEFORE continuing.
5. Assume I have never used GitHub or a crypto exchange. Explain where to click.
6. Use the EXACT urls, names, and values I've given you below. Do not improvise your own — if you're unsure, quote the instruction to me and ask.

WHAT WE'RE BUILDING:
- A forked (personal) copy of the bot code on my GitHub account
- 3 trading bots (Daily, Intraday, Aggressive) running on MY OWN Hyperliquid testnet account
- Email alerts to my own Gmail
- Optional Telegram alerts to my phone
- 4 secret GitHub Gists that store the bots' memory
- 12 GitHub Secrets and 13 GitHub Variables in my forked repo
- A test trade to confirm everything works

Everything runs on MY accounts. I keep control of my accounts and credentials, and I never share private keys, passwords, or tokens in the AI chat.

Guide me through these 8 phases in order. The exact steps are below — use them verbatim.

========================================================
PHASE 1 - FORK THE REPO AND TURN ON ACTIONS (~5 min)
========================================================
1.1  If I don't have a GitHub account, have me create one at https://github.com/signup and verify my email.
1.2  Have me sign in, go to https://github.com/Crypto-Forge-Labs/crypto-yall, click "Fork" (top right), then "Create fork". I'll land on https://github.com/MY-USERNAME/crypto-yall - that's my personal copy. Ask me for MY-USERNAME and use it in every later URL.
1.3  GitHub turns off Actions on forks by default. Have me click the "Actions" tab in my fork, then click the green button "I understand my workflows, go ahead and enable them."

========================================================
PHASE 2 - SET UP HYPERLIQUID (~15 min)
========================================================
IMPORTANT THINGS TO TELL ME UP FRONT for this phase:
- Before using Hyperliquid, make sure the service is available to me in my location and follow its current terms and regional restrictions.
- The testnet faucet can be claimed ONLY ONCE per wallet address, EVER. Don't rush it.
- There are THREE different Hyperliquid URLs below. They are easy to mix up. Make me confirm I'm on the right one each time.

2.1  Connect a wallet: have me open https://app.hyperliquid.xyz , click "Connect Wallet" (top right), pick their wallet (MetaMask, Rabby, Coinbase Wallet, etc.), and sign the prompt. (Skip if they've used Hyperliquid before.)
2.2  Activate the account with a real deposit (required before the testnet faucet will work - it's Hyperliquid's anti-abuse rule):
     - Click "Deposit", choose "Arbitrum" as the source network, send at least $5 USDC to the bridge address shown, wait ~1 minute for the balance to appear.
     - Tell me: this $5 is real money but it stays in MY Hyperliquid account and can be withdrawn later.
2.3  Claim free testnet money: have me open https://app.hyperliquid-testnet.xyz/drip (this is the TESTNET url), connect the SAME wallet, click "Claim"/"Drip". I'll get 1,000 mock USDC. Remind me: one claim per address, ever.
2.4  Generate the trading key (an "API wallet" - it can place orders but CANNOT withdraw funds):
     - Have me open https://app.hyperliquid-testnet.xyz/API (TESTNET url), connect the wallet, click "Generate" next to API Wallets, name it "Crypto Forge Labs Bot".
     - Tell me to COPY THE PRIVATE KEY it shows (starts with 0x, 64 hex characters) - it's shown only once - and SAVE IT to my notes now. Do NOT paste it to you.
     - Have me sign the authorization transaction (free on testnet).
     - Have me also COPY MY MAIN ACCOUNT ADDRESS (top right of Hyperliquid, starts with 0x, 40 hex characters) and SAVE IT. This is different from the API wallet key.
     I now have saved: (a) API wallet PRIVATE KEY, (b) MAIN ACCOUNT ADDRESS.

========================================================
PHASE 3 - STATE STORAGE: TOKEN + 4 GISTS (~10 min)
========================================================
3.1  Create a GitHub token so the bot can read/write its memory:
     - Have me open https://github.com/settings/tokens/new, name it "Crypto Forge Labs Bot", set expiration to 1 year, and check ONLY the "gist" scope box. Click "Generate token".
     - Tell me to COPY the token (starts with ghp_) immediately and SAVE IT - shown only once.
3.2  Create 4 secret Gists. For EACH one: open https://gist.github.com , set the filename, put exactly {} (two curly braces) as the content, and click "Create secret gist" (NOT public). Treat each secret Gist URL/ID as sensitive because anyone with the URL can view it. Then copy the URL - the ID is the long string after the last slash (e.g. gist.github.com/name/abc123 -> the ID is abc123). Have me save each ID with the label shown:
        filename signal_state.json      -> save its ID as GIST_ID
        filename trading_state.json     -> save its ID as TRADING_GIST_ID
        filename intraday_state.json    -> save its ID as INTRADAY_GIST_ID
        filename aggressive_state.json  -> save its ID as AGGRESSIVE_GIST_ID
     I now have 4 saved Gist IDs.

========================================================
PHASE 4 - EMAIL ALERTS VIA GMAIL (~10 min)
========================================================
4.1  Use an existing Gmail or make a new one (a new one keeps bot mail separate).
4.2  Turn on 2-Step Verification (required for app passwords): https://myaccount.google.com/security -> "2-Step Verification" -> turn on if off (needs my phone).
4.3  Create an app password: https://myaccount.google.com/apppasswords -> name "Crypto Forge Labs Bot" -> "Create" -> Google shows a 16-character password. Tell me to COPY and SAVE it immediately (shown once).
     I now have saved: my Gmail ADDRESS and the 16-character APP PASSWORD.

========================================================
PHASE 5 - TELEGRAM ALERTS (OPTIONAL, ~10 min)
========================================================
Tell me I can skip this whole phase if I only want email. If I skip it, I'll leave the two Telegram secrets blank in Phase 6.
5.1  If needed, install Telegram (https://telegram.org).
5.2  In Telegram, search @BotFather, send /newbot, set a name ("Crypto Forge Labs Bot") and a unique username ending in "bot". BotFather gives a TOKEN - have me copy and save it.
5.3  Get my chat ID: search for my new bot by its username, tap "Start" (or send "hello"), then open in a browser:
        https://api.telegram.org/bot<MY_BOT_TOKEN>/getUpdates
     (replace <MY_BOT_TOKEN> with the token). In the response find "chat":{"id": followed by a number - that number is my CHAT ID. Save it.

========================================================
PHASE 6 - ENTER SECRETS AND VARIABLES INTO MY FORK (~20 min)
========================================================
This is the longest phase. Two different pages. Tell me: for SECRETS I paste each value directly into GitHub, never into this chat. Even one extra space breaks it.

6.1  SECRETS - open https://github.com/MY-USERNAME/crypto-yall/settings/secrets/actions and click "New repository secret" for EACH of these 12. Name it exactly, then paste the matching value I saved:
        HL_PRIVATE_KEY        -> my API wallet private key (0x..., from 2.4)
        HL_ACCOUNT_ADDRESS    -> my main account address (0x..., from 2.4)
        GIST_TOKEN            -> my GitHub token (ghp_..., from 3.1)
        GIST_ID               -> the signal_state.json Gist ID
        TRADING_GIST_ID       -> the trading_state.json Gist ID
        INTRADAY_GIST_ID      -> the intraday_state.json Gist ID
        AGGRESSIVE_GIST_ID    -> the aggressive_state.json Gist ID
        GMAIL_USER            -> my Gmail address
        GMAIL_APP_PASSWORD    -> my 16-character app password
        NOTIFY_EMAILS         -> the email(s) to alert, comma-separated (just mine is fine)
        TELEGRAM_BOT_TOKEN    -> my Telegram bot token (or leave blank if I skipped Phase 5)
        TELEGRAM_CHAT_ID      -> my Telegram chat ID (or leave blank if I skipped Phase 5)
     That's 12 secrets. After I finish, remind me to count them (12, or 10 filled in if I skipped Telegram).

6.2  VARIABLES - open https://github.com/MY-USERNAME/crypto-yall/settings/variables/actions and click "New repository variable" for EACH of these 13. Use these EXACT names and values (these are the safe testnet defaults):
        HL_TESTNET                 = true     (use fake money, not real)
        KILL_SWITCH                = ON       (Daily bot enabled)
        INTRADAY_KILL_SWITCH       = ON       (Intraday bot enabled)
        AGGRESSIVE_KILL_SWITCH     = ON       (Aggressive bot enabled)
        SEGREGATED_CAPITAL         = 1000     (Daily bot pretend capital)
        INTRADAY_CAPITAL           = 500      (Intraday bot pretend capital)
        AGGRESSIVE_CAPITAL         = 300      (Aggressive bot pretend capital)
        DAILY_DD_PCT               = 5        (Daily bot: pause for the day after a 5% loss)
        INTRADAY_DD_PCT            = 5        (Intraday bot: pause after a 5% loss)
        AGGRESSIVE_DD_PCT          = 3        (Aggressive bot: pause after a 3% loss)
        MAX_POSITIONS              = 4        (Daily bot max open positions)
        INTRADAY_MAX_POSITIONS     = 2        (Intraday bot max open positions)
        AGGRESSIVE_MAX_POSITIONS   = 4        (Aggressive bot max open positions)
     That's 13 variables. After I finish, help me confirm each name is spelled exactly right.

========================================================
PHASE 7 - TEST TRADE + FIRST RUNS (~10 min)
========================================================
7.1  Run the test trade (places a tiny $10 BTC trade and closes it right away):
     - Have me open https://github.com/MY-USERNAME/crypto-yall/actions , click "Test Trade" in the left sidebar, click the "Run workflow" dropdown, then the green "Run workflow" button.
     - Wait ~1 minute, click into the new run, click the "trade" job, and read the output. Success looks like:
           Account equity: $1000.00
           Placing test LONG: ... BTC @ market
           Open response: {'status': 'ok', ...}
           Final equity: ~$999.98
       A tiny equity dip is just slippage - normal.
7.2  If it FAILED, use the TROUBLESHOOTING table below to fix it, then rerun.
7.3  Trigger each bot once so I don't have to wait for the schedule: in the Actions tab, run "Execute Trades", wait a minute, run "Execute Intraday", wait a minute, run "Execute Aggressive". Seeing "Decided on X trade(s)" means it's live.

========================================================
PHASE 8 - WRAP UP
========================================================
Have me bookmark these (replace MY-USERNAME):
   Repo:      https://github.com/MY-USERNAME/crypto-yall
   Actions:   https://github.com/MY-USERNAME/crypto-yall/actions
   Secrets:   https://github.com/MY-USERNAME/crypto-yall/settings/secrets/actions
   Variables: https://github.com/MY-USERNAME/crypto-yall/settings/variables/actions
Then tell me the two everyday controls:
   - PAUSE a bot: set its kill switch variable (KILL_SWITCH / INTRADAY_KILL_SWITCH / AGGRESSIVE_KILL_SWITCH) to OFF. Set back to ON to resume.
   - CHANGE how much a bot trades: edit its capital variable (SEGREGATED_CAPITAL / INTRADAY_CAPITAL / AGGRESSIVE_CAPITAL). Each trade risks about 1-1.5% of that number. Changes apply on the next scheduled run.

========================================================
TROUBLESHOOTING (use these exact fixes if a step fails)
========================================================
- "User or API Wallet does not exist"  -> the API wallet wasn't authorized on TESTNET. Redo Phase 2.4 on https://app.hyperliquid-testnet.xyz/API (make sure it's the testnet url).
- "Account equity: $0.00"               -> testnet not funded. Redo Phase 2.3 and claim the faucet.
- "private key must be exactly 32 bytes"-> the HL_PRIVATE_KEY secret is wrong. It must be 0x followed by exactly 64 hex characters. Re-enter it.
- "Could not load state from Gist"      -> a Gist ID or the GIST_TOKEN is wrong. Re-check the 4 IDs and the token.
- No email alerts                        -> check the run's output for an "Email sent to..." line, check spam, verify NOTIFY_EMAILS and GMAIL_APP_PASSWORD (try regenerating the app password).
- "GitHub Actions disabled on this fork" -> Phase 1.3 wasn't done. Enable Actions.
- Constant "0 trades executed" emails    -> normal in a quiet market; the bot is running, no signals fired.

HEADS-UP TO TELL ME ONCE, NEAR THE END (so I'm not surprised later):
GitHub Actions usage limits and pricing can change. Near the end, remind me to check the current Actions usage for my plan. The Aggressive bot runs frequently and can consume a large share of included Actions minutes. If usage becomes an issue, I can reduce or pause its schedule, or review GitHub's current plan options. GitHub Secrets are not displayed in the public repository, but I should still review workflow code before enabling it.

Start with Phase 1, step 1.1. Ask me for my GitHub username when we get there, and wait for my confirmation between every step. Let's go.

=== STOP COPYING ===
```

---

## What to Expect

The AI will:

1. **Ask if you have a GitHub account.** Help you sign up if needed.
2. **Walk you through forking the repo.** Click by click, using your username.
3. **Pause and wait** for you to say "done" before moving on.
4. **Ask you for the result of each step.** For example, after you create a Gist, it'll ask you to paste the Gist URL so it can extract the ID.
5. **Remind you to save important values** (private keys, tokens, app passwords) to your own notes — never into the chat.
6. **Debug with you** if something fails, using the troubleshooting steps baked into the prompt.

A typical conversation looks like this:

> **You:** *(paste the prompt)*
>
> **AI:** Great, let's start. First, do you already have a GitHub account, or do you need to create one?
>
> **You:** I have one
>
> **AI:** Perfect. What's your GitHub username? I'll use it in the links as we go.
>
> **You:** mygithubname
>
> **AI:** Thanks. Step 1.2: go to https://github.com/Crypto-Forge-Labs/crypto-yall and click "Fork" in the top right, then "Create fork". You'll land on https://github.com/mygithubname/crypto-yall. Done? Reply 'done' when you've forked it.
>
> *... and so on, one step at a time*

---

## Security Notes

When using an AI assistant for setup, follow these rules:

### Things you CAN share with the AI:
- Your GitHub username
- The Gist ID only, if needed for troubleshooting. Avoid sharing secret Gist URLs unnecessarily.
- Your Hyperliquid main wallet address, if needed for troubleshooting (it is public blockchain information)
- Error messages from failed steps
- Screenshots of confusing UI

### Things you should NEVER share with the AI:
- **Private keys** (API wallet private key, your main wallet seed phrase)
- **Passwords** (Gmail app password, anything else)
- **API tokens** (GitHub token, Telegram bot token)
- **Anything you saved as a "secret"**

The prompt tells the AI never to ask for these. If it ever does, something's off — refuse and re-paste the original prompt.

The reason: private values should stay out of chat transcripts. The AI does not need the secret itself to guide setup — it only needs to tell you *where in GitHub* to paste it.

### How to handle "secret" values:

When the AI says something like "now add `HL_PRIVATE_KEY` to your GitHub Secrets":

1. You open the GitHub Secrets page
2. You paste the value directly into GitHub (NOT into the chat)
3. You tell the AI "done" without showing it the value
4. The AI moves on

---

## What If the AI Gets Something Wrong?

This prompt now contains the exact URLs, names, and values, so hallucinations are far less likely than with older versions. But AI can still occasionally slip, especially on Hyperliquid screens that change over time.

If the AI tells you something that doesn't match what you see, or a step fails:

1. **Don't panic.** Most issues are easy to fix.
2. **Trust the screen over the AI.** If the AI describes a button that isn't there, tell it exactly what you *do* see.
3. **Refer to [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md)** — the authoritative manual version, with the same steps in written form.
4. **If you're still stuck**, review the workflow logs and the troubleshooting guide, then ask for help using the step number and the exact error message. Never include private keys, passwords, seed phrases, or tokens.

---

## Tips for Better Results

### Be specific when stuck

Instead of: "it didn't work"

Try: "I clicked Run Workflow and got this error in the logs: 'private key must be exactly 32 bytes'. Here's a screenshot."

### Verify critical values

After setup, double-check by hand:
- All 12 GitHub Secrets are present (count them at `https://github.com/your-username/crypto-yall/settings/secrets/actions`) — or 10 filled in if you skipped Telegram
- All 13 GitHub Variables are present (at `https://github.com/your-username/crypto-yall/settings/variables/actions`)
- The test trade workflow ran successfully (at your Actions tab)

### Use the same AI thread throughout

Stay in the same chat where possible so the setup context remains together. If you need to start a new chat, tell the AI which phase and step you reached.

### Don't multitask

You can pause if needed. When you come back, state the phase and step you last completed so the AI can continue accurately.

---

## After Setup is Complete

1. **Save the AI conversation** — a useful reference if something breaks later
2. **Bookmark these URLs:**
   - Your forked repo: `https://github.com/<your-username>/crypto-yall`
   - Your Actions tab: `https://github.com/<your-username>/crypto-yall/actions`
   - Your Secrets: `https://github.com/<your-username>/crypto-yall/settings/secrets/actions`
   - Your Variables: `https://github.com/<your-username>/crypto-yall/settings/variables/actions`
3. **Read [QUICKSTART.md](QUICKSTART.md)** — the daily operations guide
4. **Read [TROUBLESHOOTING.md](TROUBLESHOOTING.md)** — for when issues come up later

---

## Sample Follow-Up Prompts

Once setup is done, you can keep using the AI for ongoing operations:

### "My bot stopped sending alerts. Help me debug."
Paste that into a new chat and describe what you're seeing.

### "I want to pause the Aggressive bot for the weekend."
The AI can walk you through setting `AGGRESSIVE_KILL_SWITCH` to `OFF`.

### "I want to change how much the Daily bot trades."
The AI can walk you through editing `SEGREGATED_CAPITAL`.

### "I'm ready to go from testnet to mainnet. Walk me through it."
Point it at [MAINNET_LAUNCH.md](MAINNET_LAUNCH.md) and ask it to be your guide.

### "I want to add my friend's email to the alerts list."
The AI can walk you through updating the `NOTIFY_EMAILS` secret.

---

## Frequently Asked Questions

**Q: Which AI should I use?**

A: Use whichever AI assistant you're comfortable with. The important part is to paste the full setup prompt and keep the same conversation open while you work through the phases.

**Q: Do I need a paid AI plan?**

A: Not necessarily. Use a plan that supports a conversation long enough to work through the setup prompt.

**Q: Can I do this on my phone?**

A: Technically yes, but it's much easier on a computer because you'll navigate a lot of GitHub UI.

**Q: What if my AI conversation gets too long and it starts forgetting context?**

A: Tell it where you are: "We've finished Phases 1-4 and just set up Gmail. Now starting Phase 5 (Telegram)." Then continue.

**Q: Is this setup really safe?**

A: The setup is designed so your credentials stay in your own accounts and GitHub Secrets. Never paste private keys, passwords, seed phrases, or tokens into an AI chat. Test on Hyperliquid testnet first, review the code and workflow permissions, and only use mainnet when you understand the risks and controls.

**Q: Can I skip the AI and just do it manually?**

A: Yes — [USER_SETUP_GUIDE.md](USER_SETUP_GUIDE.md) has the same content in manual click-by-click form.