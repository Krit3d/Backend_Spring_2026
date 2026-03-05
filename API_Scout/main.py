import requests

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    # В случае исключения сообщаем об этом пользователю
    print(f"Your request returned an exception: {type(e).__name__}.")
    print("Please check your internet connection")
else:
    if response.status_code == 200:
        # Превращаем JSON-ответ в словарь Python
        data = response.json()

        # Выводим по ключу
        print(
            f"The current value of 1 BTC($): {data.get("bitcoin", {}).get("usd", "No data")}"
        )
    else:
        print("Server Error. Please wait or check if your request is right")
