alg soma_dois
var
    x, y, result;
{
    x = in();
    y = in();
    result = x + y;
    out(result);
}

/*
Lista de tokens:
[Token("ALG", "alg", 1), Token("ID", "soma_dois", 1), Token("VAR", "var", 2), Token("ID", "x", 3), Token("COMMA", ",", 3), Token("ID", "y", 3), Token("COMMA", ",", 3),
Token("ID", "result", 3), Token("SEMICOLON", ";", 3), Token("LBLOCK", "{", 4), Token("ID", "x", 5), Token("ASSIGN", "=", 5), Token("IN", "in", 5), Token("LPAR", "(", 5),
Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ID", "y", 6), Token("ASSIGN", "=", 6), Token("IN", "in", 6), Token("LPAR", "(", 6), Token("RPAR", ")", 6),
Token("SEMICOLON", ";", 6), Token("ID", "result", 7), Token("ASSIGN", "=", 7), Token("ID", "x", 7), Token("OPSUM", "+", 7), Token("ID", "y", 7), Token("SEMICOLON", ";", 7),
Token("OUT", "out", 8), Token("LPAR", "(", 8), Token("ID", "result", 8), Token("RPAR", ")", 8), Token("SEMICOLON", ";", 8), Token("RBLOCK", "}", 9), Token("EOF", "EOF", 9)]
*/