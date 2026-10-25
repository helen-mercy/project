import random




MAX = 3
BET = 100
MIN = 1

ROWS = 3
COLS = 3


symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "E": 10,
    "F": 12
}


def get_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for col in range(cols):
        column = []
        for _ in range(rows):
            value = random.choice(all_symbols)
            column.append(value)
            all_symbols.remove(value)

        columns.append(column)  # Add this line!

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def depo():
    while True:
        amount = input("what amount would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please enter a valid number")
    return amount



def get_lines():
    while True:
        lines = input("how many lines would you like to bet on (1-" + str(MAX) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX:
                break
            else:
                print(f"please enter a number between 1 and {MAX}")
        else:
            print("please enter a valid number")
    return lines



def get_bet():
    while True:
        amount = input("what amount would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN <= amount <= BET:
                break
            else:
                print(f"please enter a number between {MIN} and {BET}")
        else:
            print("please enter a valid number")
    return amount






def main():
    print("Welcome to the slot machine!")  
    balance = depo()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet <= balance:
            break
        else:
            print("you don't have enough money to place that bet")
    print(f"You have deposited ${balance} and are betting on {lines} lines with a bet of ${bet} per line. Total bet is ${lines * bet}. Good luck!")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = get_winnings(slots, lines, bet, symbols_count)
    print(f"You won ${winnings}!")
    if winning_lines:
        print(f"Congratulations! You won on lines: {', '.join(map(str, winning_lines))}")
main()