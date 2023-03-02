# Weight calculator based on gravitational forces from different planets

def weight_calc():

    # Asks user input for weight
    weight = int(input('How much do you weigh in pounds? '))
    print()

    # Asks user which planet they would like to measure their weight for
    planet_select = input('What planet would you like to use? (Venus, Earth, Mars, Jupiter, Saturn, Neptune, Uranus, Mercury) ')    # weight = mass * gravity
    print()
    planet_selection = planet_select.upper()
    
    # Planets and their respective gravitationa;l forces
    planets = {'VENUS': 8.7, 'EARTH': 9.8, 'MARS': 3.721, 'JUPITER': 24.79, 'SATURN': 10.44, 'NEPTUNE': 11.15, 'URANUS': 8.87, 'MERCURY':3.7}

    # Checks to see if planet is in dictionary; if so passes values to the equation
    if planet_selection in planets:
        # Takes the weight value of the chosen planet and plugs it into a weight calculating equation
        new_weight = (weight/9.81) * planets[planet_selection]
        print(f'Your weight on {planet_selection} is {new_weight} lbs.')
        run = input('Would you like to calculate your weight again? y or n: ')
        # Asking user if they would like to calculate their weight again
        if run == 'y':
            weight_calc()
        else:
            pass
    




weight_calc()
