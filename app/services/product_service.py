from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.product import Product
from app.models.user import User, UserRole
from app.schemas.product import ProductCreate, ProductUpdate


def get_products(db: Session, skip: int = 0, limit: int = 20) -> list[Product]:
    return db.query(Product).filter(Product.is_active == True).offset(skip).limit(limit).all()


def get_product_by_id(db: Session, product_id: int) -> Product:
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


def create_product(db: Session, data: ProductCreate, owner: User) -> Product:
    if owner.role != UserRole.admin:
        raise HTTPException(status_code=403, detail="Solo admins pueden crear productos")
    product = Product(**data.model_dump(), owner_id=owner.id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def update_product(db: Session, product_id: int, data: ProductUpdate, current_user: User) -> Product:
    product = get_product_by_id(db, product_id)
    if current_user.role != UserRole.admin and product.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sin permisos para editar este producto")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int, current_user: User) -> dict:
    product = get_product_by_id(db, product_id)
    if current_user.role != UserRole.admin and product.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Sin permisos")
    db.delete(product)
    db.commit()
    return {"message": f"Producto {product_id} eliminado"}
