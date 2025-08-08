from datetime import date


class job:
    def __init__(
        self, position: str, company: str, start_date: date, end_date: date
    ) -> None:
        self.position = position
        self.company = company
        self.start_date = start_date
        self.end_date = end_date
        self.functions = []
        self.achievements = []

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


# trabajo = job("asesor comercial", "Expertquim", date(2024, 9, 25), date(2025, 2, 14))


class study:
    def __init__(self, institution: str, title: str, degree_date: date) -> None:
        self.institution = institution
        self.title = title
        self.degree_date = degree_date

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        return f"""
        class = {cls}
        institution = {self.institution}
        title = {self.title}
        degree_date = {self.degree_date}
        """


class course:
    def __init__(self) -> None:
        pass


class user:
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
    """
