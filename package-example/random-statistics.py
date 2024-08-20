## 隨機模組
import random as rd

## 隨機選取
sequence = [1, 4, 6, 9, 15, 37]
result = rd.choice(seq=sequence)
print(result)

result = rd.sample(sequence, k=3)
print(result)

result = rd.choices(sequence, k=10)  # 取後放回 (sampling with replacement)
print(result)

## 隨機排序
rd.shuffle(sequence)
print(sequence)

## 抽取 uniform random number
print(rd.random())  # U(0, 1)
print(rd.uniform(a=0.0, b=1.0))
print(rd.uniform(a=10.0, b=15.0))

## 抽取 normal random number
print(rd.normalvariate(mu=0, sigma=1))

## 統計模組
import statistics as stat

print("mean:", stat.mean(sequence))
print("median:", stat.median(sequence))
print("sd:", stat.stdev(sequence))