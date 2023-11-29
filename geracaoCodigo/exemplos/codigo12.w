alg exemplo12
var
	num x, y, z;
{
	x = 2 ^ 5 ^ 3;
	y = 3 . 4 + 2 ^ 3 ^ 4;
	z = (2 ^ 5) ^ 3;
	out(z.2);
	out(y);
	out(x-1);
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo12"
# Inicialização de variáveis
x = 0
y = 0
z = 0
# Início do código
_TEMP_VAR_POW1 = 5 ** 3
_TEMP_VAR_POW2 = 2 ** _TEMP_VAR_POW1
x = _TEMP_VAR_POW2
_TEMP_VAR_MUL1 = 3 * 4
_TEMP_VAR_POW1 = 3 ** 4
_TEMP_VAR_POW2 = 2 ** _TEMP_VAR_POW1
_TEMP_VAR_SUM1 = _TEMP_VAR_MUL1 + _TEMP_VAR_POW2
y = _TEMP_VAR_SUM1
_TEMP_VAR_POW1 = 2 ** 5
_TEMP_VAR_POW2 = _TEMP_VAR_POW1 ** 3
z = _TEMP_VAR_POW2
_TEMP_VAR_MUL1 = z * 2
print(_TEMP_VAR_MUL1)
print(y)
_TEMP_VAR_SUM1 = x - 1
print(_TEMP_VAR_SUM1)
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo12", linha=1),
declarations=
    NoInterno(op="declarations", 
    mod=
        NoFolha(op="number", valor="0", linha=0),
    varDeclarationList=
        NoInterno(op="varDeclarationList", 
        varDeclaration=
            NoInterno(op="varDeclaration", 
            type=
                NoFolha(op="type", valor="num", linha=3),
            identifierList=
                NoInterno(op="identifierList", 
                id=
                    NoFolha(op="id", valor="x", linha=3),
                prox=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="y", linha=3),
                    prox=
                        NoInterno(op="identifierList", 
                        id=
                            NoFolha(op="id", valor="z", linha=3),
                        prox=
                            None
                        )
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
                NoFolha(op="id", valor="x", linha=5),
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
                            NoFolha(op="num", valor="2", linha=5),
                        esq=
                            None,
                        dir=
                            None
                        ),
                    dir=
                        NoInterno(op="powerTerm", 
                        oper=
                            "^",
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="num", valor="5", linha=5),
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
                                NoFolha(op="num", valor="3", linha=5),
                            esq=
                                None,
                            dir=
                                None
                            )
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
                    NoFolha(op="id", valor="y", linha=6),
                expression=
                    NoInterno(op="expression", 
                    oper=
                        None,
                    esq=
                        NoInterno(op="sumExpression", 
                        oper=
                            "+",
                        esq=
                            NoInterno(op="multiplicativeTerm", 
                            oper=
                                ".",
                            esq=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="num", valor="3", linha=6),
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
                                    NoFolha(op="num", valor="4", linha=6),
                                esq=
                                    None,
                                dir=
                                    None
                                )
                            ),
                        dir=
                            NoInterno(op="powerTerm", 
                            oper=
                                "^",
                            esq=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="num", valor="2", linha=6),
                                esq=
                                    None,
                                dir=
                                    None
                                ),
                            dir=
                                NoInterno(op="powerTerm", 
                                oper=
                                    "^",
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="num", valor="3", linha=6),
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
                                        NoFolha(op="num", valor="4", linha=6),
                                    esq=
                                        None,
                                    dir=
                                        None
                                    )
                                )
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
                        NoFolha(op="id", valor="z", linha=7),
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
                                                NoFolha(op="num", valor="2", linha=7),
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
                                                NoFolha(op="num", valor="5", linha=7),
                                            esq=
                                                None,
                                            dir=
                                                None
                                            )
                                        ),
                                    dir=
                                        None
                                    ),
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
                                    NoFolha(op="num", valor="3", linha=7),
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
                        NoInterno(op="outStatement", 
                        expression=
                            NoInterno(op="expression", 
                            oper=
                                None,
                            esq=
                                NoInterno(op="multiplicativeTerm", 
                                oper=
                                    ".",
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="id", valor="z", linha=8),
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
                                        NoFolha(op="num", valor="2", linha=8),
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
                            NoInterno(op="outStatement", 
                            expression=
                                NoInterno(op="expression", 
                                oper=
                                    None,
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="id", valor="y", linha=9),
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
                                NoInterno(op="outStatement", 
                                expression=
                                    NoInterno(op="expression", 
                                    oper=
                                        None,
                                    esq=
                                        NoInterno(op="sumExpression", 
                                        oper=
                                            "-",
                                        esq=
                                            NoInterno(op="factor", 
                                            sinal=
                                                "+",
                                            factor=
                                                NoFolha(op="id", valor="x", linha=10),
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
                                                NoFolha(op="num", valor="1", linha=10),
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
    )
)
*/