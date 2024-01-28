with open("demo.txt", "r") as file :
    content = file.readlines()
    for i in range(0, len(content), 2):
        print(content[i].replace("\n", ""))