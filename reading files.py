
# r mean read
# a means adding
# w means overwrite everything in the file
# r+ means modify the file

employee_file = open("employee.txt","r")
print(employee_file.readable())
print(" ")
print(employee_file.read())
print(" ")
print(employee_file.readline())
print(" ")
print(employee_file.readlines())
print(" ")

for employee in employee_file.readlines():
    print(employee)



employee_file.close()