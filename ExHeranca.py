class Notebook:
    marca = 'Dell'

    def ligar(self):
        print('Ligado')

    def processor_imagem(self):
        print('Processando imagem')

    def desligar(self):
        print('Desligando')


class Notebook_gamer(Notebook) :
    modelo = 'G15'
    processador = 'I7'
    GPU = 'RTX4050'

novo = Notebook()

print(novo.marca)

novo.ligar()
novo.desligar()


novoG = Notebook_gamer()
print(novoG.marca)
print(novoG.GPU)

novoG.ligar()
novoG.desligar()