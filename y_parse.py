from pyparsing import *

def parse_c():
  data = open("conf.y","r")
  
  
  LBRACE,RBRACE,LPAREN,RPAREN,SEMI,COL,AT = map(Suppress,"{}();:@")
  
  
  real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
  integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))
  
  
  string = QuotedString('"')
  
  
  # Main
  SETTINGS = Keyword("settings")
  TREE = Keyword("tree")
  
  
  # Settings
  FILE = Keyword("file")
  AUTHOR = Keyword("author")
  VERSION = Keyword("version")
  LANGUAGE = Keyword("language")
  PACKAGE = Keyword("package")
  
  
  file = Group(SETTINGS + DOT + FILE + COL + string("file") + SEMI)
  author = Group(SETTINGS + DOT + AUTHOR + COL + string("author") + SEMI)
  version = Group(SETTINGS + DOT + VERSION + COL + string("version" + SEMI))
  language = Group(SETTINGS + DOT + LANGUAGE + COL + string("language"))
  
  
  tree = Group(TREE + LPAREN + AT + string("project") + LPAREN + LBRACE + Group(ZeroOrMore(file | author | version | language))("body") + RBRACE)
  
  
  tree.ignore(cStyleComment)
  
  
  result = tree.parseString(data)
  
  
  print(result.asList())
