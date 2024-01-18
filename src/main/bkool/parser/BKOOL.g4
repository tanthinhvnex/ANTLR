grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing a Pascal identifier 
// that must begin with a lowercase letter (’a’ to ’z’),
//  but may continue with many characters
//  which are lowercase letter or digit (’0’ to ’9’).


program: EOF;

Iden: [a-z][a-z0-9]*;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;