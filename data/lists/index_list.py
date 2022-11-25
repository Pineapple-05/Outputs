def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    path_ = movements()
    for i in range(0,len(path_), 2):
        print(f"{path_[i]} for {path_[i+1]} steps")

run()