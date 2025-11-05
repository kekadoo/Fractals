import turtle as t
t.screensize(2000,2000)
t.tracer(0)
t.lt(90)
def koh(n, a,k):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1, a,k)
        t.rt(k)
        koh(n-1, a/1.5,k)
        t.rt(180)
        koh(n-1, a/1.5,k)
        t.rt(120+k)
        koh(n-1, a/1.5,k)
        t.rt(180)
        koh(n-1, a/1.5,k)
        t.rt(k)
        koh(n-1, a,k)
        
        
        

koh(3,100,20)
t.update()
t.exitonclick()
