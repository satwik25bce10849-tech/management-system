import sys
import uuid
from datetime import datetime

class MenuItem:
    """Represents a single item on the restaurant's menu."""
    def __init__(self, item_id: int, name: str, price: float, category: str):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        """String representation for display."""
        return f"ID {self.item_id:02d}: {self.name} ({self.category}) - ₹{self.price:.2f}"

class Order:
    """Represents a customer order, tracking items, status, and table."""
    def __init__(self, table_number: int):
        self.order_id = str(uuid.uuid4())[:8]
        self.table_number = table_number
        self.items = {}
        self.timestamp = datetime.now()
        self.status = "PENDING"

    def add_item(self, menu_item_id: int, quantity: int):
        """Adds or updates the quantity of an item in the order."""
        if menu_item_id in self.items:
            self.items[menu_item_id] += quantity
        else:
            self.items[menu_item_id] = quantity

    def calculate_total(self, menu):
        """Calculates the total cost of the order."""
        total = 0.0
        for item_id, quantity in self.items.items():
            menu_item = menu.get(item_id)
            if menu_item:
                total += menu_item.price * quantity
        return total

    def __str__(self):
        """Brief summary of the order for list views."""
        return f"Order #{self.order_id} | Table: {self.table_number} | Status: {self.status} | Time: {self.timestamp.strftime('%H:%M')}"

class RestaurantSystem:
    """The central manager handling all menu and order operations."""
    def __init__(self):
        self.menu = self._initialize_menu()
        self.active_orders = []
        self.next_item_id = 11

    def _initialize_menu(self):
        """Creates the initial hardcoded menu."""
        menu_items = [
            MenuItem(1, "Classic Burger", 60.00, "Mains"),
            MenuItem(2, "White Sauce Pasta", 120.00, "Mains"),
            MenuItem(3, "Salad", 100.00, "Starters"),
            MenuItem(4, "Garlic Bread", 99.00, "Starters"),
            MenuItem(5, "Chocolate Cake", 150.00, "Desserts"),
            MenuItem(6, "Mineral Water", 60.00, "Drinks"),
            MenuItem(7, "Coffee", 80.00, "Drinks"),
            MenuItem(8, "Kadai Paneer", 300.00, "Mains"),
            MenuItem(9, "Fries", 100.00, "Sides"),
            MenuItem(10, "Ice Cream", 30.00, "Desserts"),
        ]
        return {item.item_id: item for item in menu_items}

    def display_menu(self):
        """Prints the entire menu, grouped by category."""
        print("\n" + "="*50)
        print("                 RESTAURANT MENU")
        print("="*50)

        categories = sorted(list(set(item.category for item in self.menu.values())))

        for category in categories:
            print(f"\n--- {category.upper()} ---")
            items_in_category = sorted([item for item in self.menu.values() if item.category == category], key=lambda x: x.item_id)
            for item in items_in_category:
                print(f"{item.item_id:02d}. {item.name:<25} ₹{item.price:>5.2f}")
        print("="*50)

    def place_order(self, table_number: int):
        """Guided process for placing a new order."""
        new_order = Order(table_number)
        print(f"\n--- Placing New Order for Table {table_number} (ID: {new_order.order_id}) ---")

        while True:
            item_input = input("Enter Item ID and Quantity (e.g., '1 2'), or 'done' to finish: ").strip()

            if item_input.lower() == 'done':
                break

            try:
                parts = item_input.split()
                if len(parts) != 2:
                    print("Invalid format. Use 'ID Quantity'.")
                    continue

                item_id = int(parts[0])
                quantity = int(parts[1])

                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue

                if item_id in self.menu:
                    new_order.add_item(item_id, quantity)
                    item_name = self.menu[item_id].name
                    print(f"Added {quantity} x {item_name} to the order.")
                else:
                    print(f"Item ID {item_id} not found on the menu.")

            except ValueError:
                print("Invalid input. Please enter valid numbers for ID and Quantity.")

        if new_order.items:
            self.active_orders.append(new_order)
            total = new_order.calculate_total(self.menu)
            print(f"\n✅ Order #{new_order.order_id} placed successfully! Estimated Total: ₹{total:.2f}")
        else:
            print("Order cancelled as no items were added.")

    def display_active_orders(self):
        """Shows all active orders and their statuses."""
        if not self.active_orders:
            print("\nThere are no active orders currently.")
            return

        print("\n" + "-"*60)
        print("                       ACTIVE ORDERS")
        print("-" * 60)

        for idx, order in enumerate(self.active_orders):
            print(f"[{idx + 1}] {order}")

            item_names = [self.menu[id].name for id in order.items if id in self.menu]
            if item_names:
                detail_str = f"    Items: {', '.join(item_names[:2])}"
                if len(item_names) > 2:
                    detail_str += f" and {len(item_names) - 2} more items."
                print(detail_str)

        print("-" * 60)

    def update_order_status(self, order_index: int, new_status: str):
        """Updates the status of an order."""
        try:
            order_index -= 1

            if 0 <= order_index < len(self.active_orders):
                order = self.active_orders[order_index]
                order.status = new_status.upper()
                print(f"✅ Order #{order.order_id} status updated to: {order.status}")
            else:
                print(f"⚠ Error: Invalid order number {order_index + 1}.")
        except ValueError:
            print("⚠ Error: Please enter a valid number.")

    def calculate_and_close_bill(self, order_index: int):
        """Calculates the final bill and removes the order."""
        try:
            order_index -= 1

            if 0 <= order_index < len(self.active_orders):
                order = self.active_orders.pop(order_index)
                total = order.calculate_total(self.menu)

                print("\n" + "#"*40)
                print(f"         FINAL BILL FOR TABLE {order.table_number}")
                print(f"         Order ID: {order.order_id}")
                print(f"         Time Placed: {order.timestamp.strftime('%Y-%m-%d %H:%M')}")
                print("-" * 40)

                for item_id, quantity in order.items.items():
                    item = self.menu.get(item_id)
                    if item:
                        item_subtotal = item.price * quantity
                        print(f"  {quantity}x {item.name:<25} ₹{item_subtotal:>6.2f}")

                print("-" * 40)
                subtotal = total
                tax_rate = 0.08
                tax = subtotal * tax_rate
                final_total = subtotal + tax

                print(f"  Subtotal:                          ₹{subtotal:>6.2f}")
                print(f"  Tax ({tax_rate*100:.0f}%):                          ₹{tax:>6.2f}")
                print(f"  FINAL AMOUNT DUE:                  ₹{final_total:>6.2f}")
                print("#"*40)

                print(f"\n🎉 Order #{order.order_id} successfully closed and archived.")

            else:
                print(f"⚠ Error: Invalid order number {order_index + 1}.")
        except ValueError:
            print("⚠ Error: Please enter a valid number.")

def run_system():
    """The main entry point for the command-line interface."""
    system = RestaurantSystem()

    print("\n" + "="*60)
    print("           Welcome to the Python Restaurant Manager")
    print("="*60)

    while True:
        print("\n--- Main Menu ---")
        print("1. View Menu")
        print("2. Place New Order")
        print("3. View/Update Active Orders")
        print("4. Close Order and Print Bill")
        print("5. Exit System")
        print("-----------------")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            system.display_menu()

        elif choice == '2':
            try:
                table_num = int(input("Enter the Table Number for the new order: ").strip())
                if table_num <= 0:
                    print("Table number must be positive.")
                    continue
                system.display_menu()
                system.place_order(table_num)
            except ValueError:
                print("Invalid input. Please enter a valid table number.")

        elif choice == '3':
            system.display_active_orders()
            if system.active_orders:
                print("\n--- Order Actions ---")
                print("1. Change Order Status (PENDING -> PREPARING -> COMPLETE)")
                print("2. Return to Main Menu")

                action = input("Enter action (1 or 2): ").strip()
                if action == '1':
                    try:
                        order_idx = int(input("Enter the order number to update: ").strip())
                        status_map = {"1": "PREPARING", "2": "COMPLETE"}
                        print("New Status Options: [1] Preparing, [2] Complete")
                        status_choice = input("Enter status option (1 or 2): ").strip()

                        new_status = status_map.get(status_choice)
                        if new_status:
                            system.update_order_status(order_idx, new_status)
                        else:
                            print("Invalid status option.")

                    except ValueError:
                        print("Invalid input.")

        elif choice == '4':
            system.display_active_orders()
            if system.active_orders:
                try:
                    order_idx = int(input("Enter the order number to close and bill: ").strip())
                    system.calculate_and_close_bill(order_idx)
                except ValueError:
                    print("Invalid input. Please enter a valid order number.")

        elif choice == '5':
            print("Shutting down the Restaurant Manager. Have a good day!")
            sys.exit(0)

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    run_system()