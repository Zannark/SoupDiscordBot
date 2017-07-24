#Install script
import os
import sys

if not os.path.exists("Data"):
    os.makedirs("Data")

if not os.path.exists("Data/Albums.json"):
    with open("Data/Albums.json", mode="w") as Albums:
        Albums.write("{}")
else:
    print("Data/Albums.json already exists, if you wish for a new albums file rename or delete the current one.")

if not os.path.exists("Data/Data.dat"):
    with open("Data/Data.dat", mode="w") as DataFile:
        Email = input("Enter your email: ")
        Password = input("Enter your password: ")
        ID = input("Enter your default channel ID: ")
        Command = input("Enter the play command for your music bot (including prefix): ")

        DataFile.write(Email + "\n")
        DataFile.write(Password + "\n")
        DataFile.write(ID + "\n")
        DataFile.write(Command)
else:
    print("Data/Data.dat already exists, if you wish for a new data file rename or delete the current one.")
