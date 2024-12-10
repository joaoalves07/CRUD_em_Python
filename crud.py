import json
import os


arquivos_JSON = 'registros.json'


class Registro:
    def __init__(self, nome, quantia):
        self.nome = nome
        self.quantia = quantia

    def dicionario(self):
        return {"nome": self.nome, "quantia": self.quantia}


class GerenciadorRegistros:
    def __init__(self, arquivos):
        self.arquivos = arquivos
        self.registros = self.carregamento_de_dados()

    def carregamento_de_dados(self):
        if os.path.exists(self.arquivos):
            with open(self.arquivos, 'r') as arquivos:
                return [Registro(dados["nome"], dados["quantia"]) for dados in json.load(arquivos)]
        return []

    def salvar_dados(self):
        with open(self.arquivos, 'w') as arquivos:
            json.dump([registro.dicionario()
                      for registro in self.registros], arquivos, indent=4)

    def lista_de_registros(self):
        if not self.registros:
            print("Nenhum registro encontrado.")
            return
        print("\nRegistros:")
        for idx, registro in enumerate(self.registros, start=1):
            print(f"{idx}. Produto: {registro.nome}, Quantia: {registro.quantia}")

    def adicionar_registros(self):
        nome = input("Digite o nome do produto aqui: ")
        try:
            quantia = int(input("Informe quantas unidades há: "))
            self.registros.append(Registro(nome, quantia))
            self.salvar_dados()
            print("Registro incluído com sucesso.")
        except ValueError:
            print("A quantia deve ser um número válido.")

    def alteração_de_registro(self):
        self.lista_de_registros()
        try:
            indice = int(
                input("Digite o número do registro que deseja alterar: ")) - 1
            if 0 <= indice < len(self.registros):
                nome = input("Digite o novo nome: ")
                try:
                    quantia = int(input("Digite a nova quantia: "))
                    self.registros[indice] = Registro(nome, quantia)
                    self.salvar_dados()
                    print("Registro alterado com sucesso.")
                except ValueError:
                    print("A quantia deve ser um número válido.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    def remover_registro(self):
        self.lista_de_registros()
        try:
            indice = int(
                input("Digite o número do registro que deseja excluir: ")) - 1
            if 0 <= indice < len(self.registros):
                registro_removido = self.registros.pop(indice)
                self.salvar_dados()
                print(
                    f"Registro '{registro_removido.nome}' removido com sucesso.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")


class Menu:
    def __init__(self, gerenciador):
        self.gerenciador = gerenciador

    def exibir(self):
        while True:
            print("\n--- Registro ---")
            print("1. Listar produto")
            print("2. Incluir produto")
            print("3. Alterar produto")
            print("4. Excluir produto")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.gerenciador.lista_de_registros()
            elif opcao == '2':
                self.gerenciador.adicionar_registros()
            elif opcao == '3':
                self.gerenciador.alteração_de_registro()
            elif opcao == '4':
                self.gerenciador.remover_registro()
            elif opcao == '5':
                print("Encerrando...")
                break
            else:
                print("Opção inválida.")


if __name__ == "__main__":
    gerenciador = GerenciadorRegistros(arquivos_JSON)
    menu = Menu(gerenciador)
    menu.exibir()
