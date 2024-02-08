# self 문제 3-2 계수가 0인 항과 첫 번째 항의 +부호 출력X

def print_poly(f_x) -> str:
    '''

    :param f_x:
    :return:
    '''
    term = len(f_x) - 1
    poly_expression = "f(x) = "

    for i in range(len(fx)):
        coefficient = f_x[i]

        if coefficient >= 0:
            poly_expression = poly_expression + "+"
        poly_expression = poly_expression + f'{coefficient}x^{term} '
        term = term - 1

    return poly_expression


def calculation_poly(x_value, f_x) -> int:
    '''

    :param x_value:
    :param f_x:
    :return:
    '''
    return_value = 0
    term = len(f_x) - 1

    for i in range(len(fx)):
        coefficient = f_x[i]
        return_value += coefficient * pow(x_value, term)
        term = term - 1

    return return_value


fx = [2, 3, 4, 0, -9]

if __name__ == "__main__":
    print(print_poly(fx))
    print(calculation_poly(int(input("x 값 : ")), fx))