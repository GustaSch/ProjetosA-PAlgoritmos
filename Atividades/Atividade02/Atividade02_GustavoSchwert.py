import random
import time
 
# ------------------------------------------------------------
# CONFIGURAÇÃO
# ------------------------------------------------------------
 
TAMANHOS = [1_000, 5_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
 
VALOR_MINIMO = 0
VALOR_MAXIMO = 10_500
 
# n=100.000 levou ~171.313 ms num teste -> limite de 600.000ms
LIMITE_TEMPO_MS = 600_000
 
 
# ------------------------------------------------------------
# ALGORITMOS DE ORDENAÇÃO
# ------------------------------------------------------------
 
def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        houve_troca = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                houve_troca = True
        if not houve_troca:
            break
    return a
 
 
def insertion_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(1, n):
        chave = a[i]
        j = i - 1
        while j >= 0 and a[j] > chave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = chave
    return a
 
 
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
 
        t_bubble_desord = medir_tempo_ms(bubble_sort, dados_desordenados)
        print(f"Bubble Sort    (desordenado): {t_bubble_desord:.3f} ms")
 
        t_insertion_desord = medir_tempo_ms(insertion_sort, dados_desordenados)
        print(f"Insertion Sort (desordenado): {t_insertion_desord:.3f} ms")
 
        dados_ordenados = bubble_sort(dados_desordenados)
 
        t_bubble_ord = medir_tempo_ms(bubble_sort, dados_ordenados)
        print(f"Bubble Sort    (já ordenado): {t_bubble_ord:.3f} ms")
 
        t_insertion_ord = medir_tempo_ms(insertion_sort, dados_ordenados)
        print(f"Insertion Sort (já ordenado): {t_insertion_ord:.3f} ms")
 
        maior_tempo = max(t_bubble_desord, t_insertion_desord)
        if maior_tempo > LIMITE_TEMPO_MS:
            print(f"\nAVISO: tempo passou de {LIMITE_TEMPO_MS} ms. Parando por aqui.")
            break
 