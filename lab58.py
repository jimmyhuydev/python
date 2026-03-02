stop = int(input())

for a in range(5):
    result = 0
    
    for b in range(4):
        result += b
    
    result += a
    
    print(result)
    
    if result > stop:
        break

