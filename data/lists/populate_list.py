def directions():
    directions_ = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions_


def menu():
    print("Please select a direction:")
    directions_ = directions()
    for i in range(len(directions_)):
        direction = directions_[i]
        print(f"{direction}: {i}")


def run():
    menu()

run()