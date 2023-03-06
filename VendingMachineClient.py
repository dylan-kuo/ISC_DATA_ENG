import socket
import pickle

HOST = 'localhost'
PORT = 8000

def send_command(command, args=[]):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = pickle.dumps((command, args))
        s.sendall(message)
        response = s.recv(1024)
        return pickle.loads(response)


def display_items():
    response = send_command('display_items')
    print(response)

def add_money(amount):
    response = send_command('add_money', amount)
    print(response)

def purchase_item(item=None):
    if not item:
        item = input("Enter the item you want to purchase: ")
        purchase_item(item)
    else:
        confirm_item = input(f"You've selected {item}. Are you sure you want to purchase it? (y/n): ")
        if confirm_item.lower() == 'n':
            modify_item = input("Do you want to change to another item? (y/n): ")
            if modify_item == 'y':
                item = input("Enter a different item name: ")
                purchase_item(item)
            else: 
                return
        else: 
            response = send_command('purchase_item', item)
            print(response)

def display_balance():
    response = send_command('display_balance')
    print(response)

def display_help():
    response = send_command('display_help')
    print(response)

def run():
    display_help()

    while True:
        command = input("\nEnter a command: ")

        if command == "items":
            display_items()
        elif command.startswith("add"):
            try:
                amount = float(command.split(" ")[1])
                add_money(amount)
            except (ValueError, IndexError):
                print("Invalid command format. Please enter the amount to add.")
        elif command.startswith("purchase"):
            try:
                item = command.split(" ")[1]
                purchase_item(item)
            except IndexError:
                print("Invalid command format. Please enter the item to purchase.")
        elif command == "balance":
            display_balance()
        elif command == "help":
            display_help()
        elif command == "quit":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == '__main__':
    run()
