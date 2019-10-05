class Duck:
    sound = 'Quack Quack!'
    movement = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    Donald = Duck()
    Donald.quack()
    Donald.move()

if __name__ == '__main__': main()