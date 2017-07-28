from pyparsing import *

def parse_c():
  data = open("conf.y","r")
  
  
  LBRACE,RBRACE,LPAREN,RPAREN,SEMI,COL,AT,DOT = map(Suppress,"{}();:@.")
  
  
  real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
  integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))
  
  
  string = QuotedString('"')
  
  
  # Configurations
  LANGUAGE = Keyword("language")
  AUTHOR = Keyword("author")
  ORG = Keyword(org)
  
  
  # Languages
  RUBY = Keyword("ruby")
  PYTHON = Keyword("python")
  JAVASCRIPT = Keyword("javascript")
  JAVA = Keyword("java")
  

  # Major
  TREE = Keyword("tree")
  
  
  # Author Vars
  F = Keyword("f")
  L = Keyword("l")
  C = Keyword("c")
  
  
  language = Group(LANGUAGE + LPAREN + RUBY | PYTHON | JAVASCRIPT | JAVA + RPAREN + SEMI) or Group(LANGUAGE + LPAREN + string("language"))
  
  
  author = Group(AUTHOR + LPAREN + F | L | C + COL + string("author") + RPAREN + SEMI)
  
  
  org = Group(ORG + LPAREN + AT + string("organization") + RPAREN + SEMI)
  
  
  tree = Group(TREE + LPAREN + AT + string("project") + LPAREN + LBRACE + Group(ZeroOrMore(language | author | org))("body") + RBRACE)
  
  
  tree.ignore(cStyleComment)
  
  
  result = tree.parseString(data)
  
  
  print(result.asList())
