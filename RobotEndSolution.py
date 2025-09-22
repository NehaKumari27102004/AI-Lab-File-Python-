def mea_traversal(start_x, start_y, goal_x, goal_y):
    x, y = start_x, start_y

    print(f"Start Position: ({x},{y})")
    print(f"Goal Position: ({goal_x},{goal_y})")
    print("Traversal Path:")

    while x != goal_x or y != goal_y:
        diff_x = goal_x - x
        diff_y = goal_y - y

        if diff_x > 0:
            x += 1   # Move DOWN
            print(f"Move DOWN → ({x},{y})")
        elif diff_x < 0:
            x -= 1   # Move UP
            print(f"Move UP → ({x},{y})")
        elif diff_y > 0:
            y += 1   # Move RIGHT
            print(f"Move RIGHT → ({x},{y})")
        elif diff_y < 0:
            y -= 1   # Move LEFT
            print(f"Move LEFT → ({x},{y})")

    print(f"Goal Reached at ({x},{y})")


if __name__ == "__main__":
    # Take input from user
    start_x = int(input("Enter start X: "))
    start_y = int(input("Enter start Y: "))
    goal_x = int(input("Enter goal X: "))
    goal_y = int(input("Enter goal Y: "))

    mea_traversal(start_x, start_y, goal_x, goal_y)
