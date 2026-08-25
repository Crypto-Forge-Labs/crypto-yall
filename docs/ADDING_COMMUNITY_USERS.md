# Adding Community Members to Crypto Forge Labs

This guide explains practical ways to let other people use or follow the Crypto Forge Labs trading system.

> **Project note:** Crypto Forge Labs is based on the upstream `aicodepathways/crypto-yall` project. The preferred community setup is for each user to run their own fork, their own Hyperliquid account, and their own credentials.

---

## Important Principle: Keep Users Isolated

The safest structure is:

- Each person uses **their own GitHub account**
- Each person forks `https://github.com/Crypto-Forge-Labs/crypto-yall`
- Each person uses **their own Hyperliquid account**
- Each person creates **their own API wallet**
- Each person creates **their own GitHub Gists**
- Each person creates **their own Gmail/Telegram alerts**
- Each person stores credentials only in **their own GitHub Secrets**

Do not collect or centrally store other users' private keys unless you have intentionally built and reviewed infrastructure designed for that purpose.

---

## Three Ways to Share the System

### Option A: Signal-Only Service

**What it is:** Users receive trading signals or alerts and decide for themselves whether to place a trade.

**How it can work:**
1. A reference instance generates signals.
2. Users receive alerts by email, Telegram, Discord, or another channel.
3. Users decide whether to act.
4. Users place trades manually in their own accounts.

**Advantages:**
- Simplest operational model
- No need to handle users' trading credentials
- Users retain control over position sizing and whether to trade
- Easy to test whether people find the signals useful

**Limitations:**
- Users can miss signals
- Execution price can differ from the signal price
- Users may interpret or size trades differently
- You still need clear terms, risk disclosures, and appropriate legal/compliance review for your jurisdiction

**Best for:** Sharing information without operating users' trading accounts.

---

### Option B: Personal Bot Fork Per User — Recommended

**What it is:** Each user runs a complete personal copy of Crypto Forge Labs under their own GitHub account.

**How it works:**
1. User creates or signs into GitHub.
2. User forks:
   `https://github.com/Crypto-Forge-Labs/crypto-yall`
3. User configures their own:
   - Hyperliquid account and API wallet
   - Secret GitHub Gists for state
   - Gmail alerts
   - Optional Telegram alerts
   - GitHub Secrets
   - GitHub Variables
4. Their bot runs from their own GitHub Actions.
5. They control their own kill switches and capital settings.

**Advantages:**
- Strong separation between users
- Each user controls their own credentials
- No need for Crypto Forge Labs to hold users' API keys
- Each user can pause or customize their own bot
- A problem in one user's configuration does not automatically expose another user's credentials

**Limitations:**
- Setup takes time
- Users may need help with GitHub and Hyperliquid
- Different forks can end up on different code versions
- Updates may need to be merged into existing forks

**Best for:** Users who want automated trading while keeping control of their own account and credentials.

---

### Option C: Multi-User Hosted Platform

**What it is:** A centralized service runs strategies for many users.

A production version could require:
- User accounts and authentication
- A database for user settings and bot state
- Secure key-management infrastructure
- Encryption at rest and in transit
- Per-user trade execution
- Per-user dashboards and alerts
- Audit logging
- Monitoring and incident response
- Billing, if offered commercially
- Legal, regulatory, tax, privacy, and security review

**Important:** A centralized platform materially changes the risk profile because the operator may receive or process users' trading credentials and potentially influence or automate trading on their behalf.

Do not treat this as a simple extension of the current GitHub-fork model.

**Best for:** A deliberately designed commercial product after technical, security, and legal review.

---

## Recommended Community Model

For Crypto Forge Labs, the recommended model is **Option B: one personal fork per user**.

That means the person you share it with should:

1. Open:
   `https://github.com/Crypto-Forge-Labs/crypto-yall`
2. Fork the repository to their own GitHub account.
3. Follow:
   `docs/AI_ASSISTED_SETUP.md`
   or
   `docs/USER_SETUP_GUIDE.md`
4. Create their own Hyperliquid testnet setup.
5. Create their own Gists and credentials.
6. Test with mock funds before considering mainnet.

You should **not** ask them to send you their:
- Hyperliquid API private key
- Wallet seed phrase
- GitHub Personal Access Token
- Gmail app password
- Telegram bot token

Those values belong only in their own secure storage and GitHub Secrets.

---

## How to Onboard a New User

### Step 1: Send them the Crypto Forge Labs repo

Send:

`https://github.com/Crypto-Forge-Labs/crypto-yall`

Tell them to click **Fork** and create a copy under their own GitHub account.

### Step 2: Point them to the setup guide

For the easiest setup:

`docs/AI_ASSISTED_SETUP.md`

For a full manual guide:

`docs/USER_SETUP_GUIDE.md`

### Step 3: Keep setup values private

Safe things they can share while asking for help:
- GitHub username
- Error messages
- Screenshots with secrets hidden
- Public Hyperliquid account address when genuinely needed
- Variable names and non-secret settings

Things they should never share:
- Private keys
- Seed phrases
- Passwords
- GitHub tokens
- Telegram bot tokens
- Gmail app passwords

### Step 4: Test on Hyperliquid testnet

Before real money:
- Confirm Actions run successfully
- Confirm the test trade works
- Confirm alerts work
- Confirm kill switches work
- Confirm the user understands how to pause the bots
- Review capital and drawdown settings

---

## Optional Signal-Only Alerts

If you intentionally operate a signal-only service, use a separate alert system designed for that purpose rather than mixing other users into a personal trading account.

Good practice includes:
- Clear signal timestamps
- Clear asset and direction
- Clear statement that execution is the user's decision
- No collection of wallet keys
- Easy unsubscribe controls
- Clear risk disclosures
- Appropriate review of applicable laws and platform rules

Avoid representing signals as guaranteed profits or risk-free trading.

---

## What NOT to Do

### Do NOT share your own credentials

Never give another user:
- Your Hyperliquid wallet seed phrase
- Your Hyperliquid API private key
- Your GitHub Personal Access Token
- Your Gmail app password
- Your Telegram bot token

### Do NOT ask users to send you their secrets

A normal personal-fork setup does not require you to receive their:
- API private key
- Seed phrase
- GitHub token
- Gmail app password
- Telegram token

If they need help entering a secret, guide them to the correct screen and ask them to confirm only that the step is complete.

### Do NOT put secrets in the repository

Never commit:
- Private keys
- Passwords
- Tokens
- Seed phrases
- Secret Gist URLs containing sensitive state

Use GitHub Secrets or another appropriate secret-management service.

### Do NOT promise returns

Avoid statements such as:
- "The bot will make money"
- "The strategy is guaranteed"
- "You cannot lose"
- "This is risk-free"

Testnet results, backtests, and historical results do not guarantee future performance.

### Do NOT take custody of another person's funds casually

Do not ask users to transfer funds to your wallet so that you can trade on their behalf.

Handling or controlling other people's funds or trading credentials can create significant security, contractual, legal, tax, and regulatory obligations depending on the jurisdiction and how the service is structured.

Seek appropriate professional advice before offering a managed or centralized service.

---

## Frequently Asked Questions

### "Can I send you my Hyperliquid API key and have you add it for me?"

For the standard Crypto Forge Labs setup: **No.**

Keep the API private key yourself and enter it directly into your own GitHub Secret named:

`HL_PRIVATE_KEY`

The person helping you does not need to see the value.

---

### "Can I set my own position size?"

Yes.

In your own fork, you control:
- `SEGREGATED_CAPITAL`
- `INTRADAY_CAPITAL`
- `AGGRESSIVE_CAPITAL`
- Drawdown thresholds
- Maximum positions
- Kill switches

Use testnet first when changing sizing or risk controls.

---

### "Can I pause my bot without affecting anyone else?"

Yes.

Because each user has their own fork, your kill switches only affect your own bot configuration.

---

### "Will Crypto Forge Labs be able to see my GitHub Secrets?"

Repository secrets are not displayed publicly through the repository interface.

However, workflow code that receives a secret can use that secret while the workflow is running. Users should review workflow code before enabling Actions and should only run code they trust.

---

### "Can people see that I forked Crypto Forge Labs?"

A public GitHub fork can be associated with the upstream fork network and GitHub account that created it.

Do not assume a public fork is anonymous.

---

### "Are secret Gists private?"

No.

GitHub secret Gists are **unlisted**, not fully private. Anyone who obtains the URL can access them.

Treat secret Gist URLs and IDs as sensitive.

---

### "Can I use real money straight away?"

The recommended process is:
1. Set up testnet.
2. Run the test trade.
3. Observe the bots.
4. Test kill switches.
5. Understand the risk controls.
6. Only then decide whether mainnet is appropriate for you.

Real-money leveraged trading can result in substantial losses.

---

## Updating Community Forks

Because users fork the repository, they may not automatically receive every future change.

When Crypto Forge Labs releases an update, users should review what changed before merging or syncing it into their fork.

For important updates:
- Describe what changed
- Explain whether it affects trading logic, security, or configuration
- Encourage users to pause bots before major changes
- Test changes on testnet
- Never overwrite a user's Secrets or Variables

---

## Security Checklist for Community Users

Before enabling Actions:

- [ ] Fork belongs to the user's own GitHub account
- [ ] `HL_TESTNET = true`
- [ ] API wallet is authorized on Hyperliquid testnet
- [ ] API private key is stored only in GitHub Secrets
- [ ] Main wallet seed phrase has never been entered into GitHub
- [ ] Four secret Gists belong to the user
- [ ] Gist token belongs to the user
- [ ] Gmail app password belongs to the user
- [ ] Telegram token/chat ID belong to the user, if used
- [ ] User knows how to set all kill switches to `OFF`
- [ ] Test Trade succeeds before other workflows are trusted

---

## Bottom Line

Crypto Forge Labs should default to a **personal fork per user**.

Each user runs the bot using:
- Their GitHub
- Their Hyperliquid account
- Their API wallet
- Their Gists
- Their Gmail/Telegram
- Their Secrets
- Their Variables

That keeps the current system simple and avoids creating a centralized store of community members' trading credentials.

If Crypto Forge Labs is ever turned into a hosted multi-user service, treat that as a separate product requiring dedicated security architecture and professional legal/compliance review.

---

*Crypto Forge Labs community setup guide — August 2026*
