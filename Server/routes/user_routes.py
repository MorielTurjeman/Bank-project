from fastapi import APIRouter, status, HTTPException, Request
from exeptions.value_not_found_error import ValueNotFoundError
from services import user_service


router = APIRouter(prefix='/balance')


@router.get("/{user_id}", status_code=201)
def get_balance(user_id):
    try:
        return user_service.get_balance(user_id)
    except RuntimeError as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Unexpected server error, error={err}")

    except ValueNotFoundError as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="id {id} not fount")


# @router.post("/", status_code=201)
# async def add_user(request: Request):
#     body = await request.json()
#     first_name = body.get('first_name')
#     last_name = body.get('last_name')

#     # validate user
