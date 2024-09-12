import random

vetor1 = [random.randint(1, 100) for _ in range(10)]

vetor2 = [random.randint(1, 100) for _ in range(10)]

vetor3 = [None] * (len(vetor1) + len(vetor2))
vetor3[::2] = vetor1
vetor3[1::2] = vetor2

print("Vetor 1:", vetor1)
print("Vetor 2:", vetor2)
print("Vetor 3:", vetor3)
