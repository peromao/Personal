alg programa_com_uma_variavel
var
	log a
{
	a = true;
	a = false;
}

/*
Lista de tokens:
[Token("ALG", "alg", 1), Token("ID", "programa_com_uma_variavel", 1), Token("VAR", "var", 2), Token("TYPE", "log", 3), Token("ID", "a", 3), Token("LBLOCK", "{", 4),
Token("ID", "a", 5), Token("ASSIGN", "=", 5), Token("BOOLEAN", "true", 5), Token("SEMICOLON", ";", 5), Token("ID", "a", 6), Token("ASSIGN", "=", 6), Token("BOOLEAN", "false", 6),
Token("SEMICOLON", ";", 6), Token("RBLOCK", "}", 7), Token("EOF", "EOF", 7)]
*/