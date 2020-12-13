import requests


def get_list():

    url = "http://127.0.0.1:8001/api/v1/cars/list_car/"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


def del_car():
    url = "http://127.0.0.1:8001/api/v1/cars/update_car/2/"

    payload = {}
    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)


if __name__ == "__main__":
    # get_list()
    del_car()