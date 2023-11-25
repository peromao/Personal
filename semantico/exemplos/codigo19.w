alg exemplo19
var
	num a, b, c, d;
	log x, y;
{
	a = 2 ^ 5;
	b = a : 2 + 2;
	c = (b + 2) . a;
	d = 2 ^ 3 ^ 4;
	if c | d {
		x = a > b;
		out(x);
	} else {
		y = b . c;
		out(y);
	}
}

/*
// Árvore sintática:

NoInterno(op="alg", 
id=
    NoFolha(op="id", valor="exemplo19", linha=1),
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
                    NoFolha(op="id", valor="a", linha=3),
                prox=
                    NoInterno(op="identifierList", 
                    id=
                        NoFolha(op="id", valor="b", linha=3),
                    prox=
                        NoInterno(op="identifierList", 
                        id=
                            NoFolha(op="id", valor="c", linha=3),
                        prox=
                            NoInterno(op="identifierList", 
                            id=
                                NoFolha(op="id", valor="d", linha=3),
                            prox=
                                None
                            )
                        )
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
                NoFolha(op="id", valor="a", linha=6),
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
                            NoFolha(op="num", valor="5", linha=6),
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
                    NoFolha(op="id", valor="b", linha=7),
                expression=
                    NoInterno(op="expression", 
                    oper=
                        None,
                    esq=
                        NoInterno(op="sumExpression", 
                        oper=
                            "+",
                        esq=
                            NoInterno(op="multiplicativeTerm", 
                            oper=
                                ":",
                            esq=
                                NoInterno(op="factor", 
                                sinal=
                                    "+",
                                factor=
                                    NoFolha(op="id", valor="a", linha=7),
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
                                    NoFolha(op="num", valor="2", linha=7),
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
                                NoFolha(op="num", valor="2", linha=7),
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
                        NoFolha(op="id", valor="c", linha=8),
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
                                                NoFolha(op="id", valor="b", linha=8),
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
                                                NoFolha(op="num", valor="2", linha=8),
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
                                    NoFolha(op="id", valor="a", linha=8),
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
                            NoFolha(op="id", valor="d", linha=9),
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
                                        NoFolha(op="num", valor="2", linha=9),
                                    esq=
                                        None,
                                    dir=
                                        None
                                    ),
                                dir=
                                    NoInterno(op="powerTerm", 
                                    oper=
                                        "^",
                                    esq=
                                        NoInterno(op="factor", 
                                        sinal=
                                            "+",
                                        factor=
                                            NoFolha(op="num", valor="3", linha=9),
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
                                            NoFolha(op="num", valor="4", linha=9),
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
                        NoInterno(op="statementList", 
                        statement=
                            NoInterno(op="ifStatement", 
                            expression=
                                NoInterno(op="expression", 
                                oper=
                                    "|",
                                esq=
                                    NoInterno(op="factor", 
                                    sinal=
                                        "+",
                                    factor=
                                        NoFolha(op="id", valor="c", linha=10),
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
                                        NoFolha(op="id", valor="d", linha=10),
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
                                            NoFolha(op="id", valor="x", linha=11),
                                        expression=
                                            NoInterno(op="expression", 
                                            oper=
                                                ">",
                                            esq=
                                                NoInterno(op="factor", 
                                                sinal=
                                                    "+",
                                                factor=
                                                    NoFolha(op="id", valor="a", linha=11),
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
                                                    NoFolha(op="id", valor="b", linha=11),
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
                                                        NoFolha(op="id", valor="x", linha=12),
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
                            blockElse=
                                NoInterno(op="block", 
                                statementList=
                                    NoInterno(op="statementList", 
                                    statement=
                                        NoInterno(op="assignStatement", 
                                        id=
                                            NoFolha(op="id", valor="y", linha=14),
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
                                                        NoFolha(op="id", valor="b", linha=14),
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
                                                        NoFolha(op="id", valor="c", linha=14),
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
                                                    NoInterno(op="factor", 
                                                    sinal=
                                                        "+",
                                                    factor=
                                                        NoFolha(op="id", valor="y", linha=15),
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