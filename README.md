# Projeto G – Sistema de Cursos e Matrículas

## Descrição do Projeto

Este projeto implementa um sistema simples em Python para gerenciar cursos, alunos e matrículas.  
O sistema resolve o problema de organizar e consultar registros de alunos e cursos de forma automatizada, permitindo que uma escola ou instituição acompanhe os alunos matriculados em cada curso e quais cursos cada aluno está realizando.  

O projeto foi desenvolvido como atividade acadêmica, utilizando programação orientada a objetos e manipulação de arquivos CSV.

## Funcionalidades

- Cadastrar cursos  
- Listar cursos cadastrados  
- Cadastrar alunos  
- Listar alunos cadastrados  
- Matricular um aluno em um curso  
- Listar alunos matriculados em um curso  
- Listar cursos em que um aluno está matriculado  

## Estrutura de Diretórios

projeto/  
├─ src/                # Código-fonte do sistema  
│   ├─ main.py  
│   ├─ models.py  
│   ├─ repositorio_cursos.py  
│   ├─ repositorio_alunos.py  
│   └─ repositorio_matriculas.py  
├─ data/               # Arquivos CSV gerados automaticamente  
│   ├─ cursos.csv  
│   ├─ alunos.csv  
│   └─ matriculas.csv  
└─ README.md           # Este arquivo  

## Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado.  
2. Clone o repositório:  
   `git clone <URL_DO_REPOSITORIO>`  
3. Navegue até a pasta `src`:  
   `cd projeto/src`  
4. Execute o sistema:  
   `python main.py`  
5. Use os menus exibidos no terminal para interagir com o sistema.  

## Observações

- Os arquivos CSV são criados automaticamente na pasta `data`.  
- O sistema funciona totalmente em modo texto (terminal).  
- Nenhuma biblioteca externa é necessária.  




