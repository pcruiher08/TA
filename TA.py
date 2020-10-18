import ply.lex as lex
import ply.yacc as yacc
import sys
import pickle

#arreglar 2 y 5
#implementar 1

cuadruplos = []
stackDeGotos = []
value_stack = []
errores = []

tablaDeSimbolos = {}

temporals = 0

reserved = {'IF' : 'IF','END' : 'END','OTHERWISE' : 'ELSE','WHILE' : 'WHILE','FOR' : 'FOR','ENDFOR' : 'NEXT','SCALE' : 'TO','PROGRAMBEGIN' : 'PROGRAM','RUN' : 'START','PROGRAMDONE' : 'FINISH','BE' : 'DIM','as' : 'AS','INT' : 'INT','FLOAT' : 'FLOAT','ROUTINE' : 'ROUTINE','ENDROUTINE' : 'RETURN','CALL' : 'GOSUB','WRITE' : 'WRITE','WRITELINE' : 'WRITELINE','INCASE' : 'THEN','READ' : 'INPUT'}
tokens = ['NUMBER','ID','SUMAYRESTA','DIVISIONMULTIPLICACION','EQUALS','LPAREN','RPAREN','NOT','AND','OR','RELATIONAL','SEMICOLON','FLOTANTE','IZQB','DERB','STRING'] + list(reserved.values())

t_STRING = r'\".*\"'
t_IZQB = r'\['
t_DERB = r'\]'
t_EQUALS = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_RELATIONAL = r'\<\=|\!\=|\=\=|\>\=|\>|\<'
t_SEMICOLON = r'\;'
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_FLOTANTE(t):
    r'\-?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\-?\d+'
    t.value = int(t.value)
    return t

def t_SUMAYRESTA(t):
    r'\+|\-'
    return t

def t_DIVISIONMULTIPLICACION(t):
    r'\*|\/|\^|\%'
    return t

def t_error(t):
    print("no se reconoce el caracter '%s'" % t.value[0])
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()

def p_S(p):
    '''
    S : PRINCIPAL PROGRAM START DECL R PRINCIPAL_C B FINISH
    '''
    p[0] = "PROGRAM COMPILED SUCCESFULLY."

def p_PRINCIPAL_C(p):
    '''
    PRINCIPAL_C :
    '''
    global cuadruplos
    cuadruplos[0] = ('GOTO_UN', len(cuadruplos))

def p_PRINCIPAL(p):
    '''
    PRINCIPAL :
    '''
    global cuadruplos
    cuadruplos.append(('GOTO_UN'))

def p_R(p):
    '''
    R : REGLADERUTINAS R
    |
    '''

def p_SUBROURINTE_RULE(p):
    '''
    REGLADERUTINAS : ROUTINE ID SUBACTION B RETURN
    '''
    if(len(p) > 2):
        global cuadruplos, tablaDeSimbolos
        cuadruplos.append(('RETURN'))
        tablaDeSimbolos[p[2]] = tablaDeSimbolos['temp']
        del tablaDeSimbolos['temp']

def p_SUBACTION(p):
    '''
    SUBACTION :
    '''
    global tablaDeSimbolos, cuadruplos
    tablaDeSimbolos['temp'] = ('ROUTINE', len(cuadruplos))


def p_DECL(p):
    '''
    DECL : DIM ID AS TYPE SEMICOLON DECL
    | DIM ID ARRAY AS TYPE SEMICOLON DECL
    |
    '''
    global errores
    if(len(p) > 2):
        if len(p) > 7:
            if p[2] in tablaDeSimbolos():
                errores.append("Can't declare same variable more than once. Error in line " + str(p.lineno(2)))
            tablaDeSimbolos[p[2]] = (p[5] + str('Array'),p[3])
        else:
            if p[2] in tablaDeSimbolos():
                errores.append("Can't declare same variable more than once. Error in line " + str(p.lineno(2)))
            tablaDeSimbolos[p[2]] = p[4]

def p_ARRAY(p):
    '''
    ARRAY : REGLAARRAY ARRAY
    | REGLAARRAY
    '''
    if(len(p) > 2):
        p[0] = [p[1]]+p[2]
    else:
        p[0] = [p[1]]

def p_REGLAARRAY(p):
    '''
    REGLAARRAY : IZQB EXPRESSION DERB
    '''
    p[0] = p[2]

def p_TYPE(p):
    '''
    TYPE : INT
    | FLOAT
    '''
    p[0] = p[1]

def p_B(p):
    '''
    B : S B
    | S
    |
    '''

def p_S(p):
    '''
    S : REGLAIF
    | REGLAIFELSE
    | REGLAWHILE
    | REGLACALL
    | REGLAFOR
    | REGLAWRITE
    | REGLAWRITELINE
    | REGLAREAD
    | ASIGNACION
    '''

def p_REGLAREAD(p):
    '''
    REGLAREAD : INPUT LPAREN EXPRESSION RPAREN SEMICOLON
    '''
    global cuadruplos, tablaDeSimbolos, errores
    if(isinstance(p[3],list)):
        if(p[3][0] not in tablaDeSimbolos()):
            errores.append('Undeclared identifier in line ' + str(p.lineno(3)))
        else:
            temp = get_next_temporal()
            cuadruplos.append(('INPUT', temp))
            cuadruplos.append(('ASIGNACION', temp, p[3]))
    else:
        if(p[3] not in tablaDeSimbolos()):
            errores.append('Undeclared identifier in line ' + str(p.lineno(3)))
        else:
            temp = get_next_temporal()
            cuadruplos.append(('INPUT', temp))
            cuadruplos.append(('ASIGNACION', temp, p[3]))

def p_REGLAWRITE(p):
    '''
    REGLAWRITE : WRITE LPAREN STRING RPAREN SEMICOLON
    | WRITE LPAREN EXPRESSION RPAREN SEMICOLON
    '''
    global cuadruplos
    cuadruplos.append(('WRITE', p[3]))

def p_REGLAWRITELINE(p):
    '''
    REGLAWRITELINE : WRITELINE LPAREN STRING RPAREN SEMICOLON
    | WRITELINE LPAREN EXPRESSION RPAREN SEMICOLON
    '''
    global cuadruplos
    cuadruplos.append(('WRITELINE', p[3]))

def p_REGLACALL(p):
    '''
    REGLACALL : GOSUB ID SEMICOLON
    '''
    global tablaDeSimbolos, cuadruplos, errores
    if( p[2] not in tablaDeSimbolos()):
        errores.append("Undeclared Identifier in line " + str(p.lineno(2)))
    elif(not isinstance(tablaDeSimbolos[p[2]], tuple)):
        errores.append("Wrong Type of Identifier in line " + str(p.lineno(2)))
    else:
        cuadruplos.append(('FUNC_CALL', tablaDeSimbolos[p[2]][1]))

def p_REGLAFOR(p):
    '''
    REGLAFOR : FOR ASIGNACION TO EXPRESSION FOR_ACTION B NEXT ID
    '''
    global cuadruplos, stackDeGotos
    jump = stackDeGotos[-1]
    stackDeGotos.pop()
    temp = get_next_temporal()
    cuadruplos.append(('ADD', p[2], 1, temp))
    cuadruplos.append(('ASIGNACION', temp, p[2]))
    cuadruplos.append(('GOTO_UN', jump))
    cuadruplos[jump+1] = ('GOTO_TRUE', cuadruplos[jump][3], len(cuadruplos))

def p_FOR_ACTION(p):
    '''
    FOR_ACTION :
    '''
    global cuadruplos, value_stack, stackDeGotos
    temp = get_next_temporal()
    cuadruplos.append(('EQUALS', cuadruplos[-1][2], value_stack[-1], temp))
    cuadruplos.append(('GOTO_TRUE', temp))
    stackDeGotos.append(len(cuadruplos)-2)
    


def p_REGLAWHILE(p):
    '''
    REGLAWHILE : WHILE LPAREN WHILE_ACTION EXPRESSION WHILE_ACTION_JUMP RPAREN B END
    '''
    global stackDeGotos, cuadruplos
    jump = stackDeGotos[-1]
    stackDeGotos.pop()
    jump2 = stackDeGotos[-1]
    stackDeGotos.pop()
    cuadruplos.append(('GOTO_UN', jump2))
    cuadruplos[jump] = ('GOTO_FALSE', cuadruplos[jump][1], len(cuadruplos))

def p_WHILE_ACTION(p):
    '''
    WHILE_ACTION : 
    '''
    global stackDeGotos, cuadruplos
    stackDeGotos.append(len(cuadruplos))

def p_WHILE_ACTION_JUMP(p):
    '''
    WHILE_ACTION_JUMP :
    '''
    global cuadruplos, value_stack, stackDeGotos
    cuadruplos.append(('GOTO_FALSE', value_stack[-1]))
    stackDeGotos.append(len(cuadruplos)-1)
    

def p_REGLAIF(p):
    '''
    REGLAIF : IF LPAREN EXPRESSION IF_ACTION RPAREN THEN B END
    '''
    global stackDeGotos, cuadruplos
    jump = stackDeGotos[-1]
    stackDeGotos.pop()
    cuadruplos[jump] = ('GOTO_FALSE', cuadruplos[jump][1], len(cuadruplos))

def p_REGLAIFELSE(p):
    '''
    REGLAIFELSE : IF LPAREN EXPRESSION IF_ACTION RPAREN THEN B ELSE_ACTION ELSE_RULE END 
    '''
    global stackDeGotos, cuadruplos
    jump = stackDeGotos[-1]
    stackDeGotos.pop()
    cuadruplos[jump] = ('GOTO_UN', len(cuadruplos))

def p_ELSE_RULE(p):
    '''
    ELSE_RULE : ELSE B
    '''


def p_IF_ACTION(p):
    '''
    IF_ACTION :
    '''
    global cuadruplos, stackDeGotos
    cuadruplos.append(('GOTO_FALSE',value_stack[-1]))
    stackDeGotos.append(len(cuadruplos)-1)

def p_ELSE_ACTION(p):
    '''
    ELSE_ACTION :
    '''
    global cuadruplos
    cuadruplos.append(('GOTO_UN'))
    jump = stackDeGotos[-1]
    stackDeGotos.pop()
    stackDeGotos.append(len(cuadruplos)-1)
    cuadruplos[jump] = ('GOTO_FALSE', cuadruplos[jump][1], len(cuadruplos))


def p_ASIGNACION(p):
    '''
    ASIGNACION : ID EQUALS EXPRESSION SEMICOLON
    | ID ARRAY REVISA_LIMITES EQUALS EXPRESSION SEMICOLON
    '''
    global tablaDeSimbolos, errores, stackDeGotos
    if(not p[1] in tablaDeSimbolos):
        WRITE("Undeclared Identifier in line: " + str(p.lineno(1)))
        sys.exit()
    elif(len(p) < 6):
        operand1 = p[3]
        result = p[1]
        cuadruplos.append(('ASIGNACION',operand1, result))
        p[0] = p[1]
    else:
        jump = stackDeGotos.pop()
        if(isinstance(tablaDeSimbolos[p[1]], tuple)):
            if('Array' in tablaDeSimbolos[p[1]][0]):
                cuadruplos[jump] = ('BCHECK', p[2], tablaDeSimbolos[p[1]][1])
                cuadruplos.append(('ASIGNACION',p[5], [p[1], p[2]]))
            else:
                errores.append("Wrong Type of Identifier in line " + str(p.lineno(1)))
        else:
            errores.append("Wrong Type of Identifier in line " + str(p.lineno(1)))

def p_REVISA_LIMITES(p):
    '''
    REVISA_LIMITES :
    '''
    global cuadruplos
    cuadruplos.append(('BCHECK',))
    stackDeGotos.append(len(cuadruplos)-1)

def p_EXPRESSION(p):
    '''
    EXPRESSION : OR_LEVEL
    '''
    p[0] = p[1]
    value_stack.append(p[0])

def p_OR_LEVEL(p):
    '''
    OR_LEVEL : OR_LEVEL OR AND_LEVEL
    | AND_LEVEL
    '''
    if(len(p) > 2):
        temp = get_next_temporal()
        cuadruplos.append(('OR', p[1], p[3], temp))
        p[0] = temp
    else:
        p[0] = p[1]

def p_AND_LEVEL(p):
    '''
    AND_LEVEL : AND_LEVEL AND RELATIONAL_LEVEL
    | RELATIONAL_LEVEL
    '''
    if(len(p) > 2):
        temp = get_next_temporal()
        cuadruplos.append(('AND', p[1], p[3], temp))
        p[0] = temp
    else:
        p[0] = p[1]

def p_RELATIONAL_LEVEL(p):
    '''
    RELATIONAL_LEVEL : RELATIONAL_LEVEL RELATIONAL SUMAYRESTA_LEVEL
    | SUMAYRESTA_LEVEL
    '''
    if(len(p) > 2):
        temp = get_next_temporal()
        if(p[2] == '<='):
            cuadruplos.append(('LEQTHAN',p[1],p[3],temp))
        elif(p[2] == '>='):
            cuadruplos.append(('GEQTHAN',p[1],p[3],temp))
        elif(p[2] == '=='):
            cuadruplos.append(('EQUALS',p[1],p[3],temp))
        elif(p[2] == '!='):
            cuadruplos.append(('NOTEQUALS',p[1],p[3],temp))
        elif(p[2] == '>'):
            cuadruplos.append(('GTHAN', p[1], p[3], temp))
        elif(p[2] == '<'):
            cuadruplos.append(('LTHAN', p[1], p[3], temp))
        p[0] = temp
    else:
        p[0] = p[1]

def p_SUMAYRESTA_LEVEL(p):
    '''
    SUMAYRESTA_LEVEL : SUMAYRESTA_LEVEL SUMAYRESTA DIVISIONMULTIPLICACION_LEVEL
    | DIVISIONMULTIPLICACION_LEVEL
    '''
    if(len(p) > 2):
        temp = get_next_temporal()
        if(p[2] == "+"):
            cuadruplos.append(('ADD',p[1], p[3], temp))
        else:
            cuadruplos.append(('SUB',p[1], p[3], temp))
        p[0] = temp
    else:
        p[0] = p[1]

def p_DIVISIONMULTIPLICACION_LEVEL(p):
    '''
    DIVISIONMULTIPLICACION_LEVEL : DIVISIONMULTIPLICACION_LEVEL DIVISIONMULTIPLICACION NOT_LEVEL
    | NOT_LEVEL
    '''
    if(len(p) > 2):
        temp = get_next_temporal()
        if(p[2] == '*'):
            cuadruplos.append(('MULT',p[1], p[3], temp))
        elif(p[2] == '%'):
            cuadruplos.append(('MOD',p[1], p[3], temp))
        elif(p[2] == '/'):
            cuadruplos.append(('DIV',p[1], p[3], temp))
        else:
            cuadruplos.append(('POW',p[1], p[3], temp))
        p[0] = temp
    else:
        p[0] = p[1]

    
def p_NOT_LEVEL(p):
    '''
    NOT_LEVEL : NOT NOT_LEVEL
    | F
    '''
    if(len(p) > 2):
        temp = get_next_temporal()
        cuadruplos.append(('NOT', p[2], temp))
        p[0] = temp
    else:
        p[0] = p[1]


def p_F(p):
    '''
    F : ID
    | ID ARRAY REVISA_LIMITES
    | FLOTANTE
    | NUMBER
    | LPAREN EXPRESSION RPAREN
    
    '''
    global tablaDeSimbolos, errores
    if(len(p)==4 and not p[1] == '('):
        jump = stackDeGotos.pop()
        if(isinstance(tablaDeSimbolos[p[1]], tuple)):
            if('Array' in tablaDeSimbolos[p[1]][0]):
                cuadruplos[jump] = ('BCHECK', p[2], tablaDeSimbolos[p[1]][1])
                p[0] = [p[1], p[2]]
            else:
                errores.append("Wrong Type of Identifier in line " + str(p.lineno(1)))
        else:
            errores.append("Wrong Type of Identifier in line " + str(p.lineno(1)))
    elif(len(p) > 3):
        p[0] = p[2]
    else:
        if(isinstance(p[1], str)):
            if(p[1] not in tablaDeSimbolos):
                errores.append("Undeclared identifier in line " + str(p.lineno(1)))
        p[0] = p[1]

def get_next_temporal():
    global temporals
    temporals = temporals + 1
    return "t" + str(temporals)

def p_error(p):
   WRITE("\tSyntax error in line " + str(p.lineno))
   for error in errores:
            WRITE(error)
   sys.exit()

parser = yacc.yacc()

if __name__ == '__main__':
    try:
        arch_name = input()
        arch = open(arch_name,'r')
        info = arch.read()
        arch.close()
        if(yacc.parse(info, tracking = True) == 'PROGRAM COMPILED SUCCESFULLY.'):
            WRITE("Correct syntax.")
        else:
            WRITE("Syntax error.")

        if(len(errores) > 0):
            for error in errores:
                WRITE(error)
        else:
            pickle.dump({"cuadruplos": cuadruplos, "SymbolTable" : tablaDeSimbolos}, open("out.p", "wb"))
    except EOFError:
        WRITE(EOFError)