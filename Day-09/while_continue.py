# While continue

count = 0
while count <= 10:
    if count % 2 == 1:
        count += 1
        continue
    print("Hello", count)
    count += 1
    
