'''
lECTURES, lABS & eXAMS sTUFF
'''

# from IPython import get_ipython
# get_ipython().run_line_magic('reset', '-sf')

# %% Finding Square Root By Guess & Check


def sqrtByGuess(x, step_size=0.001, epsilon=0.01):
    # initial guess for the square root
    guess = 0
    # counter to keep track of the number of steps taken
    count = 0

    while True:
        # check if the square of the guess is close enough to x within the
        # epsilon tolerance
        if abs(guess**2 - x) <= epsilon:
            # print the number of steps taken
            print(f"steps taken: {count}")
            # return the guess as the square root value
            return guess

        # break out of the loop if the guess has passed over the target square root
        if (guess - step_size)**2 < x < guess**2:
            break

        # increase the guess by the step size
        guess += step_size
        # increment the step counter
        count += 1

    # print the number of steps taken when the loop terminates
    print(f"steps taken: {count}")
    # return None if the guess doesn't converge within the loop
    return None


print(sqrtByGuess(2))
print(sqrtByGuess(5))
print(sqrtByGuess(81))

# %% Newton-Raphson to find roots


def sqrtByNewtonRaphson(x, epsilon=0.01):
    # initial guess for the square root
    guess = x / 2.0
    num_guesses = 0

    # iterate until the approximation is within the epsilon tolerance
    while abs(guess * guess - x) >= epsilon:
        num_guesses += 1
        guess += - (((guess ** 2) - x) / (2 * guess))

    # return the results
    return num_guesses, guess


k = 54321
num_guesses, guess = sqrtByNewtonRaphson(k)

print(f'square root of {k} is about {guess} with {
      num_guesses} number of guesses')

# %% Finding Square Roo0t By Bisection Method


def sqrtByBisect(x, epsilon=0.0001):
    low, high = 0, x
    guess = (low + high) / 2
    count = 0

    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess

        guess = (low + high) / 2
        count += 1

    print(f"steps taken: {count}")
    return guess


# test cases
print(sqrtByBisect(2))
print(sqrtByBisect(5))
print(sqrtByBisect(81))

# %% Finding Cube Root For All Real Numbers Cubes By Bisection Method


def cube_root(x, epsilon=0.01):
    # check if the cube is negative and handle it
    neg = False
    if x < 0:
        neg = True
    cube = abs(x)

    # initialize low, high, and guess
    low, high = 0, cube
    guess = (high + low) / 2.0

    # iterate until the guess is close enough to the actual cube root
    while abs(guess ** 3 - cube) >= epsilon:
        if guess ** 3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0

    # if the original cube was negative, return the negative root
    if neg:
        guess = -guess

    # return the guess (the cube root approximation)
    return guess


cube = -27

print(f'{cube_root(cube)} is close to the cube root of {cube}')
