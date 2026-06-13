# model.py 
# from .db import Base 
# from sqlalchemy import Column, Integer, String 

# class Item(Base): 
#     __tablename__="item" 
#     id = Column(Integer, primary_key = True, index=True) 
#     name = Column(String, nullable = False) 
    
    
# schema.py 
# from pydantic import BaseModel, ConfigDict, Field

# class ItemBase(BaseModel): 
#     name: str=Field(...,min_length=3) 
    
# class ItemCreate(ItemBase): 
#     pass 

# class ItemResponse(ItemBase): 
#     id:int 
#     model_config = ConfigDict(from_attributes=True) 
    
    
# servies.py 
# from sqlalchemy.orm import Session 
# from .model import Item 
# from .schema import ItemCreate 

# def create_item(db:Session, item_data: ItemCreate) -> Item: 
#     item = Item(**item_data.model_dump()) 
#     db.add(item) 
#     db.commit() 
#     db.refresh(item) 
#     return item 

# def get_item(db:Session, item_id:int)->Item: 
#     return db.query(Item).filter(Item.id==item_id).first() 


# route.py 
# from fastapi import APIRouter , Depends
# from .db import get_db
# from .schema import ItemCreate
# from .service import create_item, get_item
# router = APIRouter(prefix="/item",tags=["Item"]) 

# @router.post("/", response_model=ItemResponse) 
# def create_item(item:ItemCreate, db: Session = Depends(get_db)): 
#     return create_item(db, item) 

# @router.get("/{item_id}",response_model = ItemResponse)
# def get_item(item_id:int, db:Session= Depends(get_db)): 
#     return get_item(db,item_id) 

# main.py 
# from fastapi import FastAPI 
# from .router import router 
# app = FastAPI() 
# app.include_router(router)