
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BE BOOLEAN_EXPRESSION CALL COMA COMPARISON CONSTANT CUBE ELSE ENDFOR ENDIF ENDWHILE EQUAL EQUAL_EQUAL FINISH FLOAT FOR GREATER_THAN GREATER_THAN_EQUAL ID IF INT LEFT_PARENTESIS LENGTH LENGTH_I LENGTH_J LENGTH_K LESS_THAN LESS_THAN_EQUAL MATHEMATICAL_CONSTANT MATHEMATICAL_EXPRESSION MATRIX MEAN MEDIAN MINUS MODE NOT NOT_EQUAL OR PLUS READ RETURN RIGHT_PARENTESIS ROUTINE RREF SEMICOLON SLASH STAR START STRING VECTOR WHILE WRITE\n    PROGRAMA : R START V B FINISH R\n    \n    V : BE VARIABLES SEMICOLON\n    |\n    \n    VARIABLES : FLOAT ID\n    | INT ID\n    | VECTOR ID LEFT_PARENTESIS LENGTH RIGHT_PARENTESIS\n    | MATRIX ID LEFT_PARENTESIS LENGTH COMA LENGTH RIGHT_PARENTESIS\n    | CUBE ID LEFT_PARENTESIS LENGTH COMA LENGTH COMA LENGTH RIGHT_PARENTESIS\n    \n    R : ROUTINE LEFT_PARENTESIS ID RIGHT_PARENTESIS V B RETURN\n    |\n    \n    B : CALL ID SEMICOLON\n    | ID EQUAL E SEMICOLON\n    | READ ID SEMICOLON\n    | WRITE STRING WRITE_AUX SEMICOLON\n    | WRITE ID WRITE_AUX SEMICOLON\n    | IF LEFT_PARENTESIS EL RIGHT_PARENTESIS B ELSE_AUX ENDIF\n    | WHILE LEFT_PARENTESIS EL RIGHT_PARENTESIS B ENDWHILE\n    | FOR LEFT_PARENTESIS EL COMA B RIGHT_PARENTESIS B ENDFOR\n    |\n    \n    ELSE_AUX : ELSE B\n    |\n    \n    WRITE_AUX : COMA STRING WRITE_AUX\n    | COMA ID WRITE_AUX\n    |\n    \n    EL : LEFT_PARENTESIS EL RIGHT_PARENTESIS EL_AUX\n    | CONSTANT EL_AUX\n    | ID EL_AUX\n    \n    EL_AUX : COMPARISON E\n    |\n    \n    E : LEFT_PARENTESIS E RIGHT_PARENTESIS E_AUX\n    | CONSTANT E_AUX\n    | ID E_AUX\n    \n    E_AUX : PLUS E\n    | STAR E\n    | SLASH E\n    | MINUS E\n    |\n    '
    
_lr_action_items = {'ROUTINE':([0,24,],[3,3,]),'START':([0,2,82,],[-10,4,-9,]),'$end':([1,24,40,82,],[0,-10,-1,-9,]),'LEFT_PARENTESIS':([3,14,15,16,26,30,31,32,36,37,38,44,50,61,62,63,64,75,],[5,30,31,32,44,50,50,50,56,57,58,44,50,44,44,44,44,44,]),'BE':([4,23,],[7,7,]),'CALL':([4,6,23,33,39,73,77,78,101,103,],[-3,10,-3,-2,10,10,10,10,10,10,]),'ID':([4,5,6,10,12,13,18,19,20,21,22,23,26,30,31,32,33,39,44,48,50,61,62,63,64,73,75,77,78,101,103,],[-3,8,11,25,27,29,34,35,36,37,38,-3,42,53,53,53,-2,11,42,70,53,42,42,42,42,11,42,11,11,11,11,]),'READ':([4,6,23,33,39,73,77,78,101,103,],[-3,12,-3,-2,12,12,12,12,12,12,]),'WRITE':([4,6,23,33,39,73,77,78,101,103,],[-3,13,-3,-2,13,13,13,13,13,13,]),'IF':([4,6,23,33,39,73,77,78,101,103,],[-3,14,-3,-2,14,14,14,14,14,14,]),'WHILE':([4,6,23,33,39,73,77,78,101,103,],[-3,15,-3,-2,15,15,15,15,15,15,]),'FOR':([4,6,23,33,39,73,77,78,101,103,],[-3,16,-3,-2,16,16,16,16,16,16,]),'FINISH':([4,6,9,33,41,46,65,68,71,102,106,111,],[-3,-19,24,-2,-11,-13,-12,-14,-15,-17,-16,-18,]),'FLOAT':([7,],[18,]),'INT':([7,],[19,]),'VECTOR':([7,],[20,]),'MATRIX':([7,],[21,]),'CUBE':([7,],[22,]),'RIGHT_PARENTESIS':([8,41,42,45,46,51,52,53,54,60,65,66,67,68,71,72,74,76,78,79,83,84,85,86,87,90,92,94,98,99,102,104,106,111,112,],[23,-11,-37,-37,-13,73,-29,-29,77,-32,-12,87,-31,-14,-15,90,-26,-27,-19,95,-33,-34,-35,-36,-37,-29,-28,103,-30,-25,-17,109,-16,-18,113,]),'EQUAL':([11,],[26,]),'STRING':([13,48,],[28,69,]),'SEMICOLON':([17,25,27,28,29,34,35,42,43,45,47,49,60,67,69,70,83,84,85,86,87,88,89,95,98,109,113,],[33,41,46,-24,-24,-4,-5,-37,65,-37,68,71,-32,-31,-24,-24,-33,-34,-35,-36,-37,-22,-23,-6,-30,-7,-8,]),'RETURN':([23,33,39,41,46,59,65,68,71,102,106,111,],[-3,-2,-19,-11,-13,82,-12,-14,-15,-17,-16,-18,]),'CONSTANT':([26,30,31,32,44,50,61,62,63,64,75,],[45,52,52,52,45,52,45,45,45,45,45,]),'COMA':([28,29,42,45,52,53,55,60,67,69,70,74,76,80,81,83,84,85,86,87,90,92,98,99,105,],[48,48,-37,-37,-29,-29,78,-32,-31,48,48,-26,-27,96,97,-33,-34,-35,-36,-37,-29,-28,-30,-25,110,]),'ELSE':([41,46,65,68,71,73,91,102,106,111,],[-11,-13,-12,-14,-15,-19,101,-17,-16,-18,]),'ENDIF':([41,46,65,68,71,73,91,100,101,102,106,107,111,],[-11,-13,-12,-14,-15,-19,-21,106,-19,-17,-16,-20,-18,]),'ENDWHILE':([41,46,65,68,71,77,93,102,106,111,],[-11,-13,-12,-14,-15,-19,102,-17,-16,-18,]),'ENDFOR':([41,46,65,68,71,102,103,106,108,111,],[-11,-13,-12,-14,-15,-17,-19,-16,111,-18,]),'PLUS':([42,45,87,],[61,61,61,]),'STAR':([42,45,87,],[62,62,62,]),'SLASH':([42,45,87,],[63,63,63,]),'MINUS':([42,45,87,],[64,64,64,]),'COMPARISON':([52,53,90,],[75,75,75,]),'LENGTH':([56,57,58,96,97,110,],[79,80,81,104,105,112,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'R':([0,24,],[2,40,]),'V':([4,23,],[6,39,]),'B':([6,39,73,77,78,101,103,],[9,59,91,93,94,107,108,]),'VARIABLES':([7,],[17,]),'E':([26,44,61,62,63,64,75,],[43,66,83,84,85,86,92,]),'WRITE_AUX':([28,29,69,70,],[47,49,88,89,]),'EL':([30,31,32,50,],[51,54,55,72,]),'E_AUX':([42,45,87,],[60,67,98,]),'EL_AUX':([52,53,90,],[74,76,99,]),'ELSE_AUX':([91,],[100,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> R START V B FINISH R','PROGRAMA',6,'p_PROGRAMA','TA.py',33),
  ('V -> BE VARIABLES SEMICOLON','V',3,'p_V','TA.py',38),
  ('V -> <empty>','V',0,'p_V','TA.py',39),
  ('VARIABLES -> FLOAT ID','VARIABLES',2,'p_VARIABLES','TA.py',44),
  ('VARIABLES -> INT ID','VARIABLES',2,'p_VARIABLES','TA.py',45),
  ('VARIABLES -> VECTOR ID LEFT_PARENTESIS LENGTH RIGHT_PARENTESIS','VARIABLES',5,'p_VARIABLES','TA.py',46),
  ('VARIABLES -> MATRIX ID LEFT_PARENTESIS LENGTH COMA LENGTH RIGHT_PARENTESIS','VARIABLES',7,'p_VARIABLES','TA.py',47),
  ('VARIABLES -> CUBE ID LEFT_PARENTESIS LENGTH COMA LENGTH COMA LENGTH RIGHT_PARENTESIS','VARIABLES',9,'p_VARIABLES','TA.py',48),
  ('R -> ROUTINE LEFT_PARENTESIS ID RIGHT_PARENTESIS V B RETURN','R',7,'p_R','TA.py',53),
  ('R -> <empty>','R',0,'p_R','TA.py',54),
  ('B -> CALL ID SEMICOLON','B',3,'p_B','TA.py',59),
  ('B -> ID EQUAL E SEMICOLON','B',4,'p_B','TA.py',60),
  ('B -> READ ID SEMICOLON','B',3,'p_B','TA.py',61),
  ('B -> WRITE STRING WRITE_AUX SEMICOLON','B',4,'p_B','TA.py',62),
  ('B -> WRITE ID WRITE_AUX SEMICOLON','B',4,'p_B','TA.py',63),
  ('B -> IF LEFT_PARENTESIS EL RIGHT_PARENTESIS B ELSE_AUX ENDIF','B',7,'p_B','TA.py',64),
  ('B -> WHILE LEFT_PARENTESIS EL RIGHT_PARENTESIS B ENDWHILE','B',6,'p_B','TA.py',65),
  ('B -> FOR LEFT_PARENTESIS EL COMA B RIGHT_PARENTESIS B ENDFOR','B',8,'p_B','TA.py',66),
  ('B -> <empty>','B',0,'p_B','TA.py',67),
  ('ELSE_AUX -> ELSE B','ELSE_AUX',2,'p_ELSE_AUX','TA.py',72),
  ('ELSE_AUX -> <empty>','ELSE_AUX',0,'p_ELSE_AUX','TA.py',73),
  ('WRITE_AUX -> COMA STRING WRITE_AUX','WRITE_AUX',3,'p_WRITE_AUX','TA.py',78),
  ('WRITE_AUX -> COMA ID WRITE_AUX','WRITE_AUX',3,'p_WRITE_AUX','TA.py',79),
  ('WRITE_AUX -> <empty>','WRITE_AUX',0,'p_WRITE_AUX','TA.py',80),
  ('EL -> LEFT_PARENTESIS EL RIGHT_PARENTESIS EL_AUX','EL',4,'p_EL','TA.py',85),
  ('EL -> CONSTANT EL_AUX','EL',2,'p_EL','TA.py',86),
  ('EL -> ID EL_AUX','EL',2,'p_EL','TA.py',87),
  ('EL_AUX -> COMPARISON E','EL_AUX',2,'p_EL_AUX','TA.py',92),
  ('EL_AUX -> <empty>','EL_AUX',0,'p_EL_AUX','TA.py',93),
  ('E -> LEFT_PARENTESIS E RIGHT_PARENTESIS E_AUX','E',4,'p_E','TA.py',98),
  ('E -> CONSTANT E_AUX','E',2,'p_E','TA.py',99),
  ('E -> ID E_AUX','E',2,'p_E','TA.py',100),
  ('E_AUX -> PLUS E','E_AUX',2,'p_E_AUX','TA.py',105),
  ('E_AUX -> STAR E','E_AUX',2,'p_E_AUX','TA.py',106),
  ('E_AUX -> SLASH E','E_AUX',2,'p_E_AUX','TA.py',107),
  ('E_AUX -> MINUS E','E_AUX',2,'p_E_AUX','TA.py',108),
  ('E_AUX -> <empty>','E_AUX',0,'p_E_AUX','TA.py',109),
]