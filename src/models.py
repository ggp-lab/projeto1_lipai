"""Classes"""

class Curso:
    def __init__(self, codigo, nome, carga_horaria):
        self.codigo = codigo
        self.nome = nome
        self.carga_horaria = carga_horaria

    def __str__(self):
        return f"Curso: {self.nome} | Código: {self.codigo} | Carga Horária: {self.carga_horaria}h"


class Aluno:
    def __init__(self, id_aluno, nome, email):
        self.id = id_aluno
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Aluno: {self.nome} | ID: {self.id} | Email: {self.email}"


class Matricula:
    def __init__(self, id_matricula, aluno, curso, data_matricula, status):
        self.id = id_matricula
        self.aluno = aluno      
        self.curso = curso      
        self.data_matricula = data_matricula
        self.status = status

    def __str__(self):
        return (
            f"ID: {self.id} "
            f"Aluno: {self.aluno.nome} "
            f"Curso: {self.curso.nome} "
            f"Data: {self.data_matricula} "
            f"Status: {self.status}"
        )
