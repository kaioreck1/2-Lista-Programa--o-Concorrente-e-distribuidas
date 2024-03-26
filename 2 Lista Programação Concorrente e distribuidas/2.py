import threading


contador_global = 0


lock = threading.Lock()


def incrementar_contador():
    global contador_global
    for _ in range(100):
     
        lock.acquire()
        contador_global += 1
       
        lock.release()

thread1 = threading.Thread(target=incrementar_contador)
thread2 = threading.Thread(target=incrementar_contador)


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Valor final do contador global:", contador_global)
