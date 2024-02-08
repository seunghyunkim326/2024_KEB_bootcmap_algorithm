def factorial(number) -> int :
    pass



def combination(n, r) -> int :
    '''
    조합함수
    :param n:
    :param r:
    :return:
    '''
    numerator = factorial(n)
    denominator = factorial(n-r)*factorial(r)
    return numerator/denominator

if __name__ == "__main__" :
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f'{n}C{r} = {combination(n,r)}')