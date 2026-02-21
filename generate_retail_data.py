import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# -------------------------------
# CONFIGURATION
# -------------------------------
start_date = datetime(2023, 10, 1)
end_date = datetime(2023, 12, 31)

items_master = [
    ("Bread", "Bakery", 30, 1, 120),
    ("Cake", "Bakery", 350, 2, 40),
    ("Pastry", "Bakery", 60, 1, 80),
    ("Sandwich", "FastFood", 90, 1, 100),
    ("Burger", "FastFood", 120, 1, 90),
    ("Pizza Slice", "FastFood", 150, 1, 70),
    ("Muffin", "Bakery", 50, 2, 85),
    ("Donut", "Bakery", 45, 2, 75),
    ("Cookies", "Bakery", 20, 7, 150),
    ("Brownie", "Bakery", 70, 3, 60),
    ("Roll", "FastFood", 80, 1, 95),
    ("Samosa", "FastFood", 25, 1, 200),
    ("Puff", "FastFood", 35, 2, 130),
    ("Bun", "Bakery", 20, 1, 140),
    ("Garlic Bread", "Bakery", 110, 2, 65),
    ("Cold Coffee", "Beverage", 140, 1, 50),
    ("Tea", "Beverage", 20, 0, 250),
    ("Juice", "Beverage", 60, 1, 100),
    ("Wrap", "FastFood", 130, 1, 75),
    ("Croissant", "Bakery", 80, 2, 55),
]

# -------------------------------
# DATA GENERATION
# -------------------------------
data = []
current_date = start_date

while current_date <= end_date:
    day_name = current_date.strftime("%A")
    weekend_multiplier = 1.15 if day_name in ["Saturday", "Sunday"] else 1

    for item in items_master:
        name, category, price, expiry, base_demand = item

        # Adjust base demand for category
        if category == "Beverage":
            seasonal_multiplier = 1.10  # slight increase
        else:
            seasonal_multiplier = 1

        adjusted_demand = int(
            base_demand * weekend_multiplier * seasonal_multiplier)

        # Production variability
        produced = adjusted_demand + np.random.randint(-15, 20)

        if produced < 10:
            produced = 10

        # Waste behavior (higher waste if expiry is 1 day)
        if expiry == 1:
            waste = np.random.randint(5, 25)
        elif expiry <= 2:
            waste = np.random.randint(3, 15)
        else:
            waste = np.random.randint(0, 8)

        sold = produced - waste

        if sold < 0:
            sold = 0

        waste_qty = produced - sold
        revenue = sold * price
        waste_loss = waste_qty * price

        data.append([
            current_date.strftime("%Y-%m-%d"),
            day_name,
            name,
            category,
            produced,
            sold,
            waste_qty,
            price,
            revenue,
            waste_loss,
            expiry
        ])

    current_date += timedelta(days=1)

columns = [
    "Date",
    "Day_of_Week",
    "Item",
    "Category",
    "Produced_Qty",
    "Sold_Qty",
    "Waste_Qty",
    "Price_Per_Unit",
    "Revenue",
    "Waste_Loss",
    "Expiry_Days"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("retail_food_waste_data.csv", index=False)

print("Dataset generated successfully!")
print("Total rows:", len(df))
