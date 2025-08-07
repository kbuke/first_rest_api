# from flask import Flask, request
# from flask_smorest import abort
# from db import items, stores
# import uuid
from flask import Flask 
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

# # GET ALL STORES
# @app.get("/store")
# def get_all_stores():
#     return {"stores": list(stores.values())}

# # GET SPECIFIC STORE
# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="Store not found.")

# # CREATE A NEW STORE
# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     if "name" not in store_data:
#         abort(400, message="Ensure name is included in JSON payload.")
#     for store in stores.values():
#         if store_data["name"] == store["name"]:
#             abort(400, message=f"Store already exists")
#     store_id = uuid.uuid4().hex
#     # **store_data will unpack all data currently stored
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201

# # DELETE A STORE
# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message": "Store deleted"}
#     except KeyError:
#         abort(404, message="Store not found")

# # CREATE NEW ITEM
# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if(
#         "price" not in item_data
#         or 'store_id' not in item_data
#         or "name" not in item_data
#     ):
#         abort(400, message="Ensure price, store_id and name are included in JSON payload")
#     for item in items.values():
#         if(
#             item_data["name"]==item["name"]
#             and item_data["store_id"] == item["store_id"]
#         ):
#             abort(400, message=f"{item} already exists")
#     if item_data["store_id"] not in stores:
#         abort(404, messaged="Store not found")
#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item
#     return item, 201

# # GET ALL ITEMS
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}

# # GET SPECIFIC ITEM
# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="Item not found.")

# # DELETE ITEM
# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted"}
#     except KeyError:
#         abort(404, message="Item not found")

# # UPDATE ITEM
# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400, message="Bad request. Ensure price and name are included in JSOn payload")
#     try:
#         item = items[item_id]
#         #this is an update dict sign (|=)
#         item |= item_data 
#         return item
#     except KeyError:
#         abort(404, message="Item not found")
