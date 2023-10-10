import requests

url = 'https://www.gismeteo.ru/diary/4976/2023/9/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    print('Status code: ', response.status_code)
    print('Text: ', response.text[:50])
except requests.exceptions.RequestException as e:
    print(f'Request failed: {str(e)}')
