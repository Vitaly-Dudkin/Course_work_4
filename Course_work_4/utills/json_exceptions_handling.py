from pydantic import ValidationError

from .colors import Color


def json_interaction_errors(function):
    def wrapper(*args, **kwargs):
        try:
            data = function(*args, **kwargs)

        except FileNotFoundError:
            print(f"{Color.red}Json file doesn't exists{Color.white}\n")

        except ValidationError as error:
            print(f"{Color.red}Error during loading/dumping json file. Check it's integrity!{Color.white}\n"
                  f"Error's text: {error}\n")
        else:
            print(f"{Color.green}Vacancies were successfully load{Color.white}\n")
            return data

    return wrapper
