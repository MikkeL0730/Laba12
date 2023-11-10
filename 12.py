#12. (|х(2n-1)|)/(2n-1)!
import numpy as np

def calculate_series_sum(x, t):
    n = x.shape[0]  # Размерность матрицы x
    factorial = 1
    term = abs(x[0, 0])  # Первый член ряда
    series_sum = term
    i = 1

    while abs(term) >= t:
        factorial *= i  # Вычисление факториала
        term = abs(x[i % n, i % n]) / factorial  # Вычисление текущего члена ряда
        series_sum += (-1) ** i * term  # Добавление текущего члена ряда к сумме
        i += 1

    return series_sum

# Пример использования
k = 3  # Ранг матрицы x
n = 5  # Номер последнего слагаемого
t = 1e-6  # Точность вычислений

x = np.random.uniform(-1, 1, (k, k))  # Генерация случайной матрицы x
series_sum = calculate_series_sum(x, t)

print("Сумма знакопеременного ряда:", series_sum)