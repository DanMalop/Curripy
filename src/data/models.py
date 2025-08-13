from datetime import date


class Curriculum_item:
    def __init__(self, id: int = 0, visible: bool = True) -> None:
        self.id = id
        self.visible = visible

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""clase = {cls}
        id = {self.id}
        visible = {self.visible}"""

    def set_visible(self, visible_set: bool):
        self.visible = visible_set


class Job_detail(Curriculum_item):
    def __init__(self, content: str, id: int = 0, visible=True) -> None:
        super().__init__(id, visible)
        self.content = content

    def __repr__(self) -> str:
        return f""" {super().__repr__()}
        description = {self.content}"""


class Job_function(Job_detail):
    def __init__(self, content: str, id: int = 0, visible=True) -> None:
        super().__init__(content, id, visible)


class Job_achievement(Job_detail):
    def __init__(self, content: str, id: int = 0, visible=True) -> None:
        super().__init__(content, id, visible)


class Job(Curriculum_item):
    def __init__(
        self,
        position: str,
        company: str,
        start_date: date,
        end_date: date,
        id: int = 0,
        visible=True,
    ) -> None:
        super().__init__(id, visible)
        self.position = position
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.functions: list[Job_function] = []
        self.achievements: list[Job_achievement] = []

    def __repr__(self) -> str:
        return f"""
        {super().__repr__()}
        position = {self.position}
        company = {self.company}
        start_date = {self.start_date}
        end_date = {self.end_date}
        functions = {self.functions}
        achievements = {self.achievements}
        """

    def add_function(self, list_functions: list[Job_function]):
        self.functions += list_functions

    def add_achievement(self, list_achievements: list[Job_achievement]):
        self.achievements = list_achievements


class Study(Curriculum_item):
    def __init__(
        self, title: str, institution: str, degree_date: date, id: int = 0, visible=True
    ) -> None:
        super().__init__(id, visible)
        self.title = title
        self.institution = institution
        self.degree_date = degree_date

    def __repr__(self) -> str:
        return f"""
        {super().__repr__()}
        title = {self.title}
        institution = {self.institution}
        degree_date = {self.degree_date}
        """


class Comp_study(Study):
    def __init__(
        self, title: str, institution: str, degree_date: date, id: int = 0, visible=True
    ) -> None:
        super().__init__(title, institution, degree_date, id, visible)


class Curriculum:
    def __init__(
        self,
        name: str,
        lastname: str,
        phone: str,
        email: str,
        linkedin: str,
        summary: str,
        photo: str,
        id: int = 0,
    ) -> None:
        self.id = id
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.summary = summary
        self.photo = photo  # Image path
        self.jobs: list[Job] = []
        self.studies: list[Study] = []
        self.comp_studies: list[Comp_study] = []

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        class = {cls}
        id = {self.id}
        name = {self.name}
        lastname = {self.lastname}
        phone = {self.phone}
        email = {self.email}
        linkedin = {self.linkedin}
        summary = {self.summary}
        """

    def set_id(self, curriculum_id: int):
        self.id = curriculum_id
        return True

    def get_id(self):
        return self.id

    def update_description(self, summary: str):
        self.summary = summary

    def update_photo(self, image):
        self.phone = image

    def add_jobs(self, work_exp: list[Job]):
        self.jobs += work_exp

    def add_studies(self, study_exp: list[Study]):
        self.studies += study_exp

    def add_comp_studies(self, Comp_study_exp: list[Comp_study]):
        self.comp_studies += Comp_study_exp


function1 = Job_function("mamar")
function1 = Job_function("peer")
achievement1 = Job_achievement("cagar mucho")
achievement2 = Job_achievement("peer mucho")
trabajo1 = Job("cagador", "cagaderia", date(2021, 4, 21), date(2024, 3, 12))
trabajo1.add_achievement([achievement1, achievement2])
estudio1 = Study("ing cagalera", "inst cagare", date(2020, 2, 3))
curso1 = Comp_study("peos op", "inst peare", date(2019, 5, 19))
hv = Curriculum(
    "Dany",
    "Peo",
    "1234",
    "bollo@pmail.com",
    "https: peo",
    "soy el mejor peador y cagador de la historia humana",
    "/cagada",
)

hv.add_comp_studies([curso1])
hv.add_studies([estudio1])
hv.add_jobs([trabajo1])
