# list(리스트) - array / 딕셔너리_해시 

stores = ['새마을식당','리춘식당','스타벅스']

print(stores)
print(stores[1])

#random 모듈 및 sample 함수 사용

import random

random.sample(stores, 1) # 값을 저장해야 쓸 수 있다
pick = random.sample(stores, 1) 
print(pick)

