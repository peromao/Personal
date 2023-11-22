alg testa_expressoes
var
	num x, y;
{
	x = (16 # 10) + 3 . (27 : 9);
	y = 2 ^ 3 ^ 4 - x;
	if x > y {
		out(x);
	} else {
		if x == y {
			out(x);
			out(y);
		} else {
			out(y);
		}
	}
}

/*
Lista de tokens:
[Token("ALG", "alg", 1), Token("ID", "testa_expressoes", 1), Token("VAR", "var", 2), Token("TYPE", "num", 3), Token("ID", "x", 3), Token("COMMA", ",", 3),
Token("ID", "y", 3), Token("SEMICOLON", ";", 3), Token("LBLOCK", "{", 4), Token("ID", "x", 5), Token("ASSIGN", "=", 5), Token("LPAR", "(", 5), Token("NUMBER", "16", 5),
Token("OPMUL", "#", 5), Token("NUMBER", "10", 5), Token("RPAR", ")", 5), Token("OPSUM", "+", 5), Token("NUMBER", "3", 5), Token("OPMUL", ".", 5), Token("LPAR", "(", 5),
Token("NUMBER", "27", 5), Token("OPMUL", ":", 5), Token("NUMBER", "9", 5), Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ID", "y", 6), Token("ASSIGN", "=", 6),
Token("NUMBER", "2", 6), Token("OPPOW", "^", 6), Token("NUMBER", "3", 6), Token("OPPOW", "^", 6), Token("NUMBER", "4", 6), Token("OPSUM", "-", 6), Token("ID", "x", 6),
Token("SEMICOLON", ";", 6), Token("IF", "if", 7), Token("ID", "x", 7), Token("OPREL", ">", 7), Token("ID", "y", 7), Token("LBLOCK", "{", 7), Token("OUT", "out", 8),
Token("LPAR", "(", 8), Token("ID", "x", 8), Token("RPAR", ")", 8), Token("SEMICOLON", ";", 8), Token("RBLOCK", "}", 9), Token("ELSE", "else", 9), Token("LBLOCK", "{", 9),
Token("IF", "if", 10), Token("ID", "x", 10), Token("OPREL", "==", 10), Token("ID", "y", 10), Token("LBLOCK", "{", 10), Token("OUT", "out", 11), Token("LPAR", "(", 11),
Token("ID", "x", 11), Token("RPAR", ")", 11), Token("SEMICOLON", ";", 11), Token("OUT", "out", 12), Token("LPAR", "(", 12), Token("ID", "y", 12), Token("RPAR", ")", 12),
Token("SEMICOLON", ";", 12), Token("RBLOCK", "}", 13), Token("ELSE", "else", 13), Token("LBLOCK", "{", 13), Token("OUT", "out", 14), Token("LPAR", "(", 14), Token("ID", "y", 14),
Token("RPAR", ")", 14), Token("SEMICOLON", ";", 14), Token("RBLOCK", "}", 15), Token("RBLOCK", "}", 16), Token("RBLOCK", "}", 17), Token("EOF", "EOF", 17)]
*/