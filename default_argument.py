#If you don't specify value of argument in function call then it'll take
#default value

def default(name,age=21):
    print('Name:',name)
    print('Age:',age)
    return

name='Nishtha'
default(name,age='19')
default(name)
