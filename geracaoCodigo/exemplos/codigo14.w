alg exemplo14
var
	num numero;
	log resultado;
{
	numero = in();
	if 2 | numero {
		resultado = true;
	} else {
		resultado = false;
		numero = in();
		if numero % 2 == 0 {
			resultado = true;
		}
	}
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo14"
# Inicialização de variáveis
numero = 0
resultado = False
# Início do código
numero = int(input())
_TEMP_VAR_MOD = numero % 2
_TEMP_VAR_REL = _TEMP_VAR_MOD == 0
if _TEMP_VAR_REL:
    resultado = True
else:
    resultado = False
    numero = int(input())
    _TEMP_VAR_MUL1 = numero % 2
    _TEMP_VAR_REL = _TEMP_VAR_MUL1 == 0
    if _TEMP_VAR_REL:
        resultado = True
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo14", linha=1),
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
                    NoFolha(op="id", valor="numero", linha=3),
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
                NoFolha(op="id", valor="numero", linha=6),
            inStatement=
                NoFolha(op="in", valor="in", linha=6)
            ),
        prox=
            NoInterno(op="statementList", 
            statement=
                NoInterno(op="ifStatement", 
                expression=
                    NoInterno(op="expression", 
                    oper=
                        "|",
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
                            NoFolha(op="id", valor="numero", linha=7),
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
                            NoInterno(op="statementList", 
                            statement=
                                NoInterno(op="assignStatement", 
                                id=
                                    NoFolha(op="id", valor="numero", linha=11),
                                inStatement=
                                    NoFolha(op="in", valor="in", linha=11)
                                ),
                            prox=
                                NoInterno(op="statementList", 
                                statement=
                                    NoInterno(op="ifStatement", 
                                    expression=
                                        NoInterno(op="expression", 
                                        oper=
                                            "==",
                                        esq=
                                            NoInterno(op="multiplicativeTerm", 
                                            oper=
                                                "%",
                                            esq=
                                                NoInterno(op="factor", 
                                                sinal=
                                                    "+",
                                                factor=
                                                    NoFolha(op="id", valor="numero", linha=12),
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
                                                    NoFolha(op="num", valor="2", linha=12),
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
                                                NoFolha(op="num", valor="0", linha=12),
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
                                                    NoFolha(op="id", valor="resultado", linha=13),
                                                expression=
                                                    NoInterno(op="expression", 
                                                    oper=
                                                        None,
                                                    esq=
                                                        NoInterno(op="factor", 
                                                        sinal=
                                                            "+",
                                                        factor=
                                                            NoFolha(op="log", valor="true", linha=13),
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
                                        None
                                    ),
                                prox=
                                    None
                                )
                            )
                        )
                    )
                ),
            prox=
                None
            )
        )
    )
)
*/