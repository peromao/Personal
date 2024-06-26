import threading 

# Variável global para armazenar a soma total
soma = 0 
# Objeto de lock para garantir acesso exclusivo à variável soma
_lock = threading.Lock()

class thread_(threading.Thread): 
    def __init__(self, lista): 
        threading.Thread.__init__(self)
        # Armazena a sub-lista que essa thread irá processar
        self.lista = lista
    
    def run(self): 
        global soma
        # Calcula a soma dos elementos da sub-lista
        local_value = sum(self.lista)
        with _lock:
            soma += local_value


def calcular(lista):
    # Cria as threads e divide a lista que vai para elas
    threads = list()
    meio = len(lista) // 2
    lista1 = lista[:meio]
    lista2 = lista[meio:]

    # Cria e inicia uma thread para cada sub-lista
    for sublist in [lista1, lista2]:
        thread = thread_(sublist)
        threads.append(thread)
        thread.start()

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

    # Printa a soma total
    print(soma)

testes = [[i for i in range(1000)], [i for i in range(100)], [i for i in range(10)]]

for teste in testes:
    calcular(teste)
    # Reseta a soma para 0 para o próximo teste
    soma = 0