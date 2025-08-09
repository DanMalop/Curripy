from datetime import date


class Job:
    def __init__(
        self, position: str, company: str, start_date: date, end_date: date
    ) -> None:
        self.position = position
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.functions: list[str] = []
        self.achievements: list[str] = []
        self.visible: bool = True

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        class = {cls}
        position = {self.position}
        company = {self.company}
        start_date = {self.start_date}
        end_date = {self.end_date}
        functions = {self.functions}
        achievements = {self.achievements}
        """

    def add_function(self, function: str):
        self.functions.append(function)

    def add_achievement(self, achievement: str):
        self.achievements.append(achievement)

    def set_visibel(self, visible_set: bool):
        self.visible = visible_set


trabajo = Job("asesor comercial", "Expertquim", date(2024, 9, 25), date(2025, 2, 14))
trabajo.add_function("mamar huevo")
print(trabajo)


class Study:
    def __init__(self, title: str, institution: str, degree_date: date) -> None:
        self.title = title
        self.institution = institution
        self.degree_date = degree_date

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        class = {cls}
        title = {self.title}
        institution = {self.institution}
        degree_date = {self.degree_date}
        """


class Course:
    def __init__(
        self, course_name: str, institution: str, certificate_date: date
    ) -> None:
        self.course_name = course_name
        self.institution = institution
        self.certificate_date = certificate_date

    def __repr__(self):
        cls = self.__class__.__name__
        return f"""
        clase = {cls}
        course_name = {self.course_name}
        institution = {self.institution}
        certificate_date = {self.certificate_date}
        """


class Curriculum:
    def __init__(
        self, name: str, lastname: str, phone: int, email: str, linkedin: str
    ) -> None:
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.email = email
        self.linkedin = linkedin
        self.description = None
        self.photo = None
        self.work_experience = []
        self.studies = []
        self.courses = []

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        class = {cls}
        name = {self.name}
        lastname = {self.lastname}
        phone = {self.phone}
        email = {self.email}
        linkedin = {self.linkedin}
        """

    def update_description(self, text_description: str):
        self.description = text_description

    def update_photo(self, image):
        self.phone = image

    def add_work_experience(self, work_exp: Job):
        self.work_experience.append(work_exp)

    def add_studies(self, study_exp: Study):
        self.studies.append(study_exp)

    def add_courses(self, course_exp: Course):
        self.courses.append(course_exp)
