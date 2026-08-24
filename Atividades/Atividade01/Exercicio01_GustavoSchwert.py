import random
import sys
import time
import math

# Python tem limite padrao de ~1000 chamadas recursivas empilhadas. Com 10.000
# elementos, o Merge Sort nao chega perto disso (profundidade ~log2(10000) = 14),
# mas o Quick Sort no pior caso poderia passar de 10.000 chamadas. Aumentamos o
# limite como rede de seguranca (o pivo aleatorio ja evita bater nesse pior caso
# na pratica, mas e bom nao depender só disso).
sys.setrecursionlimit(20000)

numbers = []


def generate_new_array():
    global numbers
    size = 10000
    numbers = [random.randint(0, 15000) for _ in range(size)]


def print_array(title):
    print(title)
    print(", ".join(str(n) for n in numbers))


# ---------- MERGE SORT (ordena o array inteiro) ----------

def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


# ---------- QUICK SORT (ordena o array inteiro, ou lista de primos) ----------

def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot_index = partition(arr, low, high)
    quick_sort(arr, low, pivot_index - 1)
    quick_sort(arr, pivot_index + 1, high)


def partition(arr, low, high):
    # Pivo aleatorio: evita o pior caso O(n^2) quando o array ja esta
    # ordenado ou quase ordenado.
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ---------- BENCHMARK ----------

def is_sorted(arr):
    return all(arr[i - 1] <= arr[i] for i in range(1, len(arr)))


def run_benchmark():
    for_merge = numbers.copy()
    for_quick = numbers.copy()

    start = time.perf_counter()
    merge_sort(for_merge, 0, len(for_merge) - 1)
    merge_seconds = time.perf_counter() - start

    start = time.perf_counter()
    quick_sort(for_quick, 0, len(for_quick) - 1)
    quick_seconds = time.perf_counter() - start

    merge_ok = is_sorted(for_merge)
    quick_ok = is_sorted(for_quick)
    same_result = for_merge == for_quick

    print("\n--- Resultado do benchmark ---")
    print(f"Tamanho do array: {len(numbers)} elementos")
    print(f"Merge Sort: {merge_seconds * 1000:.3f} ms | ordenado corretamente: {merge_ok}")
    print(f"Quick Sort: {quick_seconds * 1000:.3f} ms | ordenado corretamente: {quick_ok}")
    print(f"Os dois resultados sao identicos: {same_result}")


# ---------- PRIMOS ----------

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def binary_search(sorted_list, target):
    lo, hi = 0, len(sorted_list) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def print_primes():
    # 1) Pega os valores distintos que aparecem no array.
    distinct_values = list(set(numbers))

    # 2) Filtra quais desses distintos sao primos
    prime_candidates = [v for v in distinct_values if is_prime(v)]

    # 3) Ordena a lista de primos com Quick Sort
    quick_sort(prime_candidates, 0, len(prime_candidates) - 1)

    # 4) Para cada numero do array, busca binaria na lista de primos
    print("Numeros primos no array:")
    prime_count = 0
    for n in numbers:
        if binary_search(prime_candidates, n) >= 0:
            print(f"{n} e primo.")
            prime_count += 1
    print(f"Total de numeros primos encontrados: {prime_count}")


# ---------- MENU ----------

def main():
    generate_new_array()
    while True:
        print("\nMenu:")
        print("1 - Ordenar o array (Merge Sort)")
        print("2 - Verificar e mostrar numeros primos")
        print("3 - Apagar e gerar outro array")
        print("4 - Comparar desempenho (Merge Sort x Quick Sort)")
        print("0 - Sair")
        key = input("Escolha uma opcao: ").strip()

        if key == "0":
            break
        elif key == "1":
            merge_sort(numbers, 0, len(numbers) - 1)
            print_array("Array ordenado:")
        elif key == "2":
            print_primes()
        elif key == "3":
            generate_new_array()
            print_array("Novo array gerado:")
        elif key == "4":
            run_benchmark()
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()