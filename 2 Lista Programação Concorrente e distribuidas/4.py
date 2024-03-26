import threading
import random
import time


def tarefa():

    tempo_espera = random.randint(1, 5)
    
    
    print(f"Thread {threading.current_thread().name} iniciada.")
    
 
    time.sleep(tempo_espera)
    
  
    print(f"Thread {threading.current_thread().name} terminada.")


threads = []

for i in range(5):
    thread = threading.Thread(target=tarefa)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print("Todas as threads terminaram.")
