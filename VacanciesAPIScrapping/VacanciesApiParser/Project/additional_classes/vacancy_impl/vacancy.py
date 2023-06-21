"""
Class for interacting with data about vacancies

"""

from .models import VacancyInfo, Salary


class Vacancy:

    def __init__(self, title: str, url: str, description: str,  salary: Salary | str):
        """
        :param title: The title pf vacancy
        :param url: Url to vacancy page in the website
        :param description: Brief job description
        :param salary: class: Salary object if salary data is not empty or str: "No salary info"
        """
        self._info = VacancyInfo(
            title=title,
            url=url,
            description=description,
            salary=salary
        )

    def __str__(self) -> str:
        return f"\nTitle: {self.get_info().title}" \
               f"\nUrl: {self.get_info().url}" \
               f"\nSalary: {self.get_info().salary}" \
               f"\nDescription: {self.get_info().description}"

    def __lt__(self, other):
        """The method is overloaded for use when sorting vacancies"""
        return self.calculate_average_salary() < other.calculate_average_salary()

    def get_info(self) -> VacancyInfo:
        return self._info

    def calculate_average_salary(self) -> float:
        """
        :return float: if all salary fields are not empty
        :return 0: if any of salary fields is empty
        """
        if isinstance(self._info.salary.min, int) and isinstance(self._info.salary.max, int):
            return (self._info.salary.min + self._info.salary.max) / 2
        else:
            return 0