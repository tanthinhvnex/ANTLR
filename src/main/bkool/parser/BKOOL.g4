grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing Pascal 
// tokens For a number to be taken as "real" (or "floating point") format,
//  it must either have a decimal point, or use scientific notation.
//  For example, 1.0, 1e-12, 1.0e-12, 0.000000001 are all valid reals.
//  At least one digit must exist on either side of a decimal point.


program: EOF;

REAL: (INT DECIMAL) | (INT DECIMAL? EXP);
fragment INT: [0-9]+;
fragment DECIMAL: '.'[0-9]+;
fragment EXP: 'e''-'?[0-9]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;