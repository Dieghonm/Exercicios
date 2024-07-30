import tkinter as tk

contador = 0

def contador_label(lblRotulo):
    global contador
    contador = contador + 1
    lblRotulo.config(text=str(contador))
    lblRotulo.after(1000, contador_label, lblRotulo)  # Chama a função novamente após 1000 ms

janela = tk.Tk()
janela.title("Contagem dos Segundos")

lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()

# Inicia a contagem
contador_label(lblRotulo)

btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()

janela.mainloop()