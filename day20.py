# 함수 선언 부분 ## 
def print_poly(f_x) -> str:
    term = len(f_x) - 1  # 최고차항 숫자 = 배열길이-1
    poly_expression = "f(x) = "

    for i in range(len(f_x)):
        coefficient = f_x[i]  # 계수

        if coefficient >= 0:
            poly_expression += "+"
        poly_expression = poly_expression + f"{coefficient}x^{term}"
        term -= 1

    return poly_expression


def calculation_poly(x_value, f_x):
    return_value = 0
    term = len(f_x) - 1

    for i in range(len(f_x)):
        coefficient = f_x[i]  # 계수
        return_value += coefficient * pow(x_value, term)
        term -= 1

    return return_value


## 전역 변수 선언 부분 ## 
fx = [2, 3, 4, 0, -9]  # = 7x^3 -4x^2 +0x^1 +5x^0

## 메인 코드 부분 ## 
if __name__ == "__main__":
    print(print_poly(fx))
    print(calculation_poly(int(input("X 값 : ")), fx))

