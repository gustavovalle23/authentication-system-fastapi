from fastapi import APIRouter


router = APIRouter()


@router.get('/users/', tags=['users'])
async def read_users():
    return [{'name': 'Gustavo Valle', 'email': 'gustavo.vallerp@hotmail.com'}]
