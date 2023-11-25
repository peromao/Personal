alg exemplo9
var
	log acertou, encerrou, zerou;
	num x, y;
{
	x = 10;
	y = x + 1;
	acertou = true;
	pontuou = true;
	encerrou = false;
}


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
                NoFolha(op="type", valor="log", linha=3),
            identifierList=
                NoInterno(op="identifierList", 
                id=
                    NoFolha(op="id", valor="acertou", linha=3),
                prox=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="encerrou", linha=3),
                    prox=
                        NoInterno(op="identifierList", 
                        id=
                            NoFolha(op="id", valor="zerou", linha=3),
                        prox=
                            None
                        )
                    )
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
                        NoFolha(op="id", valor="x", linha=4),
                    prox=
                        NoInterno(op="identifierList", 
                        id=
                            NoFolha(op="id", valor="y", linha=4),
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
                        NoFolha(op="num", valor="10", linha=6),
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
                        NoInterno(op="sumExpression", 
                        oper=
                            "+",
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
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="num", valor="1", linha=7),
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
                        NoFolha(op="id", valor="acertou", linha=8),
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
                            NoFolha(op="id", valor="pontuou", linha=9),
                        expression=
                            NoInterno(op="expression", 
                            oper=
                                None,
                            esq=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="log", valor="true", linha=9),
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
                                NoFolha(op="id", valor="encerrou", linha=10),
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
                )
            )
        )
    )
)
*/