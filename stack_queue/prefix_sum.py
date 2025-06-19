arr = [1,2,3,-3,1,1,1,4,2,-3]
sum = 0
ps = []

for i in range(len(arr)):
    sum += arr[i] 
    ps.append(sum)
#    ps[i-1] = ps[j] - k
print(ps)
hash = {}
k = 3
cnt = 0
for j in range(len(ps)):
    if ps[j] == k:
        cnt += 1
    val = ps[j] - k
    if val in hash.keys():
        cnt += hash[val]
    if ps[j] not in hash.keys():
        hash[ps[j]] = 1
    else:
        hash[ps[j]] += 1


print(hash)
print(cnt)