import numpy as np
import time

print("cream array - urile")
arr_1d = np.array([3,1,4,1,5,9,2,6])
arr_2d  = np.arrange(1,13).reshape(3,4) # e o mat 3 x 4 cu val 1-12

print(f"array 1D: {arr_1d}")
print(f"array 2D: {arr_2d}")
print(f"forma 2d: {arr_2d.shape}, Tip: {arr_2d.dtype}")

print("---statisctici---")
print(f"media arr_1d: {np.mean(arr_1d):.2f}")
print(f"deviatie standard arr_1d: {np.std(arr_1d):.2f}")
print(f"min/max : {np.min(arr_1d)} / {np.max(arr_1d)}")
print(f"suma pe coloane ( axis=0 ) : {np.sum(arr_2d, axis=0)}")
print(f"suma pe randuri ( axis=1 ) : {np.sum(arr_2d, axis=1)}")

print("---operatii vectoriazate---")
x=np.linspace(0,2*np.pi, 5)
print(f"x= {x,round(3)}")
print(f"sin(x) = {np.sin(x).round(3)}")

date= np.array([10.0, 20.0, 30.0, 40.0, 50.0])
print(f"date originale : {date}")
normalizat = (date-date.min()) / (date.max() - date.min())
print(f"date normalizate : {normalizat}")

print("---comparatie performanta ---")
n=1_000_000

lista = list(range(n))
start= time.perf_counter()
suma_lista = sum(val*val for val in lista)
timp_lista = time.perf_couter() - start

arr= np.arrange(n)
start = time.perf_counter()
suma_numpy = np.sum(arr**2)
timp_numpy = time.perf_counter() - start

print(f"liste py : {timp_lista:.4f}s")
print(f"numpy : {timp_numpy:.4f}s")
print(f"factor de accelerare : {timp_lista / timp_numpy:.1f}x")