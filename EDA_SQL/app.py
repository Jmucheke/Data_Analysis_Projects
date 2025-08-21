import requests

API_BASE = "http://127.0.0.1:8000"

def fetch_menu():
    try:
        response = requests.get(f"{API_BASE}/menu")
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print("❌ Error: Failed to fetch the menu.")
        return None

def fetch_category_menu(category):
    try:
        response = requests.get(f"{API_BASE}/menu/{category}")
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print("❌", response.json().get("detail", str(e)))
        return None
    except requests.RequestException:
        print("❌ Error: Unable to connect to API.")
        return None

def place_order(category, item, amount_paid):
    payload = {
        "category": category,
        "item": item,
        "amount_paid": amount_paid
    }
    try:
        response = requests.post(f"{API_BASE}/order", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.HTTPError as e:
        print("❌", response.json().get("detail", str(e)))
        return None
    except requests.RequestException:
        print("❌ Error: Unable to send order request.")
        return None

def main():
    print("🍔 Welcome to the Fast Food Restaurant CLI!")

    menu = fetch_menu()
    if not menu:
        return

    print("\n📋 Available Categories:")
    for cat in menu.keys():
        print(f" - {cat.capitalize()}")

    category = input("\nSelect a category (breakfast, lunch, supper): ").strip().lower()
    items = fetch_category_menu(category)
    if not items:
        return

    print(f"\n🍽 {category.capitalize()} Menu:")
    for item, price in items.items():
        print(f" - {item.title()} : ${price:.2f}")

    item = input("\nSelect an item from the menu: ").strip().lower()

    try:
        amount_paid = float(input("Enter the amount you are paying: $"))
    except ValueError:
        print("❌ Invalid amount entered.")
        return

    result = place_order(category, item, amount_paid)
    if result:
        print(f"\n✅ Order Confirmed:")
        print(f"Item: {result['item'].title()}")
        print(f"Price: ${result['price']:.2f}")
        print(f"Amount Paid: ${result['amount_paid']:.2f}")
        print(f"Change: ${result['change']:.2f}")

if __name__ == "__main__":
    main()