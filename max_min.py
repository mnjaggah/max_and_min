def find_max_min(n):
    lst = []
    max_num = n[0]
    min_num = n[0]
    for num in n:
        if num >= max_num:
            max_num = num
    for num in n:
        if num <= min_num:
            min_num = num
            
    lst.append(min_num)
    lst.append(max_num)
    return lst  
    
        
