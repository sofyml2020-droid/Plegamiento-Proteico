import math
import networkx as nx
class Aminoacido:
    def __init__(self, simbolo):
        self.simbolo = simbolo
        self.tipo = self.clasificar()

    def clasificar(self):
        hidrofobicos = ["A","V","L","I","M","F","W","Y"]
        positivos = ["K","R","H"]
        negativos = ["D","E"]
        if self.simbolo in hidrofobicos: 
            return "H"
        elif self.simbolo in positivos: 
            return "+"
        elif self.simbolo in negativos: 
            return "-"
        else: 
            return "P"

class Cadena:
    def __init__(self, limite=50):
        self.aminoacidos = []
        self.limite = limite

    def agregar(self, simbolo):
        if len(self.aminoacidos) < self.limite:
            self.aminoacidos.append(Aminoacido(simbolo))
            return True
        return False
    def obtener(self):
        return self.aminoacidos
    def eliminar_ultimo(self):
        if len(self.aminoacidos) > 0:
            self.aminoacidos.pop() # Quita el último de la lista
            return True
        return False
   

class Clasificador:
    def clasificar(self, cadena):
        grupos = {"H":[], "P":[], "+":[], "-":[]}
        for aa in cadena.obtener():
            grupos[aa.tipo].append(aa)
        return grupos


class OrganizadorEspacial:
    def colocar_en_circulo(self, lista, radio):
        posiciones = {}
        n = len(lista)
        if n == 0: 
            return posiciones
        for i, aa in enumerate(lista):
            angulo = 2 * math.pi * i / n
            x = radio * math.cos(angulo)
            y = radio * math.sin(angulo)
            posiciones[aa] = (x, y)
        return posiciones

    def organizar(self, grupos):
        posiciones = {}

        # Hidrofóbicos (centro)
        posiciones.update(self.colocar_en_circulo(grupos["H"], 1.5))

        # Polares (alrededor)
        posiciones.update(self.colocar_en_circulo(grupos["P"], 4))

        # CARGADOS (+ y - INTERCALADOS)
        positivos = grupos["+"]
        negativos = grupos["-"]

        cargados = []
        for p, n in zip(positivos, negativos):
            cargados.append(p)
            cargados.append(n)

        # Agregar los que sobren
        cargados += positivos[len(negativos):]
        cargados += negativos[len(positivos):]

        # Distribuir en círculo externo
        n_c = len(cargados)
        radio = 6

        for i, aa in enumerate(cargados):
            if n_c > 0:
                angulo = 2 * math.pi * i / n_c 
            else:
                angulo=0
            x = radio * math.cos(angulo)
            y = radio * math.sin(angulo)
            posiciones[aa] = (x, y)

        return posiciones


class Visualizador:
    def obtener_datos(self, cadena, posiciones):
        G = nx.Graph()
        lista = cadena.obtener()

        # Crear nodos
        for i, aa in enumerate(lista):
            G.add_node(i, label=aa.simbolo, tipo=aa.tipo)

        # Conexión de secuencia
        for i in range(len(lista)-1):
            G.add_edge(i, i+1)

        pos = {i: posiciones[aa] for i, aa in enumerate(lista)}

        color_dict = {
            "H": "#FF6B6B",
            "P": "#4D96FF",
            "+": "#6BCB77",
            "-": "#9D4EDD"
        }

        colores = [color_dict[G.nodes[i]["tipo"]] for i in G.nodes]

        return G, pos, colores



