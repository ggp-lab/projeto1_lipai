"""menu principal"""

from datetime import date

import models
import repositorio_cursos
import repositorio_alunos
import repositorio_matriculas

def main():
    while True:
        
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Cursos")
        print("2 - Alunos")
        print("3 - Matrículas")
        print("0 - Sair")


        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cursos()
        elif opcao == "2":
            menu_alunos()
        elif opcao == "3":
            menu_matriculas()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


def menu_cursos():
    while True:
        print("\n--- MENU DE CURSOS ---")
        print("1 - Cadastrar curso")
        print("2 - Listar cursos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código do curso: ")
            nome = input("Nome do curso: ")
            carga_horaria = input("Carga horária: ")

            curso = models.Curso(codigo, nome, carga_horaria)
            repositorio_cursos.cadastrar_curso(curso)


            print("Curso cadastrado com sucesso!")

        elif opcao == "2":
            cursos = repositorio_cursos.listar_cursos()


            if not cursos:
                print("Nenhum curso cadastrado.")
            else:
                for curso in cursos:
                    print(
                        f"{curso.codigo} - {curso.nome} "
                        f"({curso.carga_horaria}h)"
                    )

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")



def menu_alunos():
    while True:
        print("\n--- MENU DE ALUNOS ---")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_aluno = input("ID do aluno: ")
            nome = input("Nome do aluno: ")
            email = input("Email do aluno: ")

            aluno = models.Aluno(id_aluno, nome, email)
            repositorio_alunos.salvar_aluno(aluno)

            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            alunos = repositorio_alunos.listar_alunos()


            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                for aluno in alunos:
                    print(f"{aluno.id} - {aluno.nome} ({aluno.email})")

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

def menu_matriculas():
    while True:
        print("\n--- MENU DE MATRÍCULAS ---")
        print("1 - Matricular aluno em curso")
        print("2 - Listar alunos de um curso")
        print("3 - Listar cursos de um aluno")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id_matricula = repositorio_matriculas.gerar_id_matricula()

            id_aluno = input("ID do aluno: ")
            codigo_curso = input("Código do curso: ")

            aluno = repositorio_alunos.buscar_aluno_por_id(id_aluno)
            curso = repositorio_cursos.buscar_curso_por_codigo(codigo_curso)


            if aluno is None or curso is None:
                print("Aluno ou curso não encontrado.")
            else:
                data_matricula = date.today().isoformat()
                status = "ativa"

                matricula = models.Matricula(
                    id_matricula,
                    aluno,
                    curso,
                    data_matricula,
                    status
                )

                repositorio_matriculas.cadastrar_matricula(matricula)
                print(f"Matrícula {id_matricula} realizada com sucesso!")

        elif opcao == "2":
            codigo_curso = input("Código do curso: ")
            matriculas = repositorio_matriculas.listar_matriculas_por_curso(codigo_curso)

            if not matriculas:
                print("Nenhum aluno matriculado nesse curso.")
            else:
                for m in matriculas:
                    print(f"{m.aluno.id} - {m.aluno.nome}")

        elif opcao == "3":
            id_aluno = input("ID do aluno: ")
            matriculas = repositorio_matriculas.listar_matriculas_por_aluno(id_aluno)

            if not matriculas:
                print("Aluno não possui matrículas.")
            else:
                for m in matriculas:
                    print(
                        f"{m.curso.codigo} - {m.curso.nome} "
                        f"({m.curso.carga_horaria}h)"
                    )

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()