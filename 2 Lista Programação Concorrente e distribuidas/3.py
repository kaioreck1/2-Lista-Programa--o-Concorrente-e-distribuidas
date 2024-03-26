import threading
import queue
import random
import time


def gerar_numeros(fila):
    while True:
        numero = random.randint(1, 100)
        fila.put(numero)
        print(f"Número gerado: {numero}")
        time.sleep(1)


def imprimir_numeros(fila):
    while True:
        numero = fila.get()
        print(f"Número retirado: {numero}")
        time.sleep(2)


fila = queue.Queue()


thread_gerar = threading.Thread(target=gerar_numeros, args=(fila,))
thread_imprimir = threading.Thread(target=imprimir_numeros, args=(fila,))


thread_gerar.start()
thread_imprimir.start()


thread_gerar.join()
thread_imprimir.join()
