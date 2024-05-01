def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with text and numbers: 98765\n")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("File created successfully.")

def read_and_display():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            print(file.read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("67890\n")
            file.write("Another line appended: 54321\n")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print("An error occurred:", e)
    else:
        print("Content appended successfully.")

def main():
    create_file()
    read_and_display()
    append_to_file()
    read_and_display()

if __name__ == "__main__":
    main()
