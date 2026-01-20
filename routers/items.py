from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from database import get_session
from models import Item

router = APIRouter()

@router.get("/items")
def read_items(session: Session = Depends(get_session)):
    items = session.exec(select(Item)).all()
    return items

@router.post("/items/")
def create_item(item: Item, session: Session = Depends(get_session)):
    session.add(item)
    session.commit()
    session.refresh(item)

    return item