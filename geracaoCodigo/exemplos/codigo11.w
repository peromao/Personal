alg exemplo11
var
{
	out(3000 # 2000);
	out(1 + 2 . 3);
}

/*
// Sugestão de código Python que deve ser gerado:

import math

# Código gerado a partir do programa "exemplo11"
# Inicialização de variáveis
# Início do código
_TEMP_VAR_MUL1 = math.gcd(3000, 2000)
print(_TEMP_VAR_MUL1)
_TEMP_VAR_MUL1 = 2 * 3
_TEMP_VAR_SUM1 = 1 + _TEMP_VAR_MUL1
print(_TEMP_VAR_SUM1)
*/

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo11", linha=1),
declarations=
    NoInterno(op="declarations", 
    mod=
        NoFolha(op="number", valor="0", linha=0),
    varDeclarationList=
        None
    ),
block=
    NoInterno(op="block", 
    statementList=
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
                        "#",
                    esq=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="num", valor="3000", linha=4),
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
                            NoFolha(op="num", valor="2000", linha=4),
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
                            NoInterno(op="multiplicativeTerm", 
                            oper=
                                ".",
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
                None
            )
        )
    )
)
*/