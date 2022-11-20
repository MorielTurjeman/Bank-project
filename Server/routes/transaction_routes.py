from fastapi import APIRouter, Request, status, HTTPException
from exeptions.value_not_found_error import ValueNotFoundError
from services import transaction_service


router = APIRouter(prefix='/transactions')

# class MyClass(BaseModel):
#     name: str
#     id: int


@router.post("/", status_code=201)
async def add_transaction(request: Request):
    body = await request.json()
    vendor = body.get('vendor')
    amount = body.get('amount')
    category_name = body.get('category_name')
    if not (vendor and type(vendor) == str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing value for vendor field")
    if not (amount and (type(amount) == float or type(amount) == int)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing value for amount field")
    if not (category_name and type(category_name) == str):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or missing value for category field")
    try:
        return (transaction_service.add_transaction(body))
    except RuntimeError as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Unexpected server error, error={err}")


@router.put("/{id}", status_code=204)
def delete_transaction(id):
    try:
        transaction_service.delete_transaction(id)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")

    except ValueNotFoundError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id {id} not fount")


@router.get("/", status_code=201)
def get_transactions():
    try:
        return transaction_service.get_transactions()
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")


@router.get("/breakdowns", status_code=201)
def sum_transactions_by_category():
    try:
        return transaction_service.sum_transactions_by_category()
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")


@router.get("/{category_name}", status_code=201)
def get_transactions_by_category(category_name):
    try:
        return transaction_service.get_transactions_by_category(category_name)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")