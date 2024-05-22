import threading 

soma = 0 

class thread(threading.Thread): 
    def __init__(self, lista): 
        threading.Thread.__init__(self)
        self.lista = lista
    
    def run(self): 
        with threading.Lock():
            local_copy = soma
            local_copy += self.lista.pop
            soma = local_copy

threads = list()
lista = [i for i in range(100000)]
midpoint = len(lista) // 2
first_half = lista[:midpoint]
second_half = lista[midpoint:]
for index in range(2):
    x = thread(lista)
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()
print(soma)