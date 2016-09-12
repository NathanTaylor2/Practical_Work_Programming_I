from guitar_info import GuitarInfo

def main():
    name = input("Name of guitar: ")
    while name != '':
        year = int(input("Year: "))
        cost = int(input("Cost: "))
        guitar = GuitarInfo(name, year, cost)
        name = input("Name of guitar: ")
main()