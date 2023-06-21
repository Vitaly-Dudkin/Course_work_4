"""
 Abstract class for any db
 New db realisation should implement 3 methods:

 1. get_vacancies (get list of vacancies from the db)
 2. save_vacancies (save list of vacancies to the db)
 3. delete_vacancies (delete list of vacancies from the db)

"""
from abc import ABC, abstractmethod

from .vacancy_impl.vacancy import Vacancy


class GenericDB(ABC):

    @staticmethod
    @abstractmethod
    def get_vacancies() -> list[Vacancy]:
        """
        :return: List of the class: 'Vacancy' objects containing information about vacancies
        """
        pass

    @staticmethod
    @abstractmethod
    def save_vacancies(vacancies: list[Vacancy]) -> None:
        """
        :param vacancies: List of the class: 'Vacancy' objects containing information about vacancies
        """
        pass

    @staticmethod
    @abstractmethod
    def delete_vacancies() -> None:
        pass
