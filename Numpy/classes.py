class Greeter(object):
    """docstring for Greeter"""

    # Constructor
    def __init__(self, name):
        super(Greeter, self).__init__()
        self.name = name
        
    # Instance method
    def greet(self, loud=False):
        if loud:
            print 'HELLO, %s' % self.name.upper()
        else:
            print 'Hello, %s' % self.name

g = Greeter('Fred')

g.greet()
g.greet(loud=True)