import tkinter as tk
from gui import MiFrame, barra_menu

def main():
    raiz = tk.Tk()
    raiz.title('Socios Asociación Geológica Argentina')
    raiz.iconbitmap('img/aga-logo300-165x165.ico')
    
    barra_menu(raiz)
    MiApp = MiFrame(raiz)

    raiz.mainloop()
if __name__ == '__main__':
    main()