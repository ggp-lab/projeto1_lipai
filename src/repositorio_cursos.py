"""Escrever e ler cursos"""

from models import Curso

CAMINHO_CURSOS = "data/cursos.csv"
SEPARADOR = ";"


def cadastrar_curso(curso: Curso) -> None:
    """
    Salva um curso no arquivo cursos.csv
    """
    with open(CAMINHO_CURSOS, "a", encoding="utf-8") as arquivo:
        linha = f"{curso.codigo}{SEPARADOR}{curso.nome}{SEPARADOR}{curso.carga_horaria}\n"
        arquivo.write(linha)


def listar_cursos() -> list:
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
        # Caso o arquivo ainda não exista
        pass

    return cursos


def buscar_curso_por_codigo(codigo: str):
    """
    Busca um curso pelo código.
    Retorna o Curso ou None.
    """
    for curso in listar_cursos():
        if curso.codigo == codigo:
            return curso

    return None
