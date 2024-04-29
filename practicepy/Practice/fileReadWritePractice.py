def readWrite():
    # file = open("../IOFiles/input.txt","r")
    # content = file.read()
    # print(content)

    with open("../IOFiles/input.txt", "r") as infile:
        with open("../IOFiles/output.txt", "w") as outfile:
            lines = infile.readlines()

            print(f"type is = {type(readed)}")
            for line in lines:
                #print(f"line is  :{line}")
                newLine=line.upper()
                #print(f"new line is {newLine}")
    # Modify content if needed
                outfile.write(newLine)

readWrite()