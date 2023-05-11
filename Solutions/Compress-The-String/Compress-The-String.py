from itertools import groupby

def hide_and_seek(s):
    out = [(len(list(g)),int(k)) for k, g in groupby(s, key=lambda x:x[0])]      
    return out
               
input_string = input()
print(*hide_and_seek(input_string), sep=' ')
