alg exemplo4
var
	num valor1, valor2;
{
	valor1 = 5 . 4;
	valor2 = 5 : 2;
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo4"
# Inicialização de variáveis
valor1 = 0
valor2 = 0
# Início do código
_TEMP_VAR_MUL1 = 5 * 4
valor1 = _TEMP_VAR_MUL1
_TEMP_VAR_MUL1 = 5 // 2
valor2 = _TEMP_VAR_MUL1
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo4", linha=1),
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
                    NoFolha(op="id", valor="valor1", linha=3),
                prox=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="valor2", linha=3),
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
                NoFolha(op="id", valor="valor1", linha=5),
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
                            NoFolha(op="num", valor="4", linha=5),
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
                    NoFolha(op="id", valor="valor2", linha=6),
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
                                NoFolha(op="num", valor="5", linha=6),
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
                None
            )
        )
    )
)
*/