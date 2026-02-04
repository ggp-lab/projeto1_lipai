'''Ler e escrever matriculas'''

from models import Matricula
from repositorio_alunos import encontrar_aluno_por_id
from repositorio_cursos import buscar_curso_por_codigo

CAMINHO_MATRICULAS = "data/matriculas.csv"
SEPARADOR = ";"


def cadastrar_matricula(matricula: Matricula) -> None:
    """
    Salva uma matrícula no arquivo matriculas.csv
    """
    with open(CAMINHO_MATRICULAS, "a", encoding="utf-8") as arquivo:
        linha = (
            f"{matricula.id}{SEPARADOR}"
            f"{matricula.aluno.id}{SEPARADOR}"
            f"{matricula.curso.codigo}{SEPARADOR}"
            f"{matricula.data_matricula}{SEPARADOR}"
            f"{matricula.status}\n"
        )
        arquivo.write(linha)


def listar_matriculas() -> list:
    """
    Retorna uma lista de objetos Matricula.
    """
    matriculas = []

    try:
        with open(CAMINHO_MATRICULAS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                (
                    id_matricula,
                    id_aluno,
                    codigo_curso,
                    data_matricula,
                    status,
                ) = linha.split(SEPARADOR)

                aluno = encontrar_aluno_por_id(id_aluno)
                curso = buscar_curso_por_codigo(codigo_curso)

                if aluno is not None and curso is not None:
                    matricula = Matricula(
                        id_matricula,
                        aluno,
                        curso,
                        data_matricula,
                        status,
                    )
                    matriculas.append(matricula)

    except FileNotFoundError:
        # Arquivo ainda não existe
        pass

    return matriculas


def listar_matriculas_por_aluno(id_aluno: str) -> list:
    """
    Retorna todas as matrículas de um aluno.
    """
    return [
        matricula
        for matricula in listar_matriculas()
        if matricula.aluno.id == id_aluno
    ]


def listar_matriculas_por_curso(codigo_curso: str) -> list:
    """
    Retorna todas as matrículas de um curso.
    """
    return [
        matricula
        for matricula in listar_matriculas()
        if matricula.curso.codigo == codigo_curso
    ]

def gerar_id_matricula() -> str:
    """
    Gera automaticamente o próximo ID de matrícula.
    Exemplo: M001, M002, M003...
    """
    matriculas = listar_matriculas()
    proximo_numero = len(matriculas) + 1
    return f"M{proximo_numero:03d}"
