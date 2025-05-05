txt = '"a" "p" "p" "l" "e"' 
commas_added = ', '.join(txt.split()) 
print(commas_added)
 
 
import re

test_str = input("Enter a word:")  
 
 
res = re.findall(r'\w+|\S', test_str) 
print("Result : " + str(res)) 

test_str = input("Enter a comma-separated list: ")
res = [s.strip() for s in test_str.split(',')]
print("Parsed List:", res)
