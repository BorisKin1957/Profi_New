import re

print(re.sub(r'\b(\w)(\w)', r'\g<2>\g<1>', input()))

'''My previous solution:
import re

result = re.sub(r'\b(\w)(\w)', r'\2\1', input())
print(result)'''