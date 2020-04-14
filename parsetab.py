
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BE BOOLEAN_EXPRESSION CALL COMA COMPARISON CONSTANT CUBE ELSE ENDFOR ENDIF ENDWHILE EQUAL EQUAL_EQUAL FINISH FLOAT FOR GREATER_THAN GREATER_THAN_EQUAL ID IF INT LEFT_PARENTESIS LENGTH LENGTH_I LENGTH_J LENGTH_K LESS_THAN LESS_THAN_EQUAL MATHEMATICAL_CONSTANT MATHEMATICAL_EXPRESSION MATRIX MEAN MEDIAN MINUS MODE NOT NOT_EQUAL OR PLUS READ RETURN RIGHT_PARENTESIS ROUTINE RREF SEMICOLON SLASH STAR START STRING VECTOR WHILE WRITE\n    PROGRAMA : R START V B FINISH R\n    \n    V : BE VARIABLES SEMICOLON B V\n    |\n    \n    VARIABLES : FLOAT ID\n    | INT ID\n    | VECTOR ID LEFT_PARENTESIS CONSTANT RIGHT_PARENTESIS\n    | MATRIX ID LEFT_PARENTESIS CONSTANT COMA CONSTANT RIGHT_PARENTESIS\n    | CUBE ID LEFT_PARENTESIS CONSTANT COMA CONSTANT COMA CONSTANT RIGHT_PARENTESIS\n    \n    R : ROUTINE LEFT_PARENTESIS ID RIGHT_PARENTESIS V B RETURN R\n    |\n    \n    B : CALL ID SEMICOLON V B\n    | ID INDICES EQUAL E SEMICOLON V B\n    | READ ID SEMICOLON V B\n    | WRITE STRING WRITE_AUX SEMICOLON V B\n    | WRITE E WRITE_AUX SEMICOLON V B\n    | IF LEFT_PARENTESIS EL RIGHT_PARENTESIS B ELSE_AUX ENDIF V B\n    | WHILE LEFT_PARENTESIS EL RIGHT_PARENTESIS V B ENDWHILE V B\n    | FOR LEFT_PARENTESIS EL COMA B RIGHT_PARENTESIS V B ENDFOR V B\n    |\n    \n    INDICES : LEFT_PARENTESIS E RIGHT_PARENTESIS\n    | LEFT_PARENTESIS E COMA E RIGHT_PARENTESIS\n    | LEFT_PARENTESIS E COMA E COMA E RIGHT_PARENTESIS\n    |\n    \n    ELSE_AUX : ELSE B\n    |\n    \n    WRITE_AUX : COMA STRING WRITE_AUX\n    | COMA ID INDICES WRITE_AUX\n    |\n    \n    EL : LEFT_PARENTESIS EL RIGHT_PARENTESIS EL_AUX\n    | CONSTANT EL_AUX\n    | ID EL_AUX\n    \n    EL_AUX : COMPARISON EL\n    |\n    \n    E : LEFT_PARENTESIS E RIGHT_PARENTESIS E_AUX\n    | CONSTANT E_AUX\n    | ID INDICES E_AUX\n    \n    E_AUX : PLUS E\n    | STAR E\n    | SLASH E\n    | MINUS E\n    |\n    '
    
_lr_action_items = {'ROUTINE':([0,24,96,],[3,3,3,]),'START':([0,2,96,114,],[-10,4,-10,-9,]),'$end':([1,24,44,96,114,],[0,-10,-1,-10,-9,]),'LEFT_PARENTESIS':([3,11,13,14,15,16,27,31,33,34,35,36,40,41,42,46,54,55,56,57,59,73,77,88,116,],[5,27,31,34,35,36,31,31,27,59,59,59,66,67,68,31,31,31,31,31,59,31,27,59,31,]),'BE':([4,23,37,45,48,65,70,74,75,78,90,92,97,98,100,101,104,115,118,120,125,128,130,132,137,138,141,142,143,145,146,],[7,7,-19,7,7,7,-19,-19,7,7,7,-2,-11,7,-13,-19,-19,-19,-14,-15,7,-12,7,7,-19,-19,-16,-17,7,-19,-18,]),'CALL':([4,6,23,37,43,45,48,65,70,74,75,78,86,90,91,92,97,98,100,101,104,109,115,118,120,123,125,128,130,132,133,137,138,141,142,143,145,146,],[-3,10,-3,10,10,-3,-3,-3,10,10,-3,-3,10,-3,10,-2,-11,-3,-13,10,10,10,10,-14,-15,10,-3,-12,-3,-3,10,10,10,-16,-17,-3,10,-18,]),'ID':([4,5,6,10,12,13,18,19,20,21,22,23,27,31,34,35,36,37,43,45,46,48,50,54,55,56,57,59,65,70,73,74,75,78,86,88,90,91,92,97,98,100,101,104,109,115,116,118,120,123,125,128,130,132,133,137,138,141,142,143,145,146,],[-3,8,11,25,28,33,38,39,40,41,42,-3,33,33,62,62,62,11,11,-3,33,-3,77,33,33,33,33,62,-3,11,33,11,-3,-3,11,62,-3,11,-2,-11,-3,-13,11,11,11,11,33,-14,-15,11,-3,-12,-3,-3,11,11,11,-16,-17,-3,11,-18,]),'READ':([4,6,23,37,43,45,48,65,70,74,75,78,86,90,91,92,97,98,100,101,104,109,115,118,120,123,125,128,130,132,133,137,138,141,142,143,145,146,],[-3,12,-3,12,12,-3,-3,-3,12,12,-3,-3,12,-3,12,-2,-11,-3,-13,12,12,12,12,-14,-15,12,-3,-12,-3,-3,12,12,12,-16,-17,-3,12,-18,]),'WRITE':([4,6,23,37,43,45,48,65,70,74,75,78,86,90,91,92,97,98,100,101,104,109,115,118,120,123,125,128,130,132,133,137,138,141,142,143,145,146,],[-3,13,-3,13,13,-3,-3,-3,13,13,-3,-3,13,-3,13,-2,-11,-3,-13,13,13,13,13,-14,-15,13,-3,-12,-3,-3,13,13,13,-16,-17,-3,13,-18,]),'IF':([4,6,23,37,43,45,48,65,70,74,75,78,86,90,91,92,97,98,100,101,104,109,115,118,120,123,125,128,130,132,133,137,138,141,142,143,145,146,],[-3,14,-3,14,14,-3,-3,-3,14,14,-3,-3,14,-3,14,-2,-11,-3,-13,14,14,14,14,-14,-15,14,-3,-12,-3,-3,14,14,14,-16,-17,-3,14,-18,]),'WHILE':([4,6,23,37,43,45,48,65,70,74,75,78,86,90,91,92,97,98,100,101,104,109,115,118,120,123,125,128,130,132,133,137,138,141,142,143,145,146,],[-3,15,-3,15,15,-3,-3,-3,15,15,-3,-3,15,-3,15,-2,-11,-3,-13,15,15,15,15,-14,-15,15,-3,-12,-3,-3,15,15,15,-16,-17,-3,15,-18,]),'FOR':([4,6,23,37,43,45,48,65,70,74,75,78,86,90,91,92,97,98,100,101,104,109,115,118,120,123,125,128,130,132,133,137,138,141,142,143,145,146,],[-3,16,-3,16,16,-3,-3,-3,16,16,-3,-3,16,-3,16,-2,-11,-3,-13,16,16,16,16,-14,-15,16,-3,-12,-3,-3,16,16,16,-16,-17,-3,16,-18,]),'FINISH':([4,6,9,37,45,48,65,70,74,75,78,92,97,98,100,101,104,115,118,120,128,130,132,137,138,141,142,143,145,146,],[-3,-19,24,-19,-3,-3,-3,-19,-19,-3,-3,-2,-11,-3,-13,-19,-19,-19,-14,-15,-12,-3,-3,-19,-19,-16,-17,-3,-19,-18,]),'FLOAT':([7,],[18,]),'INT':([7,],[19,]),'VECTOR':([7,],[20,]),'MATRIX':([7,],[21,]),'CUBE':([7,],[22,]),'RIGHT_PARENTESIS':([8,32,33,37,45,47,48,52,53,58,60,61,62,63,65,70,72,74,75,78,79,80,81,82,83,84,85,87,89,91,92,93,97,98,99,100,101,104,105,106,108,110,115,117,118,120,121,126,128,129,130,132,136,137,138,140,141,142,143,145,146,],[23,-41,-23,-19,-3,72,-3,79,-35,-41,86,-33,-33,90,-3,-19,-20,-19,-3,-3,-41,-37,-38,-39,-40,-36,106,-30,-31,-19,-2,111,-11,-3,117,-13,-19,-19,-34,-33,-32,125,-19,-21,-14,-15,-29,134,-12,136,-3,-3,-22,-19,-19,144,-16,-17,-3,-19,-18,]),'EQUAL':([11,26,72,117,136,],[-23,46,-20,-21,-22,]),'STRING':([13,50,],[29,76,]),'CONSTANT':([13,27,31,34,35,36,46,54,55,56,57,59,66,67,68,73,88,112,113,116,135,],[32,32,32,61,61,61,32,32,32,32,32,61,93,94,95,32,61,126,127,32,140,]),'SEMICOLON':([17,25,28,29,30,32,33,38,39,49,51,53,58,71,72,76,77,79,80,81,82,83,84,102,103,105,111,117,119,134,136,144,],[37,45,48,-28,-28,-41,-23,-4,-5,75,78,-35,-41,98,-20,-28,-23,-41,-37,-38,-39,-40,-36,-26,-28,-34,-6,-21,-27,-7,-22,-8,]),'RETURN':([23,37,43,45,48,65,69,70,74,75,78,92,97,98,100,101,104,115,118,120,128,130,132,137,138,141,142,143,145,146,],[-3,-19,-19,-3,-3,-3,96,-19,-19,-3,-3,-2,-11,-3,-13,-19,-19,-19,-14,-15,-12,-3,-3,-19,-19,-16,-17,-3,-19,-18,]),'COMA':([29,30,32,33,47,53,58,61,62,64,72,76,77,79,80,81,82,83,84,87,89,94,95,99,103,105,106,108,117,121,127,136,],[50,50,-41,-23,73,-35,-41,-33,-33,91,-20,50,-23,-41,-37,-38,-39,-40,-36,-30,-31,112,113,116,50,-34,-33,-32,-21,-29,135,-22,]),'PLUS':([32,33,58,72,79,117,136,],[54,-23,54,-20,54,-21,-22,]),'STAR':([32,33,58,72,79,117,136,],[55,-23,55,-20,55,-21,-22,]),'SLASH':([32,33,58,72,79,117,136,],[56,-23,56,-20,56,-21,-22,]),'MINUS':([32,33,58,72,79,117,136,],[57,-23,57,-20,57,-21,-22,]),'ELSE':([37,45,48,65,70,74,75,78,86,92,97,98,100,101,104,107,115,118,120,128,130,132,137,138,141,142,143,145,146,],[-19,-3,-3,-3,-19,-19,-3,-3,-19,-2,-11,-3,-13,-19,-19,123,-19,-14,-15,-12,-3,-3,-19,-19,-16,-17,-3,-19,-18,]),'ENDIF':([37,45,48,65,70,74,75,78,86,92,97,98,100,101,104,107,115,118,120,122,123,128,130,131,132,137,138,141,142,143,145,146,],[-19,-3,-3,-3,-19,-19,-3,-3,-19,-2,-11,-3,-13,-19,-19,-25,-19,-14,-15,130,-19,-12,-3,-24,-3,-19,-19,-16,-17,-3,-19,-18,]),'ENDWHILE':([37,45,48,65,70,74,75,78,90,92,97,98,100,101,104,109,115,118,120,124,128,130,132,137,138,141,142,143,145,146,],[-19,-3,-3,-3,-19,-19,-3,-3,-3,-2,-11,-3,-13,-19,-19,-19,-19,-14,-15,132,-12,-3,-3,-19,-19,-16,-17,-3,-19,-18,]),'ENDFOR':([37,45,48,65,70,74,75,78,92,97,98,100,101,104,115,118,120,125,128,130,132,133,137,138,139,141,142,143,145,146,],[-19,-3,-3,-3,-19,-19,-3,-3,-2,-11,-3,-13,-19,-19,-19,-14,-15,-3,-12,-3,-3,-19,-19,-19,143,-16,-17,-3,-19,-18,]),'COMPARISON':([61,62,106,],[88,88,88,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'R':([0,24,96,],[2,44,114,]),'V':([4,23,45,48,65,75,78,90,98,125,130,132,143,],[6,43,70,74,92,101,104,109,115,133,137,138,145,]),'B':([6,37,43,70,74,86,91,101,104,109,115,123,133,137,138,145,],[9,65,69,97,100,107,110,118,120,124,128,131,139,141,142,146,]),'VARIABLES':([7,],[17,]),'INDICES':([11,33,77,],[26,58,103,]),'E':([13,27,31,46,54,55,56,57,73,116,],[30,47,52,71,80,81,82,83,99,129,]),'WRITE_AUX':([29,30,76,103,],[49,51,102,119,]),'E_AUX':([32,58,79,],[53,84,105,]),'EL':([34,35,36,59,88,],[60,63,64,85,108,]),'EL_AUX':([61,62,106,],[87,89,121,]),'ELSE_AUX':([107,],[122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> R START V B FINISH R','PROGRAMA',6,'p_PROGRAMA','TA.py',113),
  ('V -> BE VARIABLES SEMICOLON B V','V',5,'p_V','TA.py',118),
  ('V -> <empty>','V',0,'p_V','TA.py',119),
  ('VARIABLES -> FLOAT ID','VARIABLES',2,'p_VARIABLES','TA.py',124),
  ('VARIABLES -> INT ID','VARIABLES',2,'p_VARIABLES','TA.py',125),
  ('VARIABLES -> VECTOR ID LEFT_PARENTESIS CONSTANT RIGHT_PARENTESIS','VARIABLES',5,'p_VARIABLES','TA.py',126),
  ('VARIABLES -> MATRIX ID LEFT_PARENTESIS CONSTANT COMA CONSTANT RIGHT_PARENTESIS','VARIABLES',7,'p_VARIABLES','TA.py',127),
  ('VARIABLES -> CUBE ID LEFT_PARENTESIS CONSTANT COMA CONSTANT COMA CONSTANT RIGHT_PARENTESIS','VARIABLES',9,'p_VARIABLES','TA.py',128),
  ('R -> ROUTINE LEFT_PARENTESIS ID RIGHT_PARENTESIS V B RETURN R','R',8,'p_R','TA.py',133),
  ('R -> <empty>','R',0,'p_R','TA.py',134),
  ('B -> CALL ID SEMICOLON V B','B',5,'p_B','TA.py',139),
  ('B -> ID INDICES EQUAL E SEMICOLON V B','B',7,'p_B','TA.py',140),
  ('B -> READ ID SEMICOLON V B','B',5,'p_B','TA.py',141),
  ('B -> WRITE STRING WRITE_AUX SEMICOLON V B','B',6,'p_B','TA.py',142),
  ('B -> WRITE E WRITE_AUX SEMICOLON V B','B',6,'p_B','TA.py',143),
  ('B -> IF LEFT_PARENTESIS EL RIGHT_PARENTESIS B ELSE_AUX ENDIF V B','B',9,'p_B','TA.py',144),
  ('B -> WHILE LEFT_PARENTESIS EL RIGHT_PARENTESIS V B ENDWHILE V B','B',9,'p_B','TA.py',145),
  ('B -> FOR LEFT_PARENTESIS EL COMA B RIGHT_PARENTESIS V B ENDFOR V B','B',11,'p_B','TA.py',146),
  ('B -> <empty>','B',0,'p_B','TA.py',147),
  ('INDICES -> LEFT_PARENTESIS E RIGHT_PARENTESIS','INDICES',3,'p_INDICES','TA.py',152),
  ('INDICES -> LEFT_PARENTESIS E COMA E RIGHT_PARENTESIS','INDICES',5,'p_INDICES','TA.py',153),
  ('INDICES -> LEFT_PARENTESIS E COMA E COMA E RIGHT_PARENTESIS','INDICES',7,'p_INDICES','TA.py',154),
  ('INDICES -> <empty>','INDICES',0,'p_INDICES','TA.py',155),
  ('ELSE_AUX -> ELSE B','ELSE_AUX',2,'p_ELSE_AUX','TA.py',160),
  ('ELSE_AUX -> <empty>','ELSE_AUX',0,'p_ELSE_AUX','TA.py',161),
  ('WRITE_AUX -> COMA STRING WRITE_AUX','WRITE_AUX',3,'p_WRITE_AUX','TA.py',166),
  ('WRITE_AUX -> COMA ID INDICES WRITE_AUX','WRITE_AUX',4,'p_WRITE_AUX','TA.py',167),
  ('WRITE_AUX -> <empty>','WRITE_AUX',0,'p_WRITE_AUX','TA.py',168),
  ('EL -> LEFT_PARENTESIS EL RIGHT_PARENTESIS EL_AUX','EL',4,'p_EL','TA.py',173),
  ('EL -> CONSTANT EL_AUX','EL',2,'p_EL','TA.py',174),
  ('EL -> ID EL_AUX','EL',2,'p_EL','TA.py',175),
  ('EL_AUX -> COMPARISON EL','EL_AUX',2,'p_EL_AUX','TA.py',180),
  ('EL_AUX -> <empty>','EL_AUX',0,'p_EL_AUX','TA.py',181),
  ('E -> LEFT_PARENTESIS E RIGHT_PARENTESIS E_AUX','E',4,'p_E','TA.py',186),
  ('E -> CONSTANT E_AUX','E',2,'p_E','TA.py',187),
  ('E -> ID INDICES E_AUX','E',3,'p_E','TA.py',188),
  ('E_AUX -> PLUS E','E_AUX',2,'p_E_AUX','TA.py',193),
  ('E_AUX -> STAR E','E_AUX',2,'p_E_AUX','TA.py',194),
  ('E_AUX -> SLASH E','E_AUX',2,'p_E_AUX','TA.py',195),
  ('E_AUX -> MINUS E','E_AUX',2,'p_E_AUX','TA.py',196),
  ('E_AUX -> <empty>','E_AUX',0,'p_E_AUX','TA.py',197),
]
