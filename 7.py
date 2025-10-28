import turtle as t

t.screensize(20000,20000)
t.tracer(0)

def koh(n,a):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1, a/2)
        t.lt(90)
        koh(n-1, a/2)
        t.rt(180)
        koh(n-1, a/2)
        t.lt(90)
        koh(n-1, a/2)



koh(1,200)

t.update()
t.exitonclick()