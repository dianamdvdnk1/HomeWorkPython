"""Find percent of letters in string."""

def function_of_percent(stroka: str):
# Берем подстроку из строки
    for slovo in napishi.split(" "): 
        bolshoi_bukva = 0
        malii_bukva = 0 # Объявляем меременные подсчета
        for bukva in slovo: # Смотрим на букву
            if bukva.isupper(): # Проверяем букву
                bolshoi_bukva += 1
            elif bukva.islower():
                malii_bukva += 1

print(round(sum() * 100 / len(), 2))
            