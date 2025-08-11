from datetime import date


class Curriculum_item:
    def __init__(self) -> None:
        self.visible: bool = True

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""clase = {cls}
        visible = {self.visible}"""

    def set_visible(self, visible_set: bool):
        self.visible = visible_set


class Job_detail(Curriculum_item):
    def __init__(self, content) -> None:
        super().__init__()
        self.content = content

    def __repr__(self) -> str:
        return f""" {super().__repr__()}
        description = {self.content}"""


class Job_function(Job_detail):
    def __init__(self, content) -> None:
        super().__init__(content)


class Job_achievement(Job_detail):
    def __init__(self, content) -> None:
        super().__init__(content)


class Job(Curriculum_item):
    def __init__(
        self, position: str, company: str, start_date: date, end_date: date
    ) -> None:
        super().__init__()
        self.position = position
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.functions: list[Job_function] = []
        self.achievements: list[Job_achievement] = []

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        {super().__repr__()}
        position = {self.position}
        company = {self.company}
        start_date = {self.start_date}
        end_date = {self.end_date}
        functions = {self.functions}
        achievements = {self.achievements}
        """

    def add_function(self, function: Job_function):
        self.functions.append(function)

    def add_achievement(self, achievement: Job_achievement):
        self.achievements.append(achievement)


trabajo = Job("asesor comercial", "Expertquim", date(2024, 9, 25), date(2025, 2, 14))
print(trabajo)


class Study(Curriculum_item):
    def __init__(self, title: str, institution: str, degree_date: date) -> None:
        super().__init__()
        self.title = title
        self.institution = institution
        self.degree_date = degree_date

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        {super().__repr__()}
        title = {self.title}
        institution = {self.institution}
        degree_date = {self.degree_date}
        """


class Comp_study(Study):
    def __init__(
        self, course_name: str, institution: str, certificate_date: date
    ) -> None:
        super().__init__(course_name, institution, certificate_date)


sena = Comp_study("aguas", "sena", date(2020, 12, 12))
sena.set_visible(False)
print(sena)


class Curriculum:
    def __init__(
        self, name: str, lastname: str, phone: int, email: str, linkedin: str
    ) -> None:
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.summary = None
        self.photo = None  # Image path
        self.jobs: list[Job] = []
        self.studies: list[Study] = []
        self.comp_studies: list[Comp_study] = []

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        class = {cls}
        name = {self.name}
        lastname = {self.lastname}
        phone = {self.phone}
        email = {self.email}
        linkedin = {self.linkedin}
        summary = {self.summary}
        """

    def update_description(self, summary: str):
        self.summary = summary

    def update_photo(self, image):
        self.phone = image

    def add_work_experience(self, work_exp: Job):
        self.jobs.append(work_exp)

    def add_studies(self, study_exp: Study):
        self.studies.append(study_exp)

    def add_courses(self, Comp_study_exp: Comp_study):
        self.comp_studies.append(Comp_study_exp)
