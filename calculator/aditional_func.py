"""File for calculate."""


def calculate(arr):
    """
    Calculates given operation and creates file with this operation.

    Args:
        arr: list - list with input.

    Returns:
        int - first + snd.
        int - first * snd.
        int - first / snd.
    """
    first, sym, snd = arr[0], arr[1], arr[2]
    with open('calculator.txt', 'a') as file_1:
        try:
            first, snd = int(first), int(snd)
        except ValueError:
            print("Формат ввода: VALUE1 <+-*/> VALUE2\nПример: 1 * 2")
        if sym == '+':
            file_1.write('{0} + {1} = {2}\n'.format(first, snd, first + snd))
            return first + snd
        if sym == '-':
            file_1.write('{0} - {1} = {2}\n'.format(first, snd, first - snd))
            return first - snd
        elif sym == '*':
            file_1.write('{0} * {1} = {2}\n'.format(first, snd, first * snd))
            return first * snd
        elif sym == '/':
            if snd == 0:
                print("It's not okay")
            else:
                file_1.write('{0} / {1} = {2}\n'.format(first, snd, first / snd))
                file_1.close()
                return first / snd
