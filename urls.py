import requests

url = "https://turkiyeapi.dev/api/v1/neighborhoods"
limit = 200
offset = 0 
neighborhoods = []

while True:
    response = requests.get(url, params={'limit': limit, 'offset': offset})
    
    if response.status_code == 200:
        data = response.json()
        neighborhoods.extend(data['data'])
        print(data)
        if len(data['data']) < limit:
            break
        else:
            offset += limit
    else:
        print(f"Veri alınamadı: {response.status_code}")
        break
