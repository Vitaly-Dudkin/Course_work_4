import requests

from additional_classes.abstract_parser import GenericParser
from additional_classes.vacancy_impl.vacancy import Vacancy
from additional_classes.vacancy_impl.models import Salary

from utills.config import SUPER_JOB_APP_KEY
from utills.web_exceptions_handling import *


class SuperJobParser(GenericParser):

    def get_vacancies(self, pages_count: int, keywords: list[str]) -> list[Vacancy]:
        vacancies = []

        content = '&'.join(f"keywords%5B{i}%5D%5Bsrws%5D=10&"
                           f"keywords%5B{i}%5D%5Bskwc%5D=and&"
                           f"keywords%5B{i}%5D%5Bkeys%5D={keyword}" for i, keyword in enumerate(keywords, start=1))

        for page in range(1, pages_count + 1):
            url = f"https://api.superjob.ru/2.0/vacancies/?keywords%5B0%5D%5Bkeys%5D=&{content}&page={page}"

            if response := self.make_request(url):
                for vacancy in response.json()["objects"]:
                    vacancies.append(self.parse_vacancy(vacancy))

        return vacancies

    @safety_connection
    @api_errors_handling
    def make_request(self, url: str) -> requests.Response:
        headers = {
            "Host": "api.superjob.ru",
            "X-Api-App-Id": SUPER_JOB_APP_KEY,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        return requests.get(url, headers=headers)

    def parse_vacancy(self, vacancy_info: dict) -> Vacancy:
        return Vacancy(
            title=vacancy_info["profession"],
            url=vacancy_info["link"],
            description=vacancy_info["candidat"],
            salary=Salary(
                min=vacancy_info["payment_from"] if vacancy_info["payment_from"] else "No info",
                max=vacancy_info["payment_to"] if vacancy_info["payment_to"] else "No info",
                currency=vacancy_info["currency"].upper() if vacancy_info["currency"] else "No info"
            )
        )
