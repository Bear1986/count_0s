
def main():
    prompt = "Enter a number ('Q' to quit)? "
    sentinel = "Q"
    count = 0
    user = ""
    while user != sentinel:
        user = input(prompt)
        count += user.count("0")

    print("You enetered", count, "zeroes")

main()