📄 Statement of Capabilities and System Description
This document serves as a formal statement detailing the architecture, functionality, and capabilities of the provided Python code for the Restaurant Management System (RMS).


🏗 System Architecture and Design
The system is constructed using the Object-Oriented Programming (OOP) paradigm, ensuring modularity, reusability, and separation of concerns. The core design revolves around three primary classes, detailed below.

Core Components (Classes)
•	MenuItem:
o	Role: Acts as a Value Object defining the structure and properties of a single item available for sale.
o	Data Fields: item_id (Integer), name (String), price (Float), and category (String).
•	Order:
o	Role: Represents a single Transaction Entity associated with a customer visit.
o	Data Fields: order_id (UUID snippet), table_number (Integer), items (Dictionary mapping item_id to quantity), timestamp (datetime object), and status (String, default "PENDING").
o	Methods: Includes logic to dynamically add items and calculate the total cost based on the current menu prices.
•	RestaurantSystem:
o	Role: The Central Manager/Controller that maintains the application state and orchestrates all operations.
o	Data Fields: menu (Dictionary mapping item_id to MenuItem objects) and active_orders (List of Order objects).
o	Initialization: The menu is initialized with hardcoded data upon system startup using the private method _initialize_menu().


⚙ Functional Capabilities
The system provides essential functionality required for front-of-house operations in a small restaurant setting, accessed via a command-line interface (CLI).
1. Menu Presentation
•	The system can display the full menu to the user.
•	Items are automatically grouped and sorted by category (e.g., Mains, Starters, Desserts) for readability.
•	Each item is displayed with its unique, zero-padded item_id, name, and price.
2. Order Management
•	Order Creation (place_order): Guides the user to input a table number and then repeatedly enter Item ID and Quantity until the order is finalized.
•	Order Tracking (active_orders): All newly placed orders are immediately added to a list of active orders, tracked by their short UUID and status.
•	Status Update (update_order_status): Allows staff to change the status of any active order (e.g., PENDING $\rightarrow$ PREPARING $\rightarrow$ COMPLETE) based on kitchen progress.
3. Billing and Closure
•	Bill Calculation (calculate_and_close_bill):
o	Calculates the subtotal by aggregating costs from all items and quantities in the order.
o	Applies a fixed 8% tax rate ($T=0.08$) to the subtotal.
o	Calculates the Final Amount Due ($FAD = \text{Subtotal} + (\text{Subtotal} \times T)$).
o	Generates a formatted, detailed receipt showing individual item costs, subtotal, tax, and final amount.
•	Order Archival: Upon billing, the Order object is removed from the active_orders list, simulating archival and freeing the table.


🔒 Limitations and Assumptions
•	Data Volatility: The system currently lacks data persistence. All menu and order data is stored in memory and is lost upon program termination.
•	Fixed Menu: The menu is hardcoded in the _initialize_menu method and cannot be modified (add/remove/edit) through the user interface.
•	Single User Model: The CLI structure assumes sequential operation by a single user or staff member; it is not designed for concurrent multi-user access.
•	Simple Status Flow: The status transition is limited to a linear flow (PENDING $\rightarrow$ PREPARING $\rightarrow$ COMPLETE).