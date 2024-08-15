## break example
n = 0

while n < 5:
    if n == 3:
        break
    n = n + 1
    print("Processing:", n)
print("Exit:", n)
print("=" * 12)

## continue example
n = 0

for i in range(4):
    if i % 2 == 0:
        continue
    print("Processing:", i)
    n += 1
print("Total:", n)
print("=" * 12)

## else example
n = 0

for i in range(11):
    n += i
else:
    print("Total:", n)

## example: Find the square root of an integer
n = int(input("Please enter a integer number:"))

for i in range(n):
    if i * i == n:
        print("The answer is", i)
        break
else:
    print("There does not exist the square root of the integer", n)