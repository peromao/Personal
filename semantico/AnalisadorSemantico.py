
# -*- coding: utf-8 -*-

from ClassesAuxiliares import NoTabela, SemanticException


class AnalisadorSemantico:
	
	def __init__(self, arvoreSintatica):
		"""
		Construtor do analisador semântico: recebe uma árvore sintática e inicializa um dicionário que representa a tabela de símbolos.
		Não modifique este método.
		"""
		self.arvore = arvoreSintatica
		self.tabela = {}  # dicionário que representa a tabela de simbolos: armazena "linhas" do tipo NoTabela
	

	def analisar(self):
		"""
		Método que inicializa o processo de análise semântica.
		Não modifique este método.
		"""
		self.visitarAlg()
		

	def visitarAlg(self):
		"""
		Adiciona o ID do programa à tabela de símbolos: a chave é o próprio nome (valor) do identificador, e o valor é um NoTabela com valor None e tipo "alg".
		Chama:
			- visitarDeclarations(), passando o nó "declarations" por parâmetro;
			- visitarBlock(), passando o nó "block" por parâmetro;
		"""
		pass
	

	def visitarDeclarations(self, noDeclarations):
		"""
		Recebe um nó "declarations" por parâmetro. Possui um laço que percorre cada declaração da lista "varDeclarationList", e chama o método
		visitarVarDeclaration() passando cada nó "varDeclaration" contido na lista como parâmetro.
		"""
		pass
	

	def visitarVarDeclaration(self, noVarDeclaration):
		"""
		Recebe um nó "varDeclaration" por parâmetro. Possui um laço que percorre a lista "identifierList", para obter os identificadores declarados no programa.
		Ao processar cada identificador, verifica se ele já existe na tabela de símbolos. Se existir, lance uma SemanticException com a seguinte mensagem:
			- O identificador "NOME_DO_IDENTIFICADOR" na linha NUMERO_DA_LINHA foi declarado anteriormente
		Caso o ID não exista na lista, adicione-o à tabela de símbolos da seguinte maneira:
			- chave: nome do identificador
			- valor: NoTabela(None, TIPO_DO_IDENTIFICADOR)
		Dica: o valor None significa que o identificador ainda não foi inicializado.
		Dica: o tipo do identificador está disponível no objeto noVarDeclaration.
		"""
		pass
	

	def visitarBlock(self, noBlock):
		"""
		Recebe um nó "block" por parâmetro. Como um "block" possui apenas um "statementList", você pode processar todo o "statementList" dentro deste método.
		Mas se preferir, pode criar métodos adicionais.

		Possui um laço que percorre a lista "statementList", para obter os nós "statement" dentro deste bloco.

		Se o "statement" for um "assignStatement", faça o seguinte:
			1- obtenha o "id" (L-value) da atribuição;
			2- verifique se este id está contido na tabela de símbolos. Se não estiver, lance uma SemanticException com a mensagem:
				- O identificador "NOME_DO_IDENTIFICADOR" na linha NUMERO_DA_LINHA não foi declarado
			3- verifique se este "statement" possui um nó "expression". Caso positivo, chame o método visitarExpression() passando o nó "expression" como parâmetro;
			4- obtenha o valor retornado pelo método visitarExpression(), e verifique, através da tabela de símbolos, se o valor retornado é do mesmo tipo do id (L-value).
			Caso sejam de tipos diferentes, lance uma SemanticException com a mensagem:
				- O identificador "NOME_DO_IDENTIFICADOR" na linha NUMERO_DA_LINHA não pode receber uma expressão do tipo "TIPO_RETORNADO_PELA_EXPRESSION"
			5- atualize o valor associado ao id (L-value) na tabela de símbolos com um valor diferente de None. Lembre-se que todo identificador não inicializado
			possui o seu valor na tabela igual a None. Sugestão: este valor pode ser o próprio nome do identificador.

		Se o "statement" for um "outStatement", faça o seguinte:
			- chame o método visitarExpression() passando o nó "expression" como parâmetro;
		
		Se o "statement" for um "ifStatement", faça o seguinte:
			1- chame o método visitarBlock() de maneira recursiva, passando o nó "blockIf" como parâmetro;
			2- se o "statement" possuir um "blockElse", faça o mesmo com o "blockElse".
		"""
		pass


	def visitarExpression(self, noExpression):
		"""
		Recebe um nó "expression" por parâmetro. Chama o método visitarSumExpression() passando o nó "esq" como parâmetro.
		Caso não exista um operador, então o método deve retornar o resultado de visitarSumExpression().

		Caso a "expression" possua um operador (nó "oper"), chama visitarSumExpression() passando o nó "dir" como parâmetro. Neste caso, este método
		deve retornar um NoTabela() cujo tipo obrigatoriamente deve ser "log".
		"""
		pass
	

	def visitarSumExpression(self, no):
		"""
		Recebe um nó por parâmetro que pode ser um "sumExpression", "multiplicativeTerm", "powerTerm" ou "factor".
		Como todos esses nós possuem os apontadores "esq" e "dir", eles podem ser tratados como nós de uma árvore binária. Ou seja, você pode
		processar todos eles dentro deste método, ou se preferir pode criar métodos adicionais.
		
		O método já possui um esqueleto do percurso em pós-ordem com comentários adicionais (abaixo).
		Sugestão: o valor de retorno deve ser sempre um NoTabela(), contendo o valor retornado (o nome de um ID, um número inteiro ou um valor booleano,
		por exemplo), e o tipo de dado deste valor ("log" ou "num").
		"""
		if no != None:  # enquanto não chegar em um nó folha, continua o percurso (continue com a recursão)
			val1 = self.visitarSumExpression(no.get("esq"))  # visita a subárvore esquerda
			val2 = self.visitarSumExpression(no.get("dir"))  # visita a subárvore direita
			# Processa a raiz (if/elifs abaixo):
			if no.op == "sumExpression" or no.op == "multiplicativeTerm" or no.op == "powerTerm":
				"""
				Se o tipo de val1 e val2 forem diferentes, lança uma SemanticException com a seguinte mensagem:
					- Tipos incompatíveis: "VALOR_ASSOCIADO_A_VAL1" e "VALOR_ASSOCIADO_A_VAL2"

				Se o operador for ":" (divisão inteira), val2 for do tipo "num" e o valor de val2 for "0", lança uma SemanticException com a seguinte mensagem:
					- Divisão por zero na linha NUMERO_DA_LINHA

				Se o operador for "^" (potência), val2 for do tipo "num" e o valor de val2 for negativo, lança uma SemanticException com a seguinte mensagem:
					- Expoente negativo na linha NUMERO_DA_LINHA
				Dica: pode haver casos em que esta situação falhe, como em: 2 ^ -3 ^ 4, mas isso pode ser tratado na próxima etapa (geração de código), com um
				erro de execução.

				Em seguida, se val1 não for nulo retorne-o. Caso contrário, retorne val2.
				"""
				pass
				
			elif no.op == "factor" and not no.get("expression"):
				"""
				Obtenha o NoFolha dentro do factor.

				Se for um "id", faça as seguintes verificações:
					Se o identificador não está na tabela de símbolos, lance uma SemanticException com a mensagem:
						- O identificador "NOME_DO_IDENTIFICADOR" na linha NUMERO_DA_LINHA não foi declarado
					Se ele existe na tabela, mas seu valor é None (nulo), ele não foi inicializado. Neste caso lance uma SemanticException com a mensagem:
						- O identificador "NOME_DO_IDENTIFICADOR" na linha NUMERO_DA_LINHA não foi inicializado
					Caso contrário, retorne o objeto NoTabela associado ao identificador.
				
				Se for um "log" (valor booleano), retorne um NoTabela com este valor (true ou false) e o tipo "log".

				Se for um "num" (valor inteiro), obtenha o seu sinal. Se for negativo, retorne este valor (inteiro) com o sinal de "-" na frente. Além disso,
				associe o tipo "num" ao NoTabela retornado.
				"""
				pass

			elif no.op == "factor" and no.get("expression"):
				return self.visitarExpression(no.get("expression"))
