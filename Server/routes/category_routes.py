from fastapi import APIRouter, status, HTTPException
from services import category_service


router = APIRouter(prefix='/categories')


@router.get("/", status_code=201)
def get_categories():
    try:
        categories = category_service.get_categories()
        return categories
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")
