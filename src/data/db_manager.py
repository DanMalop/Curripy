from typing import List, Optional
from sqlalchemy import ForeignKey, String, Date, Integer, Boolean, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Job_function_db(Base):
    pass
