# Análisis de Ejemplos:
# Implementación de Búsqueda Lineal:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Implementación de Búsqueda Binaria:
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Prueba y Evaluación:
# Prueba de búsqueda lineal
arr = [1, 2, 3, 4, 5]
target = 3
print(linear_search(arr, target))  # Output: 2

# Prueba de búsqueda binaria
arr_sorted = [1, 2, 3, 4, 5]
target = 3
print(binary_search(arr_sorted, target))  # Output: 2

# Comparación de Eficiencia:
# Para medir el tiempo de ejecución de un script en Python, puedes usar el módulo time y la función time() para registrar el tiempo antes y después de la ejecución del algoritmo. Luego, resta los tiempos para obtener la duración.

import time

# Medición del tiempo de ejecución de la búsqueda lineal
start_time = time.time()
linear_search(arr, target)
end_time = time.time()
print("Tiempo de ejecución de búsqueda lineal:", end_time - start_time)

# Medición del tiempo de ejecución de la búsqueda binaria
start_time = time.time()
binary_search(arr_sorted, target)
end_time = time.time()
print("Tiempo de ejecución de búsqueda binaria:", end_time - start_time)
