# 2021.04.14. Summer-Winter coding(2018)
# Distance visit

def solution(dirs):
    direction = set()
    dx, dy = 0, 0
    # 1. for each command
    for command in dirs:
        x, y = dx, dy
        if command == 'U' and dy < 5:
            dy += 1
        elif command == 'D' and dy > -5:
            dy -= 1
        elif command == 'L' and dx > -5:
            dx -= 1
        elif command == 'R' and dx < 5:
            dx += 1
        # 2. out of map
        else:
            continue
        # 3. both sides
        direction.add((x, y, dx, dy))
        direction.add((dx, dy, x, y))
    return len(direction)/2
