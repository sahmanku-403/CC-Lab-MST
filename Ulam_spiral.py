import turtle

def isprime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return 0
    return 1
turtle.hideturtle()
turtle.speed(0.5)
dist = 5
turtle.right(90)
maxlen= 5000 #set limit here
i = 1
n=1
turtle.penup()
while(i<=maxlen):
    for x in range(0,n):
        if(isprime(i)==1 and i != 1):
            turtle.pendown()
            turtle.circle(1)
            turtle.penup()
        turtle.forward(dist)
        i = i+1
    turtle.left(90)
    for x in range(0,n):
        if(isprime(i)==1):
            turtle.pendown()
            turtle.circle(5)
            turtle.penup()
        turtle.forward(dist)
        i=i+1
    turtle.left(90)
    n = n+1

