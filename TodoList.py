Todo_list = []
Completed_list = []
Deleted_list =[]
print("Enter your choice from Below : ")
print("Enter '1' to Add an Item to the list")
print("Enter '2' to Display the list")
print("Enter '3' to Mark an Item as completed in the list")
print("Enter '4' Close the App")

i=1
while(i<100):

    print("==========Todo- List =========")
    print("Enter your choice from Below : ")
    print("Enter '1' to Add an Item to the list")
    print("Enter '2' to Display the list")
    print("Enter '3' to Mark an Item as completed in the list")
    print("Enter '4' Close the App")
    num =int(input("Enter your Choice : "))

    match num:
        case 1:
            item = input("Enter Your Todo Item : ")
            item = item 
            Todo_list.append(item)       
        case 2:
            final_list= []
            for item in Todo_list:
                final_list.append(item + ": ToDO")
            for item in Completed_list:
                final_list.append(item + ": Done")
            for index, item in enumerate(final_list):
                print(f"{index+1}: {item}")
        case 3:
            if len(Todo_list) > 0:
                for index,item in enumerate(Todo_list):
                    print(f"{index+1}: {item} + :ToDo")    
                mark_item = int(input("Enter an Item To Mark as Complete : "))
                Completed_list.append(Todo_list[mark_item-1])
                del Todo_list[mark_item-1]
            else:
                print("No Items to Mark as Done")
        
        case 4:
            print("App is closing Current Todo Tasks are: ")
            final_list= []
            for item in Todo_list:
                final_list.append(item + ": ToDO")
            for item in Completed_list:
                final_list.append(item + ": Done")
            for index, item in enumerate(final_list):
                print(f"{index+1}: {item}")
        case _:
            print("Invalid Choice")
    print("=======================")
    i=i+1
    if num==4:
        break           