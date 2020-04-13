import Tokens
import ply.lex as lex
import ply.yacc as yacc

t_COMPARISON = r'\<|\>|\=|\<\=|\>\=|\!\=|\!'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_STAR = r'\*'
t_SLASH = r'\\'
t_SEMICOLON = r'\;'
t_LEFT_PARENTESIS = r'\('
t_RIGHT_PARENTESIS = r'\)'
t_STRING = r'\"[0-9]*[a-zA-Z]+[0-9]*\"'
t_ID = r'[0-9]*[a-zA-Z]+[0-9]*'
t_LENGTH = r'[0-9]+'
t_ignore = r' '
t_READ = r'READ'
t_BE = r'BE'
t_WRITE = r'WRITE'
t_WHILE = r'WHILE'
t_ENDWHILE = r'ENDWHILE'
t_MATRIX = r'MATRIX'
t_CALL = r'CALL'
t_START = r'START'
t_FINISH = r'FINISH'
t_RETURN = r'RETURN'
t_ROUTINE = r'ROUTINE'
t_CONSTANT = r'[0-9]+'
t_COMA = r'\,'

def t_error(t):
	print("Caracter no reconocido")

def p_PROGRAMA(p):
    '''
    PROGRAMA : R START V B FINISH R
    '''

def p_V(p):
    '''
    V : BE VARIABLES SEMICOLON
    |
    '''

def p_VARIABLES(p):
    '''
    VARIABLES : FLOAT ID
    | INT ID
    | VECTOR ID LEFT_PARENTESIS LENGTH RIGHT_PARENTESIS
    | MATRIX ID LEFT_PARENTESIS LENGTH COMA LENGTH RIGHT_PARENTESIS
    | CUBE ID LEFT_PARENTESIS LENGTH COMA LENGTH COMA LENGTH RIGHT_PARENTESIS
    '''

def p_R(p):
    '''
    R : ROUTINE LEFT_PARENTESIS ID RIGHT_PARENTESIS V B RETURN
    |
    '''

def p_B(p):
    '''
    B : CALL ID SEMICOLON
    | ID EQUAL E SEMICOLON
    | READ ID SEMICOLON
    | WRITE STRING WRITE_AUX SEMICOLON
    | WRITE ID WRITE_AUX SEMICOLON
    | IF LEFT_PARENTESIS EL RIGHT_PARENTESIS B ELSE_AUX ENDIF
    | WHILE LEFT_PARENTESIS EL RIGHT_PARENTESIS B ENDWHILE
    | FOR LEFT_PARENTESIS EL COMA B RIGHT_PARENTESIS B ENDFOR
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
    | COMA ID WRITE_AUX
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
    EL_AUX : COMPARISON E
    |
    '''
#EXPRESIONES MATEMATICAS
def p_E(p):
    '''
    E : LEFT_PARENTESIS E RIGHT_PARENTESIS E_AUX
    | CONSTANT E_AUX
    | ID E_AUX
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
	print("No valido")

tokens = Tokens.Tokens
lexer = lex.lex()
parser = yacc.yacc()
parser.parse(input())