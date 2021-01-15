# 연산자

# 산술연산자
print(3+5)
print(3 + 5)
print(3 - 5)
print(3 * 5)
print(100 / 3)
print(100 // 3)
print(100 % 3) 
print(3 ** 3)

# 비교 연산자
print(5 == 5)
print(5 >= 5)
print(5 != 5)

# 조건문

# 1. 주어진 양수 n이 홀수, 짝수인지 판별하여 출력하는 코드
n = 10
if n % 2 == 1:
    print('홀수')
else:
    print('짝수')

# 반복문
odds = ''
for i in range(1,10):
    odd = i
    if odd % 2 == 1:
        odds += str(odd) + ','
print('{0}는 홀수입니다.'.format(odds[:-1]))

# for number in numbers:
#     if number % 2 ==1:
#         print(f'{number}는 홀수입니다.')

# odd = 
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number % 2 ==1:
        print(f'{number}는 홀수입니다.', end='')


# sss = []
# 통과한 홀수들을 리스트에 쌓기 
# {리스트}는 홀수입니다.

# pip install BeautifulSoup4 requests lxml
import requests
from bs4 import BeautifulSoup

# 컨트롤 shift i / f12
# ctrl shift c 포인터로 선택
# copy 카피 셀렉터

# BeautifulSoup.select_one(#KOSPI_now)
