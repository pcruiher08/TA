import Tokens
import ply.lex as lex
import ply.yacc as yacc
import sys

t_COMPARISON = r'\<|\>|\=|\<\=|\>\=|\!\=|\!|\&|\|'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_STAR = r'\*'
t_SLASH = r'\\'
t_SEMICOLON = r'\;'
t_LEFT_PARENTESIS = r'\('
t_RIGHT_PARENTESIS = r'\)'
t_STRING = r'\"[0-9]*[a-zA-Z]+[0-9]*\"'
t_ID = r'[0-9]*[a-zA-Z]+[0-9]*'

def t_EQUAL(t):
    r'\='
    t.type = 'EQUAL'
    return t

def t_CONSTANT(t):
     r'[0-9]+'
     t.type = 'CONSTANT'
     return t

t_ignore = ' \t'

def t_READ(t):
	r'READ'
	t.type = 'READ'
	return t

def t_BE(t):
	r'BE'
	t.type = 'BE'
	return t

def t_INT(t):
    r'INT'
    t.type = 'INT'
    return t

def t_WRITE(t):
	r'WRITE'
	t.type = 'WRITE'
	return t

def t_WHILE(t):
	r'WHILE'
	t.type = 'WHILE'
	return t

def t_ENDWHILE(t):
	r'ENDWHILE'
	t.type = 'ENDWHILE'
	return t

def t_FOR(t):
    r'FOR'
    t.type = 'FOR'
    return t

def t_ENDFOR(t):
    r'ENDFOR'
    t.type = 'ENDFOR'
    return t

def t_MATRIX(t):
	r'MATRIX'
	t.type = 'MATRIX'
	return t

def t_CALL(t):
	r'CALL'
	t.type = 'CALL'
	return t

def t_START(t):
	r'START'
	t.type = 'START'
	return t

def t_FINISH(t):
	r'FINISH'
	t.type = 'FINISH'
	return t

def t_RETURN(t):
	r'RETURN'
	t.type = 'RETURN'
	return t

def t_ROUTINE(t):
	r'ROUTINE'
	t.type = 'ROUTINE'
	return t

def t_FLOAT(t):
    r'FLOAT'
    t.type='FLOAT'
    return t

t_COMA = r'\,'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Error, invalid character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_PROGRAMA(p):
    '''
    PROGRAMA : R START V B FINISH R
    '''
    p[0] = "DONE"
    symbolsTable[p[2]] = 'START'

def p_V(p):
    '''
    V : BE VARIABLES SEMICOLON B V
    |
    '''
    if len(p) > 1:
        symbolsArray.insert(0,p[2])

def p_VARIABLES(p):
    '''
    VARIABLES : FLOAT ID
    | T ID
    | T ID LEFT_PARENTESIS CONSTANT RIGHT_PARENTESIS
    | T ID LEFT_PARENTESIS CONSTANT COMA CONSTANT RIGHT_PARENTESIS
    | T ID LEFT_PARENTESIS CONSTANT COMA CONSTANT COMA CONSTANT RIGHT_PARENTESIS
    '''


def p_T(p):
    '''
    T : INT
    | VECTOR
    | MATRIX
    | CUBE
    '''
    typesArray.append(p[1])


def p_R(p):
    '''
    R : ROUTINE LEFT_PARENTESIS ID RIGHT_PARENTESIS V B RETURN R
    |
    '''
    if(len(p) > 1):
        symbolsTable[p[2]] = 'ROUTINE'

def p_B(p):
    '''
    B : CALL ID SEMICOLON V B
    | ID INDICES EQUAL E SEMICOLON V B
    | READ ID SEMICOLON V B
    | WRITE STRING WRITE_AUX SEMICOLON V B
    | WRITE E WRITE_AUX SEMICOLON V B
    | IF LEFT_PARENTESIS EL RIGHT_PARENTESIS B ELSE_AUX ENDIF V B
    | WHILE LEFT_PARENTESIS EL RIGHT_PARENTESIS V B ENDWHILE V B
    | FOR LEFT_PARENTESIS EL COMA B RIGHT_PARENTESIS V B ENDFOR V B
    |
    '''

def p_INDICES(p):
    '''
    INDICES : LEFT_PARENTESIS E RIGHT_PARENTESIS
    | LEFT_PARENTESIS E COMA E RIGHT_PARENTESIS
    | LEFT_PARENTESIS E COMA E COMA E RIGHT_PARENTESIS
    |
    '''

def p_ELSE_AUX(p):
    '''
    ELSE_AUX : ELSE B
    |
    '''

def p_WRITE_AUX(p):
    '''
    WRITE_AUX : COMA STRING WRITE_AUX
    | COMA ID INDICES WRITE_AUX
    |
    '''
#EXPRESIONES LOGICAS (BOOLEANAS)
def p_EL(p):
    '''
    EL : LEFT_PARENTESIS EL RIGHT_PARENTESIS EL_AUX
    | CONSTANT EL_AUX
    | ID EL_AUX
    '''

def p_EL_AUX(p):
    '''
    EL_AUX : COMPARISON EL
    |
    '''
#EXPRESIONES MATEMATICAS
def p_E(p):
    '''
    E : LEFT_PARENTESIS E RIGHT_PARENTESIS E_AUX
    | CONSTANT E_AUX
    | ID INDICES E_AUX
    '''

def p_E_AUX(p):
    '''
    E_AUX : PLUS E
    | STAR E
    | SLASH E
    | MINUS E
    |
    '''

def p_error(p):
	print("No valido " + str(p.lineno))


try:
    typesArray = []
    symbolsArray = []
    symbolsTable = {}


    tokens = Tokens.Tokens
    lexer = lex.lex()
    yacc.yacc()
    nameOfFile = 'test.txt'
    archivo = open(nameOfFile,"r")
    test = archivo.read()
    archivo.close()

    toParse = ''

    for char in test:
        if not(char == ' ' or char == '\t' or char == '\n' or char == '\s'):
            toParse+=char
    #toParse = test
    #print(toParse)
    print(yacc.parse(toParse,tracking = True))




    #print(toParse)
    #parser.parse(toParse)
except EOFError as e:
    print(e)