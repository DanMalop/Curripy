from datetime import date
from typing import List
from sqlalchemy import ForeignKey, String, Date, Integer, Boolean
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

# --------------------------------------------------------------#
#                      ORM table classes                       #
# --------------------------------------------------------------#


class Base(DeclarativeBase):
    pass


class Curriculum_db(Base):
    __tablename__ = "curriculums_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    lastname: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    linkedin: Mapped[str] = mapped_column(String, nullable=True)
    summary: Mapped[str] = mapped_column(String, nullable=True)
    photo: Mapped[str] = mapped_column(String, nullable=True)

    jobs: Mapped[List["Job_db"]] = relationship(
        back_populates="curriculums", cascade="all, delete-orphan"
    )

    studies: Mapped[List["Study_db"]] = relationship(
        back_populates="curriculums", cascade="all, delete-orphan"
    )

    comp_studies: Mapped[List["Comp_study_db"]] = relationship(
        back_populates="curriculums", cascade="all, delete-orphan"
    )


class Job_db(Base):
    __tablename__ = "jobs_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    position: Mapped[str] = mapped_column(String, nullable=True)
    company: Mapped[str] = mapped_column(String, nullable=True)
    start_date: Mapped[date] = mapped_column(Date, nullable=True)
    end_date: Mapped[date] = mapped_column(Date, nullable=True)
    visible: Mapped[bool] = mapped_column(Boolean, nullable=True)
    curriculum_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("curriculums_table.id")
    )

    functions: Mapped[List["Job_function_db"]] = relationship(
        back_populates="jobs", cascade="all, delete-orphan"
    )

    achievements: Mapped[List["Job_achievement_db"]] = relationship(
        back_populates="jobs", cascade="all, delete-orphan"
    )

    curriculums: Mapped["Curriculum_db"] = relationship(back_populates="jobs")


class Job_function_db(Base):
    __tablename__ = "job_functions_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String, nullable=True)
    visible: Mapped[bool] = mapped_column(Boolean, nullable=True)
    jobs_id: Mapped[int] = mapped_column(Integer, ForeignKey("jobs_table.id"))

    jobs: Mapped["Job_db"] = relationship(back_populates="functions")


class Job_achievement_db(Base):
    __tablename__ = "job_achievements_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String, nullable=True)
    visible: Mapped[bool] = mapped_column(Boolean, nullable=True)
    jobs_id: Mapped[int] = mapped_column(Integer, ForeignKey("jobs_table.id"))

    jobs: Mapped["Job_db"] = relationship(back_populates="achievements")


class Study_db(Base):
    __tablename__ = "studies_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=True)
    institution: Mapped[str] = mapped_column(String, nullable=True)
    degree_date: Mapped[date] = mapped_column(Date, nullable=True)
    visible: Mapped[bool] = mapped_column(Boolean, nullable=True)
    curriculum_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("curriculums_table.id")
    )

    curriculums: Mapped["Curriculum_db"] = relationship(back_populates="studies")


class Comp_study_db(Base):
    __tablename__ = "comp_studies_table"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=True)
    institution: Mapped[str] = mapped_column(String, nullable=True)
    degree_date: Mapped[date] = mapped_column(Date, nullable=True)
    visible: Mapped[bool] = mapped_column(Boolean, nullable=True)
    curriculum_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("curriculums_table.id")
    )

    curriculums: Mapped["Curriculum_db"] = relationship(back_populates="comp_studies")
