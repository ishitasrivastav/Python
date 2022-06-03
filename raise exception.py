try:
    n=int(input('enter any no.'))
    pp=(200/n)
    if pp==20:
        raise IOError
except:
    print('exception raised')
else:
    print('value is not equal to 20')
    
