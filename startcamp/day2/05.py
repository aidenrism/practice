# 함수
# 특정 역할을 하는 코드의 집합
# 하나의 함수는 하나의 역할만 해야한다.

# 함수 정의
def mul(a,b):
    result = a + b 
    return result #반환값  이게 없으면 none을 리턴함 
    None #리턴 아래 코드는 무시됨. 리턴 이후 코드 동작 x 
    return print('a') #이것도 안됨 
print(mul(1,2))

# 함수 실행(호출)
print(mul(2,2))
a = mul(5,5)
a
print(a)
