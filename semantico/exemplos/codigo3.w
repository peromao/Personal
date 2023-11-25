alg exemplo3
var
	log x, y;
{
	x = 3 < 5;
	y = 3 + 4 > 5 . 2;
}

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
                NoFolha(op="type", valor="log", linha=3),
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
                    "<",
                esq=
                    NoInterno(op="factor", 
                    sinal=
                        "+",
                    factor=
                        NoFolha(op="num", valor="3", linha=5),
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
                        NoFolha(op="num", valor="5", linha=5),
                    esq=
                        None,
                    dir=
                        None
                    )
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
                        ">",
                    esq=
                        NoInterno(op="sumExpression", 
                        oper=
                            "+",
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="num", valor="3", linha=6),
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
                                NoFolha(op="num", valor="4", linha=6),
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