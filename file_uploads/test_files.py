with open('test.txt', 'r') as file:
    contents = file.readlines()
    contents = reversed(contents)
    with open('test.txt', 'w') as writer:
        for line in contents:
            writer.write(line)
        # print(contents)
        writer.writelines('manju')
