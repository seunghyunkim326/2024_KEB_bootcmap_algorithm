def combination(n, r) -> int :
    '''
    조합함수
    :param n:
    :param r:
    :return:
    '''
    numerator = factorial(n)
    denominator = factorial(n-r)*factorial(r)
    return int(numerator/denominator)

# def factorial(number) -> int :
#     '''
#     factorial by repetition
#     :param number: number (int)
#     :return: result of factorial (int)
#     '''
#     result = 1
#     for i in range(1, number+1):
#         result = result * i

def factorial(number) -> int :
    '''
    factorial by recursion
    :param number: number(int)
    :return: factorial result (int)
    '''
    if number == 1:
        return 1
    else :
        return number * factorial(number-1)
