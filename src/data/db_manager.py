from typing import Type, TypeVar
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

# --------------------------------------------------------------------#
#            Function Map obj to db model or viceversa               #
# --------------------------------------------------------------------#

T = TypeVar("T")


def map_objects(source_obj: object, target_class: Type[T]) -> T:
    # this funciton mapped the domain object to a SQLAlchemy model or viceversa
    is_source_model = hasattr(source_obj, "__table__")

    if hasattr(target_class, "__table__"):
        columns_model = target_class.__table__.columns
        save = True
    elif is_source_model:
        columns_model = source_obj.__table__.columns
        save = False
    else:
        raise ValueError("Not detected any SQLAlchemy model in the mapping")

    if save:
        camps = {
            c.name: getattr(source_obj, c.name)
            for c in columns_model
            if hasattr(source_obj, c.name) and "_id" not in c.name and "id" != c.name
        }

    else:
        camps = {
            c.name: getattr(source_obj, c.name)
            for c in columns_model
            if hasattr(source_obj, c.name) and "_id" not in c.name
        }

    return target_class(**camps)


def map_all_objets(source_curriculum: object):
    if hasattr(source_curriculum, "__table__"):
        target_classes = [
            Curriculum,
            Job,
            Job_function,
            Job_achievement,
            Study,
            Comp_study,
        ]
    elif source_curriculum.__class__.__name__ == "Curriculum":
        target_classes = [
            Curriculum_db,
            Job_db,
            Job_function_db,
            Job_achievement_db,
            Study_db,
            Comp_study_db,
        ]
    else:
        raise ValueError(
            "Not detected any SQLAlchemy model or Curriculum class in the mapping"
        )

    curriculum_out = map_objects(source_curriculum, target_classes[0])

    # Mapping jobs
    for source_job in source_curriculum.jobs:
        job_out = map_objects(source_job, target_classes[1])
        # Mapping job functions
        for source_function in source_job.functions:
            job_function_out = map_objects(source_function, target_classes[2])
            job_out.functions.append(job_function_out)

        # Mapping job achievements
        for source_achievement in source_job.achievements:
            job_achievement_out = map_objects(source_achievement, target_classes[3])
            job_out.achievements.append(job_achievement_out)

        curriculum_out.jobs.append(job_out)

        # Mapping studies
    for source_study in source_curriculum.studies:
        study_out = map_objects(source_study, target_classes[4])
        curriculum_out.studies.append(study_out)

    # Mapping complementary studies
    for source_comp_study in source_curriculum.comp_studies:
        comp_study_out = map_objects(source_comp_study, target_classes[5])
        curriculum_out.comp_studies.append(comp_study_out)

    return curriculum_out


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
            curriculum_db = map_all_objets(curriculum_obj)
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

            curriculum_obj = map_all_objets(curriculum_db)
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
id = database.save_curriculum(hv)
hv.set_id(id)
print(id)
print(hv.__repr__())
