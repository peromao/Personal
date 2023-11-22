alg exemplo_if
var
{
	if true
		out(true);
	else
		out(false);
}

/*
Lista de tokens:
[Token("ALG", "alg", 1), Token("ID", "exemplo_if", 1), Token("VAR", "var", 2), Token("LBLOCK", "{", 3), Token("IF", "if", 4), Token("BOOLEAN", "true", 4),
Token("OUT", "out", 5), Token("LPAR", "(", 5), Token("BOOLEAN", "true", 5), Token("RPAR", ")", 5), Token("SEMICOLON", ";", 5), Token("ELSE", "else", 6),
Token("OUT", "out", 7), Token("LPAR", "(", 7), Token("BOOLEAN", "false", 7), Token("RPAR", ")", 7), Token("SEMICOLON", ";", 7), Token("RBLOCK", "}", 8), Token("EOF", "EOF", 14)]
*/