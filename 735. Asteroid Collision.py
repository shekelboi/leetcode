def can_collide(asteroids):
    for i in range(len(asteroids) - 1, 0, -1):
        if asteroids[i] < 0 < asteroids[i - 1]:
            return True
    return False


def asteroidCollision(asteroids):
    counter = len(asteroids) - 1
    while can_collide(asteroids):
        counter = len(asteroids) - 1
        while counter > 0:
            a2 = asteroids.pop(counter)
            counter -= 1
            a1 = asteroids[counter]
            if a2 < 0 < a1:
                if abs(a1) < abs(a2):
                    asteroids.pop(counter)
                    asteroids.insert(counter, a2)
                elif abs(a1) == abs(a2):
                    asteroids.pop(counter)
                    counter -= 1
            else:
                asteroids.insert(counter + 1, a2)
    return asteroids


a = [-2, 2, -1, -2]
print(asteroidCollision(a))
