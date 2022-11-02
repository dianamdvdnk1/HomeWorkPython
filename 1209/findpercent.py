"""Find percent of letters in string."""

def function_of_percent(stroka: str):
# Берем подстроку из строки
    res = 0
    for slovo in stroka.split(" "): 
        bolshoi_bukva = 0
        malii_bukva = 0 # Объявляем меременные подсчета
        for bukva in slovo: # Смотрим на букву
            if bukva.isupper(): # Проверяем букву
                bolshoi_bukva += 1
            else:
                malii_bukva += 1
        if bolshoi_bukva > malii_bukva:
            res += 1
    return '{0}%'.format(100 // (len(stroka.split()) // res))
            
