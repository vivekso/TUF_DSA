def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    # """
    # reverse_lst = []
    # for i in range(len(s)-1, -1, -1):
    #     print(i)
    #     reverse_lst.append(s[i])
    # return reverse_lst
    reverse_lst = []
    for i in range(len(s)-1, -1, -1):
        
        reverse_lst.append(s[i])
    return reverse_lst

s = ["h","e","l","l","o"]
print(reverseString(s))