# -*- coding: utf-8 -*-

from ClassesAuxiliares import NoInterno, NoFolha, SyntaxException, Token


class AnalisadorSintatico:

	def __init__(self, listaTokens):
		"""
		Inicializa os atributos da classe.

		OBS: Não é necessário modificar este método.
		"""
		self.tokens = listaTokens
		self.tokenCorrente = None
		self.posicao = -1
		self.proximoToken()
	

	def proximoToken(self):
		"""
		Avança o próximo token da lista de tokens.
		O token corrente ficará disponível no atributo tokenCorrente.

		OBS: Não é necessário modificar este método.
		"""
		if self.posicao <= len(self.tokens)-2:  # Garante que vai estar sempre em uma faixa válida, caso contrário sempre retorna o último token (EOF)
			self.posicao += 1
			self.tokenCorrente = self.tokens[self.posicao]
	

	def lancarErro(self, tipoEsperado=None):
		"""
		Método que lança uma exceção do tipo SyntaxException.
		Ele será chamado pelo método comparar() quando o token esperado for diferente do token corrente.

		OBS: Não modifique as mensagens de erro!
		OBS: Não é necessário modificar este método.
		"""
		if tipoEsperado:
			raise SyntaxException(f"Token inesperado: \"{self.tokenCorrente.tipo}\" ({self.tokenCorrente.valor}), tipo esperado: \"{tipoEsperado}\", na linha {self.tokenCorrente.linha}")
		else:
			raise SyntaxException(f"Token inesperado: \"{self.tokenCorrente.tipo}\" ({self.tokenCorrente.valor}) na linha {self.tokenCorrente.linha}")
	

	def comparar(self, tipoEsperado):
		"""
		Compara o tokenCorrente com o tipo esperado (tipoEsperado) do token. Caso sejam diferentes, lança uma exceção do tipo SyntaxException.

		OBS: Não é necessário modificar este método.
		"""
		# print(f'  comparar: {self.tokenCorrente.tipo} {self.tokenCorrente.valor} {tipoEsperado}')  # remova o comentário se desejar visualizar as chamadas deste método. Pode ajudar na depuração
		tokenRetorno = self.tokenCorrente
		if self.tokenCorrente.tipo == tipoEsperado.upper():
			self.proximoToken()
		else:
			self.lancarErro(tipoEsperado)
		return tokenRetorno
	

	def analisar(self):
		"""
		Método que será chamado para inicializar a análise sintática.
		Chama o método alg().

		Ao implementar a árvore sintática, deve retornar o resultado do método alg().
		"""
		self.alg()


	def alg(self):
		"""
		Método que analisa a variável <alg> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados: id (um NoFolha com op igual a "id"), declarations, block.
		O valor do atributo op deve ser "alg".
		"""
		self.comparar("ALG")
		self.comparar("ID")
		self.declarations()
		self.block()
	

	def declarations(self):
		"""
		Método que analisa a variável <declarations> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados: mod (um NoFolha com op igual a "number"), varDeclarationList.
		O valor do atributo op deve ser "declarations".
		Dica para a árvore sintática: se não houver nenhuma declaração IMPLICIT, o valor associado ao NoFolha deve ser 0 (zero), e a linha também deve ser 0 (zero)!
		"""
		if self.tokenCorrente.tipo == "IMPLICIT":
			self.comparar("IMPLICIT")
			self.comparar("MOD")
			self.comparar("LPAR")
			self.comparar("NUMBER")
			self.comparar("RPAR")
		self.comparar("VAR")
		self.varDeclarationList()
	

	def varDeclarationList(self):
		"""
		Método que analisa a variável <varDeclarationList> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados: varDeclaration, prox.
		O valor do atributo op deve ser "varDeclarationList".

		Dica: este método pode fazer uma chamada recursiva para si mesmo. Pense em como usar isso para ligar os nós da árvore sintática!
		"""
		if self.tokenCorrente.tipo == "TYPE":
			self.varDeclaration()
			self.varDeclarationList()


	def varDeclaration(self):
		"""
		Método que analisa a variável <varDeclaration> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados: type (um NoFolha com op igual a "type"), identifierList.
		O valor do atributo op deve ser "varDeclaration".
		"""
		self.comparar("TYPE")
		self.identifierList()
		self.comparar("SEMICOLON")


	def identifierList(self):
		"""
		Método que analisa a variável <identifierList> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados: id (um NoFolha com op igual a "id"), prox.
		O valor do atributo op deve ser "identifierList".

		Dica: este método pode fazer uma chamada recursiva para si mesmo. Pense em como usar isso para ligar os nós da árvore sintática!
		"""
		self.comparar("ID")
		if self.tokenCorrente.tipo == "COMMA":
			self.comparar("COMMA")
			self.identifierList()


	def block(self):
		"""
		Método que analisa a variável <block> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com o seguinte parâmetro nomeado: statementList.
		O valor do atributo op deve ser "block".
		"""
		self.comparar("LBLOCK")
		self.statementList()
		self.comparar("RBLOCK")
	

	def statementList(self):
		"""
		Método que analisa a variável <statementList> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados: statement, prox.
		O valor do atributo op deve ser "statementList".

		Dica: este método pode fazer uma chamada recursiva para si mesmo. Pense em como usar isso para ligar os nós da árvore sintática!
		"""
		if self.tokenCorrente.tipo == "OUT" or self.tokenCorrente.tipo == "IF" or self.tokenCorrente.tipo == "ID":
			self.statement()
			self.statementList()
	

	def statement(self):
		"""
		Método que analisa a variável <statement> da linguagem.
		Compara se o token corrente é OUT, IF ou ID, e chama o método específico de cada caso.

		Esse método não cria nenhum nó na árvore sintática, mas deve retornar o objeto obtido ao chamar os métodos: 
		outStatement(), ifStatement() ou assignStatement().
		"""
		if self.tokenCorrente.tipo == "OUT":
			self.outStatement()
		elif self.tokenCorrente.tipo == "IF":
			self.ifStatement()
		else:
			self.assignStatement()



	def assignStatement(self):
		"""
		Método que analisa a variável <assignStatement> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados, a depender do tipo de atribuição:
			- se o token corrente for IN: id (um NoFolha com op igual a "id", contendo a variável que está recebendo o valor da atribuição), inStatement;
			- caso contrário: id (um NoFolha com op igual a "id", contendo a variável que está recebendo o valor da atribuição), expression;
		O valor do atributo op deste NoInterno deve ser "assignStatement".
		"""
		self.comparar("ID")
		self.comparar("ASSIGN")
		if self.tokenCorrente.tipo == "IN":
			self.inStatement()
		else:
			self.expression()
		self.comparar("SEMICOLON")
	

	def inStatement(self):
		"""
		Método que analisa a variável <inStatement> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoFolha com op igual a "in" e o valor igual a "in".
		"""
		self.comparar("IN")
		self.comparar("LPAR")
		self.comparar("RPAR")
	

	def outStatement(self):
		"""
		Método que analisa a variável <outStatement> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com o seguinte parâmetro nomeado: expression.
		O valor do atributo op deve ser "outStatement".
		"""
		self.comparar("OUT")
		self.comparar("LPAR")
		self.expression()
		self.comparar("RPAR")
		self.comparar("SEMICOLON")
	

	def ifStatement(self):
		"""
		Método que analisa a variável <ifStatement> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados: expression, blockIf, blockElse.
		O valor do atributo op deve ser "ifStatement".
		"""
		self.comparar("IF")
		self.expression()
		self.block()
		if self.tokenCorrente.tipo == "ELSE":
			self.comparar("ELSE")
			self.block()


	def expression(self):
		"""
		Método que analisa a variável <expression> da linguagem.

		Ao implementar a árvore sintática, deve retornar um NoInterno com os seguintes parâmetros nomeados:
			- oper: uma string contendo o operador relacional utilizado: ==, <>, < <=, >, >=, |. Se não tiver operador relacional, deve ter valor igual a None.
			- esq: recebe o resultado da sumExpression esquerda;
			- dir: caso exista um operador relacional, recebe o resultado da sumExpressioin direita;
		O valor do atributo op deve ser "expression".

		Dica: a partir deste ponto, todos os nós do tipo NoInterno terão os atributos nomeados esq e dir, ou seja, podemos considerar que a partir daqui
		teremos uma árvore binária!
		"""
		self.sumExpression()
		if self.tokenCorrente.tipo == "OPREL":
			self.comparar("OPREL")
			self.sumExpression()
	

	def sumExpression(self):
		"""
		Método que analisa a variável <sumExpression> da linguagem.
		Deve chamar o método multiplicativeTerm(), e em seguida sumExpression2().

		Ao implementar a árvore sintática, deve guardar o objeto retornado pelo método multiplicativeTerm(), e em seguida
		passar este objeto como parâmetro para sumExpression2(). Ao final, retorne o valor (objeto) retornado por sumExpression2().
		"""
		self.multiplicativeTerm()
		self.sumExpression2()
	

	def sumExpression2(self, esq=None):
		"""
		Método que analisa a variável <sumExpression2> da linguagem.
		Se o token corrente for um OPSUM, deve:
			1- processar (comparar) o OPSUM;
			2- chamar o método multiplicativeTerm();
			3- chamar o método sumExpression2(), ou seja, faz uma chamada recursiva;

		Ao implementar a árvore sintática, considere as seguintes alterações:
		Se o token corrente for um OPSUM, deve:
		1- processar (comparar) o token OPSUM;
		2- chamar o método multiplicativeTerm();
		3- Criar um NoInterno com op igual a "sumExpression", e os seguintes parâmetros nomeados:
			- oper: uma string representando o lexema associado ao OPSUM: +, -;
			- esq: recebe o valor do parâmetro esq;
			- dir: recebe o objeto retornado quando chamamos o método multiplicativeTerm() no passo 2;
		4- retorna o resultado de sumExpression2() (chamada recursiva), passando o NoInterno criado no passo 3 como parâmetro;

		Se o token corrente não for um OPSUM, retorna o parâmetro esq.
		"""
		self.comparar("OPSUM")
		self.multiplicativeTerm()
		self.sumExpression2()
	

	def multiplicativeTerm(self):
		"""
		Método que analisa a variável <multiplicativeTerm> da linguagem.
		Deve chamar o método powerTerm(), e em seguida multiplicativeTerm2().

		Ao implementar a árvore sintática, deve guardar o objeto retornado pelo método powerTerm(), e em seguida
		passar este objeto como parâmetro para multiplicativeTerm2(). Ao final, retorne o valor retornado por multiplicativeTerm2().
		"""
		self.powerTerm()
		self.multiplicativeTerm2()
	

	def multiplicativeTerm2(self, esq=None):
		"""
		Método que analisa a variável <multiplicativeTerm2> da linguagem.
		Se o token corrente for um OPMUL, deve:
			1- processar (comparar) o OPMUL;
			2- chamar o método powerTerm();
			3- chamar o método multiplicativeTerm2(), ou seja, faz uma chamada recursiva;

		Ao implementar a árvore sintática, considere as seguintes alterações:
		Se o token corrente for um OPMUL, deve:
		1- processar (comparar) o token OPMUL;
		2- chamar o método powerTerm();
		3- Criar um NoInterno com op igual a "multiplicativeTerm", e os seguintes parâmetros nomeados:
			- oper: uma string representando o lexema associado ao OPMUL: ., :, %, #;
			- esq: recebe o valor do parâmetro esq;
			- dir: recebe o objeto retornado quando chamamos o método powerTerm() no passo 2;
		4- retorna o resultado de multiplicativeTerm2() (chamada recursiva), passando o NoInterno criado no passo 3 como parâmetro;

		Se o token corrente não for um OPMUL, retorna o parâmetro esq.
		"""
		if self.tokenCorrente.tipo == "OPMUL":
			self.comparar("OPMUL")
		self.powerTerm()
		self.multiplicativeTerm2()


	def powerTerm(self):
		"""
		Método que analisa a variável <powerTerm> da linguagem. Deve:
			1- chamar o método factor();
			Se o token corrente for OPPOW, faz os 2 próximos passos:
			2- processar (comparar) o OPPOW;
			3- chamar o método powerTerm(), ou seja, faz uma chamada recursiva;

		Ao implementar a árvore sintática, considere as seguintes alterações:
		1- guarde o objeto retornada pelo método factor();
		Se o token corrente NÃO é um OPPOW, retorne o objeto obtida acima;
		Caso contrário (se o token corrente é um OPPOW), faça os próximos passos:
		2- processe (comparar) o token OPMUL;
		3- chame o método powerTerm() e guarde o objeto retornado;
		4- Criar um NoInterno com op igual a "powerTerm", e os seguintes parâmetros nomeados:
			- oper: uma string representando o lexema associado ao OPPOW: ^;
			- esq: recebe o objeto retornado quando chamamos factor() no passo 1;
			- dir: recebe o objeto retornado quando chamamos o método powerTerm() no passo 3;
		5- retorna o NoInterno criado no passo 4;

		Dica: Note que este método é diferente de sumExpression2 e multiplicativeTerm2: isso acontece porque queremos que a operação de
		exponenciação tenha associatividade à direita, enquanto que soma e multiplicação possuem associatividade à esquerda!
		"""
		self.factor()
		if self.tokenCorrente.tipo == "OPPOW":
			self.comparar("OPPOW")
			self.powerTerm()


	def factor(self):
		"""
		Método que analisa a variável <factor> da linguagem. Deve:
		1- testar se o token corrente é um OPSUM. Se sim, processe-o (comparar);
		2- testar se o token corrente é um ID, ou um NUMBER, ou um BOOLEAN. Se for, processe o respectivo token;
		3- caso os testes do passo 2 falhem, então é uma nova expressão. Neste caso:
			- processe um LPAR
			- chame o método expression()
			- processe um RPAR

		Ao implementar a árvore sintática, o método deve sempre retornar um NoInterno com op igual a "factor", e os seguintes parâmetros nomeados em comum:
			- sinal: uma string que representa o sinal do factor. Por padrão deve ser '+', mas se o factor possuir um OPSUM na frente, deve ser o valor associado a este OPSUM;
			- esq: None
			- dir: None
		Se o token for um ID:
			- adicione um atributo nomeado extra chamado factor, cujo valor é um NoFolha com op igual a 'id', e o valor é igual ao valor associado ao token;
		Se o token for um NUMBER:
			- adicione um atributo nomeado extra chamado factor, cujo valor é um NoFolha com op igual a 'num', e o valor é igual ao valor associado ao token;
		Se o token for um BOOLEAN:
			- adicione um atributo nomeado extra chamado factor, cujo valor é um NoFolha com op igual a 'log', e o valor é igual ao valor associado ao token;
		Se for um LPAR (caso contrário aos de cima):
			- adicione um atributo nomeado extra chamado expression, com o objeto retornado pelo método expression()
		
		Em seguida, faça com que o método retorne o NoInterno criado.
		"""
		if self.tokenCorrente.tipo == "ID":
			self.comparar("ID")
		elif self.tokenCorrente.tipo == "NUMBER":
			self.comparar("NUMBER")
		elif self.tokenCorrente.tipo == "LPAR":
			self.comparar("LPAR")
			self.expression()
			self.comparar("RPAR")
		elif self.tokenCorrente.tipo == "OPSUM":
			self.comparar("OPSUM")
			self.factor()

if __name__ == '__main__':
	tokens = [Token("ALG", "alg", 1), Token("ID", "exemplo_print", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("OUT", "out", 4), Token("LPAR", "(", 4),
		Token("NUMBER", "1234", 4), Token("RPAR", ")", 4), Token("SEMICOLON", ";", 4), Token("RBLOCK", "}", 5), Token("EOF", "EOF", 5)]
	sintatico = AnalisadorSintatico(tokens)
	sintatico.analisar()