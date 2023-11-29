alg exemplo7
var
	log result;
	num k, j;
{
	k = 1 + (2 + 3) . 4 - (9 : 3);
	j = (10 . 18) : 9;
	result = j == (k+2);
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo7"
# Inicialização de variáveis
result = False
k = 0
j = 0
# Início do código
_TEMP_VAR_SUM1 = 2 + 3
_TEMP_VAR_MUL1 = _TEMP_VAR_SUM1 * 4
_TEMP_VAR_SUM2 = 1 + _TEMP_VAR_MUL1
_TEMP_VAR_MUL2 = 9 // 3
_TEMP_VAR_SUM3 = _TEMP_VAR_SUM2 - _TEMP_VAR_MUL2
k = _TEMP_VAR_SUM3
_TEMP_VAR_MUL1 = 10 * 18
_TEMP_VAR_MUL2 = _TEMP_VAR_MUL1 // 9
j = _TEMP_VAR_MUL2
_TEMP_VAR_SUM1 = k + 2
_TEMP_VAR_REL = j == _TEMP_VAR_SUM1
result = _TEMP_VAR_REL
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo7", linha=1),
declarations=
    NoInterno(op="declarations", 
    mod=
        NoFolha(op="number", valor="0", linha=0),
    varDeclarationList=
        NoInterno(op="varDeclarationList", 
        varDeclaration=
            NoInterno(op="varDeclaration", 
            type=
                NoFolha(op="type", valor="log", linha=3),
            identifierList=
                NoInterno(op="identifierList", 
                id=
                    NoFolha(op="id", valor="result", linha=3),
                prox=
                    None
                )
            ),
        prox=
            NoInterno(op="varDeclarationList", 
            varDeclaration=
                NoInterno(op="varDeclaration", 
                type=
                    NoFolha(op="type", valor="num", linha=4),
                identifierList=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="k", linha=4),
                    prox=
                        NoInterno(op="identifierList", 
                        id=
                            NoFolha(op="id", valor="j", linha=4),
                        prox=
                            None
                        )
                    )
                ),
            prox=
                None
            )
        )
    ),
block=
    NoInterno(op="block", 
    statementList=
        NoInterno(op="statementList", 
        statement=
            NoInterno(op="assignStatement", 
            id=
                NoFolha(op="id", valor="k", linha=6),
            expression=
                NoInterno(op="expression", 
                oper=
                    None,
                esq=
                    NoInterno(op="sumExpression", 
                    oper=
                        "-",
                    esq=
                        NoInterno(op="sumExpression", 
                        oper=
                            "+",
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="num", valor="1", linha=6),
                            esq=
                                None,
                            dir=
                                None
                            ),
                        dir=
                            NoInterno(op="multiplicativeTerm", 
                            oper=
                                ".",
                            esq=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
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
                                                NoFolha(op="num", valor="2", linha=6),
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
                                                NoFolha(op="num", valor="3", linha=6),
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
                                    NoFolha(op="num", valor="4", linha=6),
                                esq=
                                    None,
                                dir=
                                    None
                                )
                            )
                        ),
                    dir=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        expression=
                            NoInterno(op="expression", 
                            oper=
                                None,
                            esq=
                                NoInterno(op="multiplicativeTerm", 
                                oper=
                                    ":",
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="num", valor="9", linha=6),
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
                                        NoFolha(op="num", valor="3", linha=6),
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
                    NoFolha(op="id", valor="j", linha=7),
                expression=
                    NoInterno(op="expression", 
                    oper=
                        None,
                    esq=
                        NoInterno(op="multiplicativeTerm", 
                        oper=
                            ":",
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
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
                                            NoFolha(op="num", valor="10", linha=7),
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
                                            NoFolha(op="num", valor="18", linha=7),
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
                                NoFolha(op="num", valor="9", linha=7),
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
                        NoFolha(op="id", valor="result", linha=8),
                    expression=
                        NoInterno(op="expression", 
                        oper=
                            "==",
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="id", valor="j", linha=8),
                            esq=
                                None,
                            dir=
                                None
                            ),
                        dir=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
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
                                            NoFolha(op="id", valor="k", linha=8),
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
                                ),
                            esq=
                                None,
                            dir=
                                None
                            )
                        )
                    ),
                prox=
                    None
                )
            )
        )
    )
)
*/