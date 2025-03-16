import re, sys

s = []
for line in sys.stdin:
    s.append(line)
print(s)

#s = re.sub(r'\s*#.*', r'', ''.join(s), flags=re.DOTALL)
#print(s)
s = re.sub(r'[\n|A]([\w\W^#]+) #.*\n', r'\1\n', ''.join(s))
#s = re.sub(r'(\n[\s) #.*\n', r'\1\n', ''.join(s))
#s = re.sub(r'#.*\n', r'', ''.join(s))

s = re.sub(r'\s*""".*?"""', r'', ''.join(s), flags=re.DOTALL)

# if re.search(r' {8}', s):
#    s = re.sub(r' {8}', r'    ', s)

print(s)