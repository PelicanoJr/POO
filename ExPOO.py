class Notebook:
    marca = 'Dell'
    modelo = 'G15'
    processador = 'I7'
    GPU = 'RTX4050'

    def ligar(self):
        print('Ligado')

    def processor_imagem(self):
        print('Processando imagem')

    def desligar(self):
        print('Desligando')


novo = Notebook()

print(novo.marca)
print(novo.GPU)


novo.ligar()
novo.desligar()