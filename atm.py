#!/usr/bin/env python3
"""
Bank ATM Simulator (CLI)
Author: Hewad Rustom
Description: Simple ATM with PIN login, balance, deposit, withdraw, mini statement, and PIN change.
Data is stored in account.json in the same folder.
"""

import json
import os
import hashlib
from datetime import datetime

DATA_FILE = "account.json"
CURRENCY = "£"


# ---------------------- Utilities ----------------------
def hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def load_account() -> dict:
    """Load or initialize the account file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    # First run: create a fresh account with default PIN 1234
    acct = {
        "pin_hash": hash_pin("1234"),
        "balance": 0.0,
        "transactions": []  # each: {time, type, amount, balance_after}
    }
    save_account(acct)
    return acct


def save_account(account: dict) -> None:
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(account, f, indent=2)


def fmt_money(amount: float) -> str:
    return f"{CURRENCY}{amount:,.2f}"


def input_money(prompt: str) -> float:
    """Read a positive monetary amount with up to 2 decimals."""
    while True:
        raw = input(prompt).strip()
        try:
            value = round(float(raw), 2)
            if value <= 0:
                print("Amount must be greater than 0.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number (e.g. 25 or 25.50).")


def record_tx(account: dict, tx_type: str, amount: float) -> None:
    account["transactions"].append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": tx_type.upper(),  # DEPOSIT / WITHDRAW
        "amount": round(amount, 2),
        "balance_after": round(account["balance"], 2),
    })
    # Keep file up to date
    save_account(account)


# ---------------------- Auth ----------------------
def verify_pin(account: dict) -> bool:
    """3 attempts to enter correct PIN."""
    for attempts_left in [3, 2, 1]:
        entered = input("Enter 4-digit PIN: ").strip()
        if len(entered) == 4 and entered.isdigit():
            if hash_pin(entered) == account["pin_hash"]:
                return True
        if attempts_left > 1:
            print(f"Incorrect PIN. Attempts left: {attempts_left - 1}")
    return False


def change_pin(account: dict) -> None:
    print("\n-- Change PIN --")
    current = input("Enter current PIN: ").strip()
    if hash_pin(current) != account["pin_hash"]:
        print("Current PIN is incorrect.")
        return
    new_pin = input("Enter new 4-digit PIN: ").strip()
    if not (len(new_pin) == 4 and new_pin.isdigit()):
        print("PIN must be exactly 4 digits.")
        return
    confirm = input("Re-enter new PIN: ").strip()
    if new_pin != confirm:
        print("PINs do not match.")
        return
    account["pin_hash"] = hash_pin(new_pin)
    save_account(account)
    print("✅ PIN changed successfully.")


# ---------------------- Actions ----------------------
def show_balance(account: dict) -> None:
    print(f"\nCurrent balance: {fmt_money(account['balance'])}")


def deposit(account: dict) -> None:
    print("\n-- Deposit --")
    amount = input_money("Enter amount to deposit: ")
    if amount > 10000:
        print("For safety, single deposit must be ≤ 10,000.")
        return
    account["balance"] = round(account["balance"] + amount, 2)
    record_tx(account, "DEPOSIT", amount)
    print(f"✅ Deposited {fmt_money(amount)}. New balance: {fmt_money(account['balance'])}")


def withdraw(account: dict) -> None:
    print("\n-- Withdraw --")
    amount = input_money("Enter amount to withdraw: ")
    if amount > account["balance"]:
        print("Insufficient funds.")
        return
    account["balance"] = round(account["balance"] - amount, 2)
    record_tx(account, "WITHDRAW", amount)
    print(f"✅ Withdrew {fmt_money(amount)}. New balance: {fmt_money(account['balance'])}")


def mini_statement(account: dict) -> None:
    print("\n-- Mini Statement (last 5) --")
    txs = account["transactions"][-5:]
    if not txs:
        print("No transactions yet.")
        return
    for tx in txs:
        print(f"{tx['time']}  {tx['type']:8}  {fmt_money(tx['amount']):>10}  "
              f"Balance: {fmt_money(tx['balance_after'])}")


# ---------------------- Menu Loop ----------------------
def menu() -> str:
    print("\n=== ATM Menu ===")
    print("1) Show balance")
    print("2) Deposit")
    print("3) Withdraw")
    print("4) Mini statement")
    print("5) Change PIN")
    print("0) Exit")
    return input("Select an option: ").strip()


def main():
    print("Welcome to the Bank ATM Simulator")
    account = load_account()

    if not verify_pin(account):
        print("Too many incorrect attempts. Card retained (just kidding). Goodbye.")
        return

    while True:
        choice = menu()
        if choice == "1":
            show_balance(account)
        elif choice == "2":
            deposit(account)
        elif choice == "3":
            withdraw(account)
        elif choice == "4":
            mini_statement(account)
        elif choice == "5":
            change_pin(account)
        elif choice == "0":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
