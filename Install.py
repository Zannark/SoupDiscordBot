#Install script
import os
import sys

if not os.path.exists("Data"):
    os.makedirs("Data")

if not os.path.exists("Data/Albums.json"):
    with open("Data/Albums.json", mode="w") as Albums:
        Albums.write("{}")

if not os.path.exists("Data/Albums.json"):
    with open("Data/Data.dat", mode="w") as DataFile:
        Email = input("Enter your email: ")
        Password = input("Enter your password: ")
        ID = input("Enter your default channel ID: ")
        Command = input("Enter the play command for your music bot (including prefix): ")

        DataFile.write(Email + "\n")
        DataFile.write(Password + "\n")
        DataFile.write(ID + "\n")
        DataFile.write(Command)
