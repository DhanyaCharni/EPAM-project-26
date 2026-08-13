N, B = map(int, input().split())

scholarships = list(map(int, input().split()))

scholarships.sort()

count = 0
spent = 0

for amount in scholarships:
    if spent + amount <= B:
        spent += amount
        count += 1
    else:
        break


print(count)
