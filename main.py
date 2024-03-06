def main():

    horizontalline = [
        "   ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", '\n'
    ]

    playfield = []
    for i in range(1, 11):
        if i < 10:
            playfield.append(f"{str(i)} ")
        else:
            playfield.append(f"{str(i)}")
        for i in range(1, 11):
            playfield.append("O")
        playfield.append("\n")

    interfacePlayfield = horizontalline + playfield

    print(' '.join(interfacePlayfield))

    print(playfield)

main()
