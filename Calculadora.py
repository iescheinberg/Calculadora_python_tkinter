from tkinter import *

root = Tk()
root.iconbitmap('calculadora.ico')
root.configure(background="cornflower blue")
root.title("Calculadora Básica")

# Display
display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0
# Funciones
def obtener_numero(n):
    global i
    display.insert(i, n)
    i += 1

def obtener_operacion(operacion):
    global i
    display.insert(i, operacion)
    operacion_longitud = len(operacion)
    i += operacion_longitud


def borrar_display(): 
    display.delete(0, END)


def borrar_numero():
    display_estado = display.get()
    if len(display_estado):
        display_nuevo_estado = display_estado[:-1]
        borrar_display()
        display.insert(0, display_nuevo_estado)
    else:
        borrar_display()

def calcular():
    try:
        display_estado = display.get()
        resultado = eval(display_estado)
        borrar_display()
        display.insert(0, resultado)
    except ZeroDivisionError:
        borrar_display()
        display.insert(0, "Error: Division por cero")
    except Exception as e:
        borrar_display()
        display.insert(0, f"Error: {str(e)}")

# Botones numericos
Button(root, text=' 1 ', command=lambda:obtener_numero(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text=' 2 ', command=lambda:obtener_numero(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text=' 3 ', command=lambda:obtener_numero(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text=' 4 ', command=lambda:obtener_numero(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text=' 5 ', command=lambda:obtener_numero(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text=' 6 ', command=lambda:obtener_numero(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text=' 7 ', command=lambda:obtener_numero(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text=' 8 ', command=lambda:obtener_numero(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text=' 9 ', command=lambda:obtener_numero(9)).grid(row=4, column=2, sticky=W+E)

# Botones accesorios
Button(root, text=' C ', command=lambda:borrar_display()).grid(row=5, column=0, sticky=W+E)
Button(root, text=' 0 ', command=lambda:obtener_numero(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text=' % ', command=lambda:obtener_operacion('%')).grid(row=5, column=2, sticky=W+E)

# Botones operaciones
Button(root, text=' + ', command=lambda:obtener_operacion('+')).grid(row=2, column=3, sticky=W+E)
Button(root, text=' - ', command=lambda:obtener_operacion('-')).grid(row=3, column=3, sticky=W+E)
Button(root, text=' * ', command=lambda:obtener_operacion('*')).grid(row=4, column=3, sticky=W+E)
Button(root, text=' / ', command=lambda:obtener_operacion('/')).grid(row=5, column=3, sticky=W+E)



# Otros botones
Button(root, text=' ◀️ ', command=lambda:borrar_numero()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text=' exp ', command=lambda:obtener_operacion('**')).grid(row=3, column=4, sticky=W+E)
Button(root, text=' ^2 ', command=lambda:obtener_operacion('**2')).grid(row=3, column=5, sticky=W+E)
Button(root, text=' ( ', command=lambda:obtener_operacion('(')).grid(row=4, column=4, sticky=W+E)
Button(root, text=' ) ', command=lambda:obtener_operacion(')')).grid(row=4, column=5, sticky=W+E)
Button(root, text=' = ', command=lambda:calcular()).grid(row=5, column=4, sticky=W+E, columnspan=2)


root.mainloop()