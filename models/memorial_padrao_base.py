class MemorialPadraoBase:

    def __init__(self, titulo_carimbo, arquitetx, genero_arquitetx, cau):
        self.titulo_carimbo = titulo_carimbo
        self.arquitetx = arquitetx
        self.genero_arquitetx = genero_arquitetx
        self.cau = cau
  

    def identificaArquitetx(self):
        x = "x"
        if self.genero_arquitetx == "Masculino":
            x = "o"
        elif self.genero_arquitetx == "Feminino":
            x = "a"

        return f"Arquitet{x} {self.arquitetx} CAU {self.cau}"