import turtle as t
t.screensize(20000,20000)
t.tracer(0)
def koh(n,a):
    if n == 0:
        t.fd(a)
    else:
        koh(n-1, a/2)
        t.rt(90)
        koh(n-1, a/2)
        t.lt(90)


koh(0,500)
t.update()
t.exitonclick()