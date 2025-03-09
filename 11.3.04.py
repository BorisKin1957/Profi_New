#regex = r'[A-Z]{1,2}\d(\d?|[A-Z]?)\s\d[^CIKMOV]{2}'

regex = r'[A-Z]{1,2}\d(\d?|[A-Z]?)\s\d[ABD-HJLNPQRSTUW-Z]{2}'

'''My previous regex was:
regex = r'[A-Z]{1,2}\d[A-Z0-9]{,1} \d[A-BD-HJL-NP-UW-Z]{2}'
'''