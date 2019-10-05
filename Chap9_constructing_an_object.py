class Animal:
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'puppy'
        self._name = kwargs['name'] if 'name'in kwargs else 'Theodor'
        self._sound = kwargs['sound'] if 'sound'in kwargs else 'back-back'

    def type(self):
        return self._type
    
    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if isinstance(o, Animal):
        print('The {} is named {} and sais "{}"'.format(o.type(), o.name(), o.sound()))
    else:
        raise TypeError('print_animal(): function accepts an object of class Animal().')

def main():
    a1 = Animal(type='kitten', name='Fluffy', sound='meow')
    a2 = Animal(type='duck', name='Donald', sound='quack')
    print_animal(a1)
    print_animal(a2)
    print_animal(Animal(type='velociraptor', name='Veronica', sound='rwar'))
    print_animal(Animal())

if __name__ == '__main__': main()