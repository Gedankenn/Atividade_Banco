import datetime
import random
import re
import psycopg2 as pg

class alunos:
    def __init__(self, nome, ra, data_nasc, idade, nome_mae, cidade, estado, curso, periodo):
        self.nome = nome
        self.ra   = ra
        self.data_nasc = data_nasc
        self.idade = idade
        self.nome_mae = nome_mae
        self.cidade = cidade
        self.estado = estado
        self.curso = curso
        self.periodo = periodo


names = ["Fabio","Everton","Amanda","Geovana","Priscila",
         "Duda","Guilherme","Matheus","Ives","Ines","Gabriela",
         "Neide","Alex","Romeu","Julieta","Taina","Antonieta",
         "Charles","Cleopatra","Cesar","Nero","Jaspion","Naruto",
         "Kakashi","Pain","Kurama","Slash","Violet","Vi",
         "Mordekaiser","Jinx","Blitz","Amelia","Leandro","Jesus",
         "Otavio","Cassio","Augusto","Stanley","Willian","Lula","Jacir",
         "Cleide","Miller","Jean","Albert","Isaac","Jack","Platao",
         "Nicolau","Clovis","Bruno","Debora","Rafael","Matias","Pedro",
         "Judas","Cleiton","Cleberson","Carolina","Eloisa","Carina"]

Sobrenomes = ["das Neves","dos Santos","Oliveira","Nasceu","Pinto",
              "Amando","Sousa","Guerra","Parizanello","Pizzanelo",
              "Pintonela","Sarau","da Silva","Cansado","Mouro","Bolsonaro",
              "Delgado","Brasa","Polenta","Pena","Medeiros","da Vinci","Laplace",
              "Miller","Pacu","Tilapia","Lambari","Stalone","Sparrow","Milton",
              "da Casa","Santos","Albuquerque","Nobel","Thomazonni","Aglera",
              "Zancanaro","Thalia","Fernandes","Dresch","Risson","Ramos"]

cidades = ["Pato Branco","Curitiba","Francisco Beltrao","Eneas Marques",
           "Dois Vizinhos","Vitorino","Coronel Vivida","Marmeleiro","Chapeco","Xanxere","Xaxim",
           "Sao Paulo","Rio de Janeiro","Brasilia","Palmas"]

Cursos = ["engenharia da ComPutação","Engenharia Elétrica","Engneharia Civil","Engenharia Mecanica","LEtras",
          "AGronomia","QuiMica","ConTabeis","ADMinistracao","Analise De Sistemas"]

Estados = ["PR","RJ","SP","RG","PA","PB","BA"]

Disciplinas = ["Calculo I","Calculo II","Calculo III", "Fisica I","Fisica II","Fisica III","Fisica IV",
               "Logica Para Computacao","Comunicacao Linguistica","Fundamentos De Programacao",
               "Introducao A Engenharia","Algoritmos e Estrutura de Dados I","Algoritmos e Estrutura de Dados 2",
               "Desenho Tecnico","Metodologia de Pesquisa","Quimica","Circuitos Digitais","Matematica Discreta",
               "Programação Orientada a Objetos","Eletronica A","Eletronica B","Fundamentos de Teoria da Computação",
               "Compiladores","Principio de Sistemas de Comunicacao","Arquitetura e Organizacao de Computadores",
               "Analise e Projeto de Sistemas","Engenharia de Software","Probabilidade e Estatistica",
               "Geometria Analitica Algebra Linear","Equacoes Diferencias Ordinarias","Principio de Resistencia dos Materiais",
               "Analise de Circuitos Eletricos","Mecanica Geral","Calculo Numerico","Variaveis Complexas",
               "Sistemas de Controle I","Sistemas de Controle II","Controle Digital","Sistemas Microcontrolados",
               "Sistemas Operacionais","Instrumentação Eletroeletronica","Trabalho de Conclusao do Curso I",
               "Trabalho de Conclusao do Curso II","Oficina de Integracao","Estagio Curricular Obrigatorio",
               "Logica Reconfiguravel","Sistemas Embarcados","Sistemas Digitais","Redes de Computadores I",
               "Banco de Dados I","Redes de Computadores II","Banco de Dados II","Sistemas Inteligentes",
               "Sistemas Distribuidos","Seguranca Computacional","Economia","Etica Profissao e Cidadania",
               "Empreendedorismo","Atividades Complementares","Sistemas Lineares"]

CodDisciplinas = ["CD21NB","CD22NB","CD23NB","FI21NB","FI22NB","FI23NB","FI24NB","LC21CP","CL21NB","FP21NB",
                  "IE21CP","AE22CP","AE23CP","DT22NB","MP22NB","QU22NB","CD24CP","MD24CP","PO24CP","EL25CP",
                  "EL26CP","FT25CP","CO28CP","PS26CP","AO26CP","AP25CP","ES26CP","PE22NB","GA21NB","ED23NB",
                  "PR25CP","AC24NB","MG24NB","CN24NB","VC23NB","SC25CP","SC26CP","CD27CP","SM26CP","SO25CP",
                  "IE27CP","TC28CP","TC29CP","OI25CP","ES30CP","LR27CP","SE28CP","SD25CP","RC27CP","BD26CP",
                  "RC28CP","BD27CP","SI27CP","SD29CP","SC28CP","EC29NB","EP29NB","EE27CP","AC30CP","SL24CP"]

SiglaPreReq =    ["NULL","CD21NB","CD22NB","NULL","FI21NB","FI22NB","FI23NB","NULL","NULL","NULL",
                  "NULL","NULL","AE22CP","NULL","NULL","NULL","FI23NB","NULL","FP21NB","AC24NB",
                  "EL25CP","MD24CP","FT25CP","SL24CP","SD25CP","AE22CP","AP25CP","CD21NB","NULL","CD22NB",
                  "MG24NB","FI23NB","FI21NB","ED23NB","CD22NB","AC24NB","SC25CP","SC26CP","SD25CP","AO26CP",
                  "EL26CP","OI25CP","TC28CP","NULL","NULL","SM26CP","SM26CP","CD24CP","PS26CP","AE22CP",
                  "RC27CP","BD26CP","AE22CP","LR27CP","RC27CP","NULL","NULL","NULL","NULL","ED23NB"]

def random_data( start):
    end = start + datetime.timedelta(days=1)
    random_date = start + (end - start) * random.randint(0,365*5)
    return random_date

def send_query(query, data):
    connection = pg.connect(user = "th00r",
                        password = "valhalla",
                        host = "192.168.10.48",
                        port = "5432",
                        database = "Atividade_01")

    cursor = connection.cursor()
    cursor.execute(query,data)
    connection.commit()
    cursor.close()
    connection.close()

remove_lower = lambda text: re.sub('[a-z,ç,é,ã]','', text)
remove_2 = lambda text: re.sub(' ','',text)


inicio = datetime.datetime(year=1990, month=3, day = 22)
random_data(inicio)
N_alunos = 4

vet_alunos = []
#etapa que insere alunos
for i in range(0,N_alunos):
    nome = names[random.randint(0,len(names)-1)]
    sobrenome = ""
    for k in range(0,random.randint(1,3)):
        sobrenome = sobrenome +" " + Sobrenomes[random.randint(0,len(Sobrenomes)-1)]
    nome = nome+sobrenome
    
    nome_mae = names[random.randint(0,len(names)-1)]
    nome_mae = nome_mae + sobrenome
    
    data_nasci = random_data(inicio)
    cidade = cidades[random.randint(0,len(cidades)-1)]
    estado = Estados[random.randint(0,len(Estados)-1)]
    curso = Cursos[random.randint(0,len(Cursos)-1)]
    idade = round((datetime.datetime.now() - data_nasci).days/365)
    periodo = random.randint(0,10)
    
    ra=random.randint(1000000,99999999)
    vet_alunos.append(alunos(nome,ra,data_nasci,idade,nome_mae,cidade,estado,curso,periodo))

#etapa para inserir em disciplinas
for disciplina in Disciplinas:
    sigla = remove_2(remove_lower(disciplina))
    nome = disciplina
    monitor = ""
    if(random.randint(0,5) == 3):
        monitor = vet_alunos[random.randint(0,len(vet_alunos))].nome
    depto = remove_2(remove_lower(Cursos[random.randint(0,len(Cursos)-1)]))
    #nncred?


#Etapa de matriculas
for aluno in vet_alunos:
    ra = aluno.ra
    ano = random.randint(2016,2022)
    for a in range(ano,2023):
        semestre = random.randint(1,2)
        for i in range(0,random.randint(3,9)):
            disciplina = Disciplinas[random.randint(0,len(Disciplinas)-1)]
            sigla = str(remove_2(remove_lower(disciplina)))
            cod_turma = str(aluno.curso)+sigla+str(ano-2000)
            N1 = random.randint(0,10)
            N2 = random.randint(0,10)
            N3 = random.randint(0,10)
            NFim = (N1+N2+N3)/3
            freq = random.randint(0,100)
