alg exemplo17
implicit mod(257)
var
	num resultado1, resultado2;
{
	resultado1 = 2 ^ 7;
	resultado2 = 2 ^ -7;
	if resultado1 > resultado2 {
		out(resultado1);
	} else {
		out(resultado2);
	}
}

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo17", linha=1),
declarations=
    NoInterno(op="declarations", 
    mod=
        NoFolha(op="number", valor="257", linha=2),
    varDeclarationList=
        NoInterno(op="varDeclarationList", 
        varDeclaration=
            NoInterno(op="varDeclaration", 
            type=
                NoFolha(op="type", valor="num", linha=4),
            identifierList=
                NoInterno(op="identifierList", 
                id=
                    NoFolha(op="id", valor="resultado1", linha=4),
                prox=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="resultado2", linha=4),
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
                NoFolha(op="id", valor="resultado1", linha=6),
            expression=
                NoInterno(op="expression", 
                oper=
                    None,
                esq=
                    NoInterno(op="powerTerm", 
                    oper=
                        "^",
                    esq=
                        NoInterno(op="factor", 
                        sinal=
                            "+",
                        factor=
                            NoFolha(op="num", valor="2", linha=6),
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
                            NoFolha(op="num", valor="7", linha=6),
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
                    NoFolha(op="id", valor="resultado2", linha=7),
                expression=
                    NoInterno(op="expression", 
                    oper=
                        None,
                    esq=
                        NoInterno(op="powerTerm", 
                        oper=
                            "^",
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
                                "-",
                            factor=
                                NoFolha(op="num", valor="7", linha=7),
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
                            ">",
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="id", valor="resultado1", linha=8),
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
                                NoFolha(op="id", valor="resultado2", linha=8),
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
                                            NoFolha(op="id", valor="resultado1", linha=9),
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
                                            NoFolha(op="id", valor="resultado2", linha=11),
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
                    None
                )
            )
        )
    )
)
*/