alg soma_dois_com_mais_declaracoes
var
    num x, y, result;
    log a;
{
    x = in();
    y = in();
    result = x + y;
    out(result);
}

/*
Lista de tokens:
[Token("ALG", "alg", 1), Token("ID", "soma_dois_com_mais_declaracoes", 1), Token("VAR", "var", 2), Token("TYPE", "num", 3), Token("ID", "x", 3), Token("COMMA", ",", 3), Token("ID", "y", 3), Token("COMMA", ",", 3),
Token("ID", "result", 3), Token("SEMICOLON", ";", 3), Token("TYPE", "log", 4), Token("ID", "a", 4), Token("SEMICOLON", ";", 4), Token("LBLOCK", "{", 5), Token("ID", "x", 6), Token("ASSIGN", "=", 6),
Token("IN", "in", 6), Token("LPAR", "(", 6), Token("RPAR", ")", 6), Token("SEMICOLON", ";", 6), Token("ID", "y", 7), Token("ASSIGN", "=", 7), Token("IN", "in", 7), Token("LPAR", "(", 7),
Token("RPAR", ")", 7), Token("SEMICOLON", ";", 7), Token("ID", "result", 8), Token("ASSIGN", "=", 8), Token("ID", "x", 8), Token("OPSUM", "+", 8), Token("ID", "y", 8), Token("SEMICOLON", ";", 8),
Token("OUT", "out", 9), Token("LPAR", "(", 9), Token("ID", "result", 9), Token("RPAR", ")", 9), Token("SEMICOLON", ";", 9), Token("RBLOCK", "}", 10), Token("EOF", "EOF", 10)]
*/
