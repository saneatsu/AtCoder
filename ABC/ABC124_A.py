# 173 Byte
a, b = map(int, input().split())
coin = 0
for i in range(2):
    if a > b:
        coin += a
        a -= 1
    else:
        coin += b
        b -= 1
print(coin)

"""
78 Byte

c=max(a,b)
d=min(a,b)
e=max(c-1,d)
print(c+e)
"""