n_ls = [5, 1, 2, 1, 4,]
n_ls= sorted(n_ls)
s_ls = set(n_ls)
value=[]
dub_value=[]
if n_ls == []:
    #O(1)
    print(None)
elif n_ls == sorted(list(s_ls)):
    # O(1)
    print(None)
else:
   for i in n_ls:
       #o(i)
           if i  not in value:
               value.append(i)
           else:
               dub_value.append(i)

print(set(dub_value))






#print(s_ls)
