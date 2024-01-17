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
        4,0,5,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,5,0,15,8,0,10,0,12,0,18,9,0,1,0,1,0,4,0,22,8,0,11,0,12,0,23,5,
        0,26,8,0,10,0,12,0,29,9,0,1,0,3,0,32,8,0,1,1,4,1,35,8,1,11,1,12,
        1,36,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,
        5,1,0,4,1,0,49,57,2,0,48,57,95,95,1,0,48,57,3,0,9,10,13,13,32,32,
        51,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,
        31,1,0,0,0,3,34,1,0,0,0,5,40,1,0,0,0,7,43,1,0,0,0,9,45,1,0,0,0,11,
        32,5,48,0,0,12,16,7,0,0,0,13,15,7,1,0,0,14,13,1,0,0,0,15,18,1,0,
        0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,27,1,0,0,0,18,16,1,0,0,0,19,21,
        5,95,0,0,20,22,7,2,0,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,
        23,24,1,0,0,0,24,26,1,0,0,0,25,19,1,0,0,0,26,29,1,0,0,0,27,25,1,
        0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,32,6,0,0,0,31,
        11,1,0,0,0,31,12,1,0,0,0,32,2,1,0,0,0,33,35,7,3,0,0,34,33,1,0,0,
        0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,
        6,1,1,0,39,4,1,0,0,0,40,41,9,0,0,0,41,42,6,2,2,0,42,6,1,0,0,0,43,
        44,9,0,0,0,44,8,1,0,0,0,45,46,9,0,0,0,46,10,1,0,0,0,6,0,16,23,27,
        31,36,3,1,0,0,6,0,0,1,2,1
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "INT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[0] = self.INT_action 
            actions[2] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


