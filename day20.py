# 1~100 사이의 수를 맞추는 게임, 사용자가 입력하는 값 보다 큰지 작은지 알려주고 몇번만에 맞추는지 알아내는 게임
import random
random_number = random.randint(1, 100)
chance = 10
while chance != 0:
    input_number = int(input("Input guess number : "))
    if input_number == random_number:
        print(f'You win. Answer is {random_number}')
        # print(f'{10-chance}만에 맞췄습니다.')
        break
    elif input_number > random_number:
        print(f'{input_number} is bigger. Chance left : {chance}')
        # print(f'{chance}번의 기회가 남았습니다.')
        chance -= 1
    else :
        print(f'{input_number} is lower. Chance left : {chance}')
        # print(f'{chance}번의 기회가 남았습니다.')
        chance -= 1
# if chance == 0:
#     print("You lose!!")
else :
    print(f"You lost!! Answer is {random_number}")