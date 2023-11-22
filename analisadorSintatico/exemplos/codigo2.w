alg exemplo_print
var
{
	out(1234);
}

/*
Lista de tokens:
[Token("ALG", "alg", 1), Token("ID", "exemplo_print", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("OUT", "out", 4), Token("LPAR", "(", 4),
Token("NUMBER", "1234", 4), Token("RPAR", ")", 4), Token("SEMICOLON", ";", 4), Token("RBLOCK", "}", 5), Token("EOF", "EOF", 5)]
*/