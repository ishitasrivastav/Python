try:
    a=int(input('no.='))
    b=20/a
    print (b)
except Exception as e:
    print (type (e))

finally:
    print('bye bye')
