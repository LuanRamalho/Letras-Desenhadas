import tkinter as tk

# Função para desenhar uma letra específica no canvas
def draw_letter(canvas, letter, x, y):
    canvas.create_text(x, y, text=letter, font=('Arial', 30), anchor='center')

# Função principal para criar a janela e o canvas
def main():
    root = tk.Tk()
    root.title("Desenho do Alfabeto")

    # Criando o canvas
    canvas = tk.Canvas(root, width=450, height=280, bg='white')
    canvas.pack()

    # Definindo a posição inicial para as letras
    start_x, start_y = 50, 50
    gap = 50  # Espaçamento entre as letras

    # Desenhando o alfabeto
    for index, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        x = start_x + (index % 8) * gap  # Calcula a posição X
        y = start_y + (index // 8) * gap  # Calcula a posição Y
        draw_letter(canvas, letter, x, y)

    # Executando o loop principal
    root.mainloop()

if __name__ == "__main__":
    main()
