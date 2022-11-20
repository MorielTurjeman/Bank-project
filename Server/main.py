# from data_accses_queries import category_data
# from data_accses_queries import transaction_data
# from data_accses_queries import user_data
# # print(category_data.get_categories())
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes import transaction_routes, category_routes, user_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# print(transaction_data.get_transactions())
# # category_data.create_category('Salary')
# # transaction_data.create_transaction(1, 'CyberArk', 100, 'Salary', False)
# # print(transaction_data.get_transactions_by_category('Salary'))
# # transaction_data.delete_transaction(3)
# # category_data.delete_category('Salary')
# # print(user_data.get_balance(1))
# # user_data.update_balance(1, -5)
# print(transaction_data.sum_transactions_by_category())


app = FastAPI()
app.include_router(transaction_routes.router)
app.include_router(category_routes.router)
app.include_router(user_routes.router)


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# rest of the routes
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
