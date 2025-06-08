grammar DeepLearningDSL;

// Regla inicial
program: statement_list EOF;

statement_list: statement statement_list | ;

statement: assignment semicolon_opt
         | conditional 
         | loop
         | function_def
         | function_call semicolon_opt
         | expression semicolon_opt
         ;

// Hacer semicolon opcional (como en Python)
semicolon_opt: SEMICOLON | /* empty */ ;

// Assignments
assignment: ID ASSIGN expression ;

// Expressions con precedencia eliminando recursión izquierda
expression: term expr_rest ;
expr_rest: PLUS term expr_rest | MINUS term expr_rest | ;

term: factor term_rest ;
term_rest: MULT factor term_rest | DIV factor term_rest | MOD factor term_rest | ;

factor: base factor_rest ;
factor_rest: POWER base factor_rest | ;

// CORREGIDO: function_call ANTES de ID para resolver ambigüedad
base: function_call              // ← MOVIDO AQUÍ PRIMERO
    | ID
    | NUMBER
    | FLOAT
    | STRING
    | LPAREN expression RPAREN
    | list_or_matrix_expr
    | unary_expr
    ;

unary_expr: MINUS base | trig_func LPAREN expression RPAREN ;

trig_func: SIN | COS | TAN | SQRT ;

// Lista o matriz (auto-detectado por el intérprete)
list_or_matrix_expr: LBRACKET list_or_matrix_content RBRACKET
                   | matrix_operation
                   ;

list_or_matrix_content: list_or_matrix_row list_or_matrix_content_rest 
                      | /* empty para listas vacías */
                      ;

list_or_matrix_content_rest: COMMA list_or_matrix_row list_or_matrix_content_rest 
                           | /* empty */
                           ;

// Una fila puede ser: [1, 2, 3] o [[1, 2], [3, 4]]
list_or_matrix_row: LBRACKET expression_list RBRACKET  // Fila de matriz [[1, 2]]
                  | expression                          // Elemento simple [1, 2, 3]
                  ;

expression_list: expression expression_list_rest ;
expression_list_rest: COMMA expression expression_list_rest | ;

// Matrix operations
matrix_operation: TRANSPOSE LPAREN expression RPAREN
                | INVERSE LPAREN expression RPAREN
                | MATMULT LPAREN expression COMMA expression RPAREN
                | MATADD LPAREN expression COMMA expression RPAREN
                | MATSUB LPAREN expression COMMA expression RPAREN
                ;

// Control structures
conditional: IF LPAREN condition RPAREN LBRACE statement_list RBRACE else_part ;
else_part: ELSE LBRACE statement_list RBRACE | ;

condition: expression rel_op expression | expression ;
rel_op: EQ | NE | LT | LE | GT | GE ;

loop: for_loop | while_loop ;

for_loop: FOR LPAREN assignment semicolon_opt condition semicolon_opt assignment RPAREN LBRACE statement_list RBRACE ;

while_loop: WHILE LPAREN condition RPAREN LBRACE statement_list RBRACE ;

// Function definitions
function_def: DEF ID LPAREN param_list RPAREN LBRACE statement_list return_stmt RBRACE ;

param_list: ID param_list_rest | ;
param_list_rest: COMMA ID param_list_rest | ;

return_stmt: RETURN expression semicolon_opt ;

// Function calls (CORREGIDO: orden específico para resolver ambigüedades)
function_call: ID LPAREN arg_list RPAREN      // ← FUNCIONES DE USUARIO PRIMERO
             | ml_function                     // ← Luego ML functions
             | io_function                     // ← Luego IO functions
             | plot_function                   // ← Luego Plot functions
             ;

arg_list: expression arg_list_rest | ;
arg_list_rest: COMMA expression arg_list_rest | ;

// ML/DL Functions (COMPLETA: K-MEANS + AUTOENCODER)
ml_function: LINEAR_REGRESSION LPAREN expression COMMA expression RPAREN
           | MLP_CLASSIFIER LPAREN expression COMMA expression COMMA expression RPAREN
           | NEURAL_NETWORK LPAREN expression COMMA expression COMMA expression RPAREN
           | PREDICT LPAREN expression COMMA expression RPAREN
           | TRAIN LPAREN expression COMMA expression RPAREN
           | KMEANS LPAREN expression COMMA expression RPAREN
           | FIT_PREDICT LPAREN expression COMMA expression RPAREN
           | GET_CENTROIDS LPAREN expression RPAREN
           | AUTOENCODER LPAREN expression COMMA expression RPAREN
           | ENCODE LPAREN expression COMMA expression RPAREN
           | DECODE LPAREN expression COMMA expression RPAREN
           | RECONSTRUCT LPAREN expression COMMA expression RPAREN
           | RECONSTRUCTION_ERROR LPAREN expression COMMA expression RPAREN
           ;

// IO Functions
io_function: READ_FILE LPAREN STRING RPAREN
           | WRITE_FILE LPAREN STRING COMMA expression RPAREN
           | PRINT LPAREN expression RPAREN
           ;

// Plot Functions
plot_function: PLOT LPAREN expression RPAREN
             | SCATTER LPAREN expression COMMA expression RPAREN
             | HISTOGRAM LPAREN expression RPAREN
             ;

// LEXER RULES
// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
WHILE: 'while';
DEF: 'def';
RETURN: 'return';

// ML Keywords (COMPLETOS: REGRESSION + MLP + KMEANS + AUTOENCODER)
LINEAR_REGRESSION: 'linear_regression';
MLP_CLASSIFIER: 'mlp_classifier';
NEURAL_NETWORK: 'neural_network';
PREDICT: 'predict';
TRAIN: 'train';
KMEANS: 'kmeans';
FIT_PREDICT: 'fit_predict';
GET_CENTROIDS: 'get_centroids';
AUTOENCODER: 'autoencoder';
ENCODE: 'encode';
DECODE: 'decode';
RECONSTRUCT: 'reconstruct';
RECONSTRUCTION_ERROR: 'reconstruction_error';

// Matrix Keywords
TRANSPOSE: 'transpose';
INVERSE: 'inverse';
MATMULT: 'matmult';
MATADD: 'matadd';
MATSUB: 'matsub';

// IO Keywords
READ_FILE: 'read_file';
WRITE_FILE: 'write_file';
PRINT: 'print';

// Plot Keywords
PLOT: 'plot';
SCATTER: 'scatter';
HISTOGRAM: 'histogram';

// Math Functions
SIN: 'sin';
COS: 'cos';
TAN: 'tan';
SQRT: 'sqrt';

// Operators
ASSIGN: '=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
MOD: '%';
POWER: '^';

// Comparison
EQ: '==';
NE: '!=';
LT: '<';
LE: '<=';
GT: '>';
GE: '>=';

// Punctuation
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
COMMA: ',';
SEMICOLON: ';';

// Literals
NUMBER: [0-9]+;
FLOAT: [0-9]*'.'[0-9]+;
STRING: '"' ~["\r\n]* '"';
ID: [a-zA-Z][a-zA-Z0-9_]*;

// Whitespace
WS: [ \t\r\n]+ -> skip;
COMMENT: '//' ~[\r\n]* -> skip;