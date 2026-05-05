import customtkinter as ctk

class GUIProteina:
    def __init__(self):
        self.app = ctk.CTk()
        self.app.title("Simulador de plegamiento proteico")
        self.app.geometry("760x500")

        # ----------- COLORES -----------

        rojo = "#FF6B6B"
        azul = "#4D96FF"
        verde = "#6BCB77"
        morado = "#9D4EDD"

        # ----------- TÍTULO -----------

        self.label1 = ctk.CTkLabel(self.app, text="Simulador de plegamiento proteico", font=("Arial", 18))
        self.label1.grid(row=0, column=0, columnspan=5, pady=15)

        self.label2 = ctk.CTkLabel(self.app, text="Selecciona aminoácidos")
        self.label2.grid(row=1, column=0, columnspan=5)

        # ----------- FILA 1 -----------

        self.botonA = ctk.CTkButton(self.app, text="Alanina (A)", fg_color=rojo)
        self.botonA.grid(row=2, column=0, padx=(10,5), pady=5, sticky="we")

        self.botonV = ctk.CTkButton(self.app, text="Valina (V)", fg_color=rojo)
        self.botonV.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        self.botonL = ctk.CTkButton(self.app, text="Leucina (L)", fg_color=rojo)
        self.botonL.grid(row=2, column=2, padx=5, pady=5, sticky="we")

        self.botonI = ctk.CTkButton(self.app, text="Isoleucina (I)", fg_color=rojo)
        self.botonI.grid(row=2, column=3, padx=5, pady=5, sticky="we")

        self.botonM = ctk.CTkButton(self.app, text="Metionina (M)", fg_color=rojo)
        self.botonM.grid(row=2, column=4, padx=5, pady=5, sticky="we")

        # ----------- FILA 2 -----------

        self.botonF = ctk.CTkButton(self.app, text="Fenilalanina (F)", fg_color=rojo)
        self.botonF.grid(row=3, column=0, padx=(10,5), pady=5, sticky="we")

        self.botonW = ctk.CTkButton(self.app, text="Triptofano (W)", fg_color=rojo)
        self.botonW.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        self.botonY = ctk.CTkButton(self.app, text="Tirosina (Y)", fg_color=rojo)
        self.botonY.grid(row=3, column=2, padx=5, pady=5, sticky="we")

        self.botonK = ctk.CTkButton(self.app, text="Lisina (K)", fg_color=verde)
        self.botonK.grid(row=3, column=3, padx=5, pady=5, sticky="we")

        self.botonR = ctk.CTkButton(self.app, text="Arginina (R)", fg_color=verde)
        self.botonR.grid(row=3, column=4, padx=5, pady=5, sticky="we")

        # ----------- FILA 3 -----------

        self.botonH = ctk.CTkButton(self.app, text="Histidina (H)", fg_color=verde)
        self.botonH.grid(row=4, column=0, padx=(10,5), pady=5, sticky="we")

        self.botonD = ctk.CTkButton(self.app, text="Aspártico (D)", fg_color=morado)
        self.botonD.grid(row=4, column=1, padx=5, pady=5, sticky="we")

        self.botonE = ctk.CTkButton(self.app, text="Glutámico (E)", fg_color=morado)
        self.botonE.grid(row=4, column=2, padx=5, pady=5, sticky="we")

        self.botonS = ctk.CTkButton(self.app, text="Serina (S)", fg_color=azul)
        self.botonS.grid(row=4, column=3, padx=5, pady=5, sticky="we")

        self.botonT = ctk.CTkButton(self.app, text="Treonina (T)", fg_color=azul)
        self.botonT.grid(row=4, column=4, padx=5, pady=5, sticky="we")

        # ----------- FILA 4 -----------

        self.botonN = ctk.CTkButton(self.app, text="Asparagina (N)", fg_color=azul)
        self.botonN.grid(row=5, column=0, padx=(10,5), pady=5, sticky="we")

        self.botonQ = ctk.CTkButton(self.app, text="Glutamina (Q)", fg_color=azul)
        self.botonQ.grid(row=5, column=1, padx=5, pady=5, sticky="we")

        self.botonG = ctk.CTkButton(self.app, text="Glicina (G)", fg_color=azul)
        self.botonG.grid(row=5, column=2, padx=5, pady=5, sticky="we")

        self.botonP = ctk.CTkButton(self.app, text="Prolina (P)", fg_color=azul)
        self.botonP.grid(row=5, column=3, padx=5, pady=5, sticky="we")

        self.botonC = ctk.CTkButton(self.app, text="Cisteina (C)", fg_color=azul)
        self.botonC.grid(row=5, column=4, padx=5, pady=5, sticky="we")

        # ----------- CADENA -----------

        self.label3 = ctk.CTkLabel(self.app, text="Cadena generada")
        self.label3.grid(row=6, column=0, columnspan=5, pady=(20,5))

        self.label14 = ctk.CTkLabel(self.app, height=40, text="")
        self.label14.grid(row=7, column=0, columnspan=5, padx=20, sticky="we")

        # ----------- BOTONES FINALES -----------

        self.boton_graficar = ctk.CTkButton(self.app, text="Graficar", fg_color="#000BCF")
        self.boton_graficar.grid(row=8, column=1, pady=15)
        
        self.boton_borrar_uno = ctk.CTkButton(self.app, text="Borrar último", fg_color="#E67E22")
        self.boton_borrar_uno.grid(row=8, column=2, pady=15)

        self.boton_limpiar = ctk.CTkButton(self.app, text="Limpiar", fg_color="#CF0061")
        self.boton_limpiar.grid(row=8, column=3, pady=15)

