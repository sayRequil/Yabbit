import y_config
import y_packages
import y_parse
import os

y_config.parse_c()
y_packages.parse_p()

for file in os.listdir("/"):
    if file.endswith(".y"):
        y_parse.parse_c(file)
        
print("Parse all Yabbit files.")
