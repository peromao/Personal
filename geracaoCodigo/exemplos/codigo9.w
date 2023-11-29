alg exemplo9
var
	num mdc;
	log resultado;
{
	mdc = 126 # 162 # 180;
	if mdc >= 18 {
		resultado = true;
	} else {
		resultado = false;
	}
	mdc = 2 ^ 7 # 2 ^ 8;
	mdc = 1.2 + 3.4;
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo9"
# Inicialização de variáveis
mdc = 0
resultado = False
# Início do código
_TEMP_VAR_MUL1 = math.gcd(126, 162)
_TEMP_VAR_MUL2 = math.gcd(_TEMP_VAR_MUL1, 180)
mdc = _TEMP_VAR_MUL2
_TEMP_VAR_REL = mdc >= 18
if _TEMP_VAR_REL:
    resultado = True
else:
    resultado = False
_TEMP_VAR_POW1 = 2 ** 7
_TEMP_VAR_POW2 = 2 ** 8
_TEMP_VAR_MUL1 = math.gcd(_TEMP_VAR_POW1, _TEMP_VAR_POW2)
mdc = _TEMP_VAR_MUL1
_TEMP_VAR_MUL1 = 1 * 2
_TEMP_VAR_MUL2 = 3 * 4
_TEMP_VAR_SUM1 = _TEMP_VAR_MUL1 + _TEMP_VAR_MUL2
mdc = _TEMP_VAR_SUM1
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo9", linha=1),
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
                    NoFolha(op="id", valor="mdc", linha=3),
                prox=
                    None
                )
            ),
        prox=
            NoInterno(op="varDeclarationList", 
            varDeclaration=
                NoInterno(op="varDeclaration", 
                type=
                    NoFolha(op="type", valor="log", linha=4),
                identifierList=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="resultado", linha=4),
                    prox=
                        None
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
                NoFolha(op="id", valor="mdc", linha=6),
            expression=
                NoInterno(op="expression", 
                oper=
                    None,
                esq=
                    NoInterno(op="multiplicativeTerm", 
                    oper=
                        "#",
                    esq=
                        NoInterno(op="multiplicativeTerm", 
                        oper=
                            "#",
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="num", valor="126", linha=6),
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
                                NoFolha(op="num", valor="162", linha=6),
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
                            NoFolha(op="num", valor="180", linha=6),
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
                NoInterno(op="ifStatement", 
                expression=
                    NoInterno(op="expression", 
                    oper=
                        ">=",
                    esq=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="id", valor="mdc", linha=7),
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
                blockIf=
                    NoInterno(op="block", 
                    statementList=
                        NoInterno(op="statementList", 
                        statement=
                            NoInterno(op="assignStatement", 
                            id=
                                NoFolha(op="id", valor="resultado", linha=8),
                            expression=
                                NoInterno(op="expression", 
                                oper=
                                    None,
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="log", valor="true", linha=8),
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
                            None
                        )
                    ),
                blockElse=
                    NoInterno(op="block", 
                    statementList=
                        NoInterno(op="statementList", 
                        statement=
                            NoInterno(op="assignStatement", 
                            id=
                                NoFolha(op="id", valor="resultado", linha=10),
                            expression=
                                NoInterno(op="expression", 
                                oper=
                                    None,
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="log", valor="false", linha=10),
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
                            None
                        )
                    )
                ),
            prox=
                NoInterno(op="statementList", 
                statement=
                    NoInterno(op="assignStatement", 
                    id=
                        NoFolha(op="id", valor="mdc", linha=12),
                    expression=
                        NoInterno(op="expression", 
                        oper=
                            None,
                        esq=
                            NoInterno(op="multiplicativeTerm", 
                            oper=
                                "#",
                            esq=
                                NoInterno(op="powerTerm", 
                                oper=
                                    "^",
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="num", valor="2", linha=12),
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
                                        NoFolha(op="num", valor="7", linha=12),
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
                                        NoFolha(op="num", valor="2", linha=12),
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
                                        NoFolha(op="num", valor="8", linha=12),
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
                            NoFolha(op="id", valor="mdc", linha=13),
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
                                            NoFolha(op="num", valor="1", linha=13),
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
                                            NoFolha(op="num", valor="2", linha=13),
                                        esq=
                                            None,
                                        dir=
                                            None
                                        )
                                    ),
                                dir=
                                    NoInterno(op="multiplicativeTerm", 
                                    oper=
                                        ".",
                                    esq=
                                        NoInterno(op="factor", 
                                        sinal=
                                            "+",
                                        factor=
                                            NoFolha(op="num", valor="3", linha=13),
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
                                            NoFolha(op="num", valor="4", linha=13),
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
                        None
                    )
                )
            )
        )
    )
)
*/