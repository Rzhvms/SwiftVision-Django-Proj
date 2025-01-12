import requests
import xml.etree.ElementTree as ET
import pandas as pd


def convert_to_rub(salary_currency, date):
    """Конвертирует валюту в рубли с использованием API ЦБ РФ."""
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date}"
    response = requests.get(url)
    root = ET.fromstring(response.content)
    for currency in root.findall("Valute"):
        char_code = currency.find("CharCode").text
        if char_code == salary_currency:
            vunitrate = float(currency.find("Value").text.replace(",", "."))
            nominal = int(currency.find("Nominal").text)
            return vunitrate / nominal
    return 1.0 if salary_currency == "RUR" else None


def calculate_salary_in_rub(data_list):
    result = []
    for row in data_list:
        salary_from = float(row[2]) if pd.notna(row[2]) else 0
        salary_to = float(row[3]) if pd.notna(row[3]) else 0

        salary_currency = row[4]
        published_at = row[6]

        rate = 1.0
        if pd.notna(salary_currency) and pd.notna(published_at):
            if salary_currency != 'RUR':
                date = (published_at[:7]).split('-')
                correct_date = f'01/{date[1]}/{date[0]}'
                rate = convert_to_rub(salary_currency, correct_date)


        if rate is None:
            rate = 0

        salary_rub = 0
        if salary_from and salary_to:
            salary_rub = (salary_from + salary_to) / 2 * rate
        elif salary_from:
            salary_rub = salary_from * rate
        elif salary_to:
            salary_rub = salary_to * rate

        result.append(row[:7] + [salary_rub])

    return result


def process_file(file_path, output_path):
    """Обрабатывает входной CSV-файл, пересчитывает зарплаты в рубли и сохраняет новый файл."""
    df = pd.read_csv(file_path)
    data_list = df[['name', 'key_skills', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at']].values.tolist()
    processed_data = calculate_salary_in_rub(data_list)
    result_df = pd.DataFrame(processed_data, columns=['name', 'key_skills', 'salary_from', 'salary_to', 'salary_currency', 'area_name', 'published_at', 'salary_rub'])
    result_df.to_csv(output_path, index=False)


process_file("vacancies_2024.csv", "vacancies_rub.csv")