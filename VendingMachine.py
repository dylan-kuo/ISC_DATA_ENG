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
        for item, price in self.items.items():
            print(f"{item}: ${price:.2f}")

    def add_money(self, amount):
        """
        Add the given amount to the balance.

        Args:
            amount (float): The amount to add to the balance.

        Returns:
            None
        """
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
        else:
            self.balance += amount
            print(f"Added ${amount:.2f}. Total balance: ${self.balance:.2f}")

    def purchase_item(self, item):
        """
        Purchase the given item if it is available and the balance is sufficient.

        Args:
            item (str): The name of the item to purchase.

        Returns:
            None
        """
        if item not in self.items:
            print("Invalid item. Please enter a valid item name.")
        elif self.balance < self.items[item]:
            print("Insufficient funds. Please add more money.")
        else:
            change_item = input(f"Are you sure you want to purchase {item} for {self.items[item]:.2f}? (y/n) ")
            if change_item.lower() == 'n':
                new_item = input("Enger a different item name: ")
                self.purchase_item(new_item)
            else:
                self.balance -= self.items[item]
                print(f"Purchased {item} for ${self.items[item]:.2f}. "
                    f"Remaining balance: ${self.balance:.2f}")

    def display_balance(self):
        """
        Display the current balance.
        """
        print(f"Current balance: ${self.balance:.2f}")

    def display_prompt(self):
        """
        Display the available commands for the VendingMachine.
        """
        print("Available commands:")
        print("items - Display available items")
        print("add [amount] - Add money to balance")
        print("purchase [item] - Purchase an item")
        print("balance - Display current balance")
        print("help - Display available commands")
        print("quit - Quit the program")

    def run(self):
        """
        Run the VendingMachine program, prompting the user for commands and executing them.
        """
        self.display_prompt()

        while True:
            print("\nEnter a command: ")
            command = input()

            if command == "items":
                self.display_items()
            elif command.startswith("add"):
                try:
                    amount = float(command.split(" ")[1])
                    self.add_money(amount)
                except (ValueError, IndexError):
                    print("Invalid command format. Please enter the amount to add.")
            elif command.startswith("purchase"):
                try:
                    item = command.split(" ")[1]
                    self.purchase_item(item)
                except IndexError:
                    print("Invalid command format. Please enter the item to purchase.")
            elif command == "balance":
                self.display_balance()
            elif command == "help":
                self.display_prompt()
            elif command == "quit":
                print("Exiting program.")
                break
            else:
                print("Invalid command. Please enter a valid command.")


vending_machine = VendingMachine()
vending_machine.run()