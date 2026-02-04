"""menu principal"""

from models import Curso, Aluno, Matricula

from repositorio_cursos import (
    cadastrar_curso,
    listar_cursos,
    buscar_curso_por_codigo,
)

from repositorio_alunos import (
    salvar_aluno,
    obter_todos_os_alunos,
    encontrar_aluno_por_id,
)

from repositorio_matriculas import (
    cadastrar_matricula,
    listar_matriculas_por_aluno,
    listar_matriculas_por_curso,
    gerar_id_matricula,
)

from datetime import date


def menu_principal():
    print("\n=== SISTEMA DE CURSOS E MATRÍCULAS ===")
    print("1 - Gerenciar cursos")
    print("2 - Gerenciar alunos")
    print("3 - Gerenciar matrículas")
    print("0 - Sair")


def menu_cursos():
    print("\n--- MENU DE CURSOS ---")
    print("1 - Cadastrar curso")
    print("2 - Listar cursos")
    print("0 - Voltar")


def menu_alunos():
    print("\n--- MENU DE ALUNOS ---")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("0 - Voltar")


def menu_matriculas():
    print("\n--- MENU DE MATRÍCULAS ---")
    print("1 - Matricular aluno em curso")
    print("2 - Listar alunos de um curso")
    print("3 - Listar cursos de um aluno")
    print("0 - Voltar")


def executar():
    while True:
        menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                menu_cursos()
                opcao_curso = input("Escolha uma opção: ")

                if opcao_curso == "1":
                    codigo = input("Código do curso: ")
                    nome = input("Nome do curso: ")
                    carga_horaria = input("Carga horária: ")

                    curso = Curso(codigo, nome, carga_horaria)
                    cadastrar_curso(curso)

                    print("Curso cadastrado com sucesso!")

                elif opcao_curso == "2":
                    cursos = listar_cursos()

                    if not cursos:
                        print("Nenhum curso cadastrado.")
                    else:
                        for curso in cursos:
                            print(
                                f"{curso.codigo} - {curso.nome} "
                                f"({curso.carga_horaria}h)"
                            )

                elif opcao_curso == "0":
                    break

        elif opcao == "2":
            while True:
                menu_alunos()
                opcao_aluno = input("Escolha uma opção: ")

                if opcao_aluno == "1":
                    id_aluno = input("ID do aluno: ")
                    nome = input("Nome do aluno: ")
                    email = input("Email do aluno: ")

                    aluno = Aluno(id_aluno, nome, email)
                    salvar_aluno(aluno)

                    print("Aluno cadastrado com sucesso!")

                elif opcao_aluno == "2":
                    alunos = obter_todos_os_alunos()

                    if not alunos:
                        print("Nenhum aluno cadastrado.")
                    else:
                        for aluno in alunos:
                            print(
                                f"{aluno.id} - {aluno.nome} ({aluno.email})"
                            )

                elif opcao_aluno == "0":
                    break

        elif opcao == "3":
            while True:
                menu_matriculas()
                opcao_matricula = input("Escolha uma opção: ")

                if opcao_matricula == "1":
                    id_matricula = gerar_id_matricula()
                    id_aluno = input("ID do aluno: ")
                    codigo_curso = input("Código do curso: ")

                    aluno = encontrar_aluno_por_id(id_aluno)
                    curso = buscar_curso_por_codigo(codigo_curso)

                    if aluno is None or curso is None:
                        print("Aluno ou curso não encontrado.")
                    else:
                        data_matricula = date.today().isoformat()
                        status = "ativa"

                        matricula = Matricula(
                            id_matricula,
                            aluno,
                            curso,
                            data_matricula,
                            status,
                        )

                        cadastrar_matricula(matricula)
                        print(f"Matrícula {id_matricula} realizada com sucesso!")

                elif opcao_matricula == "2":
                    codigo_curso = input("Código do curso: ")
                    matriculas = listar_matriculas_por_curso(codigo_curso)

                    if not matriculas:
                        print("Nenhum aluno matriculado nesse curso.")
                    else:
                        for m in matriculas:
                            print(f"{m.aluno.id} - {m.aluno.nome}")

                elif opcao_matricula == "3":
                    id_aluno = input("ID do aluno: ")
                    matriculas = listar_matriculas_por_aluno(id_aluno)

                    if not matriculas:
                        print("Aluno não possui matrículas.")
                    else:
                        for m in matriculas:
                            print(f"{m.curso.codigo} - {m.curso.nome} - {m.curso.carga_horaria}h")

                elif opcao_matricula == "0":
                    break

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    executar()
