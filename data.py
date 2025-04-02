with open('data.txt', 'w') as file:
    file.write("Chocolate's embrace\n"),
    file.write("Soft caramel dream at hand,\n")
    file.write("Snickers in my grip.")

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

with open('data.txt', 'a')as file:
    file.writelines('\nIt was delicious for everyone')
    file.close()

with open('data.txt', 'r') as file:
    for line in file:
        print(line, end='')

with open('data.txt', 'rb') as source_file:
    with open('data_copy.txt', 'wb') as copy_file:
        copy_file.write(source_file.read())