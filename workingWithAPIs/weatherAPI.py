# 39c9862ba1a1e9732d3f0380de1d4892

import requests

response = requests.get(
    "http://api.openweathermap.org/data/2.5/forecast/daily?q=London&units=metric&cnt=7&appid={api}")

print(response.status_code)
