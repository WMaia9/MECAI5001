import math

X, N = map(float, input().split())
N = int(N)
S = X
sinal = -1

for i in range(2, 2*N, 2):
    print(i)
    termo = sinal * (X**i) / math.factorial(i+1)
    print(termo)
    S += termo
    sinal *= -1

print(f"{S:.6f}")
