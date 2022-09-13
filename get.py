import requests

print(requests.__version__)

print(requests.get("https://raw.githubusercontent.com/akshat799/CMPUT404Lab1/main/get.py").text)
