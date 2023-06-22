from requests import ConnectionError

from .colors import Color


def safety_connection(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ConnectionError:
            print(f"{Color.red}Communication with API interrupted. Check your internet connection{Color.white}")

    return wrapper


def api_errors_handling(function):
    def wrapper(*args, **kwargs):
        response = function(*args, **kwargs)
        if response.ok:
            return response
        else:
            print(f"{Color.red}Error occurred during request to API. Status code {response.status_code}{Color.white}")

    return wrapper
