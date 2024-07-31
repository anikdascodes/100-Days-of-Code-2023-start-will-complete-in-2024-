
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileExistsError:
    file = open("a_file.txt", "w")
    file.write("something")

except KeyError as error_message:
    print(f"the key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed.")