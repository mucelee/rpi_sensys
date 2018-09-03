#def enum(*sequential, **named):
#        enums = dict(zip(sequential, range(len(sequential))), **named)
#        return type('Enum', (), enums)

def enum(**enums):
        return type('Enum', (), enums)

Numbers = enum(ONE=0, TWO=2, THREE='three')

class SuperEnum(object):
    class __metaclass__(type):
        def __iter__(self):
            for item in self.__dict__:
                if item == self.__dict__[item]:
                    yield item
                     

class Color(SuperEnum):
    red = 1
    green = "2"
    blue = 3


class Peter():    
    def __init__(self):
        self.simpleTest = "foo";
        self.anotherVal = []
        self.anotherVal.append(self.simpleTest)
        self.anotherVal.append("a");
        self.IntegerVar = 2
        self.FloatVar = 23.1
        self.enumTest = Color.green
        self.AnotherEnum = Numbers.THREE