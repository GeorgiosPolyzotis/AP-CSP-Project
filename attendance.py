#funtion to create or find an attendance list within a larger list
def find_or_create_attendance_list(main_list, date):
    found_list = check_list(main_list, date)
    if found_list != None:
        return found_list
    else:
        new_date_attendance = [date]
        main_list.append(new_date_attendance)
        return new_date_attendance

#function to add students to a list
def add(main_list,date):  
    date_attendance = find_or_create_attendance_list(main_list,date)
    add = int(input("How many people would you like to add?(Number)"))
     
    for student in range(add):  
        studentname = str(input("Input person names that you want to add."))
        date_attendance.append(studentname)
    

#function to delete students from a list
def delete(main_list,date):
    date_attendance = check_list(main_list,date)
    if date_attendance != None:
        
        deletedstudents = int(input("how many people would you like to remove?(Number)"))
       
        for student in range(deletedstudents):   
            studentname = str(input("Input name of the person you want to delete:"))
            if studentname in date_attendance:
                date_attendance.remove(studentname)
            else:
                print("the person does not exist")
    else:   
        print("The list does not exist.")
            
    
#function to check to see if a list exists within the main list  
def check_list(main_list, date):
    for date_attendance in main_list:
        if date_attendance[0] == date:
            return date_attendance
    return None

#function to display a list of students
def print_date(main_list,date): 
    listExists = check_list(main_list,date)
    if listExists == None:  
        print("list does not exist")
    else:
        print(listExists)


#function to ask the user for which action they would like to perform
def actions(main_list):   
     
     choice = input("Would you like to add or create, print, or delete from an existing roster (add/print/delete)")
     
     if choice == "add":    
        date = input("Input the date/name of the roster you want to add to (e.g. 12/7)")
        add(main_list,date)
     if choice == "print":  
         date = input("Input the date/name of the roster you want to print (e.g. 12/7) ")
         print_date(main_list,date)
     if choice == "delete":
         date = input("Input the date/name of the roster you want to delete from (e.g. 12/7)")
         delete(main_list, date)
#initializing the main list    
main_list = []
print("Hello. This is a program that is used to make and manipulate rosters.")    
#sets a conditional to perform a loop based on the user's input
choice = "y"
while choice == "y": 
       
     actions(main_list)
     
     choice = input("Would you like to perform a further function? Warning: your data will be lost if you exit (y/n)")
     while choice != "y" and choice != "n":    
         print("input is not valid. please try again.")
         choice = input("Would you like to perform a further function? Warning: your data will be lost if you exit (y/n)")
     

     if choice == "n":   
         print("Goodbye!")