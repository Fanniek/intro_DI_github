file = open("myfile.txt", "r")
lines = file.readlines()
file.close()

new_file = open("myfile2.txt", "w")



for numbers in lines: 
    numbers = numbers.strip()
    numbers = int(numbers)
    new_file.write(str(numbers + 1) + "\n")
    
new_file.close()
