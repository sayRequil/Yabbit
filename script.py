from pyparsing import *

yabbit = open("build.y")

TREE = Keyword("tree")
NAME = Keyword("name")
AUTHOR = Keyword("author")
LANGUAGE = Keyword("language")

LBRACE,RBRACE,LPAREN,RPAREN,SEMI,EQUAL,COL = map(Suppress,"{}();=:")

real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))

string = QuotedString('"')

# example: tree:'master'{
#   name:'Yabbit';
#   author:'Zack Pace';
# };
tree = Forward()
tree << Group(TREE + COL + string("tree") + LBRACE + Group(ZeroOrMore(name | author))("body") + RBRACE)

# example: name:'Yabbit';
name = Group(NAME + COL + string("name") + SEMI)

# example: author:'Zack Pace';
author = Group(AUTHOR + COL + string("author") + SEMI)

# example: language:'Python';
language = Group(LANGUAGE + COL + string("language") + SEMI)
