def asteroidCollision(astroids):
    stack = []
    dir = -1
    prevDir = -1
    for i in range(len(astroids)):
        print(stack)
        if stack:
            if (
                (stack[-1] > 0 and astroids[i] > 0)
                or (stack[-1] < 0 and astroids[i] < 0)
                or (stack[-1] < 0 and astroids[i] > 0)
            ):
                stack.append(astroids[i])
            else:
                mag = astroids[i] * -1
                if stack[-1] == mag:
                    stack.pop()
                    continue
                flag = False
                while stack and mag > stack[-1]:
                    print(stack[-1], mag)
                    if mag == stack[-1]:
                        stack.pop()
                        break
                    if stack[-1] < 0:
                        flag = True
                        break
                    stack.pop()
                    print(stack)

                if stack and mag == stack[-1]:
                    stack.pop()
                    continue

                if flag or not stack:
                    stack.append(astroids[i])

        else:
            stack.append(astroids[i])

    return stack


print(asteroidCollision([2, -1, 1, -2]))
