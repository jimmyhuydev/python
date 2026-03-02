user_text = input()

count = 0 
for ch in user_text: 
    if ch not in [' ', '.', '!', ',']: 
        count += 1 

print(count)

