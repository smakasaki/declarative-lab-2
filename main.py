import os
import requests

def save_review(review, review_type, file_number):
    folder_path = f"dataset/{review_type}"
    file_name = str(file_number).zfill(4)  # Добавление ведущих нулей
    file_path = f"{folder_path}/{file_name}.txt"
    
    os.makedirs(folder_path, exist_ok=True)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(review['title'] + "\n")
        file.write(review['description'])