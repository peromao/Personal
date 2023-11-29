# -*- coding: utf-8 -*-

# Os imports abaixo não são necessários, mas caso você necessite, são os únicos permitidos:
#from ClassesAuxiliares import NoInterno, NoFolha, NoTabela


class GeradorCodigo:

	def __init__(self, arvoreSintatica):
		# Mantenha pelo menos os 2 atributos a seguir:
		self.saida = ""
		self.arvore = arvoreSintatica
		# Você pode modificar e/ou criar seus atributos a partir daqui:
		self.mod = ""  # é necessário guardar informação referente à declaração "implicit mod"
		self.numTabs = -1  # é necessário guardar o nível de indentação
		self.simboloTab = "    "  # sugestão: utilize 4 espaços como indentação. Você pode usar este atributo como uma constante
		# Contadores de variáveis temporárias:
		self.varNumSum = 0
		self.varNumMul = 0
		self.varNumPow = 0
		self.varNumMinus = 0
		# Crie mais atributos se achar necessário::


	def gerarPython(self):
		"""
		Método já implementado para servir de exemplo. Evite modificá-lo.
		"""
		self.saida += "import math\n"  # necessário para a operação de MDC (operador: #)
		self.saida += f"\n# Código gerado a partir do programa \"{self.arvore.get('id').valor}\"\n"
		self.saida += f"# Inicialização de variáveis\n"
		self.visitarDeclarations(self.arvore.get("declarations"))
		self.saida += f"# Início do código\n"
		self.visitarBlock(self.arvore.get("block"))
		return self.saida


	def visitarDeclarations(self, noDeclarations):
		"""
		Método que processa as declarações do programa.

		Sugestões: use o atributo mod da classe para guardar o valor do módulo implícito (comando: implicit mod), caso o valor do
		nó mod seja maior do que zero. Este valor será usado em todas as atribuições, ou seja, se mod for maior do que zero,
		todas as atribuições serão módulo este valor.
		Sugestão: para facilitar, self.mod pode ser algo como: " % X", onde X é o valor do módulo, ou então uma string vazia, caso o
		programa não tenha módulo implícito. Assim, é só concatenar self.mod a todas as atribuições mais adiante.

		Percorra o nó varDeclarationList, passando o objeto varDeclaration para o método visitarVarDeclaration().
		"""
		pass
	

	def visitarVarDeclaration(self, noVarDeclaration):
		"""
		Método que varre a lista de identificadores de um tipo específico (identifierList), cria o código Python que inicializa
		esses identificadores.
		Se forem do tipo num, devem ser inicializados como zero. Se forem do tipo log, devem ser inicializados como False.
		"""
		pass
	
	
	def visitarBlock(self, noBlock):
		"""
		Método que varre a lista statementList e cria o código Python de cada declaração contida nela.
		Ao entrar no método, incremente o atributo numTabs em 1 unidade. Antes de sair, decremente este atributo em 1 unidade.
		Para cada statement, modifique o valor dos atributos varNumSum, varNumMul, varNumPow e varNumMinus com o valor 1.

		Sugestões:
			Teste se a operação (op) contida no statement atual é uma das operações listadas abaixo. Se for, concatene o código Python necessário
			no atributo saida, considerando o nível de indentação do bloco:

			- um assignStatement que contém um atributo inStatement: neste caso, o identificador do lado esquerdo (L-value) deve
			receber int(input()). Ou seja, todo comando in() da linguagem é convertido para int(input()) em Python, e portanto a linguagem
			só é capaz de ler valores inteiros;

			- um assignStatement que contém um atributo expression: chama o método visitarExpression(), passando o nó expression como parâmetro.
			Em seguida, o identificador do lado esquerdo recebe a string retornada por visitarExpression(). Caso o programa tenha sido criado
			com a cláusula "implicit mod(X)", a atribuição deve ser sempre realizada módulo o valor de X;
			
			- um outStatement: chama o método visitarExpression() passando o nó expression como parâmetro. Cria um comando print(X),
			onde X é uma string retornada pelo método visitarExpression();

			- um ifStatement: chama o método visitarifStatement(), passando o nó ifStatement como parâmetro.
		"""
		pass
	

	def visitarifStatement(self, noIfStatement):
		"""
		Método que processa um ifStatement e cria o código Python correspondente da declaração if-else.

		Deve chamar visitarExpression(), passando o objeto expression por parâmetro. Em seguida, ao receber uma string X como resposta,
		cria o código "if X:".
		Após isso, chame o método visitarBlock(), passando o nó blockIf como parâmetro.

		Se o nó possuir um atributo blockElse, crie o código correspondente ao "else:", e em seguida chame o método visitarBlock(), passando
		o nó blockElse como parâmetro.

		OBS: lembre-se de criar o código com o nível de indentação necessário.
		"""
		pass
	

	def visitarExpression(self, noExpression):
		"""
		Método que processa um nó expression, e cria o código Python correspondente.

		1- chame visitarSumExpression(), passando o nó esq como parâmetro. Se o noExpression não contém o atributo oper, retorna como resultado
		a string E retornada por visitarSumExpression();
		2- caso noExpression possua o atributo oper, é porque noExpression é uma expressão lógica. Neste caso, chame visitarSumExpression(),
		desta vez passando o nó dir como parâmetro, e guarde seu valor de retorno na string D;
		3- crie uma variável temporária que recebe o resultado de: E operacao D, onde operação é o operador lógico equivalente em Python. Sugestão
		para o nome da variável temporária: _TEMP_VAR_REL;
		4- retorne o nome da variável temporária (_TEMP_VAR_REL);

		Dica: caso o operador lógico seja | (divide), ele funciona da seguinte forma: a | b (lê-se "a divide b?") é verdadeiro quando: b % a == 0.
		Para implementá-lo, crie outra variável temporária (sugestão: _TEMP_VAR_MOD) que armazena o resultado de b % a. Em seguida, faça com que
		_TEMP_VAR_REL receba o resultado de _TEMP_VAR_MOD == 0.
		"""
		pass
	
	
	def visitarSumExpression(self, no):
		"""
		Recebe um nó por parâmetro que pode ser um "sumExpression", "multiplicativeTerm", "powerTerm" ou "factor".
		Como todos esses nós possuem os apontadores "esq" e "dir", eles podem ser tratados como nós de uma árvore binária. Ou seja, você pode
		processar todos eles dentro deste método, ou se preferir pode criar métodos adicionais.
		"""
		if no != None:
			val1 = self.visitarSumExpression(no.get("esq"))  # visita a subárvore esquerda
			val2 = self.visitarSumExpression(no.get("dir"))  # visita a subárvore direita
			# Processa a raiz:
			if no.op == "sumExpression":
				"""
				Cria o código Python que processa um OPSUM.
				Ideia principal: crie uma variável temporária (sugestão: _TEMP_VAR_SUM@, onde @ é um número inteiro) que
				recebe o resultado de: val1 OPSUM val2.

				Em seguida, retorne uma string com nome da variável temporária.
				"""
				pass

			elif no.op == "multiplicativeTerm":
				"""
				Cria o código Python que processa um OPMUL.
				Ideia principal: crie uma variável temporária (sugestão: _TEMP_VAR_MUL@, onde @ é um número inteiro) que
				recebe o resultado de: val1 OPMUL val2.

				Dica: se o OPMUL for a operação de MDC, a variável temporária recebe o resultado de: math.gcd(val1, val2)

				Em seguida, retorne uma string com nome da variável temporária.
				"""
				pass

			elif no.op == "powerTerm":
				"""
				Cria o código Python que processa um OPPOW.
				Ideia principal: crie uma variável temporária (sugestão: _TEMP_VAR_POW@, onde @ é um número inteiro) que
				recebe o resultado de: val1 OPPOW val2.

				Em seguida, retorne uma string com nome da variável temporária.
				"""
				pass
				
			elif no.op == "factor" and not no.get("expression"):
				"""
				Cria o código Python que processa um factor.

				Se o factor for um id ou num, e o sinal for "-", crie uma variável temporária (sugestão: _TEMP_VAR_MINUS@,
				onde @ é um número inteiro) que recebe o resultado de: - X, onde X é o valor do factor.
				Em seguida, retorne uma string com nome da variável temporária.

				Caso contrário, se o factor é um log e seu valor é true, retorne a string "True";
				Caso contrário, se o factor é um log e seu valor é false, retorne a string "False";
				Caso contrário, o factor é um inteiro, então retorne o seu valor.
				"""
				pass
				
			elif no.op == "factor" and no.get("expression"):
				sinal = no.get("sinal")
				if sinal == "-":
					temp = self.visitarExpression(no.get("expression"))
					"""
					Cria o código Python que processa um factor entre parênteses.

					Neste caso, o factor é negativo. Crie uma variável temporária (sugestão: _TEMP_VAR_MINUS@, onde @ é um número inteiro) que
					recebe o resultado de: - temp.
					Em seguida, retorne uma string com nome da variável temporária.
					"""
					
				else:
					# Neste caso, não precisa fazer mais nada
					return self.visitarExpression(no.get("expression"))

