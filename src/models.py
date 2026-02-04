'''Classes'''


class Curso:
    def __init__(self, codigo: str, nome: str, carga_horaria: str):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self) -> str:
        return (
            f"Curso: {self.nome} | "
            f"Código: {self.codigo} | "
            f"Carga Horária: {self.carga_horaria}h"
        )


class Aluno:
    def __init__(self, id_aluno: str, nome: str, email: str):
        self.id = id_aluno
        self.nome = nome
        self.email = email

    def __str__(self) -> str:
        return (
            f"Aluno: {self.nome} | "
            f"ID: {self.id} | "
            f"Email: {self.email}"
        )


class Matricula:
    def __init__(
        self,
        id_matricula: str,
        aluno: Aluno,
        curso: Curso,
        data_matricula: str,
        status: str,
    ):
        self.id = id_matricula
        self.aluno = aluno
        self.curso = curso
        self.data_matricula = data_matricula
        self.status = status

    def __str__(self) -> str:
        return (
            f"ID: {self.id} | "
            f"Aluno: {self.aluno.nome} | "
            f"Curso: {self.curso.nome} | "
            f"Data: {self.data_matricula} | "
            f"Status: {self.status}"
        )
