alg exemplo16
var
	num i, j;
	log multiplo;
{
	i = 10 ^ 3;
	j = in();
	multiplo = false;
	if (i : 0) % j == 0 {
		multiplo = true;
	}
	out(multiplo);
}

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo16", linha=1),
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
                    NoFolha(op="id", valor="i", linha=3),
                prox=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="j", linha=3),
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
                        NoFolha(op="id", valor="multiplo", linha=4),
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
                NoFolha(op="id", valor="i", linha=6),
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
                            NoFolha(op="num", valor="10", linha=6),
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
                            NoFolha(op="num", valor="3", linha=6),
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
                    NoFolha(op="id", valor="j", linha=7),
                inStatement=
                    NoFolha(op="in", valor="in", linha=7)
                ),
            prox=
                NoInterno(op="statementList", 
                statement=
                    NoInterno(op="assignStatement", 
                    id=
                        NoFolha(op="id", valor="multiplo", linha=8),
                    expression=
                        NoInterno(op="expression", 
                        oper=
                            None,
                        esq=
                            NoInterno(op="factor", 
                            sinal=
                                "+",
                            factor=
                                NoFolha(op="log", valor="false", linha=8),
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
                                                    NoFolha(op="id", valor="i", linha=9),
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
                                                    NoFolha(op="num", valor="0", linha=9),
                                                esq=
                                                    None,
                                                dir=
                                                    None
                                                )
                                            ),
                                        dir=
                                            None
                                        ),
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
                                        NoFolha(op="id", valor="j", linha=9),
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
                                    NoFolha(op="num", valor="0", linha=9),
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
                                        NoFolha(op="id", valor="multiplo", linha=10),
                                    expression=
                                        NoInterno(op="expression", 
                                        oper=
                                            None,
                                        esq=
                                            NoInterno(op="factor", 
                                            sinal=
                                                "+",
                                            factor=
                                                NoFolha(op="log", valor="true", linha=10),
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
                                        NoFolha(op="id", valor="multiplo", linha=12),
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