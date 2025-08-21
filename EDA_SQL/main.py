from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Fast Food Restaurant")

# Menu data
menu = {
    "breakfast": {
        "pancakes": 5.0,
        "omelette": 4.5,
        "coffee": 2.0
    },
    "lunch": {
        "burger": 8.0,
        "fries": 3.0,
        "soda": 2.5
    },
    "supper": {
        "steak": 12.0,
        "salad": 6.0,
        "juice": 3.0
    }
}

class OrderRequest(BaseModel):
    category: str
    item: str
    amount_paid: float

class OrderResponse(BaseModel):
    item: str
    price: float
    amount_paid: float
    change: float


@app.get("/")
def root():
    return {"message": "Welcome to the Fast Food Restaurant API!"}

@app.get("/menu")
def get_full_menu():
    return menu

@app.get("/menu/{category}")
def get_category_menu(category: str):
    category = category.lower()
    if category not in menu:
        raise HTTPException(status_code=404, detail="Category not found")
    return menu[category]

@app.post("/order", response_model=OrderResponse)
def place_order(order: OrderRequest):
    category = order.category.lower()
    item = order.item.lower()

    if category not in menu:
        raise HTTPException(status_code=404, detail="Category not found")

    if item not in menu[category]:
        raise HTTPException(status_code=404, detail="Item not found in selected category")

    price = menu[category][item]
    if order.amount_paid < price:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient funds. {item.title()} costs ${price:.2f}."
        )

    change = round(order.amount_paid - price, 2)

    return OrderResponse(
        item=item,
        price=price,
        amount_paid=order.amount_paid,
        change=change
    )
