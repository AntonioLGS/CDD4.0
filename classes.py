class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.acao_atual = None  # Atributo para controlar a ação atual

    def comer(self, comida, bebida):
        if self.acao_atual is None:
            self.acao_atual = "comer"
            print(f"{self.nome} foi comer... {comida} e {bebida}")
        else:
            print(f"{self.nome} já está {self.acao_atual}, não pode iniciar outra ação.")

    def falar(self, pessoa):
        if self.acao_atual is None:
            self.acao_atual = "falar"
            print(f"{self.nome} está falando com {pessoa}")
        else:
            print(f"{self.nome} já está {self.acao_atual}, não pode iniciar outra ação.")

    def dormir(self):
        if self.acao_atual is None:
            self.acao_atual = "dormir"
            print(f"{self.nome} está dormindo")
        else:
            print(f"{self.nome} já está {self.acao_atual}, não pode iniciar outra ação.")

    def parar_acao(self):
        if self.acao_atual is not None:
            print(f"{self.nome} parou de {self.acao_atual}")
            self.acao_atual = None
        else:
            print(f"{self.nome} não está realizando nenhuma ação para parar.")

    def acao(self):
        while True:
            escolha = int(input("Digite 1 para comer, 2 para falar, 3 para dormir ou 0 para sair: "))
            if escolha == 1:
                comida = input("O que você está comendo? ")
                bebida = input("O que você está bebendo? ")
                self.comer(comida, bebida)
            elif escolha == 2:
                pessoa = input("Com quem você está falando? ")
                self.falar(pessoa)
            elif escolha == 3:
                self.dormir()
            elif escolha == 0:
                self.parar_acao()
                break
            else:
                print("Escolha inválida. Tente denovo.")
