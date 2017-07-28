from pyparsing import *

def parse_c():
  data = open("conf.yb","r")
  
  
  LBRACE,RBRACE,LPAREN,RPAREN,SEMI,COL,AT,DOT = map(Suppress,"{}();:@.")
  
  
  real = Regex(r"[+-]?\d+\.\d*").setParseAction(lambda t:float(t[0]))
  integer = Regex(r"[+-]?\d+").setParseAction(lambda t:int(t[0]))
  
  
  string = QuotedString('"')
  
  
  # Configurations
  LANGUAGE = Keyword("language")
  AUTHOR = Keyword("author")
  ORG = Keyword("org")
  DATA = Keyword("data")
  
  
  # Languages
  RUBY = Keyword("ruby")
  PYTHON = Keyword("python")
  JAVASCRIPT = Keyword("javascript")
  JAVA = Keyword("java")
  HTML = Keyword("html")
  LUA = Keyword("lua")
  

  # Major
  TREE = Keyword("tree")
  
  
  # Author Vars
  F = Keyword("f")
  L = Keyword("l")
  C = Keyword("c")
  
  
  language = Group(LANGUAGE + COL + RUBY | PYTHON | JAVASCRIPT | JAVA | HTML | LUA + SEMI)
  data = Group(DATA + COL + string("data") + SEMI)
  author = Group(AUTHOR + COL + F | L | C + COL + string("author") + SEMI)
  org = Group(ORG + COL + AT + string("organization") + SEMI)
  tree = Group(TREE + LPAREN + AT + string("project") + LPAREN + LBRACE + Group(ZeroOrMore(language | author | org | data))("body") + RBRACE)
  
  
  tree.ignore(cStyleComment)
  
  
  result = tree.parseString(data)
  
  
  print(result.asList())
