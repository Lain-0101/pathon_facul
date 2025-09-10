class Aluno:
    def __init__(self):
        self.notas = []

    def receber_notas(self):
        quantidade = int(input("Digite a quantidade de notas: "))
        for i in range(quantidade):
            nota = float(input(f"Digite a nota {i+1}: "))
            self.notas.append(nota)

    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        media = self.calcular_media()
        print(f"Média final: {media:.2f}")
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

# Uso da classe
calculadora = Aluno()
calculadora.receber_notas()
calculadora.verificar_aprovacao()