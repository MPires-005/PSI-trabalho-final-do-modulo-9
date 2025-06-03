from datetime import datetime, timedelta  # Importa bibliotecas para manipular datas


class Livro:
    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.codigo}: {self.titulo}, {self.autor} ({status})"
    
    
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = {}

    def __str__(self):
        return f"{self.matricula}: {self.nome}"
    
class Biblioteca:
    def __init__(self):
        self.catalogo = {}  
        self.alunos = {}
        
    def cadastrar_livro(self, titulo, autor, codigo):
        if codigo in self.catalogo:
            print("Livro já registrado.")
            return
        self.catalogo[codigo] = Livro(titulo, autor, codigo)
        print("Livro registrado com sucesso!")    

    def cadastrar_aluno(self, nome, matricula):
        if matricula in self.alunos:
            print(" Aluno já registrado.")
            return
        self.alunos[matricula] = Aluno(nome, matricula)
        print(" Aluno registrado com sucesso!")
   
    def emprestar_livro(self, matricula, codigo, dias):
        if matricula not in self.alunos:
            print("O aluno não se encontra no sistema.")
            return
        if codigo not in self.catalogo:
            print("O Livro não se encontra no sistema.")
            return

        livro = self.catalogo[codigo]
        aluno = self.alunos[matricula]

        if not livro.disponivel:
            print("O Livro já se encontra ocupado.")
            return

        livro.disponivel = False
        data_entrega = datetime.now() + timedelta(days=dias)
        aluno.livros_emprestados[codigo] = data_entrega
        print(f" Livro ocupado até {data_entrega.strftime('%d/%m/%Y')}.")

    
    def devolver_livro(self, matricula, codigo):
        if matricula not in self.alunos:
            print("O aluno não se encontra no sistema.")
            return
        aluno = self.alunos[matricula]
        if codigo not in aluno.livros_emprestados:
            print("Este aluno não está na posse do livro.")
            return

        livro = self.catalogo[codigo]
        livro.disponivel = True
        del aluno.livros_emprestados[codigo]
        print("Livro devolvido com sucesso!")

    def listar_livros_disponiveis(self):
        print("\n Livros Disponíveis:")
        for livro in self.catalogo.values():
            if livro.disponivel:
                print(livro)
    
    def listar_catalogo(self):
        print("\n Catálogo de Livros:")
        for livro in self.catalogo.values():
            print(livro)

    def listar_alunos(self):
        print("\n Alunos Registrados:")
        for aluno in self.alunos.values():
            print(aluno)
    
    def listar_livros_por_aluno(self, matricula):
        if matricula not in self.alunos:
            print("O Aluno não se encontra no sistema.")
            return
        aluno = self.alunos[matricula]
        print(f"\n Livros com {aluno.nome}:")
        for codigo, data in aluno.livros_emprestados.items():
            livro = self.catalogo[codigo]
            print(f"{livro.titulo} - Devolver até {data.strftime('%d/%m/%Y')}")            
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n BIBLIOTECA ESCOLAR ")
        print("1. Registrar Aluno")
        print("2. Registrar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Ver Livros Disponíveis")
        print("6. Ver Livros de um Aluno")
        print("7. Ver Alunos Registrados")
        print("8. Ver Catálogo de Livros")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula: ")
            biblioteca.cadastrar_aluno(nome, matricula)

        elif opcao == "2":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            codigo = input("Código do livro: ")
            biblioteca.cadastrar_livro(titulo, autor, codigo)

        elif opcao == "3":
            matricula = input("Matrícula do aluno: ")
            codigo = input("Código do livro: ")
            dias = int(input("Por quantos dias? "))
            biblioteca.emprestar_livro(matricula, codigo, dias)

        elif opcao == "4":
            matricula = input("Matrícula do aluno: ")
            codigo = input("Código do livro: ")
            biblioteca.devolver_livro(matricula, codigo)

        elif opcao == "5":
            biblioteca.listar_livros_disponiveis()

        elif opcao == "6":
            matricula = input("Matrícula do aluno: ")
            biblioteca.listar_livros_por_aluno(matricula)

        elif opcao == "7":
            biblioteca.listar_alunos()

        elif opcao == "8":
            biblioteca.listar_catalogo()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção não disponivel!")

menu()



