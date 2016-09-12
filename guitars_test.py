from guitar_info import GuitarInfo

guitar1 = GuitarInfo("Gibson L-5 CES", 1922, 16035.40)
guitar2 = GuitarInfo("Gibson L-10 CES", 2011, 16035.40)
print(guitar1)
print(guitar2)

print("Expected: 94 Got:", guitar1.get_age())
print("Expected: 5 Got:", guitar2.get_age())