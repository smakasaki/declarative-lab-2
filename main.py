import os
import requests
import time
import json

API_KEY = '9509ce90-8631-4769-b44e-ede406848cdb'
HEADERS = {
    'Content-Type': 'application/json',
    'X-API-KEY': API_KEY,
}

def get_last_saved_file_number(path):
    try:
        files = os.listdir(path)
        if not files:
            return -1
        max_number = max(int(f.rstrip('.txt')) for f in files)
        return max_number
    except FileNotFoundError:
        return -1

def save_review(review, review_type, file_number, film_name):
    folder_path = f"dataset/{review_type}"
    file_name = str(file_number).zfill(4)  # Добавление ведущих нулей
    file_path = f"{folder_path}/{file_name}.txt"
    
    os.makedirs(folder_path, exist_ok=True)
    author_name = review['author'] if review['author'] is not None else "Anonymous"
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(film_name + "\n")
        file.write(author_name + "\n")
        file.write(review['description'])

def get_reviews(movie_id, review_type, start_number, film_name):
    page = 1
    saved_reviews = start_number + 1
    
    while True:
        url = f"https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}/reviews?page={page}&order=DATE_DESC"
        response = requests.get(url, headers=HEADERS)
        time.sleep(0.1)  # Соблюдение ограничения по скорости запросов
        
        if response.status_code != 200:
            print(f"Failed to get data: {response.status_code}")
            break
        
        data = response.json()
        
        for item in data['items']:
            if item['type'] == review_type.upper():
                save_review(item, review_type.lower(), saved_reviews, film_name)
                saved_reviews += 1
        
        page += 1
        if page > data['totalPages']:
            break

def main():
    movie_ids = ['435', '195334', '535341']
    for movie_id in movie_ids:
        url = f"https://kinopoiskapiunofficial.tech/api/v2.2/films/{movie_id}"
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        film_name = data["nameRu"]

        for review_type in ['positive', 'negative']:
            folder_path = f"dataset/{review_type}"
            last_saved_number = get_last_saved_file_number(folder_path)
            get_reviews(movie_id, review_type, last_saved_number, film_name)

if __name__ == "__main__":
    main()