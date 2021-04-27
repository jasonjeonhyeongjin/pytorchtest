from __future__ import print_function
import torch

#초기화되어 있지 않은 3*5 행렬 생성 값은 쓰레기값
print("#초기화되어 있지 않은 3*5 행렬 생성 값은 쓰레기값")
x = torch.empty(5, 3)
print(x)
print("")
#난수로 초기화된 3*5 행렬 생성
print("#난수로 초기화된 3*5 행렬 생성")
x = torch.rand(5, 3)
print(x)
print("")

#long 타임과 0로 초기화된 3*5 행렬 생성
print("#long 타임과 0로 초기화된 3*5 행렬 생성")
x = torch.zeros(5, 3, dtype=torch.long)
print(x)
print("")

#직접 3*5텐서를 작성
print("#직접 3*5텐서를 작성")
x = torch.tensor([[5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000], [5.5000, 3.0000, 4.0000]])
print(x)
print("")


# 더블 타입의 3*5 행렬을 작성
print("# 더블 타입의 3*5 행렬을 작성")
x = x.new_ones(5, 3, dtype=torch.float64)      # new_* methods take in sizes
print(x)
print("")

print("")
# 위의 더블타입 3*5 행렬 x를 float타입으로 덮어 쓰고 값은 랜덤으로 
x = torch.randn_like(x, dtype=torch.float)    # override dtype!
print(x)
print("")

print("#텐서의 사이즈를 확인 결과 값은 튜플 torch.Size([5, 3])")
#텐서의 사이즈를 확인 결과 값은 튜플 torch.Size([5, 3])
print(x.size())
print("")

#텐서의 조작
#난수로 3*5 행렬 y를 생성
print("#난수로 3*5 행렬 y를 생성")
y = torch.rand(5, 3)
print("x tensor", x)
print("y tensor", y)
print("x+y tensor", x + y)


if torch.cuda.is_available():
    print("cude")
else:
    print("no cude")
print("")

print("# 원소의 개수가 하나인 텐서로 부터 텐서 안의 값을 추출 ")
# 원소의 개수가 하나인 텐서로 부터 텐서 안의 값을 추출 
x = torch.randn(1)
print(x)
print(x.item())
print("")

print("#pytorch에서는 토치 텐서(torch tensor)에서 넘피 배열(numpy array)로 변환 또는 그반대가 가능하다.")
#numpy와의 접속
#pytorch에서는 토치 텐서(torch tensor)에서 넘피 배열(numpy array)로 변환 또는 그반대가 가능하다.
a = torch.ones(5)
print("create tensor", a)

b = a.numpy()
print("convert tensor to numpy", b)
print("")

print("#tensor and numpy sharing memory")
#tensor and numpy sharing memory
a.add_(1)
print("tensor", a)
print("numpy", b)
print("")


print("#from numpy to tensor")
#from numpy to tensor
import numpy as np
# numpy array of 5 elements
a = np.ones(5)
print("numpy1", a)
# convert numpy to tenser
b = torch.from_numpy(a)
# add 1 to each element of numpy
np.add(a, 1, out=a)
print("numpy", a)
print("tensor", b)

("tensor", b)