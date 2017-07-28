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
  
  
  tree = Group(TREE + LPAREN + AT + string("project") + LPAREN + LBRACE + Group(ZeroOrMore(pack | data))("body") + RBRACE)
  pack = Group(PACK + DOT + string("package"))
  data = Group(DATA + DOT + string("data"))
  
  
  tree.ignore(cStyleComment)
  
  
  result = tree.parseString(data)
  
  
  print(result.asList())
