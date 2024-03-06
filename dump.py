playfield = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

horizontalInterFaceLine = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
interfacePlayfield = []
for i in range(len(horizontalInterFaceLine)):
    interfacePlayfield.insert(0, horizontalInterFaceLine)
    interfacePlayfield.insert(0, playfield)


# print(interfacePlayfield)


verticalPlayfieldLine = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]

for i in range(1,11):
    print(verticalPlayfieldLine[i])
    lines = i * 10
    print(playfield[i-1, lines])

# for row in range(1, 11):
#     print(row)
#     for i in range(1, 11):
#         print(playfield[row * 1])

# for row in range(1, 11):


