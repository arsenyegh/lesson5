strn=''
#maxlen = 0

def find_longes_line(path):
    maxlen = 0
    ff=open(path)
    for line in ff:
        if len(line)>maxlen:
            maxlen=len(line)
            strn=line
    ff.close()
    return strn.strip()



print("the longest line is ")
print(find_longes_line("data.txt"))