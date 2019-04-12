class par(object):
    x = 1
class c1(par):
    pass
class c2(par):
    pass

print(par.x,c1.x,c2.x)
c1.x=2
print(par.x,c1.x,c2.x)
par.x=3
print(par.x,c1.x,c2.x)