import numpy as np
import matplotlib.pyplot as plt


K = int(input("Введите число K "))
N = int(input("Введите четное число N > 1 "))
while N % 2 != 0 or N == 1:
    N = int(input("Введите четное число N > 1 "))

A = np.random.randint(-10, 10 + 1, N * N).reshape(N, N)
print(f'\nA = \n{A}\n')

F = A.copy()
print(f'\nF = \n{F}\n')

center = int(N / 2)
E = A[:center, :center]
B = A[:center, center:]
D = A[center:, :center]
C = A[center:, center:]

print(f'\nE = \n{E}\n')
print(f'\nB = \n{B}\n')
print(f'\nD = \n{D}\n')
print(f'\nC = \n{C}\n')

maxValueE = np.amax(E[:, :: 2])

sumE = np.sum(E[::2, :])

# print(maxValueE)
# print (sumE)
if maxValueE > sumE :
    print("Макс. число в нечетных столбцах в матрице Е больше,чем сумма чисел в нечетных строках")
    for i in range(center, len(F)):
        F[:, i] = np.vstack((C, B))[:, i - center]
else:
    print("Макс. число в нечетных столбцах в матрице Е меньше,чем сумма чисел в нечетных строках")
    for j in range(center):
        F[j] = np.hstack((B[j][::-1], E[j][::-1]))

print("Матрица F после изменения")
print(f'\nF = \n{F}\n')

det_A = np.linalg.det(A)
print(f'Определитель матрицы А: = {det_A}')

diagonals_A = np.sum(np.diagonal(F)) + sum(np.diagonal(np.flip(F, axis=1)))
print(f'Сумма диагоналей матрицы F: = {diagonals_A}')

if det_A > diagonals_A:
    print("Определитель матрицы А больше суммы диагоналей матрицы F")
    result = np.linalg.inv(A) * np.transpose(A) - K * np.linalg.inv(F)
else:
    print("Определитель матрицы А меньше суммы диагоналей матрицы F")
    result = (np.transpose(A) + np.tril(A) - np.transpose(F)) * K

print(f'Результат = {result}')


fig = plt.figure(figsize=(8, 8))
fig.suptitle('Demonstration Matplotlib', fontsize = 30)

fig1 = fig.add_subplot(411)
fig1.plot(F)
fig1.set_title("Demonstration plot", fontsize = 14)

fig2 = fig.add_subplot(423)
fig2.imshow(F, cmap='plasma', aspect='equal', interpolation='gaussian', origin="lower")
fig2.set_title("Demonstration imshow", fontsize = 14)

fig3 = fig.add_subplot(424)
fig3.pcolormesh(F, cmap='plasma', edgecolors="k", shading='flat')
fig3.set_title("Demonstration pcolormesh", fontsize = 14)

fig4 = fig.add_subplot(413)
fig4.scatter(F[::, :center], F[::, center:])
fig4.set_title("Demonstration scatter", fontsize = 14)

plt.show()