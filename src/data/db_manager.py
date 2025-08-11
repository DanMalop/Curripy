from datetime import date
from typing import List
from sqlalchemy import ForeignKey, String, Date, Integer, Boolean, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    session,
    sessionmaker,
)

from data.models import Curriculum


# -----------------------------------------------------------------------------------------------------------
#                            ORM table classes
# ----------------------------------------------------------------------------------------------------------


class Base(DeclarativeBase):
    pass


class Curriculum_db(Base):
    __tablename__ = "curriculums"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    lastname: Mapped[str] = mapped_column(String)
    phone: Mapped[int] = mapped_column(Integer)
    email: Mapped[str] = mapped_column(String)
    linkedin: Mapped[str] = mapped_column(String)
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
    __tablename__ = "jobs"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    position: Mapped[str] = mapped_column(String)
    company: Mapped[str] = mapped_column(String)
    start_date: Mapped[date] = mapped_column(Date)
    end_date: Mapped[date] = mapped_column(Date)
    visible: Mapped[bool] = mapped_column(Boolean)

    job_functions: Mapped[List["Job_function_db"]] = relationship(
        back_populates="jobs", cascade="all, delete-orphan"
    )

    job_achievements: Mapped[List["Job_achievement_db"]] = relationship(
        back_populates="jobs", cascade="all, delete-orphan"
    )

    curriculums: Mapped["Curriculum_db"] = relationship(back_populates="jobs")


class Job_function_db(Base):
    __tablename__ = "job_functions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String)
    visible: Mapped[bool] = mapped_column(Boolean)
    jobs_id = mapped_column(Integer, ForeignKey("jobs.id"))

    jobs: Mapped["Job_db"] = relationship(back_populates="job_functions")


class Job_achievement_db(Base):
    __tablename__ = "job_achievements"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    content: Mapped[str] = mapped_column(String)
    visible: Mapped[bool] = mapped_column(Boolean)
    jobs_id = mapped_column(Integer, ForeignKey("jobs.id"))

    jobs: Mapped["Job_db"] = relationship(back_populates="job_achievements")


class Study_db(Base):
    __tablename__ = "studies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    institution: Mapped[str] = mapped_column(String)
    degree_date: Mapped[date] = mapped_column(Date)
    visible: Mapped[bool] = mapped_column(Boolean)

    curriculums: Mapped["Curriculum_db"] = relationship(back_populates="studies")


class Comp_study_db(Base):
    __tablename__ = "comp_studies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String)
    institution: Mapped[str] = mapped_column(String)
    degree_date: Mapped[date] = mapped_column(Date)
    visible: Mapped[bool] = mapped_column(Boolean)

    curriculums: Mapped["Curriculum_db"] = relationship(back_populates="comp_studies")


# -----------------------------------------------------------------------------------------------------------
#                            DataBase manager class
# ----------------------------------------------------------------------------------------------------------


class db_manager:
    def __init__(self, db_file: str = "curripy.db") -> None:
        self.engine = create_engine(f"sqlite:///{db_file}", echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def _create_tables(self):
        # Create tables in the database if doesn't exist
        try:
            Base.metadata.create_all(
                self.engine
            )  # this line create all the table/classes above that inherit from Base

        except SQLAlchemyError as e:
            print(f"Error al crear las tablas: {e}")

    # ----------------------------- / Save curriculum / -------------------------------

    def save_curriculum(self, curriculum_obj: Curriculum):
        # Save all the Curriculum objet in the database
        session = self.Session()

        try:
            # create a database object from the model object
            curriculum_db = Curriculum_db(
                name=curriculum_obj.name,
                lastname=curriculum_obj.lastname,
                phone=curriculum_obj.phone,
                email=curriculum_obj.email,
                linkedin=curriculum_obj.linkedin,
                summary=curriculum_obj.summary,
            )

            # Mapping jobs
            for job_obj in curriculum_obj.jobs:
                job_db = Job_db(
                    visible=job_obj.visible,
                    position=job_obj.position,
                    company=job_obj.company,
                    start_date=job_obj.start_date,
                    end_date=job_obj.end_date,
                )

                # Mapping job functions
                for function_obj in job_obj.functions:
                    job_function_db = Job_function_db(
                        visible=function_obj.visible, content=function_obj.content
                    )
                    job_db.job_functions.append(job_function_db)

                # Mapping job achievements
                for achievement_obj in job_obj.achievements:
                    job_achievement_db = Job_achievement_db(
                        visible=achievement_obj.visible, content=achievement_obj.content
                    )
                    job_db.job_achievements.append(job_achievement_db)

                curriculum_db.jobs.append(job_db)

            # Mapping studies
            for study_obj in curriculum_obj.studies:
                study_db = Study_db(
                    visible=study_obj.visible,
                    title=study_obj.title,
                    institution=study_obj.institution,
                    degree_date=study_obj.degree_date,
                )
                curriculum_db.studies.append(study_db)

            # Mapping complementary studies
            for comp_study_obj in curriculum_obj.comp_studies:
                comp_study_db = Comp_study_db(
                    visible=comp_study_obj.visible,
                    title=comp_study_obj.title,
                    institution=comp_study_obj.institution,
                    degree_date=comp_study_obj.degree_date,
                )
                curriculum_db.comp_studies.append(comp_study_db)

            session.add(curriculum_db)
            session.commit()

            return curriculum_db.id

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error saving curriculum: {e}")
            return None

        finally:
            session.close()

    # ---------------------- / Get curriculums / ------------------------

    def get_curriculum(self, curriculum_id: int):
        session = self.Session()
