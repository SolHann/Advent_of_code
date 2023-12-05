def p1(input):
    sum = 0
    for game in items:
        game_possible = True

        id, game_result = game.split(':')
        id = id.split()[1]

        subsets = game_result.split(';')
        for subset in subsets:
            subset = subset.split(',')

            for cubes in subset:
                _, no_of_cubes, cube_colour = (cubes.split(' '))
                if cube_colour == 'blue' and int(no_of_cubes) > 14:
                    game_possible = False
                if cube_colour == 'green' and int(no_of_cubes) > 13:
                    game_possible = False
                if cube_colour == 'red' and int(no_of_cubes) > 12:
                    game_possible = False

        if game_possible:
            sum += int(id)
    return sum


def p2 (input):
    sum = 0
    for game in items:
        min_blue,min_green,min_red =0,0,0

        id, game_result = game.split(':')
        id = id.split()[1]

        subsets = game_result.split(';')
        for subset in subsets:
            subset = subset.split(',')

            for cubes in subset:
                _, no_of_cubes, cube_colour = (cubes.split(' '))
                if cube_colour == 'blue' and int(no_of_cubes) > min_blue:
                    min_blue = int(no_of_cubes)
                if cube_colour == 'green' and int(no_of_cubes) > min_red:
                    min_red = int(no_of_cubes)
                if cube_colour == 'red' and int(no_of_cubes) > min_green:
                    min_green = int(no_of_cubes)

        power = min_blue * min_red * min_green
        sum += power

    return sum

with open('input.txt', 'r') as f:
    items = [line.strip() for line in f]
    print(p1(items))
    print(p2(items))
