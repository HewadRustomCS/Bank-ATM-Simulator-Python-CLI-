# 🏦 Bank ATM Simulator (Python CLI)

A simple, professional ATM simulation you can run in the terminal. It supports PIN login, checking balance, deposits, withdrawals, a mini statement (last 5 transactions), and changing your PIN. Data is saved to `account.json` so your balance persists between runs.

## 🚀 Features
- 4-digit PIN login (default PIN on first run: **1234**)
- Check **balance**
- **Deposit** (with basic safety limit)
- **Withdraw** (with insufficient funds checks)
- **Mini statement** (last 5 transactions with timestamps)
- **Change PIN** (with confirmation)
- Persistent storage in `account.json`

## 🛠️ How to Run
```bash
python atm.py
