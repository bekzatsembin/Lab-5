import re
l = "abc_defgh_ijkl_mnop qrst uv_wxyz"
pattern = re.findall(r"[a-z]+_[a-z]+",l)
print(pattern)
