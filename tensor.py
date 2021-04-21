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