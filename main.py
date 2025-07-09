from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://jt4qzv.csb.app/"],  # or your deployed frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Product data (mock database)
products_data = [
    # Mobiles
    {"title": "Samsung Galaxy S24", "price": "₹79,999", "rating": 4.5},
    {"title": "Apple iPhone 15", "price": "₹89,900", "rating": 4.7},
    {"title": "OnePlus 12", "price": "₹64,999", "rating": 4.3},
    {"title": "Redmi Note 13 Pro", "price": "₹23,499", "rating": 4.2},
    {"title": "Realme Narzo 60", "price": "₹19,999", "rating": 4.0},
    {"title": "iQOO Z9", "price": "₹18,999", "rating": 4.1},
    {"title": "Lava Blaze 5G", "price": "₹11,999", "rating": 4.0},

    # Watches
    {"title": "boAt Xtend Smartwatch", "price": "₹2,499", "rating": 4.2},
    {"title": "Noise ColorFit Ultra", "price": "₹2,999", "rating": 4.3},
    {"title": "Fire-Boltt Ninja Call Pro", "price": "₹1,699", "rating": 4.1},

    # TVs
    {"title": "Sony Bravia 55-inch 4K TV", "price": "₹59,999", "rating": 4.6},
    {"title": "LG 43-inch LED TV", "price": "₹32,999", "rating": 4.4},
    {"title": "Mi 5A 32-inch Smart TV", "price": "₹14,999", "rating": 4.2},

    # ACs
    {"title": "Voltas 1.5 Ton Inverter AC", "price": "₹33,999", "rating": 4.3},
    {"title": "LG 1 Ton Split AC", "price": "₹29,499", "rating": 4.4},
    {"title": "Samsung Convertible 5-in-1 AC", "price": "₹38,990", "rating": 4.5},

    # Laptops
    {"title": "HP Pavilion 15", "price": "₹55,999", "rating": 4.2},
    {"title": "Dell Inspiron 14", "price": "₹48,999", "rating": 4.1},
    {"title": "Apple MacBook Air M2", "price": "₹99,900", "rating": 4.8},
    {"title": "Lenovo IdeaPad Slim 5", "price": "₹52,499", "rating": 4.3}
]

# ✅ Product search logic
def get_products(query=None):
    if not query:
        return products_data
    return [product for product in products_data if query.lower() in product["title"].lower()]

# ✅ All products endpoint
@app.get("/api/products")
def all_products():
    return get_products()

# ✅ Search products endpoint
@app.get("/api/products/search")
def search_products(query: str):
    return get_products(query)
