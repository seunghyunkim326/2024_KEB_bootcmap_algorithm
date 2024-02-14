

def fibo_repetition(num: int) -> int:
    """
    fibonacci function by repetition
    :param num: integer number
    :return: integer number
    """
    a = 0
    b = 1
    for _ in range(num):
        # a = b
        # b = a + b
        a, b = b, a + b

    return a