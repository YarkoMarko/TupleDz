lst = [["*" for _ in range(3)] for _ in range(3)]

player_dict = {input("Player 1, enter your nickname: "): 0,
               input("Player 2, enter your nickname: "): 0}

lst_keys = list(player_dict.keys())

player1_sign = str(input(f"{lst_keys[0]}, enter your sign: "))
player2_sign = str(input(f"{lst_keys[1]}, enter your sign: "))

round_turn = 0
player_turn = 0

check = True

winner_player1 = False
winner_player2 = False

while True:
    if check:

        for i in range(len(lst_keys)):
            print(f"{lst_keys[i]}: {player_dict[lst_keys[i]]}")

        [print(*x) for x in lst]

        print(f"Round {round_turn + 1}")

    [print(*x) for x in lst]

    choice_row = int(input(f"{lst_keys[player_turn % len(lst_keys)]}, enter row to put your sign: "))
    choice_col = int(input(f"{lst_keys[player_turn % len(lst_keys)]}, enter col to put your sign: "))
    check = False

    if 1 < choice_row > 3 or 1 < choice_col > 3:
        print("You enter wrong place")
        continue

    elif lst[choice_row - 1][choice_col - 1] != "*":
        print("This place is filled")
        continue

    else:
        if round_turn % len(lst_keys) == 0:
            lst[choice_row - 1][choice_col - 1] = player1_sign

        else:
            lst[choice_row - 1][choice_col - 1] = player2_sign

    check = True
    round_turn += 1
    player_turn += 1

    for i in range(len(lst)):
        if lst[i][0] == lst[i][1] == lst[i][2] == player1_sign:
            winner_player1 = True
            break

        elif lst[i][0] == lst[i][1] == lst[i][2] == player2_sign:
            winner_player2 = True
            break

        elif lst[0][i] == lst[1][i] == lst[2][i] == player1_sign:
            winner_player1 = True
            break

        elif lst[0][i] == lst[1][i] == lst[2][i] == player2_sign:
            winner_player2 = True
            break

        elif lst[0][0] == lst[1][1] == lst[2][2] == player1_sign or lst[0][2] == lst[1][1] == lst[2][0] == player1_sign:
            winner_player1 = True
            break

        elif lst[0][0] == lst[1][1] == lst[2][2] == player2_sign or lst[0][2] == lst[1][1] == lst[2][0] == player2_sign:
            winner_player2 = True
            break

    if winner_player1:
        player_dict[lst_keys[0]] += 1

        for i in range(len(lst_keys)):
            print(f"{lst_keys[i]}: {player_dict[lst_keys[i]]}")

        [print(*x) for x in lst]

        print(f"{lst_keys[0]} won")

        break

    elif winner_player2:
        player_dict[lst_keys[1]] += 1

        for i in range(len(lst_keys)):
            print(f"{lst_keys[i]}: {player_dict[lst_keys[i]]}")

        [print(*x) for x in lst]

        print(f"{lst_keys[1]} won")

        break

    if round_turn == 9 and winner_player1 == winner_player2 == False:
        for i in range(len(lst_keys)):
            print(f"{lst_keys[i]}: {player_dict[lst_keys[i]]}")

        [print(*x) for x in lst]

        print(f"Nobody won")

        break
