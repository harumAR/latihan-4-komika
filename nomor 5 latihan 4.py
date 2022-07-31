s= 0
list_kamu = ['abc', 'xyz', 'aba', '1221']
for x in list_kamu:
    if len(x)>=2 and x[0]==x[-1]:
        print(x)
        s = s +1 
print(s)