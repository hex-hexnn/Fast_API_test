from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get('/users/')
async def get_users():
    return [{'name': 'Aleks'}]