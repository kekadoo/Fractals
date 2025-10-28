import turtle as t
t.screensize(2000,2000)

t.tracer(0)
def koh(n,a):
    if n > 0 and a > 0:
        for i in range(4):
            t.fd(a)
            t.rt(90)
        t.up()
        t.rt(8)
        t.fd(0.08 * a)
        t.down()
        koh(n-1,a-(0.1*a))
                
        

koh(1,200)
t.update()
t.exitonclick()