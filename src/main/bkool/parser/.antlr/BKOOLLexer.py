# Generated from d:/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,5,62,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,0,1,0,1,0,3,0,23,8,0,1,0,1,0,3,0,27,8,0,
        1,1,4,1,30,8,1,11,1,12,1,31,1,2,1,2,4,2,36,8,2,11,2,12,2,37,1,3,
        1,3,3,3,42,8,3,1,3,4,3,45,8,3,11,3,12,3,46,1,4,4,4,50,8,4,11,4,12,
        4,51,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,0,0,8,1,1,3,0,5,0,7,0,9,
        2,11,3,13,4,15,5,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,65,0,1,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,26,1,0,
        0,0,3,29,1,0,0,0,5,33,1,0,0,0,7,39,1,0,0,0,9,49,1,0,0,0,11,55,1,
        0,0,0,13,58,1,0,0,0,15,60,1,0,0,0,17,18,3,3,1,0,18,19,3,5,2,0,19,
        27,1,0,0,0,20,22,3,3,1,0,21,23,3,5,2,0,22,21,1,0,0,0,22,23,1,0,0,
        0,23,24,1,0,0,0,24,25,3,7,3,0,25,27,1,0,0,0,26,17,1,0,0,0,26,20,
        1,0,0,0,27,2,1,0,0,0,28,30,7,0,0,0,29,28,1,0,0,0,30,31,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,4,1,0,0,0,33,35,5,46,0,0,34,36,7,0,0,
        0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,6,1,
        0,0,0,39,41,5,101,0,0,40,42,5,45,0,0,41,40,1,0,0,0,41,42,1,0,0,0,
        42,44,1,0,0,0,43,45,7,0,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,
        0,0,0,46,47,1,0,0,0,47,8,1,0,0,0,48,50,7,1,0,0,49,48,1,0,0,0,50,
        51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,6,4,0,
        0,54,10,1,0,0,0,55,56,9,0,0,0,56,57,6,5,1,0,57,12,1,0,0,0,58,59,
        9,0,0,0,59,14,1,0,0,0,60,61,9,0,0,0,61,16,1,0,0,0,8,0,22,26,31,37,
        41,46,51,2,6,0,0,1,5,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    REAL = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "REAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "REAL", "INT", "DECIMAL", "EXP", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


