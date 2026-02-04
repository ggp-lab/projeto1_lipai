"""Escrever e ler alunos"""

from models import Aluno

ARQUIVO_ALUNOS = "data/alunos.csv"
SEPARADOR = ";"


def salvar_aluno(aluno: Aluno) -> None:
    """
    Salva um aluno no arquivo alunos.csv.
    Não retorna nada.
    """
    with open(ARQUIVO_ALUNOS, "a", encoding="utf-8") as arquivo:
        linha = f"{aluno.id}{SEPARADOR}{aluno.nome}{SEPARADOR}{aluno.email}\n"
        arquivo.write(linha)


def listar_alunos() -> list[Aluno]:
    """
    Retorna uma lista de objetos Aluno cadastrados.
    """
    alunos = []

    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                identificador, nome, email = linha.split(SEPARADOR)
                aluno = Aluno(identificador, nome, email)
                alunos.append(aluno)

    except FileNotFoundError:
        # Arquivo ainda não existe
        pass

    return alunos


def buscar_aluno_por_id(id_procurado: str) -> Aluno | None:

    """
    Busca um aluno pelo ID.
    Retorna o Aluno encontrado ou None.
    """
    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()

                if linha == "":
                    continue

                identificador, nome, email = linha.split(SEPARADOR)

                if identificador == id_procurado:
                    return Aluno(identificador, nome, email)

    except FileNotFoundError:
        pass

    return None
