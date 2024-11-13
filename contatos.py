import json
import os

# Arquivo onde os contatos serão armazenados
ARQUIVO_CONTATOS = 'contatos.json'

class GerenciadorContatos:
    def __init__(self):
        self.contatos = self.carregar_contatos()

    def carregar_contatos(self):
        """Carrega os contatos do arquivo JSON."""
        if os.path.exists(ARQUIVO_CONTATOS):
            with open(ARQUIVO_CONTATOS, 'r') as arquivo:
                try:
                    return json.load(arquivo)
                except json.JSONDecodeError:
                    print("Erro ao ler os contatos. O arquivo pode estar corrompido.")
                    return []
        else:
            return []

    def salvar_contatos(self):
        """Salva os contatos no arquivo JSON."""
        with open(ARQUIVO_CONTATOS, 'w') as arquivo:
            try:
                json.dump(self.contatos, arquivo, indent=4)
            except Exception as e:
                print(f"Erro ao salvar os contatos: {e}")

    def adicionar_contato(self, nome, telefone):
        """Adiciona um novo contato à lista."""
        novo_contato = {"nome": nome, "telefone": telefone}
        self.contatos.append(novo_contato)
        self.salvar_contatos()
        print(f"Contato '{nome}' adicionado com sucesso!")

    def listar_contatos(self):
        """Exibe todos os contatos cadastrados."""
        if not self.contatos:
            print("Nenhum contato encontrado.")
        else:
            print("\nLista de Contatos:")
            for i, contato in enumerate(self.contatos, 1):
                print(f"{i}. {contato['nome']} - {contato['telefone']}")

    def editar_contato(self, indice, nome, telefone):
        """Edita um contato existente pelo índice."""
        if 0 <= indice < len(self.contatos):
            self.contatos[indice]['nome'] = nome
            self.contatos[indice]['telefone'] = telefone
            self.salvar_contatos()
            print(f"Contato #{indice + 1} editado com sucesso!")
        else:
            print("Contato não encontrado.")

    def remover_contato(self, indice):
        """Remove um contato pelo índice."""
        if 0 <= indice < len(self.contatos):
            removed = self.contatos.pop(indice)
            self.salvar_contatos()
            print(f"Contato '{removed['nome']}' removido com sucesso!")
        else:
            print("Contato não encontrado.")

def exibir_menu():
    """Exibe o menu de opções."""
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Editar Contato")
    print("4. Remover Contato")
    print("5. Sair")

def main():
    """Função principal para gerenciar os contatos."""
    gerenciador = GerenciadorContatos()

    while True:
        exibir_menu()
        try:
            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                nome = input("Digite o nome do contato: ")
                telefone = input("Digite o telefone do contato: ")
                gerenciador.adicionar_contato(nome, telefone)
            elif opcao == 2:
                gerenciador.listar_contatos()
            elif opcao == 3:
                gerenciador.listar_contatos()
                indice = int(input("Digite o número do contato a ser editado: ")) - 1
                nome = input("Digite o novo nome: ")
                telefone = input("Digite o novo telefone: ")
                gerenciador.editar_contato(indice, nome, telefone)
            elif opcao == 4:
                gerenciador.listar_contatos()
                indice = int(input("Digite o número do contato a ser removido: ")) - 1
                gerenciador.remover_contato(indice)
            elif opcao == 5:
                print("Saindo... Até mais!")
                break
            else:
                print("Opção inválida, tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == '__main__':
    main()
