alg exemplo8
implicit mod(60)
var
	num minutos, copia;
{
	minutos = 7 ^ 2;
	copia = minutos;
	minutos = minutos + 10;
	minutos = 2 + minutos;
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo8"
# Inicialização de variáveis
minutos = 0
copia = 0
# Início do código
_TEMP_VAR_POW1 = 7 ** 2
minutos = _TEMP_VAR_POW1 % 60
copia = minutos % 60
_TEMP_VAR_SUM1 = minutos + 10
minutos = _TEMP_VAR_SUM1 % 60
_TEMP_VAR_SUM1 = 2 + minutos
minutos = _TEMP_VAR_SUM1 % 60
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo8", linha=1),
declarations=
    NoInterno(op="declarations", 
    mod=
        NoFolha(op="number", valor="60", linha=2),
    varDeclarationList=
        NoInterno(op="varDeclarationList", 
        varDeclaration=
            NoInterno(op="varDeclaration", 
            type=
                NoFolha(op="type", valor="num", linha=4),
            identifierList=
                NoInterno(op="identifierList", 
                id=
                    NoFolha(op="id", valor="minutos", linha=4),
                prox=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="copia", linha=4),
                    prox=
                        None
                    )
                )
            ),
        prox=
            None
        )
    ),
block=
    NoInterno(op="block", 
    statementList=
        NoInterno(op="statementList", 
        statement=
            NoInterno(op="assignStatement", 
            id=
                NoFolha(op="id", valor="minutos", linha=6),
            expression=
                NoInterno(op="expression", 
                oper=
                    None,
                esq=
                    NoInterno(op="powerTerm", 
                    oper=
                        "^",
                    esq=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="num", valor="7", linha=6),
                        esq=
                            None,
                        dir=
                            None
                        ),
                    dir=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="num", valor="2", linha=6),
                        esq=
                            None,
                        dir=
                            None
                        )
                    ),
                dir=
                    None
                )
            ),
        prox=
            NoInterno(op="statementList", 
            statement=
                NoInterno(op="assignStatement", 
                id=
                    NoFolha(op="id", valor="copia", linha=7),
                expression=
                    NoInterno(op="expression", 
                    oper=
                        None,
                    esq=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="id", valor="minutos", linha=7),
                        esq=
                            None,
                        dir=
                            None
                        ),
                    dir=
                        None
                    )
                ),
            prox=
                NoInterno(op="statementList", 
                statement=
                    NoInterno(op="assignStatement", 
                    id=
                        NoFolha(op="id", valor="minutos", linha=8),
                    expression=
                        NoInterno(op="expression", 
                        oper=
                            None,
                        esq=
                            NoInterno(op="sumExpression", 
                            oper=
                                "+",
                            esq=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="id", valor="minutos", linha=8),
                                esq=
                                    None,
                                dir=
                                    None
                                ),
                            dir=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="num", valor="10", linha=8),
                                esq=
                                    None,
                                dir=
                                    None
                                )
                            ),
                        dir=
                            None
                        )
                    ),
                prox=
                    NoInterno(op="statementList", 
                    statement=
                        NoInterno(op="assignStatement", 
                        id=
                            NoFolha(op="id", valor="minutos", linha=9),
                        expression=
                            NoInterno(op="expression", 
                            oper=
                                None,
                            esq=
                                NoInterno(op="sumExpression", 
                                oper=
                                    "+",
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="num", valor="2", linha=9),
                                    esq=
                                        None,
                                    dir=
                                        None
                                    ),
                                dir=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="id", valor="minutos", linha=9),
                                    esq=
                                        None,
                                    dir=
                                        None
                                    )
                                ),
                            dir=
                                None
                            )
                        ),
                    prox=
                        None
                    )
                )
            )
        )
    )
)
*/