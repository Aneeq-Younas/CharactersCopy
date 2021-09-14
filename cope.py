
def sub_str_copy(string, n):
    copy= 12
    if copy > len(string):
        copy= len(string)
    x= string[:copy]

    result= " "
    for i in range (n):
        result= result + x
    return result

print(sub_str_copy(" Aneeq ", 7))
print(sub_str_copy(" Programmer ", 5))


CharactersCopy

This program create copies of same character