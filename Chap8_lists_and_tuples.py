def main():
    game = ['Stone', 'Scissors', 'Paper', 'Well', 'Fire']
    print_list(game)

    print('\nReturn value of item with index 3:') # will also work for tuples
    print(game[3])

    print('\nReturn a part of list with indexes from 1 to 4 with step 2:') # will also work for tuples
    print(game[1:4:2])

    print('\nReturn index of item "Paper":') # will also work for tuples
    value = game.index('Paper')
    print(value)

    print('\nAdd one more list item to the end:')
    game.append('Water')
    print_list(game)

    print('\nInsert one list item before item "Fire":')
    game.insert(4, 'Inserted_item')
    print_list(game)

    print('\nDelete the list item "Inserted_item"')
    game.remove('Inserted_item')
    print_list(game)

    print('\nDelete the last list item')
    game.pop()
    print_list(game)

    print('\nDelete the list item with index 2 and display it separately')
    item = game.pop(2)
    print(item)
    print_list(game)

    
    print('\nDelete the list items from index 1 to index 3 with step 2')
    del game[1:4:2]
    print_list(game)

    print('\nJoin list items via separator ", " while printing') # will also work for tuples
    print(', '.join(game))

    print('\nPrint length of the list') # will also work for tuples
    print(len(game))

    print('\nTUPLE:')
    game_tuple = ('Stone', 'Scissors', 'Paper', 'Well', 'Fire')
    print_list(game_tuple)

    print('\nReturn value of item with index 3:') # will also work for tuples
    print(game_tuple[3])

    print('\nReturn a part of list with indexes from 1 to 4 with step 2:') # will also work for tuples
    print(game_tuple[1:4:2])

    print('\nReturn index of item "Paper":') # will also work for tuples
    value = game_tuple.index('Paper')
    print(value)

    print('\nJoin list items via separator ", " while printing') # will also work for tuples
    print(', '.join(game_tuple))

    print('\nPrint length of the list') # will also work for tuples
    print(len(game_tuple))

def print_list(l):
    for i in l:
        print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
