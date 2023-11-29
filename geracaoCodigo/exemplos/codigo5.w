alg exemplo5
var
	num x, y;
{
	x = 1 + 2 + 3 - 4 - 5 + 6 + 7;
	y = 2 . 3 . 4 . 5 : 6;
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo5"
# Inicialização de variáveis
x = 0
y = 0
# Início do código
_TEMP_VAR_SUM1 = 1 + 2
_TEMP_VAR_SUM2 = _TEMP_VAR_SUM1 + 3
_TEMP_VAR_SUM3 = _TEMP_VAR_SUM2 - 4
_TEMP_VAR_SUM4 = _TEMP_VAR_SUM3 - 5
_TEMP_VAR_SUM5 = _TEMP_VAR_SUM4 + 6
_TEMP_VAR_SUM6 = _TEMP_VAR_SUM5 + 7
x = _TEMP_VAR_SUM6
_TEMP_VAR_MUL1 = 2 * 3
_TEMP_VAR_MUL2 = _TEMP_VAR_MUL1 * 4
_TEMP_VAR_MUL3 = _TEMP_VAR_MUL2 * 5
_TEMP_VAR_MUL4 = _TEMP_VAR_MUL3 // 6
y = _TEMP_VAR_MUL4
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo5", linha=1),
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
                NoFolha(op="id", valor="x", linha=5),
            expression=
                NoInterno(op="expression", 
                oper=
                    None,
                esq=
                    NoInterno(op="sumExpression", 
                    oper=
                        "+",
                    esq=
                        NoInterno(op="sumExpression", 
                        oper=
                            "+",
                        esq=
                            NoInterno(op="sumExpression", 
                            oper=
                                "-",
                            esq=
                                NoInterno(op="sumExpression", 
                                oper=
                                    "-",
                                esq=
                                    NoInterno(op="sumExpression", 
                                    oper=
                                        "+",
                                    esq=
                                        NoInterno(op="sumExpression", 
                                        oper=
                                            "+",
                                        esq=
                                            NoInterno(op="factor", 
                                            sinal=
                                                "+",
                                            factor=
                                                NoFolha(op="num", valor="1", linha=5),
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
                                                NoFolha(op="num", valor="2", linha=5),
                                            esq=
                                                None,
                                            dir=
                                                None
                                            )
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
                                    ),
                                dir=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="num", valor="4", linha=5),
                                    esq=
                                        None,
                                    dir=
                                        None
                                    )
                                ),
                            dir=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="num", valor="5", linha=5),
                                esq=
                                    None,
                                dir=
                                    None
                                )
                            ),
                        dir=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="num", valor="6", linha=5),
                            esq=
                                None,
                            dir=
                                None
                            )
                        ),
                    dir=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="num", valor="7", linha=5),
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
                    NoFolha(op="id", valor="y", linha=6),
                expression=
                    NoInterno(op="expression", 
                    oper=
                        None,
                    esq=
                        NoInterno(op="multiplicativeTerm", 
                        oper=
                            ":",
                        esq=
                            NoInterno(op="multiplicativeTerm", 
                            oper=
                                ".",
                            esq=
                                NoInterno(op="multiplicativeTerm", 
                                oper=
                                    ".",
                                esq=
                                    NoInterno(op="multiplicativeTerm", 
                                    oper=
                                        ".",
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
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="num", valor="5", linha=6),
                                esq=
                                    None,
                                dir=
                                    None
                                )
                            ),
                        dir=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="num", valor="6", linha=6),
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
*/