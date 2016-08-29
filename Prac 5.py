"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = dict((k.lower(), v) for k, v in
                   {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory",
                    "WA": "Western Australia",
                    "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}.items())


for state in STATE_NAMES:
    print(state.upper(), ": ", STATE_NAMES[state])

state = input("Enter short state: ").lower()
while state != "":
    if state.lower() in STATE_NAMES:
        print(state.upper(), "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").lower()
