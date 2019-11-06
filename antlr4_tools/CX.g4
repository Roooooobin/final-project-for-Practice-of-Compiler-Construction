grammar CX;
program: statement*;

statement
: expressionstatement
| compoundstatement
| selectionstatement
| iterationstatement
| BREAK SEMICOLON
| CONTINUE SEMICOLON
| WRITE expression SEMICOLON
| WRITELN expression SEMICOLON
| basetype IDENTIFIER (ASSIGN expression)? SEMICOLON
;

compoundstatement: LEFTBRACE statement* RIGHTBRACE;

expressionstatement: expression? SEMICOLON;

selectionstatement: IF LEFTPARENTHESIS expression RIGHTPARENTHESIS statement (ELSE statement)?;

iterationstatement
: WHILE LEFTPARENTHESIS expression RIGHTPARENTHESIS statement
| FOR LEFTPARENTHESIS expression? SEMICOLON expression? SEMICOLON expression? RIGHTPARENTHESIS statement
| DO statement WHILE LEFTPARENTHESIS expression RIGHTPARENTHESIS SEMICOLON
| REPEAT statement UNTIL LEFTPARENTHESIS expression RIGHTPARENTHESIS SEMICOLON 
;

expression
: assignmentexpression
;

assignmentexpression
: conditionalexpression
| IDENTIFIER ASSIGN expression
;

conditionalexpression
: logicorexpression
;

logicorexpression
: logicandexpression
| logicorexpression OR logicandexpression
;

logicandexpression
: logicxorexpression
| logicandexpression AND logicxorexpression
;

logicxorexpression
: equalityexpression
| logicxorexpression XOR equalityexpression
;

equalityexpression
: comparisonexpression
| equalityexpression EQUAL comparisonexpression
| equalityexpression NOTEQUAL comparisonexpression
;

comparisonexpression
: additiveexpression
| comparisonexpression LESSTHAN additiveexpression
| comparisonexpression GREATERTHAN additiveexpression
| comparisonexpression LESSTHANOREQUAL additiveexpression
| comparisonexpression GREATERTHANOREQUAL additiveexpression
;

additiveexpression
: multiplicativeexpression
| additiveexpression PLUS multiplicativeexpression
| additiveexpression MINUS multiplicativeexpression
;

multiplicativeexpression
: castexpression
| multiplicativeexpression STAR castexpression
| multiplicativeexpression SLASH castexpression
| multiplicativeexpression MOD castexpression
;

castexpression
: postfixexpression
| LEFTPARENTHESIS (INT | REAL) RIGHTPARENTHESIS expression
;

postfixexpression
: unaryexpression
| postfixexpression PLUSPLUS
| postfixexpression MINUSMINUS
;

unaryexpression
: primaryexpression
| (NOT | MINUS | ODD) unaryexpression
;

primaryexpression
: IDENTIFIER
| constant
| LEFTPARENTHESIS expression RIGHTPARENTHESIS
;

constant: TRUE | FALSE | NUMBER | REALNUMBER;

basetype
: INT | BOOLEAN | REAL
;


COMMENT
: (BEGININLINECOMMENT .*? NEWLINE
| BEGINCOMMENT .*? ENDCOMMENT) -> skip
;

WHITESPACE: (' '|'\t')+ -> skip;
NEWLINE: '\r'? '\n' -> skip;

WRITE: 'write';
WRITELN: 'writeln';
INT: 'int';
BOOLEAN: 'bool';
LEFTBRACE: '{';
RIGHTBRACE: '}';
SEMICOLON: ';';
IF: 'if';
DO: 'do';
LEFTPARENTHESIS: '(';
RIGHTPARENTHESIS: ')';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
TRUE: 'true';
FALSE: 'false';
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
EQUAL: '==';
NOTEQUAL: '!=';
LESSTHAN: '<';
GREATERTHAN: '>';
LESSTHANOREQUAL: '<=';
GREATERTHANOREQUAL: '>=';
NOT: '!';
AND: '&&';
OR: '||';
XOR: '^';
BEGININLINECOMMENT: '//';
BEGINCOMMENT: '/*';
ENDCOMMENT: '*/';
COMMA: ',';
LEFTSHIFT: '<<';
RIGHTSHIFT: '>>';
QUESTIONMARK: '?';
NUMBER: '0' | [1-9][0-9]*;
REALNUMBER: [1-9][0-9]*'.'[0-9]+;
COLON: ':';
MOD: '%';
ODD: 'odd';
PLUSPLUS: '++';
MINUSMINUS: '--';
CONST: 'const';
BREAK: 'break';
CONTINUE: 'continue';
REPEAT: 'repeat';
UNTIL: 'until';
REAL: 'real';
IDENTIFIER: ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;
