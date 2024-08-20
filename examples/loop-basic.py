## while loop
n = 1
summation = 0

while n <= 10:
    print(f"Num: {n}")
    summation += n
    n += 1
print(f"Sum: {summation}")
print("=" * 12)
## for loop
summation = 0
for num in range(1, 11):
    summation += num
print(summation)

for string in "Hello":
    print(string)

for num in [1, 2, 3, 4, 5]:
    print(num)