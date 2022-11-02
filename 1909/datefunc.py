"""Check date for truth."""


def date(day:int, month:int, year:int):
    """
    Function which testing existence of date.

    Args:
        thedate: str - variable which rebuild into day, month, year.

    Returns:
        bool: bool - True or False if date is existence.

    Raise:
        ValueError: An error when we could not get int value.
    """
    try:
        if 
        except Exception:
        print("Error")
    # Проверка месяца
    if day <= 0 or month <= 0 or year < 0:
        return False
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and year%100!=0 or year%400==0: # Проверка высокосного года
        months[1] = 29 # Замена дня в высокосный день
        if day <= months[month - 1]: #Список с количеством дней, под индексом(номером месяца -1)
            if month <= 12: 
                return True
            return False
            
print(date(day, month, year))
