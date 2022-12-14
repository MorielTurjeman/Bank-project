from fastapi import APIRouter, Request, status, HTTPException
from exeptions.value_not_found_error import ValueNotFoundError
from services import transaction_service
from services import category_service
from services import user_service


router = APIRouter(prefix='/transactions')


def get_connected_user():
    user_id = user_service.get_logged_in_user()
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not logged in")

    return user_id

# Throws error if validation failes, or returns if everything is ok


def validate_input(vendor, amount, category_name):
    if not (vendor and type(vendor) == str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing value for vendor field")

    if not (amount and type(amount) in [float, int]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing value for amount field")
        # TODO: Add test to check if category is in the db

    if not (category_name and type(category_name) == str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing value for category field")

    if not category_service.is_in_categories(category_name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Category does not exist")


def is_id_valid(id):
    if not type(id) == int:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="id does not exist, must be numer")


@router.post("/", status_code=201)
async def add_transaction(request: Request):
    body = await request.json()
    vendor = body.get('vendor')
    amount = body.get('amount')
    category_name = body.get('category_name')
    user_id = get_connected_user()

    validate_input(vendor, amount, category_name)
    try:
        return (transaction_service.add_transaction(body, user_id))
    except RuntimeError as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected server error, error={err}")


@router.delete("/{id}", status_code=204)
def delete_transaction(id):
    try:
        is_id_valid(id)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")

    user_id = get_connected_user()
    try:
        transaction_service.delete_transaction(id, user_id)
    except ValueNotFoundError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"id {id} not fount ")
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")


@router.get("/", status_code=201)
def get_transactions():
    user_id = get_connected_user()
    try:
        return transaction_service.get_transactions(user_id)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")


@router.get("/breakdowns", status_code=201)
def sum_transactions_by_category():
    user_id = get_connected_user()
    try:
        return transaction_service.sum_transactions_by_category(user_id)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")


@router.get("/{category_name}", status_code=201)
def get_transactions_by_category(category_name):
    user_id = get_connected_user()
    try:
        return transaction_service.get_transactions_by_category(category_name, user_id)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")


@router.put("/{id}", status_code=201)
async def update_transaction(request: Request, id):
    body = await request.json()
    vendor = body.get('vendor')
    amount = body.get('amount')
    category_name = body.get('category_name')
    if (id != body.get('id')):
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
                            detail="Bad request, mismatch in transaction id")
    user_id = get_connected_user()

    validate_input(vendor, amount, category_name)
    try:
        return (transaction_service.update_transaction(body))
    except ValueNotFoundError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found")
    except RuntimeError as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected server error, error={err}")
