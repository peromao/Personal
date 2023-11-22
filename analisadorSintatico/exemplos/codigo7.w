alg relogio
implicit mod(24)
var
    num hora1;
    num hora2, hora3;
    log virou;
{
    hora1 = 15;
    hora2 = in();
    hora3 = hora1 + hora2;
    virou = hora3 <= 15;
    if virou {
        out(virou);
        out(hora3);
    } else {
        out(hora3);
    }
}

/*
Lista de tokens:
[Token("ALG", "alg", 1), Token("ID", "relogio", 1), Token("IMPLICIT", "implicit", 2), Token("MOD", "mod", 2), Token("LPAR", "(", 2), Token("NUMBER", "24", 2),
Token("RPAR", ")", 2), Token("VAR", "var", 3), Token("TYPE", "num", 4), Token("ID", "hora1", 4), Token("SEMICOLON", ";", 4), Token("TYPE", "num", 5),
Token("ID", "hora2", 5), Token("COMMA", ",", 5), Token("ID", "hora3", 5), Token("SEMICOLON", ";", 5), Token("TYPE", "log", 6), Token("ID", "virou", 6),
Token("SEMICOLON", ";", 6), Token("LBLOCK", "{", 7), Token("ID", "hora1", 8), Token("ASSIGN", "=", 8), Token("NUMBER", "15", 8), Token("SEMICOLON", ";", 8),
Token("ID", "hora2", 9), Token("ASSIGN", "=", 9), Token("IN", "in", 9), Token("LPAR", "(", 9), Token("RPAR", ")", 9), Token("SEMICOLON", ";", 9),
Token("ID", "hora3", 10), Token("ASSIGN", "=", 10), Token("ID", "hora1", 10), Token("OPSUM", "+", 10), Token("ID", "hora2", 10), Token("SEMICOLON", ";", 10),
Token("ID", "virou", 11), Token("ASSIGN", "=", 11), Token("ID", "hora3", 11), Token("OPREL", "<=", 11), Token("NUMBER", "15", 11), Token("SEMICOLON", ";", 11),
Token("IF", "if", 12), Token("ID", "virou", 12), Token("LBLOCK", "{", 12), Token("OUT", "out", 13), Token("LPAR", "(", 13), Token("ID", "virou", 13),
Token("RPAR", ")", 13), Token("SEMICOLON", ";", 13), Token("OUT", "out", 14), Token("LPAR", "(", 14), Token("ID", "hora3", 14), Token("RPAR", ")", 14),
Token("SEMICOLON", ";", 14), Token("RBLOCK", "}", 15), Token("ELSE", "else", 15), Token("LBLOCK", "{", 15), Token("OUT", "out", 16), Token("LPAR", "(", 16),
Token("ID", "hora3", 16), Token("RPAR", ")", 16), Token("SEMICOLON", ";", 16), Token("RBLOCK", "}", 17), Token("RBLOCK", "}", 18), Token("EOF", "EOF", 18)]
*/