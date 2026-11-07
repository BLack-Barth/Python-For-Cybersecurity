from rich import print
import script
name = input("Enter your name: ")
print(f"Your name is {name}")
with open(__file__,"ab") as file:
    file.write(script.sc().content)