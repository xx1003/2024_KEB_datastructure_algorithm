import time
# def factorial(number) -> int :
#     """
#     factorial by repetition
#     :param number: number(int)
#     :return: factorial result(int)
#     """
#     result = 1
#     for i in range(1, number+1):
#         result = result * i
#     return result

def factorial(number) -> int:
    """
    factorial by repetition
    :param number: number(int)
    :return: factorial result(int)
    """
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def nCr(n, r) -> int :
    """
    조합 함수
    :param n: int
    :param r: int
    :return: int
    """
    start = time.time()
    numerator = factorial(n)
    denominator = factorial(n-r) * factorial(r)
    end = time.time()
    print(f"소요시간 : {end - start}")
    return int(numerator / denominator)