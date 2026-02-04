"""Escrever e ler alunos"""

from models import Aluno

ARQUIVO_ALUNOS = "data/alunos.csv"
SEPARADOR = ";"


def salvar_aluno(aluno: Aluno) -> None:
    """
    Salva um aluno no arquivo de alunos
    """
    with open(ARQUIVO_ALUNOS, "a", encoding="utf-8") as arquivo_alunos:
        linha_formatada = (
            f"{aluno.id}{SEPARADOR}"
            f"{aluno.nome}{SEPARADOR}"
            f"{aluno.email}\n"
        )
        arquivo_alunos.write(linha_formatada)


def obter_todos_os_alunos() -> list:
    """
    Retorna uma lista com todos os alunos cadastrados
    """
    lista_alunos = []

    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as arquivo_alunos:
            for linha in arquivo_alunos:
                linha = linha.strip()

                if not linha:
                    continue

                identificador, nome, email = linha.split(SEPARADOR)
                aluno = Aluno(identificador, nome, email)
                lista_alunos.append(aluno)

    except FileNotFoundError:
        # Arquivo ainda não existe
        pass

    return lista_alunos


def encontrar_aluno_por_id(id_procurado: str):
    """
    Procura um aluno pelo ID
    Retorna um objeto Aluno ou None
    """
    alunos_cadastrados = obter_todos_os_alunos()

    for aluno in alunos_cadastrados:
        if aluno.id == id_procurado:
            return aluno

    return None
