def main():
    import random
    quick_pick_lines = int(input("How many quick picks? "))
    for i in range(quick_pick_lines):
        create_quick_pick = sorted([random.randint(1,45) for i in range(6)])
        print(create_quick_pick)

main()
