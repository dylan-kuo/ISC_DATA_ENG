import socket
import threading
import pickle


class VendingMachine:
    def __init__(self):
        """
        Initialize the VendingMachine object with a dictionary of items and their prices,
        and an initial balance of 0.0.
        """
        self.items = {
            "Coke": 1.00,
            "Cracker": 1.50,
            "Chocolate": 2.25,
            "Water": 1.25
        }
        self.balance = 0.0

    def display_items(self):
        """
        Display the available items and their prices.
        """
        return self.items

    def add_money(self, amount):
        """
        Add the given amount to the balance.

        Args:
            amount (float): The amount to add to the balance.

        Returns:
            None
        """
        if amount <= 0:
            return "Invalid amount. Please enter a positive number."
        else:
            self.balance += amount
            return f"Added ${amount:.2f}. Total balance: ${self.balance:.2f}"

    def purchase_item(self, item):
        """
        Purchase the given item if it is available and the balance is sufficient.

        Args:
            item (str): The name of the item to purchase.

        Returns:
            None
        """
        if item not in self.items:
            return "Invalid item. Please enter a valid item name."
        elif self.balance < self.items[item]:
            return "Insufficient funds. Please add more money."
        else:
            self.balance -= self.items[item]
            return f"Purchased {item} for ${self.items[item]:.2f}. Remaining balance: ${self.balance:.2f}"
    

    def display_balance(self):
        """
        Display the current balance.
        """
        return f"Current balance: ${self.balance:.2f}"
    
    def display_help(self):
        response = 'Available commands:\n'
        response += 'items - Display the available items and their prices.\n'
        response += 'add <amount> - Add money to your account balance.\n'
        response += 'purchase <item> - Purchase an item from the vending machine.\n'
        response += 'change - Change the item you want to purchase.\n'
        response += 'balance - Display your current account balance.\n'
        response += 'help - Display this help message.\n'
        response += 'quit - Quit the program.\n'
        return response


class VendingMachineServer:
    def __init__(self, host="127.0.0.1", port=8000):
        self.host = host
        self.port = port
        self.vending_machine = VendingMachine()

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(1)

        print(f"Listening on {self.host}:{self.port}...")

        while True:
            client, address = sock.accept()
            print(f"Accepted connection from {address[0]}:{address[1]}")
            threading.Thread(target=self.handle_client, args=(client,)).start()

    def handle_client(self, client):
        while True:
            try:
                data = client.recv(1024)
                if not data:
                    break
                command, *args = pickle.loads(data)
                result = self.execute_command(command, args)
                client.send(pickle.dumps(result))
            except Exception as e:
                print(f"Error handling client: {e}")
                break

        client.close()

    def execute_command(self, command, args):
        if command == "display_items":
            return self.vending_machine.display_items()
        elif command == "add_money":
            return self.vending_machine.add_money(*args)
        elif command == "purchase_item":
            return self.vending_machine.purchase_item(*args)
        elif command == "display_balance":
            return self.vending_machine.display_balance()
        elif command == "display_help":
            return self.vending_machine.display_help()
        else:
            return "Invalid command. Please enter a valid command."


if __name__ == '__main__':
    vending_machine_server = VendingMachineServer()
    vending_machine_server.run()
