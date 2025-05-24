import os


#                      part 2                     #

with open("python/file_operations/test file.txt",'w') as file:
    file.write("Hello i am a Penguin")
    file.write("Come join me in antarctica")

file.close()
file = open("python/file_operations/test file.txt")
print(file.read())
file.close()
print (os.getcwd())

