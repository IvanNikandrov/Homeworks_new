from fastapi import APIRouter

router = APIRouter(tags=['Items'], prefix='/items')

@router.get('')
def get_items():
    return [{'items':1}]

@router.post('')
def create_item(data:dict):
    return {'data':data}

@router.get('/{item_id}')
def get_item(item_id:int):
    return {'iten_id':item_id}

