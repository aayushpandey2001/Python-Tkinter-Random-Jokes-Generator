import tkinter as tk
import pyjokes
root = tk.Tk()
root.geometry("350x200")
root.configure(bg="yellow")
root.title("Jokes Generator")

def joke():
    global joke
    joke = pyjokes.get_joke()
    T.insert(tk.END,joke)
def clear():
    T.delete("1.0","end")

T=tk.Text(root)
T.place(x=5,y=5,height=80,width=340)
b=tk.Button(root,text="Joke",fg="black",bg="red",command=joke)
b.place(x=55,y=100,height=50,width=100)
b2=tk.Button(root,text="Clear",fg="black",bg="green",command=clear)
b2.place(x=190,y=100,height=50,width=100)

root.mainloop()