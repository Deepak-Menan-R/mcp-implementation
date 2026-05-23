import requests


tool = {
    "name": "exchange_rate",
    "description": "Get exchange rate between currencies"
}


def execute(frm, to):

    url = f"https://open.er-api.com/v6/latest/{frm}"

    response = requests.get(url)

    data = response.json()

    rate = data["rates"].get(to)

    return f"1 {frm} = {rate} {to}"