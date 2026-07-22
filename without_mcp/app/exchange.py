import requests

def get_exchange_rate(frm, to):

    url = f"https://open.er-api.com/v6/latest/{frm}"

    response = requests.get(url)

    data = response.json()

    rate = data["rates"].get(to)

    if not rate:
        return "Invalid currency"

    return f"1 {frm} = {rate} {to}"
