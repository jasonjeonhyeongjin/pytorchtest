from __future__ import print_function
import torch

#초기화되어 있지 않은 3*5 행렬 생성 값은 쓰레기값
x = torch.empty(5, 3)
print(x)

#난수로 초기화된 3*5 행렬 생성
x = torch.rand(5, 3)
print(x)

#long 타임과 0로 초기화된 3*5 행렬 생성
x = torch.zeros(5, 3, dtype=torch.long)
print(x)

#직접 3*5텐서를 작성
x = torch.tensor([[5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000]])
print(x)

# 더블 타입의 3*5 행렬을 작성
x = x.new_ones(5, 3, dtype=torch.float64)      # new_* methods take in sizes
print(x)

# 위의 더블타입 3*5 행렬 x를 float타입으로 덮어 쓰고 값은 랜덤으로 
x = torch.randn_like(x, dtype=torch.float)    # override dtype!
print(x)

#텐서의 사이즈를 확인 결과 값은 튜플 torch.Size([5, 3])
print(x.size())


#텐서의 조작
#난수로 3*5 행렬 y를 생성

y = torch.rand(5, 3)
print("x tensor", x)
print("y tensor", y)
print("x+y tensor", x + y)
