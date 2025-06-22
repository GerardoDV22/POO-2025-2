import tkinter as tk

error = False

def escribir(simbolo):
    global error
    if error:
        resultado.set("")  # Limpiar si hubo error antes
        error = False
    resultado.set(resultado.get() + simbolo)

def calcular():
    global error
    try:
        expresion = resultado.get().replace("x", "*").replace("÷", "/")
        resultado.set(str(eval(expresion)))
        error = False
    except Exception:
        resultado.set("Error")
        error = True

def borrar():
    global error
    resultado.set("")
    error = False

v = tk.Tk()
v.geometry("300x500")
v.title("Calculadora Estandar")

for i in range(5):
    v.rowconfigure(i, weight=1)
for i in range(5):
    v.columnconfigure(i, weight=1)

resultado = tk.StringVar()

tk.Entry(v,textvariable=resultado,font=("Arial",45,"bold"),state="readonly").grid(row=0,column=0,columnspan=5,sticky="nsew")

tk.Button(v, text="7",command=lambda: escribir("7"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=1,column=0,sticky="nsew")
tk.Button(v, text="4",command=lambda: escribir("4"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=2,column=0,sticky="nsew")
tk.Button(v, text="1",command=lambda: escribir("1"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=3,column=0,sticky="nsew")
tk.Button(v, text="8",command=lambda: escribir("8"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=1,column=1,sticky="nsew")
tk.Button(v, text="5",command=lambda: escribir("5"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=2,column=1,sticky="nsew")
tk.Button(v, text="2",command=lambda: escribir("2"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=3,column=1,sticky="nsew")
tk.Button(v, text="9",command=lambda: escribir("9"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=1,column=2,sticky="nsew")
tk.Button(v, text="6",command=lambda: escribir("6"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=2,column=2,sticky="nsew")
tk.Button(v, text="3",command=lambda: escribir("3"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=3,column=2,sticky="nsew")
tk.Button(v, text="0",command=lambda: escribir("0"),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=4,column=1,sticky="nsew")
tk.Button(v, text=".",command=lambda: escribir("."),bg="MistyRose3",font=("Arial",15,"bold")).grid(row=4,column=2,sticky="nsew")

tk.Button(v, text="+",command=lambda: escribir("+"),bg="LightSalmon3",font=("Arial",15,"bold")).grid(row=1,column=3,sticky="nsew")
tk.Button(v, text="-",command=lambda: escribir("-"),bg="LightSalmon3",font=("Arial",15,"bold")).grid(row=1,column=4,sticky="nsew")
tk.Button(v, text="x",command=lambda: escribir("x"),bg="LightSalmon3",font=("Arial",15,"bold")).grid(row=2,column=3,sticky="nsew")
tk.Button(v, text="÷",command=lambda: escribir("÷"),bg="LightSalmon3",font=("Arial",15,"bold")).grid(row=2,column=4,sticky="nsew")

tk.Button(v, text="=",command=lambda: calcular(),bg="coral4",font=("Arial",15,"bold")).grid(row=3,column=3,rowspan=2,sticky="nsew")
tk.Button(v, text="C",command=lambda: borrar(),bg="coral4",font=("Arial",15,"bold")).grid(row=3,column=4,rowspan=2,sticky="nsew")

v.mainloop()