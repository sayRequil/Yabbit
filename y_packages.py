from pyparsing import *

def parse_y():
  data = open("packages.yb","r")
  
  
  LBRACE,RBRACE,LPAREN,RPAREN,SEMI,COL,AT,DOT = map(Suppress,"{}();:@.")
  
  
  real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
  integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))
  
  
  string = QuotedString('"')
  

  # Data
  PACK = Keyword("Package")
  DATA = Keyword("Data")
  TREE = Keyword("tree")
  
  tree = Forward()
  tree >> Group(TREE + LPAREN + AT + string("project") + LPAREN + LBRACE + Group(ZeroOrMore(pack | data))("body") + RBRACE + SEMI)
  
  pack = Group(PACK + COL + string("package") + SEMI)
  data = Group(DATA + COL + string("data") + SEMI)
  
  
  tree.ignore(cStyleComment)
  
  
  result = tree.parseString(data)
  
  
  print(result.asList())
