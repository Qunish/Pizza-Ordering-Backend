from ast import List
from datetime import datetime
from typing import Union
from fastapi import FastAPI, Query
import nest_asyncio
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

menu = [
    {
    "item_id": 1,
    "name": "Margherita",
    "cost": 240,
    "size": "Regular",
    "details": "Classic delight with 100/% /real mozzarella cheese"
    },
        {
    "item_id": 2,
    "name": "Paneer",
    "cost": 450,
    "size": "Medium",
    "details": "Flavorful trio of juicy paneer, crisp capsicum with spicy red paprika"
    },
        {
    "item_id": 3,
    "name": "Farmhouse",
    "cost": 460,
    "size": "Medium",
    "details": "Delightful combination of onion, capsicum, tomato & grilled mushroom"
    },
        {
    "item_id": 4,
    "name": "Extravaganza",
    "cost": 550,
    "size": "Medium",
    "details": "Black olives, capsicum, onion, grilled mushroom, corn, tomato, jalapeno & extra cheese"
    },
        {
    "item_id": 5,
    "name": "Chocolava",
    "cost": 110,
    "size": "",
    "details": "Chocolate lovers delight! Indulgent, gooey molten lava inside chocolate cake"
    }
]

orders = []

def cost_calculator(item_id):
    total_cost = 0
    for items in item_id:
        for i in range(len(menu)):
            if menu[i]["item_id"] == items:
                total_cost += menu[i]["cost"]
    return total_cost

order_id = 0

class Item(BaseModel):
    item_ids: list[int]
    mobile: int

@app.post("/create_order")
async def create_order(q: Item):
    global order_id
    order_id+=1              
    orders.append({"order_id": order_id,
                  "mobile": q.mobile,
                  "item_id": q.item_ids,
                  "status": "Under process",
                  "timestamp": str(datetime.now()),
                  "total_cost": cost_calculator(q.item_ids)})    
    return orders  
# create_order(2, [3, 4, 1])
# create_order(253, [1, 4, 13])
# create_order(2435, [1, 2])
# create_order(434, [2, 4])

@app.post("/update_order_status/{order_id}/{status}")
async def update_order_status(order_id: int, status: str):
    for i in range(len(orders)):
        if orders[i]["order_id"] == order_id:
            orders[i]["status"] = status
    return {"order_id": order_id}
# update_order_status(1, "Delivered")

@app.post("/update_order_items/{order_id}")
async def update_order_items(order_id: int, add_item: list[int], remove_item: list[int]):
    for i in range(len(orders)):
        if orders[i]["order_id"] == order_id:
            for item in add_item:
                orders[i]["item_id"].append(item)
            for item in remove_item:
                orders[i]["item_id"].remove(item)
    
        orders[i]["total_cost"] = cost_calculator(orders[i]["item_id"])
        return {"Updated total cost": orders[i]["total_cost"]}
# update_order_items(1, [2, 5], [1])

@app.post("/cancel_order/{order_id}")
async def cancel_order(order_id: int):
    for i in range(len(orders)):
        if orders[i]['order_id'] == order_id:
            del orders[i]
            break
        return {"Deleted order": order_id}
# cancel_order(2)

async def show_pending_order():
    pendingOrders = [item for item in orders if item['status'] != 'Delivered']
    return pendingOrders

@app.get("/pending_orders")
async def pending_orders():
    result = await show_pending_order()
    return result

nest_asyncio.apply()
uvicorn.run(app, port=8000)