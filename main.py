#!/usr/bin/env python3

import random

MAX_LINES = 3
MIN_BET = 20
MAX_BET = 500

ROWS = 3
COLS = 3

symbol_count = {
        "A": 2,
        "B": 4,
        "C": 6,
        "D": 8
}

symbol_value = {
        "A": 5,
        "B": 4,
        "C": 3,
        "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if symbol != column[line]:
                break
        else:
            winning_lines.append(line + 1)
            winnings += values[symbol] * bet
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for indx, column in enumerate(columns):
            separator = " | "
            if indx == len(columns) - 1:
                separator = "\n"
            print(column[row], end = separator)



def deposit():
    amount = input("Enter deposit amount: $")
    while True:
        if amount.isdigit(): # check if provided amount is number
            amount = int(amount) # convert amount from string to intiger
            if amount > 0: # check if amount is non-zero
                return amount
            else:
                amount = input("Amount must be greater than zero, try again: $")
        else:
            amount = input("Please provide valid amount (amount must be a number): $")

def get_number_of_lines():
    lines = input("Enter number of lines (min. 1, max " + str(MAX_LINES) +"): ")
    while True:
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                lines = input("Lines must be between 1 and " + str(MAX_LINES) + ", try again: ")
        else:
            lines = input("Enter VALID number of lines from 1 to "+ str(MAX_LINES) +": ")

def get_bet():
    amount = input("Enter bet amount: $")
    while True:
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                amount = input("Bet amount must be between " + str(MIN_BET) + " and " + str(MAX_BET) + ", try again: $")
        else:
            amount = input("Please provide valid bet amount (must be a number): $")

def spin(balance):
    while True:
        bet = get_bet()
        lines = get_number_of_lines()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        print("Total bet exceeds your balance, try again.\nCurrent balance " + str(balance))

    
    print(f"You are betting ${bet} on {lines} line(s). Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"winning lines: ", *winning_lines)
    return winnings - total_bet

 
def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        user_input = input("Press enter to spin (q to quit).\n")
        if user_input == "q":
            break
        balance += spin(balance)

    
main()

