colors = 'wwwbbbwbbwwb'
countW = 0
countB = 0
subW = 'www'
subB = 'bbb'

for i in range(len(colors) - len(subW) + 1):
    if colors[i:i + len(subW)] == subW:
            countW += 1
    
    
for i in range(len(colors) - len(subB) + 1):
    if colors[i:i + len(subB)] == subB:
        countB += 1
        
if(countW > countB):
    print('wendy')
else:
    print('bob')

