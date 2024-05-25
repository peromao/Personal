import threading 

class thread_(threading.Thread): 
    def __init__(self, lista, resultado): 
        threading.Thread.__init__(self)
        self.lista = lista
        self.resultado = resultado
    
    def run(self): 
        # Calcula a soma dos elementos da sub-lista e armazena no resultado fornecido
        self.resultado[0] = sum(self.lista)

def calcular(lista):
    # Cria as threads e divide a lista que vai para elas
    threads = list()
    meio = len(lista) // 2
    lista1 = lista[:meio]
    lista2 = lista[meio:]
    # Variáveis de cada thread para colocar o resultado
    resultado1 = [0]
    resultado2 = [0]

    # Cria e inicia uma thread para cada sub-lista e para variavel de resultado
    for sublist, resultado in zip([lista1, lista2], [resultado1, resultado2]):
        thread = thread_(sublist, resultado)
        threads.append(thread)
        thread.start()

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

    # Printa a soma total
    print(resultado1[0] + resultado2[0])

testes = [[i for i in range(1000)], [i for i in range(100)], [i for i in range(10)]]

for teste in testes:
    calcular(teste)
    # Reseta a soma para 0 para o próximo teste
    soma = 0