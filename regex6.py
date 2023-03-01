import re
s = "I am a student of Kbtu, this is my first year."
pattern = s.replace(" ", ":").replace(",",":").replace(".", ":")
print(pattern)