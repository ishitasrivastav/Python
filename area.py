pi=3.14
def circle (a):
    print (pi*a*a) #area of circle
    print(2*pi*a)   #circumference

circle(3)

def rectangle(l,b):
    print (l*b)       #area of rectangle
    print(2*(l+b))    #perimeter
rectangle(2,3)

def square(a):
    print (a*a)    #area of square
square (4)

price=20
def books (n):
    print ("price of books =" ,n*price)  #price of n books
books(10)

def triangle (x,y):
    print ("area=", ((x*y)/2))  #area of right angle triangle

triangle(2,3)

def cy(r,h):
    print (pi*r*r*h)   #volume of cylinder
cy(2,3)

def tri(h,v):
    b=(((h*h)-(v*v))**(1/2))   #base of triangle
    print (b)
tri(4,2)    


    
