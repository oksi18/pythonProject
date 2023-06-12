# 1


with open('emails.txt', 'r') as file:
    lines = file.readlines()

gmail_emails = []

for line in lines:
    words = line.split()
    for word in words:
        if "gmail.com" in word:
            gmail_emails.append(word)

with open('new_email.txt', 'w') as file:
    for email in gmail_emails:
        file.write(email + '\n')

print('Emails are in a new file')

# 2
import json


class Purchase:
    def __init__(self, purchase_id, name, price):
        self.purchase_id = purchase_id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            'id': self.purchase_id,
            'name': self.name,
            'price': self.price
        }

    def __str__(self):
        return f"ID: {self.purchase_id}, Name: {self.name}, Price: {self.price}"


class PurchaseBook:
    def __init__(self, file_name):
        self.file_name = file_name

    def all_purchases(self):
        purchases = self.load_purchases()
        if purchases:
            for purchase in purchases:
                print(purchase)
        else:
            print("Purchase not found!")

    def add_purchase(self):
        purchase_id = input("Id of purchase: ")
        purchase_name = input("Name of purchase: ")
        purchase_price = float(input("Price of purchase: "))

        purchase = Purchase(purchase_id, purchase_name, purchase_price)
        purchases = self.load_purchases()
        purchases.append(purchase.to_dict())
        self.save_purchases(purchases)
        print("Purchase add!")

    def search_purchase(self):
        search_field = input("Write (id, name, price): ")
        search_value = input("Enter a value: ")

        purchases = self.load_purchases()
        found_purchases = [Purchase(**purchase) for purchase in purchases if
                           str(purchase[search_field]) == search_value]

        if found_purchases:
            print("Purchase found:")
            for purchase in found_purchases:
                print(purchase)
        else:
            print("Purchase not found!")

    def the_most_expensive_purchase(self):
        purchases = self.load_purchases()
        if purchases:
            most_expensive_purchase = max(purchases, key=lambda purchase: float(purchase[
                                                                                    'price']))  # функція макс приймає 2 аргументи, одна з яких key - для порівнювання елементів за значенням, лямбда - безіменна функція в пайтоні, дозволяє визначити функцію без необхідності присвоювати їй ім'я. Функції lambda зазвичай використовуються в ситуаціях, де потрібно передати коротку функцію як аргумент у функції вищого порядку, такі як map(), filter(), sorted(), max(), min() і багато інших.
            print(f"The most expensive purchase: {most_expensive_purchase}")
        else:
            print("Purchase not found!")

    def delete_purchase_by_id(self):
        purchase_id = input("Enter id: ")
        purchases = self.load_purchases()

        filtered_purchases = [purchase for purchase in purchases if purchase['id'] != purchase_id]

        if len(filtered_purchases) < len(purchases):
            self.save_purchases(filtered_purchases)
            print(f"Purchase with ID {purchase_id} delete.")
        else:
            print(f"Purchase with ID {purchase_id} not found.")

    def load_purchases(self):
        try:
            with open(self.file_name, 'r') as file:
                purchases = json.load(file)
                return purchases
        except FileNotFoundError:
            return []

    def save_purchases(self, purchases):
        with open(self.file_name, 'w') as file:
            json.dump(purchases, file, indent=4)  # indent - пробіли

    def display_menu(self):
        menu = """
        --- Purchase Book ---
        1. All purchase
        2. Add new purchase
        3. Find purchase
        4. The most expensive purchase
        5. Delete purchase
        6. Exit
        """

        while True:
            print(menu)
            choice = input("Choose option: ")
            if choice == '1':
                self.all_purchases()
            elif choice == '2':
                self.add_purchase()
            elif choice == '3':
                self.search_purchase()
            elif choice == '4':
                self.the_most_expensive_purchase()
            elif choice == '5':
                self.delete_purchase_by_id()
            elif choice == '6':
                print("Good Bye!")
                break
            else:
                print("Not found...")


purchase_book = PurchaseBook('purchase_book.json')
purchase_book.display_menu()

