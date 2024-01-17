grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.


program: EOF;

INT: '0' | [1-9][_0-9]*('_'[0-9]+)* {self.text = self.text.replace('_','')};


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;