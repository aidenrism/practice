#파일명 옆에 > 동그라미 저장이 안되었다 ctrl+s 저장. 수시로
# 터미널 정리 : clear 입력 or ctrl+l
# # 주석처리 : Ctr + K + C

# # 주석해제 : Ctrl + K + U

# ctrl + l 현재줄선택 shift+ alt+ a 여러줄 따옴표 주석처리 

# 소스 > 터미널 ctrl + `  /    터미널 > 소스 ctrl + 1


# 1. 저장
# 1)변수 2)리스트: 리스트는 복수형으로 쓰는게 좋음 , 인덱스 넘버로 접근
# 3)딕셔너리: 키로만 접근가능
# 2. 조건(if)
# 3. 반복(while, for)

greeting = '안녕하세요'
print(greeting)
print(greeting)
print(greeting)
print(greeting)

n=0
while n >6:
    print('greeting')
    n = n+1
##
for _ in range(5):
        print('greeting')

for i in range(1,6):
    if i < 6:
        print('안녕하십니까!')

# i 를 _ 로 대체가능





