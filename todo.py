def do():
    task=[]
    print("-----------Welome-------------")
    num=int(input("Enter the number of task:"))
    for i in range(1,num+1):
        tname=input(f"Enter task {i}= ")
        task.append(tname)
    print("Todays task are:",task)
    choice=int(input("Entet choice :1-Add\n2-update\n3-Delete\n4-View\n5-End"))

    
    while True:
        if choice==1:
            adds=input(" \n Enter the task to input:")
            task.append(adds)
            print(f"task'{adds}' is added successfully!!")
            break
        elif choice==2:
            upd=input("Entet the task you want to update:")
            if upd in task:
                idx=task.index(upd)
                val=("Enter the new task:")
                task[idx]==val
            print(f"Task {upd} is updated successfully!!")
            break
        elif choice==3: 
            dil=input("Enter the element to delete:")
            if dil in task:
                task.remove(dil)
                print(f"Task {dil} is deleted successfully")
                break
        elif choice==4:
            print(task)
            break

        else:
            print("loging out... \n Thank you")
            break
do()