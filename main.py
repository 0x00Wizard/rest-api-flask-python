from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "my store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store")
def get_store():
    return {"store": stores}


if __name__ == "__main__":
    app.run()
