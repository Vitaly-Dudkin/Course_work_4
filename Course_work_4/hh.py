import requests

from additional_classes.abstract_parser import GenericParser
from additional_classes.vacancy_impl.vacancy import Vacancy
from additional_classes.vacancy_impl.models import Salary

from utills.web_exceptions_handling import *


class HeadHunterParser(GenericParser):

    def get_vacancies(self, pages_count: int, keywords: list[str]) -> list[Vacancy]:
        vacancies = []
        content = '+'.join(keywords)

        for page in range(1, pages_count + 1):
            url = f"https://api.hh.ru/vacancies?text={content}&page={page}"

            if response := self.make_request(url):
                for vacancy in response.json()["items"]:
                    vacancies.append(self.parse_vacancy(vacancy))

        return vacancies

    @safety_connection
    @api_errors_handling
    def make_request(self, url: str) -> requests.Response:
        return requests.get(url)

    def parse_vacancy(self, vacancy_info: dict) -> Vacancy:
        description = vacancy_info["snippet"]["requirement"]\
            .replace("<highlighttext>", "")\
            .replace("</highlighttext>", "")\
            if vacancy_info["snippet"]["requirement"] else "No description"

        return Vacancy(
            title=vacancy_info["name"],
            url=vacancy_info["alternate_url"],
            description=description,
            salary=Salary(
                min=vacancy_info["salary"]["from"] if vacancy_info["salary"]["from"] else "No info",
                max=vacancy_info["salary"]["to"] if vacancy_info["salary"]["to"] else "No info",
                currency=vacancy_info["salary"]["currency"].upper() if vacancy_info["salary"]["currency"] else "No info"
            ) if vacancy_info["salary"] else Salary(min="No info", max="No info", currency="No info")
        )