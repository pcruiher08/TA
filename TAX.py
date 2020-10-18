import pickle
from decimal import *
import sys

def calculaOffset(dimensions, indexes):
  dimensionsProduct = 1
  indexes = indexes[::-1]
  for i in dimensions: 
    dimensionsProduct *= i
  dimensionsProduct /= dimensions[0]
  result = 0
  for i in range(len(indexes)):
    result += (indexes[len(indexes) - i - 1] * dimensionsProduct)
    dimensionsProduct /= dimensions[i]
  return int(result)

def revisaElTipo(element):
  if(isinstance(element,str)):
    return 'str'
  elif(isinstance(element,list)):
    return "list"
  elif(isinstance(element,dict)):
    return 'dict'
  elif(isinstance(element,int)):
    return 'int'
  elif(isinstance(element,float)):
    return 'float'
  return 'None'

def getValue(element):
  t = revisaElTipo(element)
  if(t == 'str'):
    return variablesDelPrograma[element].get('value')
  if(t == 'list'):
    return getValueArray(element)
  if(t == 'int'):
    return int(element)
  if(t == 'float'):
    return Decimal(element)
    
def getValueArray(element):
  elem = element.copy()
  indexes = elem[1].copy()
  for i in range(len(indexes)):
    indexes[i] = getValue(indexes[i])
  dimensions = variablesDelPrograma[elem[0]].get('dimensions').copy()
  offset = calculaOffset(dimensions, indexes)
  real_value = int(variablesDelPrograma[elem[0]].get('value')[offset])
  return real_value

def setValue(val, busco):
  global variablesDelPrograma
  t = revisaElTipo(busco)
  if(t == 'list'):
    setArrayValue(val, busco)
    return
  ty = variablesDelPrograma[busco].get('type')
  if(ty == 'INT'):
    variablesDelPrograma[busco]['value'] = int(getValue(val))
  else:
    variablesDelPrograma[busco]['value'] = Decimal(getValue(val))
  return

def setArrayValue(val, busco):
  global variablesDelPrograma
  indexes = busco[1].copy()
  for i in range(len(indexes)):
    indexes[i] = int(getValue(indexes[i]))
  info = variablesDelPrograma[busco[0]]
  dimensions = info.get('dimensions').copy()
  offset = calculaOffset(dimensions, indexes)
  if('int' in info.get('type')):
    info['value'][offset] = int(getValue(val))
  else:
    info['value'][offset] = Decimal(getValue(val))
  return
  
def ApplyOperation(op_one,op_two,operator):
  if(operator == 'plus'):
    return getValue(op_one) + getValue(op_two)
  elif(operator == 'minus'):
    return getValue(op_one) - getValue(op_two)
  elif(operator == 'multiply'):
    return getValue(op_one) * getValue(op_two)
  elif(operator == 'divide'):
    if(getValue(op_two) == 0):
      print("Can't divide by 0")
      print("Program Terminated")
      sys.exit()
    return getValue(op_one) / getValue(op_two)
  elif(operator == 'pow'):
    return getValue(op_one) ** getValue(op_two)
  elif(operator == 'mod'):
    return getValue(op_one) % getValue(op_two)
  elif(operator == 'equals'):
    return getValue(op_one) == getValue(op_two)
  elif(operator == 'nequals'):
    return getValue(op_one) != getValue(op_two)
  elif(operator == 'gthan'):
    return getValue(op_one) > getValue(op_two)
  elif(operator == 'lthan'):
    return getValue(op_one) < getValue(op_two)
  elif(operator == 'geqthan'):
    return getValue(op_one) >= getValue(op_two)
  elif(operator == 'leqthan'):
    return getValue(op_one) <= getValue(op_two)
  elif(operator == 'and'):
    return getValue(op_one) and getValue(op_two)
  elif(operator == 'or'):
    return getValue(op_one) or getValue(op_two)
  
  

def ejecutaInstrucciones():
    global quadruplos, numeroDeInstruccion
    inst = quadruplos[numeroDeInstruccion]
    #print(inst)
    if(inst[0] == 'GOTO_UN'):
        UnconditionalGoto(inst)
    elif(inst[0] == 'GOTO_FALSE'):
        gotoFalse(inst)
    elif(inst[0] == 'GOTO_TRUE'):
        gotoTrue(inst)
    elif(inst[0] == 'FUNC_CALL'):
        llamadaARutina(inst)
    elif(inst[0] == 'PRINT'):
        Print(inst)
    elif(inst[0] == 'BCHECK'):
        BoundCheck(inst)
    elif(inst[0] == 'PRINTLN'):
        PrintLn(inst)
    elif(inst[0] == 'INPUT'):
        Input(inst)
    elif(inst[0] == 'ASSIGN'):
        Assign(inst)
    elif(inst == 'RETURN'):
        Return(inst)
    elif(inst[0] == 'EQUALS'):
        Equals(inst)
    elif(inst[0] == 'ADD'):
        Add(inst)
    elif(inst[0] == 'SUB'):
        Substract(inst)
    elif(inst[0] == 'MULT'):
        Multiply(inst)
    elif(inst[0] == 'DIV'):
        Divide(inst)
    elif(inst[0] == 'POW'):
        Pow(inst)
    elif(inst[0] == 'MOD'):
        Mod(inst)
    elif(inst[0] == 'NOTEQUALS'):
        NotEquals(inst)
    elif(inst[0] == 'GTHAN'):
        GreaterThan(inst)
    elif(inst[0] == 'LTHAN'):
        LessThan(inst)
    elif(inst[0] == 'GEQTHAN'):
        GreaterEqualThan(inst)
    elif(inst[0] == 'LEQTHAN'):
        LessEqualThan(inst)
    elif(inst[0] == 'AND'):
        And(inst)
    elif(inst[0] == 'OR'):
        Or(inst)

def UnconditionalGoto(inst):
  global numeroDeInstruccion
  numeroDeInstruccion = inst[1]
  return

def gotoFalse(inst):
  global numeroDeInstruccion
  if(not getValue(inst[1])):
    numeroDeInstruccion = inst[2]
  else:
    numeroDeInstruccion += 1
  return

def gotoTrue(inst):
  global numeroDeInstruccion
  if(getValue(inst[1])):
    numeroDeInstruccion = inst[2]
  else:
    numeroDeInstruccion+=1
  return

def llamadaARutina(inst):
  global numeroDeInstruccion, program_stack
  program_stack.append(numeroDeInstruccion+1)
  numeroDeInstruccion = inst[1]
  return

def Return(inst):
  global program_stack, numeroDeInstruccion
  numeroDeInstruccion = program_stack.pop()
  return

def Assign(inst):
  global numeroDeInstruccion
  setValue(inst[1],inst[2])
  numeroDeInstruccion += 1
  return

def BoundCheck(inst):
    global variablesDelPrograma, numeroDeInstruccion, quadruplos
    bounds = inst[2]
    busco = inst[1]
    if(len(bounds)!=len(busco)):
        print("Matrix size error")
        print("Program terminated")
        numeroDeInstruccion == len(quadruplos)
    else:
        for (indx, value) in enumerate(busco):
            if(value in variablesDelPrograma.keys()):
                value = variablesDelPrograma[value].get('value')
            if(value >= bounds[indx]):
                print("Array out of bounds error")
                print("Program terminated")
                numeroDeInstruccion = len(quadruplos)
    numeroDeInstruccion+=1
    return

def Input(inst):
  global numeroDeInstruccion, variablesDelPrograma
  read_variable = float(input())
  variablesDelPrograma[inst[1]] = {'value': read_variable, 'type' : 'float'}
  numeroDeInstruccion += 1
  return

def Add(inst):
  global numeroDeInstruccion, variablesDelPrograma
  answer = ApplyOperation(inst[1],inst[2],'plus')
  variablesDelPrograma[inst[3]] = {'value': answer, 'type' : 'float'}
  numeroDeInstruccion += 1
  return

def Substract(inst):
  global numeroDeInstruccion, variablesDelPrograma
  answer = ApplyOperation(inst[1],inst[2],'minus')
  variablesDelPrograma[inst[3]] = {'value': answer, 'type' : 'float'}
  numeroDeInstruccion += 1
  return

def Multiply(inst):
  global numeroDeInstruccion, variablesDelPrograma
  answer = ApplyOperation(inst[1],inst[2],'multiply')
  variablesDelPrograma[inst[3]] = {'value': answer, 'type' : 'float'}
  numeroDeInstruccion += 1
  return

def Divide(inst):
  global numeroDeInstruccion, variablesDelPrograma
  answer = ApplyOperation(inst[1],inst[2],'divide')
  variablesDelPrograma[inst[3]] = {'value': answer, 'type' : 'float'}
  numeroDeInstruccion += 1
  return

def Pow(inst):
  global numeroDeInstruccion, variablesDelPrograma
  answer = ApplyOperation(inst[1],inst[2],'pow')
  variablesDelPrograma[inst[3]] = {'value': answer, 'type' : 'float'}
  numeroDeInstruccion += 1
  return

def Mod(inst):
  global numeroDeInstruccion, variablesDelPrograma
  answer = ApplyOperation(inst[1],inst[2],'mod')
  variablesDelPrograma[inst[3]] = {'value': answer, 'type' : 'float'}
  numeroDeInstruccion += 1
  return

def Equals(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'equals')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def NotEquals(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'nequals')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def GreaterThan(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'gthan')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def LessThan(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'lthan')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def GreaterEqualThan(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'geqthan')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def LessEqualThan(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'leqthan')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def And(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'and')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def Or(inst):
  global numeroDeInstruccion, variablesDelPrograma
  comparison = ApplyOperation(inst[1], inst[2], 'or')
  variablesDelPrograma[inst[3]] = {'value': int(comparison), 'type': 'int'}
  numeroDeInstruccion += 1
  return

def Print(inst):
  global numeroDeInstruccion, variablesDelPrograma
  val = inst[1]
  t = revisaElTipo(val)
  if(t == 'str' and val not in variablesDelPrograma.keys()):
    print(val.replace('"',""), end='')
  else:
    print(getValue(val), end='')
  numeroDeInstruccion += 1
  return

def PrintLn(inst):
  global numeroDeInstruccion, variablesDelPrograma
  val = inst[1]
  t = revisaElTipo(val)
  if(t == 'str' and val not in variablesDelPrograma.keys()):
    print(val.replace('"',""))
  else:
    print(getValue(val))
  numeroDeInstruccion += 1
  return

def inicializa():
  global variables, variablesDelPrograma
  for var in variables.items():
      if(isinstance(var[1], tuple) and 'Array' in var[1][0]):
          length = 1
          for n in var[1][1]:
              length = length * n
          variablesDelPrograma[var[0]] = {"type":var[1][0],"value":[0]*length,"dimensions":var[1][1]}
      else:
          variablesDelPrograma[var[0]] = {"type":var[1],"value":0}


if __name__ == '__main__':
    global numeroDeInstruccion, data, quadruplos, variables, variablesDelPrograma, program_stack
    getcontext().prec=6
    numeroDeInstruccion = 0
    data = pickle.load(open("out.p","rb"))
    quadruplos = data['Quadruples']
    variables = data['SymbolTable']
    variablesDelPrograma = {}
    program_stack = []
    inicializa()

    while(numeroDeInstruccion < len(quadruplos)):
        ejecutaInstrucciones()
