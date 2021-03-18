import cgpa as cg
import tkinter as tk
import tkinter.font as font

def cal():
    
    res = cg.calculate(rollNoEntry.get(),variable.get())
    if res == -1:
        resultLabel = tk.Label(root,justify=tk.LEFT,text="Invalid Roll Number")
        resultLabel.place(x=0,y=180,height=300,width=550)
    else:
        result = ""
        graderesult = ""
        for i in res[:-1]:
            result += i[0] + "\n"
            graderesult += i[1] + "\n"
    
        resultLabel = tk.Label(root,justify=tk.LEFT,text=result)
        resultLabel.place(x=0,y=180,height=300)
        resultLabel2 = tk.Label(root,justify=tk.LEFT,text=graderesult)
        resultLabel2.place(x=500,y=180,height=300)
        grade = "SGPA: " + str(res[-1]) 
        finalGrade = tk.Label(root,justify=tk.CENTER,text=grade)
        finalGrade.place(x=100,y=400,height=100)  

root = tk.Tk()
root.title("Sgpa Calculator")   #Window Title
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.resizable(0,0)

myFont = font.Font(family='Times',size=20)

semesterList = ["1-1","1-2","2-1","2-2","3-1","3-2","4-1","4-2"]
variable = tk.StringVar(root)
variable.set(semesterList[0])

rollNo = tk.StringVar()

rollNoLabel = tk.Label(root,text="Enter Roll No : ")
rollNoLabel['font'] = myFont
rollNoLabel.place(x=5,y=10,width=250,height=50)

rollNoEntry = tk.Entry(textvariable = rollNo,bg = 'white',fg = 'black')
rollNoEntry['font'] = font.Font(size=12)
rollNoEntry.place(x=265,y=20,width=200,height=30)

selectLabel = tk.Label(root,text="Select Semester : ")
selectLabel['font'] = myFont
selectLabel.place(x = 5, y = 70, width = 250, height = 50)

semMenu = tk.OptionMenu(root,variable,*semesterList)
semMenu['font'] = font.Font(family="Helvetica",size=12)
semMenu.place(x=265,y=80,width=200,height=30)

button = tk.Button(text='Check Result',command=cal)
button.place(x= 170,y = 150,width= 150,height=30)

root.mainloop()  #tells Python to run the Tkinter event loop