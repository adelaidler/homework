output = open("pelican.txt", "w")
#on a new line
output.write("A wonderful bird is the pelican,")
output.close()
#
#
output = open("pelican.txt", "a")
#on a new line
output.write("\nHis bill holds more than his belican,")
output.close()
#
#
output = open("pelican.txt", "a")
lines = ["\nHe can take in his beak,", "\nEnough food for a week,",
         "\nBut I'm damned if I see how the helican."]
#Use "\n" to start new line of text
#Write a specific line
output.writelines(lines)
output.close()
print(lines)
#