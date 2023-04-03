import requests

url = "https://basketapi1.p.rapidapi.com/api/basketball/search/kevin"

headers = {
	"X-RapidAPI-Key": "f8c1edc71amsh2ceb94e75170cf3p1172ddjsn28d9990da6a6",
	"X-RapidAPI-Host": "basketapi1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)