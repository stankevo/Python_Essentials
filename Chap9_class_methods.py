class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'unknown anymal'
        self._name = kwargs['name'] if 'name'in kwargs else 'chupakabra'
        self._sound = kwargs['sound'] if 'sound'in kwargs else 'chupakabra sound'

    def type(self, t=None):
        if t: self._type = t
        return self._type

    def name(self, n=None):
        if n: self._name = n
        return self._name
    
    def sound(self, s=None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named {self.name()} and sais {self.sound()}.'
    
def main():
    a1 = Animal(type = 'kitten', name = 'Fluffy', sound = 'pur-pur')
    a2 = Animal(type = 'puppy', name = 'Arnold', sound = 'back-back')
    print(a1)
    print(a2)
    print(Animal())
    a1.sound('meow')
    print(a1)

if __name__ == '__main__': main()