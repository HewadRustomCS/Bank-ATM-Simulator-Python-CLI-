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
Welcome to the Bank ATM Simulator
Enter 4-digit PIN: 1234

=== ATM Menu ===
1) Show balance
2) Deposit
3) Withdraw
4) Mini statement
5) Change PIN
0) Exit
Select an option: 2

-- Deposit --
Enter amount to deposit: 150
✅ Deposited £150.00. New balance: £150.00

=== ATM Menu ===
Select an option: 3

-- Withdraw --
Enter amount to withdraw: 40
✅ Withdrew £40.00. New balance: £110.00

=== ATM Menu ===
Select an option: 4

-- Mini Statement (last 5) --
2025-09-07 13:45:02  DEPOSIT     £150.00  Balance: £150.00
2025-09-07 13:46:11  WITHDRAW     £40.00  Balance: £110.00
---

## 📖 What I Learned
- File I/O and JSON persistence in Python  
- Input validation and error handling  
- Basic authentication with hashed PINs  
- Clean CLI menu design and modular functions  
