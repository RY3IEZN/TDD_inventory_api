from .db_config import Base
import sqlalchemy
from sqlalchemy import (
    Column,
    Integer,
    CheckConstraint,
    String,
    Boolean,
    UniqueConstraint,
    Text,
    text,
    DateTime,
    Enum,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(
        String(120),
        nullable=False,
    )
    is_active = Column(Boolean, nullable=False, default=False, server_default="FALSE")
    level = Column(Integer, nullable=False, default="200", server_default="100")
    parent_id = Column(Integer, ForeignKey("category.id"), nullable=True)

    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="category_name_length_check"),
        CheckConstraint("LENGTH(slug) > 0", name="category_slug_length_check"),
        UniqueConstraint("name", "level", name="unq_category_name_level"),
        UniqueConstraint("slug", name="unq_category_name_level"),
    )


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, nullable=False)
    pid = Column(
        UUID(as_uuid=True),
        nullable=False,
        unique=True,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String(200), nullable=False)
    slug = Column(
        String(220),
        nullable=False,
    )
    description = Column(Text, nullable=True)
    is_digital = Column(Boolean, nullable=False, default=False, server_default="False")
    created_at = Column(
        DateTime, server_default=text("CURRENT_TIMESTAMP"), nullable=False
    )
    update_at = Column(
        DateTime,
        server_default=text("CURRENT_TIMESTAMP"),
        nullable=False,
        onupdate=sqlalchemy.func.now(),
    )
    is_active = Column(Boolean, nullable=False, default=False, server_default="False")
    stock_status = Column(
        Enum("oos", "is", "obo", name="status_enum"),
        nullable=False,
        server_default="oos",
    )
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    # seasonal_id = Column(Integer, ForeignKey("seasonal_event.id"), nullable=True)

    __table_args__ = (
        CheckConstraint("LENGTH(name) > 0", name="product_name_length_check"),
        CheckConstraint("LENGTH(slug) > 0", name="product_slug_length_check"),
        UniqueConstraint("name", name="unq_product_name_level"),
        UniqueConstraint("slug", name="unq_product_name_slug"),
    )
