grammar CX;


program: statement*;

statement
: SEMICOLON
| BREAK SEMICOLON
| CONTINUE SEMICOLON
| RETURN (expression|VOID)?
| expression SEMICOLON
| IF LPAREN expression RPAREN statement (ELSE statement)?
| LBRACE statement* RBRACE
| WHILE LPAREN expression RPAREN statement
| FOR LPAREN expression? SEMICOLON expression? SEMICOLON expression? RPAREN statement
| basetype ID LPAREN (VOID|basetype ID? (COMMA basetype ID?)*)? RPAREN (SEMICOLON|LBRACE statement* RBRACE)
;


expression
: TRUE|FALSE|NUM
| ID LPAREN (expression (COMMA expression)*)? RPAREN
| variable ASSIGN expression
| variable
| basetype ID (COMMA ID)+ (ASSIGN expression)?
| (MINUS|NOT|AMPERSAND|STAR) expression|variable
| LPAREN expression RPAREN
| expression (EQUAL|NOTEQUAL|GREATERTHAN|LESSTHAN|LESSTHANOREQUAL|GREATERTHANOREQUAL) expression
| expression (AND|OR) expression
| expression LSQUAREBRACKET expression RSQUAREBRACKET
| variable (PLUS PLUS|MINUS MINUS)
| expression (STAR|SLASH) expression
| expression (PLUS|MINUS) expression
;

// variable only support identifier
variable: ID;


basetype
: CONST basetype
| (VOID|ID)
;


// the reserved keywords/tokens for this compiler
AMPERSAND: '&';
AND: '&&';
ASSIGN: '=';
BEGINCOMMENT: '/*';
BEGININLINECOMMENT: '//';
BREAK: 'break';
COMMA: ',';
CONST: 'const';
CONTINUE: 'continue';
DQUOTE: '"';
DOT: '.';
ELSE: 'else';
ENDCOMMENT: '*/';
EQUAL: '==';
FOR: 'for';
GREATERTHAN: '>';
GREATERTHANOREQUAL: '>=';
IF: 'if';
INCLUDE: '#include';
LBRACE: '{';
LESSTHAN: '<';
LESSTHANOREQUAL: '<=';
LPAREN: '(';
LSQUAREBRACKET: '[';
MINUS: '-';
NOT: '!';
NOTEQUAL: '!=';
OR: '||';
PLUS: '+';
RBRACE: '}';
RETURN: 'return';
RPAREN: ')';
RSQUAREBRACKET: ']';
SEMICOLON: ';';
SLASH: '/';
SQUOTE: '\'';
STAR: '*';
TYPEDEF: 'typedef';
VOID: 'void';
WHILE: 'while';

// only support bool and int
TRUE: 'true';
FALSE: 'false';
NUM: INT;
INT: '0' | [1-9][0-9]*;


// A legal CX identifier begins with a letter from the alphabet
// and may be followed by alphanumeric characters, including the underscore.
ID: [a-zA-Z][a-zA-Z0-9]*;

// Skip comments /* to start and */ to end the comments
COMMENT: BEGINCOMMENT .*? ENDCOMMENT  -> skip;

WHITESPACE: (' '|'\t')+ -> skip;
NEWLINE: '\r'? '\n'  -> skip;