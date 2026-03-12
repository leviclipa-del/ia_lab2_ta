import numpy as np

# Setăm seed pentru reproductibilitate
np.random.seed(42)

# Generarea matricelor aleatoare A (4x3) și B (3x5)
A = np.random.randint(1, 11, size=(4, 3))
B = np.random.randint(1, 11, size=(3, 5))

print("Matricea A:")
print(A)
print("\nMatricea B:")
print(B)

# Calculul produsului matriceal
C = A @ B
print("\nProdusul matriceal C = A @ B:")
print(C)

# Analiza matricei C
suma_totala = np.sum(C)
media_pe_coloane = np.mean(C, axis=0)
valoare_maxima = np.max(C)

print(f"\nSuma tuturor elementelor din C: {suma_totala}")
print(f"Media pe fiecare coloană: {media_pe_coloane}")
print(f"Valoarea maximă globală: {valoare_maxima}")

# Bonus: Generarea matricei pătratice M (3x3)
M = np.random.randint(1, 11, size=(3, 3))
print("\nMatricea pătratică M:")
print(M)

M_inversa = np.linalg.inv(M)
determinant = np.linalg.det(M)

print("\nInversa matricei M:")
print(M_inversa)
print(f"\nDeterminantul matricei M: {determinant}")

# Verificarea produsului cu inversa
identitate_aproape = np.allclose(M @ M_inversa, np.eye(3))
print(f"\nM @ inv(M) este aproape de matricea identitate? {identitate_aproape}")