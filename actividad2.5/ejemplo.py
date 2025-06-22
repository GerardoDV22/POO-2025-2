import tkinter as tk

def sumar():
    try:
        num1 = float(entrada1.get())
        num2 = float(entrada2.get())
        resultado.set(str(num1 + num2))
    except ValueError:
        resultado.set("Error")

# Ventana principal
ventana = tk.Tk()
ventana.title("Mi primera calculadora")
ventana.geometry("400x200")
ventana.configure(bg="white")

# Variables
resultado = tk.StringVar()

# Widgets
tk.Label(ventana, text="Primer numero", bg="yellow").place(x=10, y=20)
entrada1 = tk.Entry(ventana, bg="pink")
entrada1.place(x=130, y=20)

tk.Label(ventana, text="Segundo numero", bg="yellow").place(x=10, y=50)
entrada2 = tk.Entry(ventana, bg="pink")
entrada2.place(x=130, y=50)

tk.Button(ventana, text="Sumar", command=sumar).place(x=250, y=45)

tk.Label(ventana, text="Resultado", bg="yellow").place(x=10, y=90)
tk.Entry(ventana, textvariable=resultado, bg="pink").place(x=130, y=90)

ventana.mainloop()

""" vent = tk.Tk()
vent.geometry("300x200")

for i in range(3):
    vent.rowconfigure(i, weight=1)
    vent.columnconfigure(i, weight=1)

tk.Label(vent, text="A", bg="red").grid(row=0, column=0, sticky="nsew")
tk.Label(vent, text="B", bg="green").grid(row=0, column=1, columnspan=2, sticky="nsew")
tk.Label(vent, text="C", bg="blue").grid(row=1, column=0, rowspan=2, sticky="nsew")
tk.Label(vent, text="D", bg="yellow").grid(row=1, column=1, sticky="nsew")
tk.Label(vent, text="E", bg="pink").grid(row=2, column=2, sticky="nsew")

vent.mainloop() """
