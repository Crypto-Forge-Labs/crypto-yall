# Crypto Forge Labs — Mainnet Launch Guide

This guide explains how to move a Crypto Forge Labs setup from Hyperliquid testnet (mock funds) to mainnet (real funds).

> **Important:** Mainnet uses real money. Read the entire guide before changing `HL_TESTNET` or authorizing a live API wallet.
>
> **Project note:** Crypto Forge Labs is based on the upstream `aicodepathways/crypto-yall` project. This guide assumes you are running your own fork, your own Hyperliquid account, and your own credentials.

---

## What "Mainnet" Means

On **testnet**, the bots trade with mock funds.

On **mainnet**, the bots can place real orders using real USDC in your Hyperliquid account.

The switch between environments is controlled by:

`HL_TESTNET`

- `true` = testnet
- `false` = mainnet

Changing this variable is the **last** step, not the first.

---

## Before You Consider Mainnet

You should be able to answer "yes" to all of these:

- [ ] I have run the bots on testnet long enough to understand their normal behaviour
- [ ] I have seen the bots operate in more than one type of market condition
- [ ] I understand the alerts and workflow logs
- [ ] I have successfully paused and resumed each bot
- [ ] I understand the difference between Daily, Intraday, and Aggressive
- [ ] I know how to set all three kill switches to `OFF`
- [ ] I understand that leveraged perpetual trading can cause substantial or total loss of the capital I allocate
- [ ] I know how much money I am prepared to lose without affecting essential expenses
- [ ] I have considered the tax and legal implications that apply in my own jurisdiction
- [ ] I understand that testnet and historical results do not guarantee mainnet performance

If any of these are "no," remain on testnet.

---

## About Shared Accounts and Sub-Accounts

The standard Crypto Forge Labs setup uses one Hyperliquid account for all three bots.

Each bot tracks its own intended positions in its own state Gist, but Hyperliquid may show the **net exchange position** when two bots trade the same asset in opposite directions.

Sub-accounts can provide cleaner separation if your Hyperliquid account is eligible for them.

Because Hyperliquid requirements and features can change, check the current Hyperliquid interface and documentation before relying on a particular sub-account eligibility threshold.

This guide assumes the normal **single-account** setup unless you intentionally configure sub-accounts.

---

## Pre-Launch Checklist

Complete these in order:

- [ ] **Step 1:** Choose a small starting allocation
- [ ] **Step 2:** Authorize an API wallet on mainnet
- [ ] **Step 3:** Fund your Hyperliquid mainnet account
- [ ] **Step 4:** Review and tighten risk settings
- [ ] **Step 5:** Reset testnet state before live trading
- [ ] **Step 6:** Run a tiny mainnet test trade
- [ ] **Step 7:** Confirm `HL_TESTNET = false`
- [ ] **Step 8:** Watch the first live runs closely
- [ ] **Step 9:** Scale only if you choose to do so after successful monitoring

---

## Step 1: Choose a Small Starting Allocation

The Crypto Forge Labs testnet defaults are:

| Bot | Testnet capital variable |
|---|---:|
| Daily | `1000` |
| Intraday Standard | `500` |
| Aggressive | `300` |

For mainnet, do **not** assume you must use those exact amounts.

Choose an amount you can afford to lose and understand that the three bots share the same Hyperliquid account unless you have deliberately configured sub-accounts.

### Why start small?

- Mainnet includes real fees and slippage
- Actual fills may differ from testnet
- Shared-account netting becomes important when real positions are involved
- You need time to verify that alerts, state tracking, and exchange positions match
- Smaller exposure reduces the financial impact of a configuration mistake

Do not scale because of one profitable trade or one profitable day.

---

## Step 2: Authorize Your API Wallet on Mainnet

Testnet and mainnet are separate environments.

A testnet-authorized API wallet should not be assumed to be authorized for mainnet.

1. Open:
   https://app.hyperliquid.xyz
2. Connect **your own main wallet**
3. Open:
   https://app.hyperliquid.xyz/API
4. Generate or authorize an API wallet for mainnet
5. Save the private key securely
6. Store the key only in your own GitHub Secret:
   `HL_PRIVATE_KEY`
7. Confirm your main account address is stored in:
   `HL_ACCOUNT_ADDRESS`

Never paste the API private key into:
- An AI chat
- GitHub code
- A public issue
- A screenshot
- A message to another person

If you generate a separate live key, keep the testnet and mainnet keys clearly labelled in your own secure notes.

---

## Step 3: Fund Hyperliquid Mainnet

Only fund the account with an amount you have independently decided you are prepared to risk.

Use the current Hyperliquid deposit flow shown in your account.

Before transferring funds:

- Confirm you are on the real Hyperliquid mainnet site
- Confirm the source network and asset shown in the interface
- Confirm the destination shown by Hyperliquid
- Start with an amount you are comfortable testing with
- Verify the deposit appears in your Hyperliquid account before proceeding

Do not proceed merely because a bot workflow is waiting.

---

## Step 4: Review and Tighten Risk Settings

Open your own fork's Variables page:

`https://github.com/<your-username>/crypto-yall/settings/variables/actions`

The testnet defaults are:

| Variable | Testnet default |
|---|---:|
| `DAILY_DD_PCT` | `5` |
| `INTRADAY_DD_PCT` | `5` |
| `AGGRESSIVE_DD_PCT` | `3` |
| `MAX_POSITIONS` | `4` |
| `INTRADAY_MAX_POSITIONS` | `2` |
| `AGGRESSIVE_MAX_POSITIONS` | `4` |

For real money, you may choose tighter drawdown limits and smaller capital allocations.

A conservative example would be:

| Variable | Example tighter value |
|---|---:|
| `DAILY_DD_PCT` | `3` |
| `INTRADAY_DD_PCT` | `3` |
| `AGGRESSIVE_DD_PCT` | `2` |

These are examples, not guarantees of safety.

Also review:

- `SEGREGATED_CAPITAL`
- `INTRADAY_CAPITAL`
- `AGGRESSIVE_CAPITAL`

Set them deliberately. Do not copy a value from someone else's account.

---

## Step 5: Reset Testnet State Before Live Trading

The bots remember state in their Gists.

Before moving to mainnet, clear the testnet state so the bots do not carry testnet ownership records into the live environment.

### State Gists to reset

- `trading_state.json`
- `intraday_state.json`
- `aggressive_state.json`

Replace the contents of each with:

```json
{}
```

If you want to preserve your testnet history, save a copy before resetting.

You may also reset `signal_state.json` if you want signal-alert memory to start fresh.

Secret Gists are unlisted, not fully private. Keep their URLs and IDs private.

---

## Step 6: Run a Tiny Mainnet Test Trade

Before enabling normal live operation, verify that the bot can:

- Authenticate to mainnet
- Read account equity
- Place an order
- Confirm the fill
- Close the test position

### Procedure

1. Set all three trading kill switches to `OFF`
2. Temporarily set:
   `HL_TESTNET = false`
3. Open:
   `https://github.com/<your-username>/crypto-yall/actions`
4. Select **Test Trade**
5. Run the workflow
6. Open the run log
7. Confirm the test order opens and closes successfully
8. Verify the result directly on Hyperliquid

A small difference in equity can occur because of fees and execution price.

If the test fails:

- Do **not** enable the normal bots
- Read the error
- Check the troubleshooting guide
- Verify the correct mainnet API wallet
- Verify `HL_ACCOUNT_ADDRESS`
- Verify the account is funded

---

## Step 7: Confirm the Mainnet Flag

When you are satisfied with the mainnet test:

1. Open:
   `https://github.com/<your-username>/crypto-yall/settings/variables/actions`
2. Find:
   `HL_TESTNET`
3. Confirm it is:
   `false`

At this point the workflows are configured for real-money trading.

Keep the three bot kill switches `OFF` until you are ready to enable each bot.

---

## Step 8: Enable and Watch the First Live Runs

Do not turn all three bots on blindly.

A safer sequence is:

1. Enable one bot
2. Watch its workflow
3. Verify any exchange position directly on Hyperliquid
4. Confirm the alert matches the actual fill
5. Confirm its state Gist updates correctly
6. Continue monitoring before enabling additional bots

For the first live period, compare:

- GitHub Actions logs
- Email/Telegram alerts
- State Gists
- Hyperliquid positions
- Hyperliquid account equity

### If anything does not match

1. Set all relevant kill switches to `OFF`
2. Check Hyperliquid directly
3. Do not assume the dashboard is correct
4. Review the workflow logs
5. Investigate before resuming

---

## Step 9: Scale Only Deliberately

There is no required scaling schedule.

If you decide to increase capital:

1. Review live results over a meaningful period
2. Review drawdowns, not only profits
3. Check whether shared-account netting caused confusion
4. Verify your alerts and state tracking remained reliable
5. Increase exposure only by an amount you can afford to lose

Do not automatically double or multiply capital just because the bot had a profitable week.

---

## What to Do If Something Goes Wrong on Mainnet

### One unexpected trade

1. Pause the affected bot
2. Check the workflow log
3. Check the actual Hyperliquid fill
4. Compare the bot's state Gist
5. Resume only after you understand what happened

### Repeated errors

1. Set the affected bot's kill switch to `OFF`
2. Review the exact repeated error
3. Check credentials and environment
4. Confirm the exchange account state
5. Leave the bot paused until the cause is identified

### Unexpected large loss or position

1. Set **all three kill switches to `OFF`**
2. Open Hyperliquid directly
3. Review all open positions
4. If you decide to exit, close the relevant positions manually
5. Save screenshots/logs with secrets hidden
6. Investigate before re-enabling anything

Do not try to recover a loss by increasing position size or rapidly changing settings.

---

## Rolling Back to Testnet

If you decide to stop live operation:

1. Set all bot kill switches to `OFF`
2. Review and close any live positions you want to exit
3. Withdraw live funds if that is your decision
4. Change:
   `HL_TESTNET = true`
5. Confirm the correct testnet API wallet is configured
6. Reset or restore the testnet state Gists as needed
7. Re-enable only the bots you want to test

Do not flip environments while live positions are still being managed without first understanding the consequences.

---

## Trading Costs

Mainnet trading can involve:

- Trading fees
- Slippage
- Perpetual funding payments or receipts
- Network/bridge costs
- Possible tax/accounting costs

Fee schedules and funding mechanics can change.

Check Hyperliquid's current fee information rather than relying on fixed percentages in this guide.

---

## GitHub Actions Usage

The three workflows run frequently, particularly the Aggressive bot.

GitHub Actions usage limits and pricing depend on:
- Repository visibility
- Your GitHub plan
- Current GitHub policies
- Workflow duration

Check your current GitHub Actions usage and billing information in GitHub.

If usage becomes too high:
- Pause a bot
- Reduce schedule frequency
- Review your GitHub plan/options

Do not assume an old Actions-minute allowance or price is still current.

---

## Streamlit Dashboard Cost

A dashboard is optional.

If you deploy Streamlit or another hosting service, check that service's current pricing and limits.

The trading workflows do not require a dashboard in order to run.

---

## Tax and Legal Notice

This guide is operational, not legal, tax, or investment advice.

Real-money crypto and derivatives trading can create:
- Tax reporting obligations
- Record-keeping requirements
- Regulatory considerations
- Exchange/platform terms you must follow

The exact rules depend on where you live and your circumstances.

Keep records of:
- Deposits and withdrawals
- Trades and fills
- Fees
- Funding payments/receipts
- Realized gains and losses

For meaningful real-money activity, consider obtaining advice from an appropriately qualified tax or legal professional in your jurisdiction.

---

## Summary

Moving to mainnet should be deliberate.

1. **Understand the system on testnet**
2. **Use your own mainnet API wallet**
3. **Start with limited exposure**
4. **Review drawdown and position settings**
5. **Reset testnet state**
6. **Run a tiny live connection/trade test**
7. **Enable bots gradually**
8. **Verify exchange positions directly**
9. **Scale only if you independently decide the risk is acceptable**

Mainnet is not simply "testnet with real money." Real execution introduces real financial consequences.

---

## Final Reminder

Testnet and historical results do not guarantee future results.

Real-money trading introduces:

- Real fees
- Real slippage
- Real liquidation risk
- Real operational risk
- Real tax/accounting consequences
- Real financial loss

There is no urgency to move to mainnet.

Stay on testnet until you understand the system well enough to operate and stop it without relying on someone else.

---

## Optional: Sub-Account Setup

Only use this section if your Hyperliquid account currently supports sub-accounts and you understand how they work.

### Why use sub-accounts?

Potential benefits include:

- Separate margin per bot
- Reduced netting between opposite bot positions
- Cleaner accounting
- Easier separation of strategies

### Example names

- `Crypto Forge Labs Daily`
- `Crypto Forge Labs Intraday`
- `Crypto Forge Labs Aggressive`

### Security rule

For each sub-account:

- Keep its API private key private
- Store the key only in your own secure secret storage
- Never send the private key to another person
- Never commit it to GitHub

### Code support

The standard Crypto Forge Labs fork uses one shared Hyperliquid credential set.

Using a separate API wallet for each sub-account requires a deliberate code/configuration change, for example separate secrets such as:

- `HL_DAILY_KEY`
- `HL_INTRADAY_KEY`
- `HL_AGGRESSIVE_KEY`

Do not assume these separate-key variables work unless the executor code has actually been updated to use them.

Test any such modification on testnet or in a non-live environment before using real money.

---

*Crypto Forge Labs mainnet launch guide — August 2026*
