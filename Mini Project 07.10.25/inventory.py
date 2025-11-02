
inventory = {"laptop": 10, "mouse": 25, "keyboard": 15}

inventory["monitor"] = 5

inventory["laptop"] -= 2 

if "mouse" in inventory:
    print(f"Mouse stock: {inventory['mouse']} units")

if inventory.get("keyboard", 0) > 0:
    print(f"Keyboard is in stock: {inventory['keyboard']} units")
else:
    print("Keyboard is out of stock")

print("\nCurrent Inventory:")
for item, stock in inventory.items():
    print(f"{item}: {stock}")
