#05_함수.ipynb TODO

# 1. 시작 정수, 끝 정수를 받아 그 사이의 모든 정수의 합을 구해서 반환하는 함수를 구현(ex: 1, 20 => 1에서 20 사이의 모든 정수의 합계)
def summation(start:int=0, end:int=10) -> int:
    ''' 
    Start 정수 ~ End 정수 까지의 합을 계산하는 함수
    Args:
        start(int): 계산 범위의 시작 정수 default: 0
        end(int): 계산 범위의 끝 정수 default: 10
    Returns
        int: start~end 까지의 모든 정수들의 합계
    '''
    result = 0
    for v in range(start, end+1):
        result += v
    return result
print(summation(1,10))
print(summation(end=20))
print(summation(5))
# 2. 2번 문제에서 시작을 받지 않은 경우 0을, 끝 정수를 받지 않으면 10이 들어가도록 구현을 변경

# 3. 구구단을 출력하는 함수를 구현한다. 입력으로 출력하고 싶은 단을 parameter로 입력받아서 `N * 1` ~ `N * 9` 를 출력한다. (N: 입력받은 단)
def print_gugudan(dan:int):
    print(f'{dan} 단을 출력합니다.')
    for v in range(1, 10):
        print(f'{dan} * {v} = {dan * v}')
print_gugudan(3)
print('='*30)
print_gugudan(7)

# 4. 체질량 지수는 비만도를 나타내는 지수로 키가 a미터 이고 몸무게가 b kg일때 b/(a**2) 로 구한다.
# 체질량 지수가
# - 18.5 미만이면 저체중
# - 18.5이상 25미만이면 정상
# - 25이상이면 과체중
# - 30이상이면 비만으로 하는데
# 몸무게와 키를 매개변수로 받아 비만인지 과체중인지 반환하는 함수를 구현하시오.
def check_weight(tall:float, weight:float) -> tuple[float, str]:
    ''' 
    BMI 지술ㄹ 계산해서 체중상태를 알려주는 함수
    Args:
        tall(float):키 단위:미터
        weight(float): 몸무게, 단위:kg
    Returns
        tuple: BMI 지수와 체중상태를 튜플로 묶어서 반환
    '''
    bmi = weight / tall**2
    result = None
    if bmi < 18.5:
        result = '저체중'
    elif bmi < 25:
        result = '정상체중'
    elif bmi < 30:
        result = '과체중'
    else:
        result = '비만'
    return bmi, result
print(check_weight(1.6, 60))

def plus(num)


    
