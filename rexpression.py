import re

# pattern = r"[A-Z]ello"
# pattern = r"\whello"

# text = """Hello ,hellloooo space ello"""

# match = re.search(pattern, text)
# if match:
#     print(match)


pattern = r"[Hh]ello"
pattern1 = r"\d{4}"
text = "Hello world! 3444 hello again. 1234"

# matches = re.findall(pattern, text)
matches = re.findall(pattern1, text) #gives the numbers cause we have used r"\d" d-digits
print(matches)  
