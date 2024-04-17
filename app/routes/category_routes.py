from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schema.category_schema import CategoryReturn, CategoryCreate
from app.db.db_config import SessionLocal, get_db
from app.db.models import Category
from app.utils.category_utils import check_existing_category

router = APIRouter()
db = SessionLocal()


@router.post("/", response_model=CategoryReturn, status_code=201)
async def create_category(category_data: CategoryCreate, db: Session = Depends(get_db)):
    # check if product exist
    check_existing_category(db, category_data)
    # continue if not already exist
    new_category = Category(**category_data.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
