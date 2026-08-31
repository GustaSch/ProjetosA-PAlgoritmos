import random
import time
 
# ------------------------------------------------------------
# CONFIGURAÇÃO
# ------------------------------------------------------------
 
TAMANHOS = [1_000, 5_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
 
VALOR_MINIMO = 0
VALOR_MAXIMO = 10_500
  
 
# ------------------------------------------------------------
# ALGORITMOS DE ORDENAÇÃO
# ------------------------------------------------------------
 
def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a
 
 
def quick_sort(arr):
    a = arr[:]
 
    def particionar(lo, hi):
        pivo_idx = random.randint(lo, hi)
        a[pivo_idx], a[hi] = a[hi], a[pivo_idx]

        pivo = a[hi]
        i = lo - 1
        for j in range(lo, hi):
            if a[j] <= pivo:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[hi] = a[hi], a[i + 1]
        return i + 1
 
    def ordenar(lo, hi):
        while lo < hi:
            p = particionar(lo, hi)
            if p - lo < hi - p:
                ordenar(lo, p - 1)
                lo = p + 1
            else:
                ordenar(p + 1, hi)
                hi = p - 1
 
    if a:
        ordenar(0, len(a) - 1)
    return a
 
 
def merge_sort(arr):
    a = arr[:]
 
    def mesclar(esq, dir):
        resultado = []
        i = j = 0
        while i < len(esq) and j < len(dir):
            if esq[i] <= dir[j]:
                resultado.append(esq[i])
                i += 1
            else:
                resultado.append(dir[j])
                j += 1
        resultado.extend(esq[i:])
        resultado.extend(dir[j:])
        return resultado
 
    def dividir(lista):
        if len(lista) <= 1:
            return lista
        meio = len(lista) // 2
        esq = dividir(lista[:meio])
        dir = dividir(lista[meio:])
        return mesclar(esq, dir)
 
    return dividir(a)
 
 
# ------------------------------------------------------------
# GERAÇÃO DE DADOS E MEDIÇÃO
# ------------------------------------------------------------
 
def gerar_array_aleatorio(n):
    return [random.randint(VALOR_MINIMO, VALOR_MAXIMO) for _ in range(n)]
 
 
def medir_tempo_ms(func, dados):
    inicio = time.perf_counter()
    func(dados)
    fim = time.perf_counter()
    return (fim - inicio) * 1000.0
 
 
def formatar_n(n):
    return f"{n:,}".replace(",", ".")
 
 
# ------------------------------------------------------------
# EXECUÇÃO
# ------------------------------------------------------------
 
if __name__ == "__main__":
    for n in TAMANHOS:
        print(f"\n=== n = {formatar_n(n)} ===")
 
        dados_desordenados = gerar_array_aleatorio(n)

        t_shell_desord = medir_tempo_ms(shell_sort, dados_desordenados)
        print(f"Shell Sort  (desordenado): {t_shell_desord:.3f} ms")
 
        t_quick_desord = medir_tempo_ms(quick_sort, dados_desordenados)
        print(f"Quick Sort  (desordenado): {t_quick_desord:.3f} ms")
 
        t_merge_desord = medir_tempo_ms(merge_sort, dados_desordenados)
        print(f"Merge Sort  (desordenado): {t_merge_desord:.3f} ms")
 
        dados_ordenados = merge_sort(dados_desordenados)
 
        t_shell_ord = medir_tempo_ms(shell_sort, dados_ordenados)
        print(f"Shell Sort  (ja ordenado): {t_shell_ord:.3f} ms")
 
        t_quick_ord = medir_tempo_ms(quick_sort, dados_ordenados)
        print(f"Quick Sort  (ja ordenado): {t_quick_ord:.3f} ms")
 
        t_merge_ord = medir_tempo_ms(merge_sort, dados_ordenados)
        print(f"Merge Sort  (ja ordenado): {t_merge_ord:.3f} ms")
 
 
        maior_tempo = max(t_shell_desord, t_quick_desord, t_merge_desord)