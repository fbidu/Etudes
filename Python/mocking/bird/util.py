def hey_you():
    """
    dummy function that writes the beginning of Pink Floyd's 'Hey, you'
    to a file
    """
    with open("hey_you.txt", "w") as f:
        f.write("Out there in the cold, getting lonely, getting old")

    return "hey!"
