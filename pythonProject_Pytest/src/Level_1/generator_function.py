#how to return values upto a number in sequence()

def gener_fun():
    a=1
    while a<=10:
        return a
        a+=1

print(gener_fun())

def generator_fun():
    a=1
    while a<=10:
        yield a
        a+=1

print(list(generator_fun()))

#what is iter() object