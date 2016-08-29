"""
CP1404/CP5632 Practical
Colour Codes names in a dictionary
"""

COLOUR_CODES = dict((k.lower(), v) for k, v in
                   {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "beige": "#f5f5dc",
                    "black": "#000000",
                    "BlanchedAlmond": "#ffebcd", "BlueViolet": "#8a2be2", "burlywood": "#deb887", "CadetBlue": "#5f9ea0", "chocolate": "#d2691e", "CornflowerBlue": "#6495ed"}.items())

print("Colour Options:")
for colour in COLOUR_CODES:
    print(colour.upper())

colour = input("Enter colour: ").lower()
while colour != "":
    if colour.lower() in COLOUR_CODES:
        print(colour.upper(), "is", COLOUR_CODES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()