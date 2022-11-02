"""Check date for truth."""


fordel = 400


def date(thedate):
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
        day, month, year = map(int, list(thedate.split('.')))
    except ValueError:
        return False
    # Проверка месяца
    if day <= 0 or month <= 0 or year < 0:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % fordel == 0 and year % 100 == 0 or year % 4 == 0 and year % 100 != 0: # Проверка высокосного года
            months[1] = 29 # Замена дня в высокосный день
        if day <= months[month - 1]: #Список с количеством дней, под индексом(номером месяца -1)
            if month <= 12: 
                return True
    return False
