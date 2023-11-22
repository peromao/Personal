# -*- coding: utf-8 -*-

from AnalisadorSintatico import AnalisadorSintatico
from ClassesAuxiliares import Token, SyntaxException
import re, os.path
import sys
import pytest


class Tracer:

	def __init__(self, func):
		self.__func = func
		self.__stack = []
	
	def trace(self, *args, **kwargs):
		sys.settrace(self.trace_calls)
		result = self.__func(*args, **kwargs)
		sys.settrace(None)
		return result, self.__stack
	
	def trace_calls(self, frame, event, arg):
		if event == "call":
			function_name = frame.f_code.co_name
			caller_name = frame.f_back.f_code.co_name
			self.__stack.append((caller_name, function_name))


def verifica_imports(arq="AnalisadorSintatico.py", excecoes=["ClassesAuxiliares", "Token", "NoInterno", "NoFolha", "SyntaxException"]):
	excecoes += ["import", "from"]
	if os.path.exists(arq):
		with open(arq, "r", encoding="utf-8") as f:
			for linha in f:
				if re.search(r"(^import[ ]|[ ]import[ ])", linha):
					bibliotecas = re.findall(r"(?is)\w+", linha)
					for nome in bibliotecas:
						assert nome in excecoes, f"Erro: o arquivo \"{arq}\" não pode importar bibliotecas externas"



@pytest.mark.parametrize('arquivo,tokens,metodos',
[
	# Teste do codigo0.w
	("codigo0.w", [Token("ALG", "alg", 1), Token("ID", "exemplo", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("RBLOCK", "}", 3), Token("EOF", "EOF", 3)],
	['alg', 'analisar', 'block', 'comparar', 'declarations', 'proximoToken', 'statementList', 'varDeclarationList']),
	
	# Teste do codigo1.w
	("codigo1.w", [Token("ALG", "alg", 1), Token("ID", "exemplo2", 1), Token("IMPLICIT", "implicit", 2), Token("MOD", "mod", 2), Token("LPAR", "(", 2), Token("NUMBER", "257", 2),
	Token("RPAR", ")", 2), Token("VAR", "var", 3), Token("LBLOCK", "{", 4), Token("RBLOCK", "}", 4), Token("EOF", "EOF", 4)],
	['alg', 'analisar', 'block', 'comparar', 'declarations', 'proximoToken', 'statementList', 'varDeclarationList']),

	# Teste do codigo2.w
	("codigo2.w", [Token("ALG", "alg", 1), Token("ID", "exemplo_print", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("OUT", "out", 4), Token("LPAR", "(", 4),
		Token("NUMBER", "1234", 4), Token("RPAR", ")", 4), Token("SEMICOLON", ";", 4), Token("RBLOCK", "}", 5), Token("EOF", "EOF", 5)],
	['alg', 'analisar', 'block', 'comparar', 'declarations', 'expression', 'factor', 'multiplicativeTerm', 'multiplicativeTerm2', 'outStatement', 'powerTerm', 'proximoToken', 'statement',
  'statementList', 'sumExpression', 'sumExpression2', 'varDeclarationList']),
	
	# Teste do codigo3.w
	("codigo3.w", [Token("ALG", "alg", 1), Token("ID", "exemplo_if", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("IF", "if", 4), Token("BOOLEAN", "true", 4),
		Token("LBLOCK", "{", 4), Token("RBLOCK", "}", 6), Token("ELSE", "else", 6), Token("LBLOCK", "{", 6), Token("RBLOCK", "}", 8), Token("RBLOCK", "}", 9), Token("EOF", "EOF", 9)],
	['alg', 'analisar', 'block', 'comparar', 'declarations', 'expression', 'factor', 'ifStatement', 'multiplicativeTerm', 'multiplicativeTerm2', 'powerTerm', 'proximoToken', 'statement',
  'statementList', 'sumExpression', 'sumExpression2', 'varDeclarationList']),
	
	# Teste do codigo4.w
	("codigo4.w", [Token("ALG", "alg", 1), Token("ID", "programa_com_uma_variavel", 1), Token("VAR", "var", 2), Token("TYPE", "log", 3), Token("ID", "a", 3), Token("SEMICOLON", ";", 3),
		Token("LBLOCK", "{", 4), Token("ID", "a", 5), Token("ASSIGN", "=", 5), Token("BOOLEAN", "true", 5), Token("SEMICOLON", ";", 5), Token("ID", "a", 6), Token("ASSIGN", "=", 6),
		Token("BOOLEAN", "false", 6), Token("SEMICOLON", ";", 6), Token("RBLOCK", "}", 7), Token("EOF", "EOF", 7)],
	['alg', 'analisar', 'assignStatement', 'block', 'comparar', 'declarations', 'expression', 'factor', 'identifierList', 'multiplicativeTerm', 'multiplicativeTerm2', 'powerTerm', 'proximoToken',
  'statement', 'statementList', 'sumExpression', 'sumExpression2', 'varDeclaration', 'varDeclarationList']),
	
	# Teste do codigo5.w
	("codigo5.w", [Token("ALG", "alg", 1), Token("ID", "soma_dois", 1), Token("VAR", "var", 2), Token("TYPE", "num", 3), Token("ID", "x", 3), Token("COMMA", ",", 3), Token("ID", "y", 3),
				Token("COMMA", ",", 3), Token("ID", "result", 3), Token("SEMICOLON", ";", 3), Token("LBLOCK", "{", 4), Token("ID", "x", 5), Token("ASSIGN", "=", 5), Token("IN", "in", 5),
				Token("LPAR", "(", 5), Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ID", "y", 6), Token("ASSIGN", "=", 6), Token("IN", "in", 6), Token("LPAR", "(", 6),
				Token("RPAR", ")", 6), Token("SEMICOLON", ";", 6), Token("ID", "result", 7), Token("ASSIGN", "=", 7), Token("ID", "x", 7), Token("OPSUM", "+", 7), Token("ID", "y", 7),
				Token("SEMICOLON", ";", 7), Token("OUT", "out", 8), Token("LPAR", "(", 8), Token("ID", "result", 8), Token("RPAR", ")", 8), Token("SEMICOLON", ";", 8), Token("RBLOCK", "}", 9), Token("EOF", "EOF", 9)],
	['alg', 'analisar', 'assignStatement', 'block', 'comparar', 'declarations', 'expression', 'factor', 'identifierList', 'inStatement', 'multiplicativeTerm', 'multiplicativeTerm2', 'outStatement',
  'powerTerm', 'proximoToken', 'statement', 'statementList', 'sumExpression', 'sumExpression2', 'varDeclaration', 'varDeclarationList']),

  # Teste do codigo6.w
	("codigo6.w", [Token("ALG", "alg", 1), Token("ID", "soma_dois_com_mais_declaracoes", 1), Token("VAR", "var", 2), Token("TYPE", "num", 3), Token("ID", "x", 3), Token("COMMA", ",", 3), Token("ID", "y", 3), Token("COMMA", ",", 3),
			Token("ID", "result", 3), Token("SEMICOLON", ";", 3), Token("TYPE", "log", 4), Token("ID", "a", 4), Token("SEMICOLON", ";", 4), Token("LBLOCK", "{", 5), Token("ID", "x", 6), Token("ASSIGN", "=", 6),
			Token("IN", "in", 6), Token("LPAR", "(", 6), Token("RPAR", ")", 6), Token("SEMICOLON", ";", 6), Token("ID", "y", 7), Token("ASSIGN", "=", 7), Token("IN", "in", 7), Token("LPAR", "(", 7),
			Token("RPAR", ")", 7), Token("SEMICOLON", ";", 7), Token("ID", "result", 8), Token("ASSIGN", "=", 8), Token("ID", "x", 8), Token("OPSUM", "+", 8), Token("ID", "y", 8), Token("SEMICOLON", ";", 8),
			Token("OUT", "out", 9), Token("LPAR", "(", 9), Token("ID", "result", 9), Token("RPAR", ")", 9), Token("SEMICOLON", ";", 9), Token("RBLOCK", "}", 10), Token("EOF", "EOF", 10)],
	['alg', 'analisar', 'assignStatement', 'block', 'comparar', 'declarations', 'expression', 'factor', 'identifierList', 'inStatement', 'multiplicativeTerm', 'multiplicativeTerm2', 'outStatement', 'powerTerm', 
  'proximoToken', 'statement', 'statementList', 'sumExpression', 'sumExpression2', 'varDeclaration', 'varDeclarationList']),

	# Teste do codigo7.w
	("codigo7.w", [Token("ALG", "alg", 1), Token("ID", "relogio", 1), Token("IMPLICIT", "implicit", 2), Token("MOD", "mod", 2), Token("LPAR", "(", 2), Token("NUMBER", "24", 2),
		Token("RPAR", ")", 2), Token("VAR", "var", 3), Token("TYPE", "num", 4), Token("ID", "hora1", 4), Token("SEMICOLON", ";", 4), Token("TYPE", "num", 5),
		Token("ID", "hora2", 5), Token("COMMA", ",", 5), Token("ID", "hora3", 5), Token("SEMICOLON", ";", 5), Token("TYPE", "log", 6), Token("ID", "virou", 6),
		Token("SEMICOLON", ";", 6), Token("LBLOCK", "{", 7), Token("ID", "hora1", 8), Token("ASSIGN", "=", 8), Token("NUMBER", "15", 8), Token("SEMICOLON", ";", 8),
		Token("ID", "hora2", 9), Token("ASSIGN", "=", 9), Token("IN", "in", 9), Token("LPAR", "(", 9), Token("RPAR", ")", 9), Token("SEMICOLON", ";", 9),
		Token("ID", "hora3", 10), Token("ASSIGN", "=", 10), Token("ID", "hora1", 10), Token("OPSUM", "+", 10), Token("ID", "hora2", 10), Token("SEMICOLON", ";", 10),
		Token("ID", "virou", 11), Token("ASSIGN", "=", 11), Token("ID", "hora3", 11), Token("OPREL", "<=", 11), Token("NUMBER", "15", 11), Token("SEMICOLON", ";", 11),
		Token("IF", "if", 12), Token("ID", "virou", 12), Token("LBLOCK", "{", 12), Token("OUT", "out", 13), Token("LPAR", "(", 13), Token("ID", "virou", 13),
		Token("RPAR", ")", 13), Token("SEMICOLON", ";", 13), Token("OUT", "out", 14), Token("LPAR", "(", 14), Token("ID", "hora3", 14), Token("RPAR", ")", 14),
		Token("SEMICOLON", ";", 14), Token("RBLOCK", "}", 15), Token("ELSE", "else", 15), Token("LBLOCK", "{", 15), Token("OUT", "out", 16), Token("LPAR", "(", 16),
		Token("ID", "hora3", 16), Token("RPAR", ")", 16), Token("SEMICOLON", ";", 16), Token("RBLOCK", "}", 17), Token("RBLOCK", "}", 18), Token("EOF", "EOF", 18)],
	['alg', 'analisar', 'assignStatement', 'block', 'comparar', 'declarations', 'expression', 'factor', 'identifierList', 'ifStatement', 'inStatement', 'multiplicativeTerm',
  'multiplicativeTerm2', 'outStatement', 'powerTerm', 'proximoToken', 'statement', 'statementList', 'sumExpression', 'sumExpression2', 'varDeclaration', 'varDeclarationList']),
	
	# Teste do codigo8.w
	("codigo8.w", [Token("ALG", "alg", 1), Token("ID", "testa_expressoes", 1), Token("VAR", "var", 2), Token("TYPE", "num", 3), Token("ID", "x", 3), Token("COMMA", ",", 3),
		Token("ID", "y", 3), Token("SEMICOLON", ";", 3), Token("LBLOCK", "{", 4), Token("ID", "x", 5), Token("ASSIGN", "=", 5), Token("LPAR", "(", 5), Token("NUMBER", "16", 5),
		Token("OPMUL", "#", 5), Token("NUMBER", "10", 5), Token("RPAR", ")", 5), Token("OPSUM", "+", 5), Token("NUMBER", "3", 5), Token("OPMUL", ".", 5), Token("LPAR", "(", 5),
		Token("NUMBER", "27", 5), Token("OPMUL", ":", 5), Token("NUMBER", "9", 5), Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ID", "y", 6), Token("ASSIGN", "=", 6),
		Token("NUMBER", "2", 6), Token("OPPOW", "^", 6), Token("NUMBER", "3", 6), Token("OPPOW", "^", 6), Token("NUMBER", "4", 6), Token("OPSUM", "-", 6), Token("ID", "x", 6),
		Token("SEMICOLON", ";", 6), Token("IF", "if", 7), Token("ID", "x", 7), Token("OPREL", ">", 7), Token("ID", "y", 7), Token("LBLOCK", "{", 7), Token("OUT", "out", 8),
		Token("LPAR", "(", 8), Token("ID", "x", 8), Token("RPAR", ")", 8), Token("SEMICOLON", ";", 8), Token("RBLOCK", "}", 9), Token("ELSE", "else", 9), Token("LBLOCK", "{", 9),
		Token("IF", "if", 10), Token("ID", "x", 10), Token("OPREL", "==", 10), Token("ID", "y", 10), Token("LBLOCK", "{", 10), Token("OUT", "out", 11), Token("LPAR", "(", 11),
		Token("ID", "x", 11), Token("RPAR", ")", 11), Token("SEMICOLON", ";", 11), Token("OUT", "out", 12), Token("LPAR", "(", 12), Token("ID", "y", 12), Token("RPAR", ")", 12),
		Token("SEMICOLON", ";", 12), Token("RBLOCK", "}", 13), Token("ELSE", "else", 13), Token("LBLOCK", "{", 13), Token("OUT", "out", 14), Token("LPAR", "(", 14), Token("ID", "y", 14),
		Token("RPAR", ")", 14), Token("SEMICOLON", ";", 14), Token("RBLOCK", "}", 15), Token("RBLOCK", "}", 16), Token("RBLOCK", "}", 17), Token("EOF", "EOF", 17)],
	['alg', 'analisar', 'assignStatement', 'block', 'comparar', 'declarations', 'expression', 'factor', 'identifierList', 'ifStatement', 'multiplicativeTerm', 'multiplicativeTerm2',
  'outStatement', 'powerTerm', 'proximoToken', 'statement', 'statementList', 'sumExpression', 'sumExpression2', 'varDeclaration', 'varDeclarationList']),
	
	
])
def test_codigo_sem_erro_sem_arvore(arquivo, tokens, metodos):
	sintatico = None
	try:
		sintatico = AnalisadorSintatico(tokens)
	except:
		raise AssertionError("Erro ao instanciar a classe AnalisadorSintatico")
	if sintatico:
		try:
			dictMetodos = {k: 0 for k in metodos}
			tracer = Tracer(sintatico.analisar)
			resultado, pilha = tracer.trace()
			for metodoAnt, metodoProx in pilha:
				if metodoProx in dictMetodos:
					dictMetodos[metodoProx] += 1
			metodosNaoChamados = []
			for metodo in sorted(dictMetodos.keys()):
				if dictMetodos[metodo] == 0:
					metodosNaoChamados.append(metodo)
			if metodosNaoChamados:  # se a lista não é vazia
				raise AssertionError("Métodos não chamados: " + ", ".join(metodosNaoChamados))
		except SyntaxException:
			raise AssertionError("A classe AnalisadorSintatico lançou um SyntaxException quando não deveria")



@pytest.mark.parametrize('arquivo,tokens,metodos,arv',
[
	# Teste do codigo0.w
	("codigo0.w", [Token("ALG", "alg", 1), Token("ID", "exemplo", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("RBLOCK", "}", 3), Token("EOF", "EOF", 3)],
	['alg', 'analisar', 'block', 'comparar', 'declarations', 'proximoToken', 'statementList', 'varDeclarationList'],
	['NoInterno(op="alg", block=NoInterno(op="block", statementList=None), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=None), id=NoFolha(op="id", valor="exemplo", linha=1))']),

	# Teste do codigo1.w
	("codigo1.w", [Token("ALG", "alg", 1), Token("ID", "exemplo2", 1), Token("IMPLICIT", "implicit", 2), Token("MOD", "mod", 2), Token("LPAR", "(", 2), Token("NUMBER", "257", 2),
	Token("RPAR", ")", 2), Token("VAR", "var", 3), Token("LBLOCK", "{", 4), Token("RBLOCK", "}", 4), Token("EOF", "EOF", 4)],
	['alg', 'analisar', 'block', 'comparar', 'declarations', 'proximoToken', 'statementList', 'varDeclarationList'],
	['NoInterno(op="alg", block=NoInterno(op="block", statementList=None), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="257", linha=2), varDeclarationList=None), id=NoFolha(op="id", valor="exemplo2", linha=1))']),
	

	# Teste do codigo3.w
	("codigo3.w", [Token("ALG", "alg", 1), Token("ID", "exemplo_print", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("OUT", "out", 4), Token("LPAR", "(", 4),
		Token("NUMBER", "1234", 4), Token("RPAR", ")", 4), Token("SEMICOLON", ";", 4), Token("RBLOCK", "}", 5), Token("EOF", "EOF", 5)],
	['alg', 'analisar', 'block', 'comparar', 'declarations', 'expression', 'factor', 'multiplicativeTerm', 'multiplicativeTerm2', 'outStatement', 'powerTerm', 'proximoToken', 'statement',
  'statementList', 'sumExpression', 'sumExpression2', 'varDeclarationList'],
	['NoInterno(op="alg", block=NoInterno(op="block", statementList=NoInterno(op="statementList", prox=None, statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="1234", linha=4), sinal="+"), oper=None)))), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=None), id=NoFolha(op="id", valor="exemplo_print", linha=1))']),

	# Teste do codigo6.w
	("codigo6.w", [Token("ALG", "alg", 1), Token("ID", "soma_dois_com_mais_declaracoes", 1), Token("VAR", "var", 2), Token("TYPE", "num", 3), Token("ID", "x", 3), Token("COMMA", ",", 3), Token("ID", "y", 3), Token("COMMA", ",", 3),
			Token("ID", "result", 3), Token("SEMICOLON", ";", 3), Token("TYPE", "log", 4), Token("ID", "a", 4), Token("SEMICOLON", ";", 4), Token("LBLOCK", "{", 5), Token("ID", "x", 6), Token("ASSIGN", "=", 6),
			Token("IN", "in", 6), Token("LPAR", "(", 6), Token("RPAR", ")", 6), Token("SEMICOLON", ";", 6), Token("ID", "y", 7), Token("ASSIGN", "=", 7), Token("IN", "in", 7), Token("LPAR", "(", 7),
			Token("RPAR", ")", 7), Token("SEMICOLON", ";", 7), Token("ID", "result", 8), Token("ASSIGN", "=", 8), Token("ID", "x", 8), Token("OPSUM", "+", 8), Token("ID", "y", 8), Token("SEMICOLON", ";", 8),
			Token("OUT", "out", 9), Token("LPAR", "(", 9), Token("ID", "result", 9), Token("RPAR", ")", 9), Token("SEMICOLON", ";", 9), Token("RBLOCK", "}", 10), Token("EOF", "EOF", 10)],
	['alg', 'analisar', 'assignStatement', 'block', 'comparar', 'declarations', 'expression', 'factor', 'identifierList', 'inStatement', 'multiplicativeTerm', 'multiplicativeTerm2', 'outStatement', 'powerTerm', 
  'proximoToken', 'statement', 'statementList', 'sumExpression', 'sumExpression2', 'varDeclaration', 'varDeclarationList'],
	['NoInterno(op="alg", block=NoInterno(op="block", statementList=NoInterno(op="statementList", prox=NoInterno(op="statementList", prox=NoInterno(op="statementList", prox=NoInterno(op="statementList", prox=None, statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="result", linha=9), sinal="+"), oper=None))), statement=NoInterno(op="assignStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="sumExpression", dir=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="y", linha=8), sinal="+"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="x", linha=8), sinal="+"), oper="+"), oper=None), id=NoFolha(op="id", valor="result", linha=8))), statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="y", linha=7), inStatement=NoFolha(op="in", valor="in", linha=7))), statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="x", linha=6), inStatement=NoFolha(op="in", valor="in", linha=6)))), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", prox=NoInterno(op="varDeclarationList", prox=None, varDeclaration=NoInterno(op="varDeclaration", identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="a", linha=4), prox=None), type=NoFolha(op="type", valor="log", linha=4))), varDeclaration=NoInterno(op="varDeclaration", identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="result", linha=3), prox=None))), type=NoFolha(op="type", valor="num", linha=3)))), id=NoFolha(op="id", valor="soma_dois_com_mais_declaracoes", linha=1))']),

  # Teste do codigo8.w
	("codigo8.w", [Token("ALG", "alg", 1), Token("ID", "testa_expressoes", 1), Token("VAR", "var", 2), Token("TYPE", "num", 3), Token("ID", "x", 3), Token("COMMA", ",", 3),
		Token("ID", "y", 3), Token("SEMICOLON", ";", 3), Token("LBLOCK", "{", 4), Token("ID", "x", 5), Token("ASSIGN", "=", 5), Token("LPAR", "(", 5), Token("NUMBER", "16", 5),
		Token("OPMUL", "#", 5), Token("NUMBER", "10", 5), Token("RPAR", ")", 5), Token("OPSUM", "+", 5), Token("NUMBER", "3", 5), Token("OPMUL", ".", 5), Token("LPAR", "(", 5),
		Token("NUMBER", "27", 5), Token("OPMUL", ":", 5), Token("NUMBER", "9", 5), Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ID", "y", 6), Token("ASSIGN", "=", 6),
		Token("NUMBER", "2", 6), Token("OPPOW", "^", 6), Token("NUMBER", "3", 6), Token("OPPOW", "^", 6), Token("NUMBER", "4", 6), Token("OPSUM", "-", 6), Token("ID", "x", 6),
		Token("SEMICOLON", ";", 6), Token("IF", "if", 7), Token("ID", "x", 7), Token("OPREL", ">", 7), Token("ID", "y", 7), Token("LBLOCK", "{", 7), Token("OUT", "out", 8),
		Token("LPAR", "(", 8), Token("ID", "x", 8), Token("RPAR", ")", 8), Token("SEMICOLON", ";", 8), Token("RBLOCK", "}", 9), Token("ELSE", "else", 9), Token("LBLOCK", "{", 9),
		Token("IF", "if", 10), Token("ID", "x", 10), Token("OPREL", "==", 10), Token("ID", "y", 10), Token("LBLOCK", "{", 10), Token("OUT", "out", 11), Token("LPAR", "(", 11),
		Token("ID", "x", 11), Token("RPAR", ")", 11), Token("SEMICOLON", ";", 11), Token("OUT", "out", 12), Token("LPAR", "(", 12), Token("ID", "y", 12), Token("RPAR", ")", 12),
		Token("SEMICOLON", ";", 12), Token("RBLOCK", "}", 13), Token("ELSE", "else", 13), Token("LBLOCK", "{", 13), Token("OUT", "out", 14), Token("LPAR", "(", 14), Token("ID", "y", 14),
		Token("RPAR", ")", 14), Token("SEMICOLON", ";", 14), Token("RBLOCK", "}", 15), Token("RBLOCK", "}", 16), Token("RBLOCK", "}", 17), Token("EOF", "EOF", 17)],
	['alg', 'analisar', 'assignStatement', 'block', 'comparar', 'declarations', 'expression', 'factor', 'identifierList', 'ifStatement', 'multiplicativeTerm', 'multiplicativeTerm2',
  'outStatement', 'powerTerm', 'proximoToken', 'statement', 'statementList', 'sumExpression', 'sumExpression2', 'varDeclaration', 'varDeclarationList'],
	['NoInterno(op="alg", block=NoInterno(op="block", statementList=NoInterno(op="statementList", prox=NoInterno(op="statementList", prox=NoInterno(op="statementList", prox=None, statement=NoInterno(op="ifStatement", blockElse=NoInterno(op="block", statementList=NoInterno(op="statementList", prox=None, statement=NoInterno(op="ifStatement", blockElse=NoInterno(op="block", statementList=NoInterno(op="statementList", prox=None, statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="y", linha=14), sinal="+"), oper=None)))), blockIf=NoInterno(op="block", statementList=NoInterno(op="statementList", prox=NoInterno(op="statementList", prox=None, statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="y", linha=12), sinal="+"), oper=None))), statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="x", linha=11), sinal="+"), oper=None)))), expression=NoInterno(op="expression", dir=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="y", linha=10), sinal="+"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="x", linha=10), sinal="+"), oper="==")))), blockIf=NoInterno(op="block", statementList=NoInterno(op="statementList", prox=None, statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="x", linha=8), sinal="+"), oper=None)))), expression=NoInterno(op="expression", dir=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="y", linha=7), sinal="+"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="x", linha=7), sinal="+"), oper=">"))), statement=NoInterno(op="assignStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="sumExpression", dir=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="id", valor="x", linha=6), sinal="+"), esq=NoInterno(op="powerTerm", dir=NoInterno(op="powerTerm", dir=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="4", linha=6), sinal="+"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="3", linha=6), sinal="+"), oper="^"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="2", linha=6), sinal="+"), oper="^"), oper="-"), oper=None), id=NoFolha(op="id", valor="y", linha=6))), statement=NoInterno(op="assignStatement", expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="sumExpression", dir=NoInterno(op="multiplicativeTerm", dir=NoInterno(op="factor", dir=None, esq=None, expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="multiplicativeTerm", dir=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="9", linha=5), sinal="+"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="27", linha=5), sinal="+"), oper=":"), oper=None), sinal="+"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="3", linha=5), sinal="+"), oper="."), esq=NoInterno(op="factor", dir=None, esq=None, expression=NoInterno(op="expression", dir=None, esq=NoInterno(op="multiplicativeTerm", dir=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="10", linha=5), sinal="+"), esq=NoInterno(op="factor", dir=None, esq=None, factor=NoFolha(op="num", valor="16", linha=5), sinal="+"), oper="#"), oper=None), sinal="+"), oper="+"), oper=None), id=NoFolha(op="id", valor="x", linha=5)))), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", prox=None, varDeclaration=NoInterno(op="varDeclaration", identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=3), prox=None)), type=NoFolha(op="type", valor="num", linha=3)))), id=NoFolha(op="id", valor="testa_expressoes", linha=1))']),
])
def test_codigo_sem_erro_com_arvore(arquivo, tokens, metodos, arv):
	arvStr = arv[0]  # a string que representa a árvore está em uma lista de 1 posição para deixar a saída dos testes mais compacta
	sintatico = None
	try:
		sintatico = AnalisadorSintatico(tokens)
	except:
		raise AssertionError("Erro ao instanciar a classe AnalisadorSintatico")
	if sintatico:
		try:
			dictMetodos = {k: 0 for k in metodos}
			tracer = Tracer(sintatico.analisar)
			resultado, pilha = tracer.trace()
			for metodoAnt, metodoProx in pilha:
				if metodoProx in dictMetodos:
					dictMetodos[metodoProx] += 1
			metodosNaoChamados = []
			for metodo in sorted(dictMetodos.keys()):
				if dictMetodos[metodo] == 0:
					metodosNaoChamados.append(metodo)
			if metodosNaoChamados:  # se a lista não é vazia
				raise AssertionError("Métodos não chamados: " + ", ".join(metodosNaoChamados))
			if resultado == None:
				raise AssertionError("A árvore sintática é vazia (None)")
			else:
				arvStrObtida = str(resultado)
				if arvStrObtida != arvStr:
					# Se for diferente, mostra a partir de qual ponto está diferente
					pos = 0
					while pos < len(arvStrObtida) and pos < len(arvStr) and arvStrObtida[pos] == arvStr[pos]:
						pos += 1
					raise AssertionError(f"A árvore sintática é diferente da esperada a partir de: {arvStrObtida[pos:pos+80]}...")
		except SyntaxException:
			raise AssertionError("A classe AnalisadorSintatico lançou um SyntaxException quando não deveria")



@pytest.mark.parametrize('arquivo,tokens,msgErroEsperada',
[
	# Teste do codigo9.w
	("codigo9.w", [Token("ALG", "alg", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("RBLOCK", "}", 3), Token("EOF", "EOF", 3)],
	['Token inesperado: "VAR" (var), tipo esperado: "ID", na linha 2']),
	
	# Teste do codigo10.w
	("codigo10.w", [Token("ALG", "alg", 1), Token("ID", "exemplo2", 1), Token("IMPLICIT", "implicit", 2), Token("MOD", "mod", 2), Token("LPAR", "(", 2), Token("LPAR", "(", 2), Token("NUMBER", "257", 2),
		Token("RPAR", ")", 2), Token("VAR", "var", 3), Token("LBLOCK", "{", 4), Token("RBLOCK", "}", 4), Token("EOF", "EOF", 4)],
	['Token inesperado: "LPAR" ((), tipo esperado: "NUMBER", na linha 2']),
	
	# Teste do codigo11.w
	("codigo11.w", [Token("ALG", "alg", 1), Token("ID", "exemplo_print", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("ID", "print", 4), Token("LPAR", "(", 4),
		Token("NUMBER", "1234", 4), Token("RPAR", ")", 4), Token("SEMICOLON", ";", 4), Token("RBLOCK", "}", 5), Token("EOF", "EOF", 5)],
	['Token inesperado: "LPAR" ((), tipo esperado: "ASSIGN", na linha 4']),
	
	# Teste do codigo12.w
	("codigo12.w", [Token("ALG", "alg", 1), Token("ID", "exemplo_if", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("IF", "if", 4), Token("BOOLEAN", "true", 4),
		Token("OUT", "out", 5), Token("LPAR", "(", 5), Token("BOOLEAN", "true", 5), Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ELSE", "else", 6),
		Token("OUT", "out", 7), Token("LPAR", "(", 7), Token("BOOLEAN", "false", 7), Token("RPAR", ")", 7), Token("SEMICOLON", ";", 7), Token("RBLOCK", "}", 8), Token("EOF", "EOF", 14)],
	['Token inesperado: "OUT" (out), tipo esperado: "LBLOCK", na linha 5']),
	
	# Teste do codigo13.w
	("codigo13.w", [Token("ALG", "alg", 1), Token("ID", "programa_com_uma_variavel", 1), Token("VAR", "var", 2), Token("TYPE", "log", 3), Token("ID", "a", 3),
				 Token("LBLOCK", "{", 4), Token("ID", "a", 5), Token("ASSIGN", "=", 5), Token("BOOLEAN", "true", 5), Token("SEMICOLON", ";", 5), Token("ID", "a", 6),
				 Token("ASSIGN", "=", 6), Token("BOOLEAN", "false", 6), Token("SEMICOLON", ";", 6), Token("RBLOCK", "}", 7), Token("EOF", "EOF", 7)],
	['Token inesperado: "LBLOCK" ({), tipo esperado: "SEMICOLON", na linha 4']),
	
	# Teste do codigo14.w
	("codigo14.w", [Token("ALG", "alg", 1), Token("ID", "soma_dois", 1), Token("VAR", "var", 2), Token("ID", "x", 3), Token("COMMA", ",", 3), Token("ID", "y", 3), Token("COMMA", ",", 3),
		Token("ID", "result", 3), Token("SEMICOLON", ";", 3), Token("LBLOCK", "{", 4), Token("ID", "x", 5), Token("ASSIGN", "=", 5), Token("IN", "in", 5), Token("LPAR", "(", 5),
		Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ID", "y", 6), Token("ASSIGN", "=", 6), Token("IN", "in", 6), Token("LPAR", "(", 6), Token("RPAR", ")", 6),
		Token("SEMICOLON", ";", 6), Token("ID", "result", 7), Token("ASSIGN", "=", 7), Token("ID", "x", 7), Token("OPSUM", "+", 7), Token("ID", "y", 7), Token("SEMICOLON", ";", 7),
		Token("OUT", "out", 8), Token("LPAR", "(", 8), Token("ID", "result", 8), Token("RPAR", ")", 8), Token("SEMICOLON", ";", 8), Token("RBLOCK", "}", 9), Token("EOF", "EOF", 9)],
	['Token inesperado: "ID" (x), tipo esperado: "TYPE", na linha 3']),
	
])
def test_codigo_com_erro(arquivo, tokens, msgErroEsperada):
	sintatico = None
	ok = False
	try:
		sintatico = AnalisadorSintatico(tokens)
	except:
		raise AssertionError("Erro ao instanciar a classe AnalisadorSintatico")
	if sintatico:
		try:
			sintatico.analisar()
		except SyntaxException as e:
			ok = True
			assert msgErroEsperada[0] == str(e), f"A mensagem de erro está diferente: {str(e)}"
	if not ok:
		raise AssertionError("A classe AnalisadorSintatico não lançou a exceção esperada")



if __name__ == '__main__':
	pytest.main()

