from pyparsing import *

def parse_c(file):
  data = open(file,"r")
  
  
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
  EMAIL = Keyword("email")
  
  
  # Other
  ENTRY = Keyword("entry")
  
  
  # Version
  YABBIT = Keyword("Yabbit")
  
  
  # Defining syntax
  file = Group(SETTINGS + DOT + FILE + COL + string("file") + SEMI)
  author = Group(SETTINGS + DOT + AUTHOR + COL + string("author") + SEMI)
  version = Group(SETTINGS + DOT + VERSION + COL + string("version") + SEMI)
  language = Group(SETTINGS + DOT + LANGUAGE + COL + string("language") + SEMI)
  package = Group(SETTINGS + DOT + PACKAGE + COL + string("package") + SEMI)
  email = Group(SETTINGS + DOT + EMAIL + COL + string("email") + SEMI)
  yabbit = Group(YABBIT + DOT + real + COL + string("yabbit") + SEMI) # Yabbit.1.0.0:"latest"
  entry = Group(ENTRY + COL + string("entry") + SEMI)
  
  
  tree = Group(TREE + LPAREN + AT + string("project") + LPAREN + LBRACE + Group(ZeroOrMore(file | author | version | language | package | email | yabbit))("body") + RBRACE)
  
  
  tree.ignore(cStyleComment)
  
  
  result = tree.parseString(data)
  
  
  print(result.asList())
