#Used to slurp contents of file pelican.txt
pelican_file = open("pelican.txt", "r")
print(pelican_file)
print()

#Type of data is '_io.TextIOWrapper'
print(type(pelican_file))
print()

#Output to a list
line = pelican_file.read().splitlines()
print(line)
print()

#Number of items in list
print("Number of Items in List:",len(line))
print()

#Print contents of the file
with open("pelican.txt", "r") as infile:
    for line in infile:
        print(line, end="")
