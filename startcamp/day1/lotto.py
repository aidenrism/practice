import random


# 1.  1~45 까지의 수
numbers = range(1,46)

pick = random.sample(numbers,6) #샘플의 특징은 리턴이 리스트 
print(pick)

# string-interpolation (보간법) _삽입 비슷한것
print('오늘의 로또 번호는 {0} 입니다.'.format(pick)) #포멧 
print(f'오늘의 로또 번호는 {pick}입니다!') # f스트링

