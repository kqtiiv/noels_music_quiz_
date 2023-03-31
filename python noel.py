# Noel music game
import random

# authorised users
users = {
    "usernames": [],
    "passwords": []
}
user = ""


def load_users(dict_of_users):
    with open("authorised_users.txt", "r") as authorised_users:
        for user in authorised_users:
            u, p = user.strip().split()
            dict_of_users["usernames"].append(u)
            dict_of_users["passwords"].append(p)


def new_user():
    new_username = input("Create your username (no spaces, caps sensitive): ")
    new_password = input("Create your password (no spaces, caps sensitive): ")
    # this appends the user and pass
    with open("authorised_users.txt", "a") as authorised_users:
        authorised_users.write(f"{new_username} {new_password}\n")


def authentication(dict_of_users):
    username = input("Enter your username: ").strip()
    existing_users = dict_of_users["usernames"]
    if username in existing_users:
        index = existing_users.index(username)
        password = input("Enter your password: ")
        if dict_of_users["passwords"][index] == password:
            global access_granted
            access_granted = True
            return access_granted
        else:
            print("Incorrect password!")
            global count
            count -= 1
            if count > 0:
                print("try again")
                authentication(dict_of_users)
    else:
        print("This user doesn't exist!")
        authentication(dict_of_users)


def load_songs(dict_of_songs):
    with open("songs.txt") as songs:
        for song in songs:
            n, a = song.strip().split(" - ")
            dict_of_songs["song_name"].append(n)
            dict_of_songs["song_artist"].append(a)


def guess_song(random_song, random_artist):
    # first letter of each word
    first_letters = ""
    for _ in random_song.split():
        first_letters += f"{_[0]} "

    print("Guess the song: ")
    print(f"Artist: {random_artist}, Song: {first_letters}")
    guess = input("Guess the song: ").title()
    return guess


def is_guess_correct(guess):
    global chances, points, random_song, random_artist
    if guess == random_song:
        chances = 2
        points += 1
        print("Correct!\n")
    else:
        chances -= 1
        if chances > 0:
            print("Try again!\n")
            is_guess_correct(guess_song(random_song, random_artist))
        else:
            print("\nGame Over!")
            print(f"Points: {points}")


def load_leaderboard(dictionary):
    with open("leaderboard.txt") as leaderboard:
        for line in leaderboard:
            key, value = line.strip().split(": ")
            dictionary[key] = int(value)


def leaderboard(username, points):
    # this writes the user's points in external file
    with open("leaderboard.txt", "a") as leaderboard:
        leaderboard.write(f"{username}: {points}\n")


def display_leaderboard(dictionary):
    print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░██░▄▄█░▄▄▀█░▄▀█░▄▄█░▄▄▀█░▄▄▀█▀▄▄▀█░▄▄▀█░▄▄▀█░▄▀█▀██
█░██░▄▄█░▀▀░█░█░█░▄▄█░▀▀▄█░▄▄▀█░██░█░▀▀░█░▀▀▄█░█░████
█▄▄█▄▄▄█▄██▄█▄▄██▄▄▄█▄█▄▄█▄▄▄▄██▄▄██▄██▄█▄█▄▄█▄▄██▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
""")
    # this creates a list of the top 5 players
    top_players_list = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    for player in top_players_list[:5]:
        print(f"{player[0]}: {player[1]}")


def play():
    play_again = input("Would you like to play again? Yes or No: ").lower()
    if play_again == "yes":
        return
    if play_again == "no":
        global playing
        playing = False
        return playing
    else:
        print("That is not a valid option!")
        play()


# authentication
access_granted = False
count = 3

while True:
    choice = input("Do you want to register or log in? Type R for register, L for log in: ").upper()
    if choice == "L":
        # load users to dictionary
        load_users(users)
        authentication(users)
        break
    elif choice == "R":
        new_user()
    else:
        print("exited.")
        break

if access_granted:
    print("Access granted")
elif count == 0:
    print("You have been locked out!")

# game
songs = {
    "song_name": [],
    "song_artist": []
}

playing = True

while playing and access_granted:
    points = 0
    chances = 2

    print("""
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▀██░██░▄▄▄░██░▄▄▄██░████░██░▄▄▄░████░▄▀▄░██░██░██░▄▄▄░█▄░▄██░▄▄▀████░▄▄░██░██░█▄░▄██░▄▄▄░██
██░█░█░██░███░██░▄▄▄██░███████▄▄▄▀▀████░█░█░██░██░██▄▄▄▀▀██░███░███████░██░██░██░██░███▀▀▀▄▄██
██░██▄░██░▀▀▀░██░▀▀▀██░▀▀░████░▀▀▀░████░███░██▄▀▀▄██░▀▀▀░█▀░▀██░▀▀▄████▄▄░▀██▄▀▀▄█▀░▀██░▀▀▀░██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
    """)

    while access_granted and chances > 0:
        load_songs(songs)

        # generates random song from the list of songs
        names = songs["song_name"]
        artists = songs["song_artist"]
        random_index = random.randint(0, len(names) - 1)
        random_song = names[random_index]
        random_artist = artists[random_index]
        guess = guess_song(random_song, random_artist)
        is_guess_correct(guess)

    # leaderboard
    top_players = {}

    load_leaderboard(top_players)
    leaderboard(user, points)
    display_leaderboard(top_players)
    play()
