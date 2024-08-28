

class ToDo:
    def __init__(self):
        self.tasks= []


    def addTask(self,task):
        
        self.tasks.append(task)
        print(f"Task '{task}' added to the list. ")

    def removeTask(self,task):
        
        
            
            if task in self.tasks:
                self.tasks.remove(task)
                
                print(f"Task '{task}' have been removed. ")
            else:
                print(f"Task '{task}' was not found")

    
            

    def displayTasks(self):
        if self.tasks:
            print("Current Tasks: ")
            for i, task in enumerate(self.tasks, start=1):
                print(f"Task {i}. {task}")
        else:
            print("There are no tasks currently")

    def markTask(self,task):
        if task in self.tasks:
            
            print(f"'{task}' has been marked as completed.")
        else:
            print(f"'{task}' is not in your to-do list.")



def main():
    todo_list= ToDo()
      
    while True:
        print("\n----------To-Do List------------")
        print("1. Display Tasks")
        print("2. Add Tasks")
        print("3. Mark Tasks")
        print("4. Remove Tasks")
        print("5. Exit")

        choice = input("Choose on which task you want to add: ")
        if choice== "1":
            todo_list.displayTasks()

           
        elif choice== "2":
            task = input("Enter task to add: ")
            todo_list.addTask(task)
           
                        
        elif choice== "3":
            task = (input("Enter task to mark as completed: "))
            todo_list.markTask(task)
          
        elif choice == "4":
            task = input("Enter task to remove: ")
            todo_list.removeTask(task)
           
        elif choice== "5":
            print("Tasks saved. Exit...")
            break
        else:
            print("Invalid choice, Please try again")

if __name__=="__main__":
    main()

