from additional_classes.abstract_db import GenericDB
from additional_classes.vacancy_impl.models import Vacancies
from additional_classes.vacancy_impl.vacancy import Vacancy

from utills.config import PATH_TO_JSON_FILE
from utills.json_exceptions_handling import json_interaction_errors


class JsonDB(GenericDB):

    @staticmethod
    @json_interaction_errors
    def get_vacancies() -> list[Vacancy]:
        with open(PATH_TO_JSON_FILE, "r") as file:
            json_data = file.read()

            vacancies_data = Vacancies.parse_raw(json_data)

            return [
                Vacancy(
                    title=vacancy.title,
                    url=vacancy.url,
                    description=vacancy.description,
                    salary=vacancy.salary,

                ) for vacancy in vacancies_data.vacancies
            ]

    @staticmethod
    @json_interaction_errors
    def save_vacancies(vacancies: list[Vacancy]) -> None:
        with open(PATH_TO_JSON_FILE, "w") as file:
            file.write(
                Vacancies(
                    vacancies=[vacancy.get_info() for vacancy in vacancies]
                ).json()
            )

    @staticmethod
    def delete_vacancies() -> None:
        with open(PATH_TO_JSON_FILE, "w") as file:
            file.write("")
