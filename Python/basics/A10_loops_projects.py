#FOR LOOPS
for i in range(1, 11):
    print(f"Scanning: 192.168.1.{i}")
print()

#CONNECTION RETRY(WHILE LOOP)
attempt = 1
while attempt <= 5:
    if attempt < 4:
        print(f"Attempt {attempt}: Connection failed. Retrying...")
    else:
        print(f"Attempt {attempt}: Connected successfully!")
        break
    attempt += 1