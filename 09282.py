def can_transform(str1, str2):
    n, m = len(str1), len(str2)
    if m > n:
        return []  
    indices = []
    indnext = 0
    for i in range(m):
        find = False
        for j in range(indnext, n+i-m+1):
            if str1[j] == str2[i]:
                indices.append(j)
                indnext = j+1
                find = True
                break
        if not find:
            indnext += 1
    print(indices)
    if len(indices) == m:
        return indices
    if len(indices) == m-1:
        ind = indices[0]
        for i in indices:
            if ind == i:
                ind += 1
            else:
                indices.append(ind)
                indices.sort()
    return []
str1 = "aaaaa"
str2 = "abc"
result= can_transform(str1, str2)
print(result)
