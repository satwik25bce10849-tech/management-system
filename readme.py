🍽️ Python Restaurant Management System (CLI)This project is a simple, command-line interface (CLI) application developed in Python to simulate basic operations of a restaurant management system. It uses Object-Oriented Programming (OOP) principles to handle menu display, order placement, status tracking, and bill generation.

✨ Features

Menu Management:Displays a hardcoded menu categorized by item type.
Order Creation: Allows placing new orders for specific tables by selecting item IDs and quantities.
Order Tracking: Keeps a list of active orders with unique IDs, table numbers, and timestamps.
Status Updates: Ability to change the status of active orders (e.g., PENDING, PREPARING, COMPLETE).Billing: Calculates and prints a detailed final bill (including an 8% tax) and closes the order.OOP Structure: Implemented using classes (MenuItem, Order, RestaurantSystem) for clear separation of concerns.

🚀 Getting Started

Prerequisites
You only need Python 3.x installed on your system.

How to Run
Save the Code: Save the provided Python code into a file named restaurant_manager.py.
Run from Terminal: Navigate to the directory where you saved the file and execute:Bashpython restaurant_manager.py
Follow the Prompts: The main menu will appear, guiding you through the available operations.

📝 Usage
The system operates via a numbered menu interface in the console:
Main Menu Options
1. View Menu: Displays the current menu items, prices, and categories.
2. Place New Order:
Starts the guided process for entering the table number.
Allows entering Item ID and Quantity (e.g., 1 2) repeatedly.
Finalize the order by typing done.
3. View/Update Active Orders:
Lists all ongoing orders.
Allows changing an order's status (e.g., to PREPARING or COMPLETE).
4. Close Order and Print Bill:
Lists all active orders.
Selects an order, calculates the final total (including 8% tax), prints the detailed receipt, and archives the order.
5. Exit System: Shuts down the application.

Placing an Order (Example)
When prompted for an item, use the format ID Quantity:

Enter Item ID and Quantity (e.g., '1 2'), or 'done' to finish: 1 2
Added 2 x Classic Burger to the order.
Enter Item ID and Quantity (e.g., '1 2'), or 'done' to finish: 7 1
Added 1 x Coffee to the order.
Enter Item ID and Quantity (e.g., '1 2'), or 'done' to finish: done

✅ Order #XXXX placed successfully! Estimated Total: ₹200.00 (2*60 + 1*80)

📦 Class Breakdown
The system is built on three core classes, each handling a specific domain function:
MenuItem:
Role: The fundamental Data Model for an item.
Functionality: Stores item details: item_id, name, price, and category.
Order:
Role: The Transaction Tracker for a specific table.
Functionality:
Generates a unique order_id (based on UUID).
Tracks the table_number, order status, and timestamp.
Manages the ordered items in an items dictionary (ID: Quantity).
Calculates the order subtotal using the prices from the menu.
RestaurantSystem:
Role: The Central Manager and application controller.
Functionality:
Holds the master menu dictionary and the list of active_orders.
Contains methods for all system operations: display_menu, place_order, update_order_status, and calculate_and_close_bill.

💡 Potential Enhancements

Data Persistence: Implement saving and loading of menu and active orders using json or another format so data persists when the program is restarted.
Menu Editing: Add functionality to dynamically add, remove, or modify items within the RestaurantSystem
Order Modification: Allow editing the quantity or adding/removing items from an existing active order.