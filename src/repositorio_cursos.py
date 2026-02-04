"""Escrever e ler cursos"""

from models import Curso

CAMINHO_CURSOS = "data/cursos.csv"
SEPARADOR = ";"


def cadastrar_curso(curso: Curso) -> None:
    """
    Salva um curso no arquivo cursos.csv.
    Não retorna nada.
    """
    with open(CAMINHO_CURSOS, "a", encoding="utf-8") as arquivo:
        linha = (
            f"{curso.codigo}{SEPARADOR}"
            f"{curso.nome}{SEPARADOR}"
            f"{curso.carga_horaria}\n"
        )
        arquivo.write(linha)


def listar_cursos() -> list[Curso]:
    """
    Retorna uma lista de objetos Curso cadastrados.
    """
    cursos = []

    try:
        with open(CAMINHO_CURSOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                codigo, nome, carga_horaria = linha.split(SEPARADOR)
                curso = Curso(codigo, nome, carga_horaria)
                cursos.append(curso)

    except FileNotFoundError:
        # Arquivo ainda não existe
        pass

    return cursos


def buscar_curso_por_codigo(codigo: str) -> Curso | None:
    """
    Busca um curso pelo código.
    Retorna o Curso encontrado ou None.
    """
    try:
        with open(CAMINHO_CURSOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                cod, nome, carga_horaria = linha.split(SEPARADOR)

                if cod == codigo:
                    return Curso(cod, nome, carga_horaria)

    except FileNotFoundError:
        pass

    return None
