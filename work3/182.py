import math

p=1009
q=3643
n = p * q
φ = (p-1)*(q-1)
tmp_list = []
tmp = 0 
dic = {}
for e in range(2, φ):
    if (math.gcd(e, φ) == 1):
        tmp_list.append(e)
        dic[e] = (math.gcd(e-1, p-1)+1) * (math.gcd(e-1, q-1)+1)
for e in tmp_list:
    if dic[e] == 9 :
        tmp = tmp + e
print(tmp)
