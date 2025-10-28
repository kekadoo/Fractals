import turtle as t

t.screensize(20000,20000)
t.tracer(0)

def koh(n,a):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1, a/3)
        t.lt(60)
        koh(n-1, a/3)
        t.rt(120)
        koh(n-1, a/3)
        t.lt(60)
        koh(n-1, a/3)



koh(1,300)

t.update()
t.exitonclick()