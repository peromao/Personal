alg exemplo10
implicit mod(256)
var
	num x;
{
	x = 267;
	out(x);
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo10"
# Inicialização de variáveis
x = 0
# Início do código
x = 267 % 256
print(x)
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo10", linha=1),
declarations=
    NoInterno(op="declarations", 
    mod=
        NoFolha(op="number", valor="256", linha=2),
    varDeclarationList=
        NoInterno(op="varDeclarationList", 
        varDeclaration=
            NoInterno(op="varDeclaration", 
            type=
                NoFolha(op="type", valor="num", linha=4),
            identifierList=
                NoInterno(op="identifierList", 
                id=
                    NoFolha(op="id", valor="x", linha=4),
                prox=
                    None
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
                        NoFolha(op="num", valor="267", linha=6),
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
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="id", valor="x", linha=7),
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
*/