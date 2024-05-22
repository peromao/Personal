import threading 

soma = 0 
_lock = threading.Lock()

class thread_(threading.Thread): 
    def __init__(self, lista): 
        threading.Thread.__init__(self)
        self.lista = lista
    
    def run(self): 
        global soma
        local_value = sum(self.lista)
        with _lock:
            soma += local_value


def calcular(lista):
    threads = list()
    meio = len(lista) // 2
    lista1 = lista[:meio]
    lista2 = lista[meio:]


    for sublist in [lista1, lista2]:
        thread = thread_(sublist)
        threads.append(thread)
        thread.start()

    for thread in enumerate(threads):
        thread.join()

    print(soma)

testes = [[i for i in range(1000)], [i for i in range(100)], [i for i in range(10)]]

for teste in testes:
    calcular(teste)
    soma = 0