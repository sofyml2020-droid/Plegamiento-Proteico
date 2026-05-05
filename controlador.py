import matplotlib.pyplot as plt
import networkx as nx
from codigo import Cadena, Clasificador, OrganizadorEspacial, Visualizador
from guiproteina import GUIProteina

class ControladorProteina:
    def __init__(self, gui):
        self.gui = gui
        self.cadena = Cadena()
        self.clasificador = Clasificador()
        self.organizador = OrganizadorEspacial()
        self.visualizador = Visualizador()
        
        self.conectar_interfaz()

    def conectar_interfaz(self):
        self.gui.botonA.configure(command=self.presion_A)
        self.gui.botonV.configure(command=self.presion_V)
        self.gui.botonL.configure(command=self.presion_L)
        self.gui.botonI.configure(command=self.presion_I)
        self.gui.botonM.configure(command=self.presion_M)
        self.gui.botonF.configure(command=self.presion_F)
        self.gui.botonW.configure(command=self.presion_W)
        self.gui.botonY.configure(command=self.presion_Y)
        self.gui.botonK.configure(command=self.presion_K)
        self.gui.botonR.configure(command=self.presion_R)
        self.gui.botonH.configure(command=self.presion_H)
        self.gui.botonD.configure(command=self.presion_D)
        self.gui.botonE.configure(command=self.presion_E)
        self.gui.botonS.configure(command=self.presion_S)
        self.gui.botonT.configure(command=self.presion_T)
        self.gui.botonN.configure(command=self.presion_N)
        self.gui.botonQ.configure(command=self.presion_Q)
        self.gui.botonG.configure(command=self.presion_G)
        self.gui.botonP.configure(command=self.presion_P)
        self.gui.botonC.configure(command=self.presion_C)

        # Botones de control
        self.gui.boton_borrar_uno.configure(command=self.borrar_ultimo)
        self.gui.boton_graficar.configure(command=self.graficar)
        self.gui.boton_limpiar.configure(command=self.limpiar)

    def presion_A(self): 
        self.agregar_aa("A")
    def presion_V(self): 
        self.agregar_aa("V")
    def presion_L(self): 
        self.agregar_aa("L")
    def presion_I(self): 
        self.agregar_aa("I")
    def presion_M(self): 
        self.agregar_aa("M")
    def presion_F(self): 
        self.agregar_aa("F")
    def presion_W(self): 
        self.agregar_aa("W")
    def presion_Y(self): 
        self.agregar_aa("Y")
    def presion_K(self): 
        self.agregar_aa("K")
    def presion_R(self): 
        self.agregar_aa("R")
    def presion_H(self): 
        self.agregar_aa("H")
    def presion_D(self): 
        self.agregar_aa("D")
    def presion_E(self): 
        self.agregar_aa("E")
    def presion_S(self): 
        self.agregar_aa("S")
    def presion_T(self): 
        self.agregar_aa("T")
    def presion_N(self): 
        self.agregar_aa("N")
    def presion_Q(self): 
        self.agregar_aa("Q")
    def presion_G(self): 
        self.agregar_aa("G")
    def presion_P(self): 
        self.agregar_aa("P")
    def presion_C(self): 
        self.agregar_aa("C")
    
    def borrar_ultimo(self):
        if self.cadena.eliminar_ultimo():
            simbolos = [aa.simbolo for aa in self.cadena.obtener()]
            nuevo_texto = " ".join(simbolos)
            self.gui.label14.configure(text=nuevo_texto)
    def agregar_aa(self, letra):
        if self.cadena.agregar(letra):
            actual = self.gui.label14.cget("text")
            self.gui.label14.configure(text=f"{actual} {letra}".strip())

    def limpiar(self):
        self.cadena = Cadena()
        self.gui.label14.configure(text="")

    def graficar(self):
        if not self.cadena.aminoacidos: return
        
        grupos = self.clasificador.clasificar(self.cadena)
        posiciones = self.organizador.organizar(grupos)
        G, pos_final, colores = self.visualizador.obtener_datos(self.cadena, posiciones)
        
        plt.figure(figsize=(7,7))
        nx.draw(G, pos_final, with_labels=True, 
                labels=nx.get_node_attributes(G, 'label'),
                node_color=colores, node_size=800)
        plt.title("Plegamiento Proteico")
        plt.show()

    def run(self):
        self.gui.app.mainloop()


vista = GUIProteina()
app = ControladorProteina(vista)
app.run()