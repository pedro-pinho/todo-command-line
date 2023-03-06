while True:
    with open("coin_flip.txt", "r") as file:
        sides = file.readlines()
    heads_or_tails = input("Throw the coin and enter head or tail here: ? ") + "\n"

    sides.append(heads_or_tails)

    with open("coin_flip.txt", "w") as file:
        file.writelines(sides)

    nr_heads = sides.count("head\n")
    probability = nr_heads / len(sides) * 100

    print(f"Heads {probability}%")

