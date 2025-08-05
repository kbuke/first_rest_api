from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store") # this is the endpoint
def get_stores():
    return{"stores": stores}