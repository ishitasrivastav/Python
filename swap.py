
def fact(a):
    z=str(a)
    l=len(z)
    f=z[:1]
    c=z[1:l-1]
    la=z[l-1:l]
    return la+c+f
print(fact(7648))


