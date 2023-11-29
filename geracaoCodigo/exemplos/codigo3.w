alg exemplo3
var
	num valor1, valor2;
{
	valor1 = 1 + 2;
	valor2 = 1 - 2;
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo3"
# Inicialização de variáveis
valor1 = 0
valor2 = 0
# Início do código
_TEMP_VAR_SUM1 = 1 + 2
valor1 = _TEMP_VAR_SUM1
_TEMP_VAR_SUM1 = 1 - 2
valor2 = _TEMP_VAR_SUM1
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo3", linha=1),
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
                        NoInterno(op="sumExpression", 
                        oper=
                            "-",
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