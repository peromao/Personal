alg exemplo2
var
	num x, y;
	log a, b;
{
	x = 1;
	y = 2;
	a = true;
	b = false;
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo2"
# Inicialização de variáveis
x = 0
y = 0
a = False
b = False
# Início do código
x = 1
y = 2
a = True
b = False
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo2", linha=1),
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
            NoInterno(op="varDeclarationList", 
            varDeclaration=
                NoInterno(op="varDeclaration", 
                type=
                    NoFolha(op="type", valor="log", linha=4),
                identifierList=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="a", linha=4),
                    prox=
                        NoInterno(op="identifierList", 
                        id=
                            NoFolha(op="id", valor="b", linha=4),
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
                NoFolha(op="id", valor="x", linha=6),
            expression=
                NoInterno(op="expression", 
                oper=
                    None,
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
                    None
                )
            ),
        prox=
            NoInterno(op="statementList", 
            statement=
                NoInterno(op="assignStatement", 
                id=
                    NoFolha(op="id", valor="y", linha=7),
                expression=
                    NoInterno(op="expression", 
                    oper=
                        None,
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
                        None
                    )
                ),
            prox=
                NoInterno(op="statementList", 
                statement=
                    NoInterno(op="assignStatement", 
                    id=
                        NoFolha(op="id", valor="a", linha=8),
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
                    NoInterno(op="statementList", 
                    statement=
                        NoInterno(op="assignStatement", 
                        id=
                            NoFolha(op="id", valor="b", linha=9),
                        expression=
                            NoInterno(op="expression", 
                            oper=
                                None,
                            esq=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="log", valor="false", linha=9),
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
            )
        )
    )
)
*/