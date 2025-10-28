import turtle as t

t.screensize(20000,20000)
t.tracer(0)

def koh(n,a):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1, a)
        t.lt(120)
        koh(n-1, a/2)
        t.lt(180)
        koh(n-1, a/2)
        t.lt(120)
        koh(n-1, a/2)
        t.lt(180)
        koh(n-1, a/2)
        t.lt(120)
        koh(n-1, a)



koh(1,50)

t.update()
t.exitonclick()
