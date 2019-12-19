def swap_case(s):

    l = list(s)
    for i in range(len(l)):
        if l[i].isupper() == True:
            l[i] = l[i].lower()
        elif l[i].islower() == True:
            l[i] = l[i].upper()
    s = ''.join(l)
  
    return s

