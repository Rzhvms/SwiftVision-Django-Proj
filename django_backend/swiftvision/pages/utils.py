import requests
from datetime import datetime

def get_vacancy_details(vacancy_id):
    url = f"https://api.hh.ru/vacancies/{vacancy_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_vacancies(profession_keywords):
    params = {
        'text': profession_keywords,
        'order_by': 'publication_time',
        'per_page': 10,
        'search_field': 'name'
    }

    response = requests.get("https://api.hh.ru/vacancies", params=params)
    if response.status_code != 200:
        print(f"Ошибка: {response.status_code}. {response.text}")
        return []

    return response.json().get('items', [])

def get_salary(salary):
    if not salary:
        return 'Не указан'
    salary_from = salary.get('from')
    salary_to = salary.get('to')
    currency = salary.get('currency', 'RUR')
    gross = '(gross)' if salary.get('gross') else ''
    if salary_from and salary_to:
        return f"{salary_from} - {salary_to} {currency} {gross}"
    elif salary_from:
        return f"{salary_from} {currency} {gross}"
    elif salary_to:
        return f"до {salary_to} {currency} {gross}"
    return 'Не указан'

def get_date(date_str):
    if not date_str:
        return 'Не указана'
    try:
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z')
        return date_obj.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return 'Не указана'

def correct_text(text, max_length=500):
    return text if len(text) <= max_length else text[:max_length - 3] + '...'