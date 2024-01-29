#Write a python program to insert into sorted list

lst = []
fg = 1
while fg:

    val = int (input('Enter Element: '))
    pos = len(lst)-1

    while pos >=0:
        if val >= lst[pos]:
            break
        pos -= 1
    
    if(len(lst) == 0 or pos == len(lst) - 1):
        lst.append(val)
    else:
        lst.insert(pos + 1,val)
    
    print(lst)
    fg = int(input('Do you want to continue (0/1): '))

print('Final list is: ',lst)