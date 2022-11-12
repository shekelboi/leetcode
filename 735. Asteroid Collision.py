def asteroidCollision(asteroids: [int]):
    result = []

    a2 = asteroids.pop()
    while len(asteroids) != 0:
        a1 = asteroids.pop()

        if a1 < 0 and a2 > 0:
            result.append(a2)
            a2 = a1


a = [5, 10, -5]
print(a)
