"""
간단한 3층 신경망 구현
입력 x값 3개, 출력 y값 2개로 설정. 순방향
"""

import numpy as np

def relu1(x):
    # 이 경우, 숫자 1개가 입력되었을 때만 가능함. (어레이 입력시 코드 변경 필요)
    if x > 0:
        return x
    else:
        return 0

def relu2(x):
    # np.max()는 입력 array 내에서의 최댓값을 출력함.
    # np.maximum은 여러 array 사이에서 각 위치의 최대값을 출력함.
    return np.maximum(x, 0)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def try1():
    # y = Wx+b
    x = np.array([1, 2])
    W = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([1, 2, 3])

    y = np.dot(x, W) + b
    print(y)

if __name__ == '__main__':
    try1()