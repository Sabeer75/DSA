s = "(a+b)*c"

rev = s[::-1]

rev = rev.replace("(", "#")
rev = rev.replace(")", "(")
rev = rev.replace("#", ")")
print(rev)
