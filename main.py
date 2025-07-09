from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from amazon_model import get_products

app = FastAPI()

# Allow requests from your React frontend (adjust origin as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React default dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products")
def all_products():
    return get_products()

@app.get("/api/products/search")
def search_products(query: str):
    return get_products(query)
