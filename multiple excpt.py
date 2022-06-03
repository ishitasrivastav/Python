try:
    a=int(input('no.='))
    b=20/a
    print (b)
except ValueError:
    print('xyz')
except ZeroDivisionError:
    print('infinity')

   
#except(ValueError,ZeroDivisionError):
 #   print('d')
finally:
    print('bye bye')
    
