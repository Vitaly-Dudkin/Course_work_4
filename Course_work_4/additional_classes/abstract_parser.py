"""
 Abstract class for any parser
 New parser realisation should implement 3 methods:

 1. get_vacancies (get vacancies page)
 2. parse_vacancy (get vacancy data)
 3. make_request (make request to website API)

"""
import requests

from abc import ABC, abstractmethod

from .vacancy_impl.vacancy import Vacancy


class GenericParser(ABC):

    @abstractmethod
    def get_vacancies(self, pages_count: int, keywords: list[str]) -> list[Vacancy]:
        """
        :param pages_count: Number of pages to parse (20 vacancies per page)
        :param keywords: List of words for searching in the vacancy description

        :return: List of the class: 'Vacancy' objects containing information about vacancies
        """

        pass

    @abstractmethod
    def parse_vacancy(self, vacancy_info: dict) -> Vacancy:
        """
        :param vacancy_info: Dictionary with some fields  containing information about the current vacancy

        :return: Vacancy object with parsed fields
        """
        pass

    @abstractmethod
    def make_request(self, url: str) -> requests.Response:
        """
        :param url: Url to website API

        :return: API response
        """
        pass