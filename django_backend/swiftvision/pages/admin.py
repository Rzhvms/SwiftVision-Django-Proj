from django.contrib import admin
from .models import *

# Регистрация моделей

# Динамика уровня зарплат по годам

@admin.register(SalaryDynamycsAll)
class SalaryDynamycsAll(admin.ModelAdmin):
    img_display = ('image')  

@admin.register(SalaryDynamycsProf)
class SalaryDynamycsProf(admin.ModelAdmin):
    img_display = ('image') 

# Динамика количества вакансий по годам
 
@admin.register(VacancyDynamycsAll)
class VacancyDynamycsAll(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(VacancyDynamycsProf)
class VacancyDynamycsProf(admin.ModelAdmin):
    img_display = ('image') 

# Уровень зарплат по городам

@admin.register(CitySalaryDynamicsAll)
class CitySalaryDynamicsAll(admin.ModelAdmin):
    img_display = ('image')  

@admin.register(CitySalaryDynamicsProf)
class CitySalaryDynamicsProf(admin.ModelAdmin):
    img_display = ('image')

# Доля вакансий по городам

@admin.register(CitySalaryShareAll)
class CitySalaryShareAll(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(CitySalaryShareProf)
class CitySalaryShareProf(admin.ModelAdmin):
    img_display = ('image')  

#Топ скиллы для всех

@admin.register(TopSkillsAll2015)
class TopSkillsAll2015(admin.ModelAdmin):
    img_display = ('image')  

@admin.register(TopSkillsAll2016)
class TopSkillsAll2016(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2017)
class TopSkillsAll2017(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2018)
class TopSkillsAll2018(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2019)
class TopSkillsAll2019(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2020)
class TopSkillsAll2020(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2021)
class TopSkillsAll2021(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2022)
class TopSkillsAll2022(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2023)
class TopSkillsAll2023(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkillsAll2024)
class TopSkillsAll2024(admin.ModelAdmin):
    img_display = ('image') 

#Топ скиллы для профессии

@admin.register(TopSkills2015)
class TopSkills2015(admin.ModelAdmin):
    img_display = ('image')  

@admin.register(TopSkills2016)
class TopSkills2016(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2017)
class TopSkills2017(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2018)
class TopSkills2018(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2019)
class TopSkills2019(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2020)
class TopSkills2020(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2021)
class TopSkills2021(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2022)
class TopSkills2022(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2023)
class TopSkills2023(admin.ModelAdmin):
    img_display = ('image') 

@admin.register(TopSkills2024)
class TopSkills2024(admin.ModelAdmin):
    img_display = ('image') 

#таблицы

@admin.register(SalaryDynamycsAll_Table)
class SalaryDynamycsAll_Table(admin.ModelAdmin):
    year_col = ('year')
    avg_sal = ('avg_salary')
    vac_count = ('vacancy_count')

@admin.register(SalaryDynamycsProf_Table)
class SalaryDynamycsProf_Table(admin.ModelAdmin):
    year_col = ('year')
    avg_sal = ('avg_salary')
    vac_count = ('vacancy_count')
    
@admin.register(CitySalaryDynamycs_Table)
class CitySalaryDynamycs_Table(admin.ModelAdmin):
    city_is_all = ('city_all')
    salary_is_all = ('salary_all')
    city_is_prof = ('city_prof')
    salary_is_prof = ('salary_prof')

@admin.register(CitySalaryShare_Table)
class CitySalaryShare_Table(admin.ModelAdmin):
    city_is_all = ('city_all')
    share_is_all = ('share_all')
    city_is_prof = ('city_prof')
    share_is_prof = ('share_prof')


@admin.register(Skills_Table_2015)
class Skills_Table_2015(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2016)
class Skills_Table_2016(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2017)
class Skills_Table_2017(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2018)
class Skills_Table_2018(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2019)
class Skills_Table_2019(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2020)
class Skills_Table_2020(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2021)
class Skills_Table_2021(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2022)
class Skills_Table_2022(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2023)
class Skills_Table_2023(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')

@admin.register(Skills_Table_2024)
class Skills_Table_2024(admin.ModelAdmin):
    top_num = ('num')
    skills_is_all = ('skills_all')
    freq_is_all = ('freq_all')
    skills_is_prof = ('skills_prof')
    freq_is_prof = ('freq_prof')