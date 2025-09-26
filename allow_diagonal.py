def mea_traversal(start_x, start_y, goal_x, goal_y, allow_diagonal=False):
    x, y = start_x, start_y

    print(f"Start Position: ({x},{y})")
    print(f"Goal Position: ({goal_x},{goal_y})")
    print("Traversal Path:")

    while x != goal_x or y != goal_y:
        diff_x = goal_x - x
        diff_y = goal_y - y

        if allow_diagonal and diff_x != 0 and diff_y != 0:
            # Take diagonal step
            step_x = 1 if diff_x > 0 else -1
            step_y = 1 if diff_y > 0 else -1
            x += step_x
            y += step_y
            direction = ""
            if step_x == 1 and step_y == 1:
                direction = "UP-RIGHT"
            elif step_x == 1 and step_y == -1:
                direction = "DOWN-RIGHT"
            elif step_x == -1 and step_y == 1:
                direction = "UP-LEFT"
            else:
                direction = "DOWN-LEFT"
            print(f"Move DIAGONAL {direction} → ({x},{y})")

        elif diff_x > 0:
            x += 1
            print(f"Move RIGHT → ({x},{y})")
        elif diff_x < 0:
            x -= 1
            print(f"Move LEFT → ({x},{y})")
        elif diff_y > 0:
            y += 1
            print(f"Move UP → ({x},{y})")
        elif diff_y < 0:
            y -= 1
            print(f"Move DOWN → ({x},{y})")

    print(f" Goal Reached at ({x},{y})")


if __name__ == "__main__":
    start_x = int(input("Enter start X: "))
    start_y = int(input("Enter start Y: "))
    goal_x = int(input("Enter goal X: "))
    goal_y = int(input("Enter goal Y: "))
    allow_diagonal = input("Allow diagonal moves? (y/n): ").lower() == "y"

    mea_traversal(start_x, start_y, goal_x, goal_y, allow_diagonal)
