def removeOccurrences(s,sub):
    lenSub = len(sub)
    i = 0
    while i < len(s):
        while s[i:i+lenSub] == sub:
            s = s.replace(sub,"")
            
            i -= 1
        
        if i == len(s):
            break
        
        print(s,i)
        i += 1
    return s
print(removeOccurrences("yjyjqnaxlbqnaxlbfss","yjqnaxlb"))