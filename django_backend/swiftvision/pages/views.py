from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, "main_page.html")

def statisctic(request):
    salary_dynamics_all = SalaryDynamycsAll.objects.all()
    vacancy_dynamics_all = VacancyDynamycsAll.objects.all()
    city_salary_dynamics_all = CitySalaryDynamicsAll.objects.all()
    city_vacancy_share_all = CitySalaryShareAll.objects.all()
    top_skills_all_2015 = TopSkillsAll2015.objects.all()
    top_skills_all_2016 = TopSkillsAll2016.objects.all()
    top_skills_all_2017 = TopSkillsAll2017.objects.all()
    top_skills_all_2018 = TopSkillsAll2018.objects.all()
    top_skills_all_2019 = TopSkillsAll2019.objects.all()
    top_skills_all_2020 = TopSkillsAll2020.objects.all()
    top_skills_all_2021 = TopSkillsAll2021.objects.all()
    top_skills_all_2022 = TopSkillsAll2022.objects.all()
    top_skills_all_2023 = TopSkillsAll2023.objects.all()
    top_skills_all_2024 = TopSkillsAll2024.objects.all()

    salary_dynamics_table_all = SalaryDynamycsAll_Table.objects.all()
    city_salary_dynamics_table = CitySalaryDynamycs_Table.objects.all()
    city_salary_share_table = CitySalaryShare_Table.objects.all()

    skills_table_2015 = Skills_Table_2015.objects.all()
    skills_table_2016 = Skills_Table_2016.objects.all()
    skills_table_2017 = Skills_Table_2017.objects.all()
    skills_table_2018 = Skills_Table_2018.objects.all()
    skills_table_2019 = Skills_Table_2019.objects.all()
    skills_table_2020 = Skills_Table_2020.objects.all()
    skills_table_2021 = Skills_Table_2021.objects.all()
    skills_table_2022 = Skills_Table_2022.objects.all()
    skills_table_2023 = Skills_Table_2023.objects.all()
    skills_table_2024 = Skills_Table_2024.objects.all()

    return render(request, "statistic.html", 
                  {'salary_dynamics_all': salary_dynamics_all, 
                  'vacancy_dynamics_all': vacancy_dynamics_all,
                  'city_salary_dynamics_all': city_salary_dynamics_all,
                  'city_vacancy_share_all': city_vacancy_share_all,
                  'top_skills_all_2015': top_skills_all_2015,
                  'top_skills_all_2016': top_skills_all_2016,
                  'top_skills_all_2017': top_skills_all_2017,
                  'top_skills_all_2018': top_skills_all_2018,
                  'top_skills_all_2019': top_skills_all_2019,
                  'top_skills_all_2020': top_skills_all_2020,
                  'top_skills_all_2021': top_skills_all_2021,
                  'top_skills_all_2022': top_skills_all_2022,
                  'top_skills_all_2023': top_skills_all_2023,
                  'top_skills_all_2024': top_skills_all_2024,
                  'salary_dynamics_table_all': salary_dynamics_table_all,
                  'city_salary_dynamics_table': city_salary_dynamics_table,
                  'city_salary_share_table': city_salary_share_table,
                  'skills_table_2015': skills_table_2015,
                  'skills_table_2016': skills_table_2016,
                  'skills_table_2017': skills_table_2017,
                  'skills_table_2018': skills_table_2018,
                  'skills_table_2019': skills_table_2019,
                  'skills_table_2020': skills_table_2020,
                  'skills_table_2021': skills_table_2021,
                  'skills_table_2022': skills_table_2022,
                  'skills_table_2023': skills_table_2023,
                  'skills_table_2024': skills_table_2024}
                  )


def geography(request):
    city_salary_dynamics_prof = CitySalaryDynamicsProf.objects.all()
    city_vacancy_share_prof = CitySalaryShareProf.objects.all()
    city_salary_dynamics_table = CitySalaryDynamycs_Table.objects.all()
    city_salary_share_table = CitySalaryShare_Table.objects.all()

    return render(request, "geography.html", 
                  {'city_salary_dynamics_prof': city_salary_dynamics_prof,
                  'city_vacancy_share_prof': city_vacancy_share_prof,
                  'city_salary_dynamics_table': city_salary_dynamics_table,
                  'city_salary_share_table': city_salary_share_table})

def demand(request):
    salary_dynamics_prof = SalaryDynamycsProf.objects.all()
    vacancy_dynamics_prof = VacancyDynamycsProf.objects.all()
    salary_dynamics_table_prof = SalaryDynamycsProf_Table.objects.all()

    return render(request, "demand.html", 
                  {'salary_dynamics_prof': salary_dynamics_prof, 
                  'vacancy_dynamics_prof': vacancy_dynamics_prof,
                  'salary_dynamics_table_prof': salary_dynamics_table_prof}
                  )

def skills(request):
    top_skills_2015 = TopSkills2015.objects.all()
    top_skills_2016 = TopSkills2016.objects.all()
    top_skills_2017 = TopSkills2017.objects.all()
    top_skills_2018 = TopSkills2018.objects.all()
    top_skills_2019 = TopSkills2019.objects.all()
    top_skills_2020 = TopSkills2020.objects.all()
    top_skills_2021 = TopSkills2021.objects.all()
    top_skills_2022 = TopSkills2022.objects.all()
    top_skills_2023 = TopSkills2023.objects.all()
    top_skills_2024 = TopSkills2024.objects.all()

    skills_table_2015 = Skills_Table_2015.objects.all()
    skills_table_2016 = Skills_Table_2016.objects.all()
    skills_table_2017 = Skills_Table_2017.objects.all()
    skills_table_2018 = Skills_Table_2018.objects.all()
    skills_table_2019 = Skills_Table_2019.objects.all()
    skills_table_2020 = Skills_Table_2020.objects.all()
    skills_table_2021 = Skills_Table_2021.objects.all()
    skills_table_2022 = Skills_Table_2022.objects.all()
    skills_table_2023 = Skills_Table_2023.objects.all()
    skills_table_2024 = Skills_Table_2024.objects.all()

    return render(request, "skills.html", 
                  {'top_skills_2015': top_skills_2015,
                  'top_skills_2016': top_skills_2016,
                  'top_skills_2017': top_skills_2017,
                  'top_skills_2018': top_skills_2018,
                  'top_skills_2019': top_skills_2019,
                  'top_skills_2020': top_skills_2020,
                  'top_skills_2021': top_skills_2021,
                  'top_skills_2022': top_skills_2022,
                  'top_skills_2023': top_skills_2023,
                  'top_skills_2024': top_skills_2024,
                  'skills_table_2015': skills_table_2015,
                  'skills_table_2016': skills_table_2016,
                  'skills_table_2017': skills_table_2017,
                  'skills_table_2018': skills_table_2018,
                  'skills_table_2019': skills_table_2019,
                  'skills_table_2020': skills_table_2020,
                  'skills_table_2021': skills_table_2021,
                  'skills_table_2022': skills_table_2022,
                  'skills_table_2023': skills_table_2023,
                  'skills_table_2024': skills_table_2024})

def vacancies(request):
    return render(request, "vacancies.html")