# -*- coding: utf-8 -*-

from GeradorCodigo import GeradorCodigo
from ClassesAuxiliares import NoInterno, NoFolha
import re, os.path
import sys
from io import StringIO
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


def verifica_imports(arq="GeradorCodigo.py", excecoes=["ClassesAuxiliares", "NoTabela", "NoFolha", "NoTabela"]):
	excecoes += ["import", "from"]
	if os.path.exists(arq):
		with open(arq, "r", encoding="utf-8") as f:
			for linha in f:
				if re.search(r"(^import[ ]|[ ]import[ ])", linha):
					bibliotecas = re.findall(r"(?is)\w+", linha)
					for nome in bibliotecas:
						assert nome in excecoes, f"Erro: o arquivo \"{arq}\" não pode importar bibliotecas externas"


def verifica_metodos_chamados(gerador, metodos):
	dictMetodos = {k: 0 for k in metodos}
	tracer = Tracer(gerador.gerarPython)
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


@pytest.mark.parametrize('arquivo,arvore,metodos,valoresEsperados',
[

# Teste do codigo0.w
("codigo0.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo0", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="a", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="b", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="soma", linha=3), prox=None)))), prox=None)), block=NoInterno(op="block", statementList=None)),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarVarDeclaration'],
{'a':0, 'b':0, 'soma':0}),

# Teste do codigo1.w
("codigo1.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo1", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="log", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="flagBooleano", linha=3), prox=None)), prox=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=4), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=4), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=4), prox=None))), prox=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="log", linha=5), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="w", linha=5), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="z", linha=5), prox=None))), prox=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=6), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="qtd", linha=6), prox=None)), prox=None))))), block=NoInterno(op="block", statementList=None)),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarVarDeclaration'],
{'x':0, 'y':0, 'qtd':0, 'flagBooleano':False, 'w':False, 'z':False}),

# Teste do codigo2.w
("codigo2.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo2", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=3), prox=None))), prox=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="log", linha=4), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="a", linha=4), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="b", linha=4), prox=None))), prox=None))), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="x", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=6), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="y", linha=7), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=7), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="a", linha=8), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="log", valor="true", linha=8), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="b", linha=9), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="log", valor="false", linha=9), esq=None, dir=None), dir=None)), prox=None)))))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarVarDeclaration'],
{'x':1, 'y':2, 'a':True, 'b':False}),

# Teste do codigo3.w
("codigo3.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo3", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="valor1", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="valor2", linha=3), prox=None))), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="valor1", linha=5), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=5), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=5), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="valor2", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="-", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=6), esq=None, dir=None)), dir=None)), prox=None)))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'valor1':3, 'valor2':-1}),

# Teste do codigo4.w
("codigo4.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo4", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="valor1", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="valor2", linha=3), prox=None))), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="valor1", linha=5), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=5), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=5), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="valor2", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper=":", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=6), esq=None, dir=None)), dir=None)), prox=None)))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'valor1':20, 'valor2':2}),

# Teste do codigo5.w
("codigo5.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo5", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=3), prox=None))), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="x", linha=5), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="sumExpression", oper="-", esq=NoInterno(op="sumExpression", oper="-", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=5), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="6", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="7", linha=5), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="y", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper=":", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=6), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=6), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=6), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="6", linha=6), esq=None, dir=None)), dir=None)), prox=None)))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'x':10, 'y':20}),

# Teste do codigo6.w
("codigo6.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo6", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="log", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=3), prox=None))), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="x", linha=5), expression=NoInterno(op="expression", oper=">", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=5), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=5), esq=None, dir=None)), dir=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="sumExpression", oper="-", esq=NoInterno(op="factor", sinal="-", factor=NoFolha(op="num", valor="4", linha=5), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="6", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="7", linha=5), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=5), esq=None, dir=None)))), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="y", linha=6), expression=NoInterno(op="expression", oper="<=", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=6), esq=None, dir=None)), dir=NoInterno(op="multiplicativeTerm", oper=":", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=6), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=6), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=6), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="6", linha=6), esq=None, dir=None)))), prox=None)))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'x':False, 'y':True}),

# Teste do codigo7.w
("codigo7.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo7", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="log", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="result", linha=3), prox=None)), prox=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=4), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="k", linha=4), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="j", linha=4), prox=None))), prox=None))), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="k", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="-", esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=6), esq=None, dir=None), dir=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=6), esq=None, dir=None)), dir=None), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=6), esq=None, dir=None))), dir=NoInterno(op="factor", sinal="+", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper=":", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="9", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=6), esq=None, dir=None)), dir=None), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="j", linha=7), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper=":", esq=NoInterno(op="factor", sinal="+", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="10", linha=7), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="18", linha=7), esq=None, dir=None)), dir=None), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="9", linha=7), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="result", linha=8), expression=NoInterno(op="expression", oper="==", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="j", linha=8), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="k", linha=8), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=8), esq=None, dir=None)), dir=None), esq=None, dir=None))), prox=None))))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'k':18, 'j':20, 'result':True}),

# Teste do codigo8.w
("codigo8.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo8", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="60", linha=2), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=4), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="minutos", linha=4), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="copia", linha=4), prox=None))), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="minutos", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="7", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=6), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="copia", linha=7), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="minutos", linha=7), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="minutos", linha=8), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="minutos", linha=8), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="10", linha=8), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="minutos", linha=9), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=9), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="minutos", linha=9), esq=None, dir=None)), dir=None)), prox=None)))))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'copia':49, 'minutos':1}),

# Teste do codigo9.w
("codigo9.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo9", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="mdc", linha=3), prox=None)), prox=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="log", linha=4), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="resultado", linha=4), prox=None)), prox=None))), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="mdc", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper="#", esq=NoInterno(op="multiplicativeTerm", oper="#", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="126", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="162", linha=6), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="180", linha=6), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="ifStatement", expression=NoInterno(op="expression", oper=">=", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="mdc", linha=7), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="18", linha=7), esq=None, dir=None)), blockIf=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="resultado", linha=8), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="log", valor="true", linha=8), esq=None, dir=None), dir=None)), prox=None)), blockElse=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="resultado", linha=10), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="log", valor="false", linha=10), esq=None, dir=None), dir=None)), prox=None))), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="mdc", linha=12), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper="#", esq=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=12), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="7", linha=12), esq=None, dir=None)), dir=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=12), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="8", linha=12), esq=None, dir=None))), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="mdc", linha=13), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=13), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=13), esq=None, dir=None)), dir=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=13), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=13), esq=None, dir=None))), dir=None)), prox=None)))))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration', 'visitarifStatement'],
{'mdc':14, 'resultado':True}),

])
def test_codigo_simples(arquivo, arvore, metodos, valoresEsperados):
	gerador = None
	try:
		gerador = GeradorCodigo(arvore)
	except:
		raise AssertionError("Erro ao instanciar a classe GeradorCodigo")
	if gerador:
		# Analisa os métodos chamados
		verifica_metodos_chamados(gerador, metodos)
		# Analisa o código gerado
		gerador = GeradorCodigo(arvore) # se chegou até aqui, é porque não houve problema ao instanciar a classe
		saida = gerador.gerarPython()
		globals = {} # dicionário que armazena os identificadores globais do programa executado
		exec(saida, globals)  # executa o código Python gerado
		for id in valoresEsperados.keys():
			if id in globals:
				assert globals[id] == valoresEsperados[id], f"A variável '{id}' deve ser igual a {valoresEsperados[id]}, mas seu valor é {globals[id]}"
			else:
				raise AssertionError(f"A variável '{id}' deveria existir no programa, mas não foi encontrada")



@pytest.mark.parametrize('arquivo,arvore,metodos,valoresEsperados,saidaEsperada',
[

# Teste do codigo10.w
("codigo10.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo10", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="256", linha=2), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=4), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=4), prox=None)), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="x", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="267", linha=6), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="x", linha=7), esq=None, dir=None), dir=None)), prox=None)))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'x':11},
[r'(?is)11']),

# Teste do codigo11.w
("codigo11.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo11", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=None), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper="#", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3000", linha=4), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2000", linha=4), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=5), esq=None, dir=None), dir=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=5), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=5), esq=None, dir=None))), dir=None)), prox=None)))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression'],
{},
[r'(?is)1000\s+7']),

# Teste do codigo12.w
("codigo12.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo12", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="z", linha=3), prox=None)))), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="x", linha=5), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=5), esq=None, dir=None), dir=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=5), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=5), esq=None, dir=None))), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="y", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="+", esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=6), esq=None, dir=None)), dir=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=6), esq=None, dir=None), dir=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=6), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="4", linha=6), esq=None, dir=None)))), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="z", linha=7), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="powerTerm", oper="^", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=7), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="5", linha=7), esq=None, dir=None)), dir=None), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="3", linha=7), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="multiplicativeTerm", oper=".", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="z", linha=8), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=8), esq=None, dir=None)), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="y", linha=9), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="outStatement", expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="sumExpression", oper="-", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="x", linha=10), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="1", linha=10), esq=None, dir=None)), dir=None)), prox=None)))))))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
{'x':42535295865117307932921825928971026432, 'y':2417851639229258349412364, 'z':32768},
[r'(?is)65536\s+2417851639229258349412364\s+42535295865117307932921825928971026431']),

])
def test_codigo_print(arquivo, arvore, metodos, valoresEsperados, saidaEsperada):
	gerador = None
	try:
		gerador = GeradorCodigo(arvore)
	except:
		raise AssertionError("Erro ao instanciar a classe GeradorCodigo")
	if gerador:
		# Analisa os métodos chamados
		verifica_metodos_chamados(gerador, metodos)
		# Analisa o código gerado
		gerador = GeradorCodigo(arvore) # se chegou até aqui, é porque não houve problema ao instanciar a classe
		saida = gerador.gerarPython()
		globals = {} # dicionário que armazena os identificadores globais do programa executado
		print(saida)
		OLD_STDOUT = sys.stdout
		sys.stdout = NEW_STDOUT = StringIO()
		exec(saida, globals)  # executa o código Python gerado
		sys.stdout = OLD_STDOUT
		saidaPrints = NEW_STDOUT.getvalue().strip()
		for id in valoresEsperados.keys():
			if id in globals:
				assert globals[id] == valoresEsperados[id], f"A variável '{id}' deve ser igual a {valoresEsperados[id]}, mas seu valor é {globals[id]}"
			else:
				raise AssertionError(f"A variável '{id}' deveria existir no programa, mas não foi encontrada")
		assert re.match(saidaEsperada[0], saidaPrints) != None, "A saída impressa é diferente da esperada"


@pytest.mark.parametrize('arquivo,arvore,metodos,valoresEntrada,valoresEsperados',
[

# Teste do codigo13.w
("codigo13.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo13", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="x", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="y", linha=3), prox=NoInterno(op="identifierList", id=NoFolha(op="id", valor="z", linha=3), prox=None)))), prox=None)), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="x", linha=5), inStatement=NoFolha(op="in", valor="in", linha=5)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="y", linha=6), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="30", linha=6), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="z", linha=7), inStatement=NoFolha(op="in", valor="in", linha=7)), prox=None))))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration'],
[10, 20],
{'x':10, 'y':30, 'z':20}),

# Teste do codigo14.w
("codigo14.w", NoInterno(op="alg", id=NoFolha(op="id", valor="exemplo14", linha=1), declarations=NoInterno(op="declarations", mod=NoFolha(op="number", valor="0", linha=0), varDeclarationList=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="num", linha=3), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="numero", linha=3), prox=None)), prox=NoInterno(op="varDeclarationList", varDeclaration=NoInterno(op="varDeclaration", type=NoFolha(op="type", valor="log", linha=4), identifierList=NoInterno(op="identifierList", id=NoFolha(op="id", valor="resultado", linha=4), prox=None)), prox=None))), block=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="numero", linha=6), inStatement=NoFolha(op="in", valor="in", linha=6)), prox=NoInterno(op="statementList", statement=NoInterno(op="ifStatement", expression=NoInterno(op="expression", oper="|", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=7), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="numero", linha=7), esq=None, dir=None)), blockIf=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="resultado", linha=8), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="log", valor="true", linha=8), esq=None, dir=None), dir=None)), prox=None)), blockElse=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="resultado", linha=10), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="log", valor="false", linha=10), esq=None, dir=None), dir=None)), prox=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="numero", linha=11), inStatement=NoFolha(op="in", valor="in", linha=11)), prox=NoInterno(op="statementList", statement=NoInterno(op="ifStatement", expression=NoInterno(op="expression", oper="==", esq=NoInterno(op="multiplicativeTerm", oper="%", esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="id", valor="numero", linha=12), esq=None, dir=None), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="2", linha=12), esq=None, dir=None)), dir=NoInterno(op="factor", sinal="+", factor=NoFolha(op="num", valor="0", linha=12), esq=None, dir=None)), blockIf=NoInterno(op="block", statementList=NoInterno(op="statementList", statement=NoInterno(op="assignStatement", id=NoFolha(op="id", valor="resultado", linha=13), expression=NoInterno(op="expression", oper=None, esq=NoInterno(op="factor", sinal="+", factor=NoFolha(op="log", valor="true", linha=13), esq=None, dir=None), dir=None)), prox=None)), blockElse=None), prox=None))))), prox=None)))),
['gerarPython', 'visitarBlock', 'visitarDeclarations', 'visitarExpression', 'visitarSumExpression', 'visitarVarDeclaration', 'visitarifStatement'],
[11, 12],
{'numero':12, 'resultado':True}),

])
def test_codigo_input(arquivo, arvore, metodos, valoresEntrada, valoresEsperados):
	gerador = None
	try:
		gerador = GeradorCodigo(arvore)
	except:
		raise AssertionError("Erro ao instanciar a classe GeradorCodigo")
	if gerador:
		# Analisa os métodos chamados
		verifica_metodos_chamados(gerador, metodos)
		# Analisa o código gerado
		gerador = GeradorCodigo(arvore) # se chegou até aqui, é porque não houve problema ao instanciar a classe
		saida = gerador.gerarPython()
		for valor in valoresEntrada:
			saida = re.sub(r"=\s*int\s*[(]\s*input[(]\s*[)]\s*[)]", f"= {valor}", saida, count=1) # substitui a primeira ocorrência de "= int(input())" para "= {valor}"
		globals = {} # dicionário que armazena os identificadores globais do programa executado
		exec(saida, globals)  # executa o código Python gerado
		for id in valoresEsperados.keys():
			if id in globals:
				assert globals[id] == valoresEsperados[id], f"A variável '{id}' deve ser igual a {valoresEsperados[id]}, mas seu valor é {globals[id]}"
			else:
				raise AssertionError(f"A variável '{id}' deveria existir no programa, mas não foi encontrada")



if __name__ == '__main__':
	pytest.main()

