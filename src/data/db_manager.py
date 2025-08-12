from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import (
    sessionmaker,
)
# import traceback

from models import Comp_study, Curriculum, Job, Job_achievement, Job_function, Study, hv
from db_models import (
    Base,
    Job_db,
    Job_function_db,
    Job_achievement_db,
    Study_db,
    Comp_study_db,
    Curriculum_db,
)

# ----------------------------------------------------------------#
#                     DataBase manager class                      #
# ----------------------------------------------------------------#


class Db_manager:
    def __init__(self, db_file: str = "curripy.db") -> None:
        self.engine = create_engine(f"sqlite:///{db_file}", echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self._create_tables()

    # ------------------- / Create tables /------------------------#

    def _create_tables(self):
        # Create tables in the database if doesn't exist
        try:
            Base.metadata.create_all(
                self.engine
            )  # this line create all the table/classes above that inherit from Base

        except SQLAlchemyError as e:
            print(f"Error al crear las tablas: {e}")
            # traceback.print_exc()

    # ----------------- / Save curriculum / ----------------------#

    def save_curriculum(self, curriculum_obj: Curriculum):
        # Save all the Curriculum objet in the database
        session = self.Session()

        try:
            curriculum_db = Curriculum_db(
                name=curriculum_obj.name,
                lastname=curriculum_obj.lastname,
                phone=curriculum_obj.phone,
                email=curriculum_obj.email,
                linkedin=curriculum_obj.linkedin,
                summary=curriculum_obj.summary,
                photo=curriculum_obj.photo,
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
                    job_db.functions.append(job_function_db)

                # Mapping job achievements
                for achievement_obj in job_obj.achievements:
                    job_achievement_out = Job_achievement_db(
                        visible=achievement_obj.visible, content=achievement_obj.content
                    )
                    job_db.achievements.append(job_achievement_out)

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
            # traceback.print_exc()
            return 0

        finally:
            session.close()

    # ---------------- / Get curriculum / --------------------#

    def get_curriculum(self, curriculum_id: int):
        session = self.Session()
        try:
            curriculum_db = (
                session.query(Curriculum_db).filter_by(id=curriculum_id).first()
            )
            if not curriculum_db:
                return None

            curriculum_obj = Curriculum(
                name=curriculum_db.name,
                lastname=curriculum_db.lastname,
                phone=curriculum_db.phone,
                email=curriculum_db.email,
                linkedin=curriculum_db.linkedin,
                summary=curriculum_db.summary,
                photo=curriculum_db.photo,
            )

            # Mapping jobs
            for job_db in curriculum_db.jobs:
                job_obj = Job(
                    visible=job_db.visible,
                    position=job_db.position,
                    company=job_db.company,
                    start_date=job_db.start_date,
                    end_date=job_db.end_date,
                )

                # Mapping job functions
                for function_db in job_db.functions:
                    job_function_obj = Job_function(
                        visible=function_db.visible, content=function_db.content
                    )
                    job_obj.functions.append(job_function_obj)

                # Mapping job achievements
                for achievement_db in job_db.achievements:
                    job_achievement_obj = Job_achievement(
                        visible=achievement_db.visible, content=achievement_db.content
                    )
                    job_obj.achievements.append(job_achievement_obj)

                curriculum_obj.jobs.append(job_obj)

            # Mapping studies
            for study_db in curriculum_db.studies:
                study_obj = Study(
                    visible=study_db.visible,
                    title=study_db.title,
                    institution=study_db.institution,
                    degree_date=study_db.degree_date,
                )
                curriculum_obj.studies.append(study_obj)

            # Mapping complementary studies
            for comp_study_db in curriculum_db.comp_studies:
                comp_study_obj = Comp_study(
                    visible=comp_study_db.visible,
                    title=comp_study_db.title,
                    institution=comp_study_db.institution,
                    degree_date=comp_study_db.degree_date,
                )
                curriculum_obj.comp_studies.append(comp_study_obj)

            return curriculum_obj

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error getting curriculum: {e}")
            # return None

        finally:
            session.close()

    # ------------------- Update curriculum ----------------------#

    def update_curriculum(self, curriculum_id: int, updated_data: Curriculum):
        session = self.Session()

        try:
            curriculum_db = (
                session.query(Curriculum_db).filter_by(id=curriculum_id).first()
            )
            if not curriculum_db:
                return False

            curriculum_db.name = updated_data.name
            curriculum_db.lastname = updated_data.lastname
            curriculum_db.phone = updated_data.phone
            curriculum_db.email = updated_data.email
            curriculum_db.linkedin = updated_data.linkedin
            curriculum_db.summary = updated_data.summary
            curriculum_db.photo = updated_data.photo

            session.commit()
            return True

        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error updating the curriculum: {e}")
            return False

        finally:
            session.close()


database = Db_manager()
curricu = database.get_curriculum(1)

print(curricu.__repr__())
