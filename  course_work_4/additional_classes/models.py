"""
Dataclasses to simple conversion to/from json

"""


from pydantic import BaseModel


class Salary(BaseModel):
    min: int | str
    max: int | str
    currency: str

    def __str__(self) -> str:
        return f"from: {self.min}, to: {self.max}, currency: {self.currency}"


class VacancyInfo(BaseModel):
    title: str
    url: str
    description: str
    salary: str | Salary


class Vacancies(BaseModel):
    vacancies: list[VacancyInfo]
