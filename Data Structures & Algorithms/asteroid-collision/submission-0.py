# [-9,4,-6, 5]

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # create stack
        # Invariant: all asteroids moving right, at that index
        #   - does not include asteroids that have been destroyed asteroids moving left before that index

        # keep track of a diverging_left_asteroids list
        # - all asteroids that have made it past the stack (destroyed all stack asteroids)
        # final output: diverging_left_asteroids + stack (diverging_right_asteroids)

        # walk the list
        # acculuate astroids moving right
        # when we reach an asteroid moving left it collides with asteroids moving right in the stack
        #   - collisions happen with asteroids from the top of the stack down
        #   - UNTIL: left moving asteroid is destroyed OR stack is empty

        stack = []
        diverging_left_asteroids = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                destroyed = False
                while stack:
                    # collisions
                    top_right_moving_asteroid = stack[-1]
                    if top_right_moving_asteroid == abs(asteroid):
                        # both destroyed
                        stack.pop()
                        destroyed = True
                        break
                    elif top_right_moving_asteroid > abs(asteroid):
                        # left moving asteroid destroyed
                        destroyed = True
                        break
                    else:
                        # right moving asteroid destroyed
                        # left continues down the stack colliding with asteroids
                        stack.pop()
                if not destroyed:
                    diverging_left_asteroids.append(asteroid)

        diverging_left_asteroids.extend(stack)
        return diverging_left_asteroids
