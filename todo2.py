

while True:
    
    todos=open('todolist.txt','a')

    x=input("what todo would you add:  ")
    todos.write(f"{x}\n")
    todos.close()
   
    todos=open('todolist.txt','r')

    print(todos.read())

    todos.close()
    



