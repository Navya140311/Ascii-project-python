  from tkinter import *
 
  root=Tk()
  root.title("Ascii")
  root.geometry("400x400")
  root.configure(background = 'yellow')
 
  enter_word = Entry(root)
  enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
  label = Label(root, text = "Name in Ascii:   ", bg="light blue", fg="black")
  label1 = Label(root, text = "Encrypted Name   ", bg="light blue", fg="black")
  
  def Ascii():
      value= enter_word.get()
      for letter in value :
          label["text"] += str(ord(letter)) + " "
          label_text= label.get()
          decrese=0;
         label_text-=decrese
        decrese1=inr(decrese)
         label["text"] += str(decrese1)+""
         
btn=Button(root,text="Show name in Ascii",command=Ascii, bg='gold',fg='black')
btn.place(relx=0.5, rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.6,anchor=CENTER)
label1.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()
          
