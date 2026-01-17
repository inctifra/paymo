import requests
import time

BASE_URL = "https://devapi.currencycloud.com"  # Demo
# BASE_URL = "https://api.currencycloud.com"   # Production

LOGIN_ID = "inctifra@gmail.com"
API_KEY = "20ce683bb870edb23fb511049181831e76936a98bf5dcb1e18c4019e78927d85"


def authenticate():
    url = f"{BASE_URL}/v2/authenticate/api"

    data = {
        "login_id": LOGIN_ID,
        "api_key": API_KEY,
    }

    response = requests.post(url, data=data, timeout=10)
    response.raise_for_status()

    auth_token = response.json()["auth_token"]
    return auth_token

def logout(auth_token):
    url = f"{BASE_URL}/v2/authenticate/close_session"
    headers = {
        "X-Auth-Token": auth_token
    }

    response = requests.post(url, headers=headers)
    response.raise_for_status()


def get_headers(auth_token):
    return {
        "X-Auth-Token": auth_token
    }


def get_currency_balance(auth_token, currency):
    url = f"{BASE_URL}/v2/balances/{currency}"
    response = requests.get(url, headers=get_headers(auth_token))
    response.raise_for_status()
    return response.json()
def get_all_balances(auth_token):
    url = f"{BASE_URL}/v2/balances/find"
    response = requests.get(url, headers=get_headers(auth_token))
    response.raise_for_status()
    return response.json()

def main():
    auth_token = authenticate()
    print("Auth token:", auth_token)
    time.sleep(1)
    balance = get_currency_balance(auth_token, "KES")
    print("account balance: ", balance)
    time.sleep(1)
    balance = get_all_balances(auth_token)
    print("all account balance: ", balance)

if __name__ == "__main__":
    main()

