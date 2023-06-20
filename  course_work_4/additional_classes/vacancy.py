from .models import VacancyInfo, Salary


class Vacancy:

    def __init__(self, title: str, url: str, description: str,  salary: Salary | str):
        self._info = VacancyInfo(
            title=title,
            url=url,
            description=self._validate_description(description),
            salary=salary
        )

    def __str__(self) -> str:
        return f"\nTitle: {self.get_info().title}" \
               f"\nUrl: {self.get_info().url}" \
               f"\nSalary: {self.get_info().salary}" \
               f"\nDescription: {self.get_info().description}"

    def __lt__(self, other):
        return self._calculate_average_salary() < other._calculate_average_salary()

    def get_info(self) -> VacancyInfo:
        return self._info

    @staticmethod
    def _validate_description(description: str) -> str:
        if description:
            return description.replace("<highlighttext>", "").replace("</highlighttext>", "")
        else:
            return "No description"

    def _calculate_average_salary(self) -> float:
        if isinstance(self._info.salary.min, int) and isinstance(self._info.salary.max, int):
            return (self._info.salary.min + self._info.salary.max) / 2
        else:
            return 0
