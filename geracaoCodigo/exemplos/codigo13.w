alg exemplo13
var
	num x, y, z;
{
	x = in();
	y = 30;
	z = in();
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo13"
# Inicialização de variáveis
x = 0
y = 0
z = 0
# Início do código
x = int(input())
y = 30
z = int(input())
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo13", linha=1),
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
            inStatement=
                NoFolha(op="in", valor="in", linha=5)
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
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="num", valor="30", linha=6),
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
                        NoFolha(op="id", valor="z", linha=7),
                    inStatement=
                        NoFolha(op="in", valor="in", linha=7)
                    ),
                prox=
                    None
                )
            )
        )
    )
)
*/