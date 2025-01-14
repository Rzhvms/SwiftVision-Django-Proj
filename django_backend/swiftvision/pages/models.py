from django.db import models

# Динамика уровня зарплат по годам

class SalaryDynamycsAll(models.Model):
    image = models.ImageField(upload_to='static/images/')

class SalaryDynamycsProf(models.Model):
    image = models.ImageField(upload_to='static/images/')

# Динамика количества вакансий по годам

class VacancyDynamycsAll(models.Model):
    image = models.ImageField(upload_to='static/images/')

class VacancyDynamycsProf(models.Model):
    image = models.ImageField(upload_to='static/images/')

# Уровень зарплат по городам

class CitySalaryDynamicsAll(models.Model):
    image = models.ImageField(upload_to='static/images/')

class CitySalaryDynamicsProf(models.Model):
    image = models.ImageField(upload_to='static/images/')

# Доля вакансий по городам

class CitySalaryShareAll(models.Model):
    image = models.ImageField(upload_to='static/images/')

class CitySalaryShareProf(models.Model):
    image = models.ImageField(upload_to='static/images/')

# Топ скиллы для всех

class TopSkillsAll2015(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2016(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2017(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2018(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2019(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2020(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2021(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2022(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2023(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkillsAll2024(models.Model):
    image = models.ImageField(upload_to='static/images/')

# Топ скиллы для профессии

class TopSkills2015(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2016(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2017(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2018(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2019(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2020(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2021(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2022(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2023(models.Model):
    image = models.ImageField(upload_to='static/images/')

class TopSkills2024(models.Model):
    image = models.ImageField(upload_to='static/images/')


class SalaryDynamycsAll_Table(models.Model):
    year = models.IntegerField(unique=True, verbose_name="Год")
    avg_salary = models.IntegerField(verbose_name="Средняя зарплата")
    vacancy_count = models.IntegerField(verbose_name="Количество вакансий")
    
class SalaryDynamycsProf_Table(models.Model):
    year = models.IntegerField(unique=True, verbose_name="Год")
    avg_salary = models.IntegerField(verbose_name="Средняя зарплата")
    vacancy_count = models.IntegerField(verbose_name="Количество вакансий")

class CitySalaryDynamycs_Table(models.Model):
    city_all = models.CharField(max_length=50, verbose_name="Города (ВСЕ)")
    salary_all = models.IntegerField(verbose_name="Средняя зарплата (ВСЕ)")
    city_prof = models.CharField(max_length=50, verbose_name="Города (iOS)")
    salary_prof = models.IntegerField(verbose_name="Средняя зарплата (iOS)")

class CitySalaryShare_Table(models.Model):
    city_all = models.CharField(max_length=50, verbose_name="Города (ВСЕ)")
    share_all = models.FloatField(verbose_name="Доля вакансий (ВСЕ)")
    city_prof = models.CharField(max_length=50, verbose_name="Города (iOS)")
    share_prof = models.FloatField(verbose_name="Доля вакансий (iOS)")

class Skills_Table_2015(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2016(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2017(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2018(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2019(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2020(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2021(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2022(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2023(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")

class Skills_Table_2024(models.Model):
    number = models.IntegerField(verbose_name="Топ")
    skills_all = models.CharField(max_length=50, verbose_name="Навыки (ВСЕ)")
    freq_all = models.IntegerField(verbose_name="Частотность (ВСЕ)")
    skills_prof = models.CharField(max_length=50, verbose_name="Навыки (iOS)")
    freq_prof = models.IntegerField(verbose_name="Частотность (iOS)")