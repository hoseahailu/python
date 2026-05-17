karen_rounds = 0
stu_rounds = 0

while not (
    karen_rounds == 6 or stu_rounds == 6 or (karen_rounds == 5 and stu_rounds == 5)
):

    round_winner = input("Who won the round? (Karen/Stu): ")

    match round_winner:
        case "Karen":
            karen_rounds += 1

        case "Stu":
            stu_rounds += 1

        case _:
            print("Invalid name. Try again.")
            continue

    print(f"Score -> Karen: {karen_rounds}, Stu: {stu_rounds}")

print("\nGame Over!")

if karen_rounds > stu_rounds:
    print("Karen wins the game!")
elif stu_rounds > karen_rounds:
    print("Stu wins the game!")
else:
    print("The game ends in a draw at 5-5.")
