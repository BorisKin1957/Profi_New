day = r'(([0-2][0-9])|(3[01]))'
month = r'((0[1-9])|(1[0-2]))'
year = r'\d{4}'
dot = r'\.'

regex = f'{year}{dot}{month}{dot}{day}|{day}{dot}{month}{dot}{year}|{year}/{month}/{day}|{day}/{month}/{year}'



'''My previous solution:

#regex = r''
regex = r'[0-3][0-9]\.[0-1][0-9]\.[0-9]{4}|[0-3][0-9]/[0-1][0-9]/[0-9]{4}
|[0-9]{4}/[0-1][0-9]/[0-3][0-9]|[0-9]{4}\.[0-1][0-9]\.[0-3][0-9]'''