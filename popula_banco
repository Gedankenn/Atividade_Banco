import datetime
import random
import re

names = ["Fabio","Everton","Amanda","Geovana","Priscila",
         "Duda","Guilherme","Matheus","Ives","Ines","Gabriela",
         "Neide","Alex","Romeu","Julieta","Taina","Antonieta",
         "Charles","Cleopatra","Cesar","Nero","Jaspion","Naruto",
         "Kakashi","Pain","Kurama","Slash","Violet","Vi",
         "Mordekaiser","Jinx","Blitz","Amelia","Leandro","Jesus",
         "Otavio","Cassio","Augusto","Stanley","Willian","Lula","Jacir"]

Sobrenomes = ["das Neves","dos Santos","Oliveira","Nasceu","Pinto",
              "Amando","Sousa","Guerra","Parizanello","Pizzanelo",
              "Pintonela","Sarau","Lamborguini","Ferrari","Mazzerati",
              "Audi","Tesla","Wolkswagen","Mercedes","BWM","Honda","Chiron",
              "Jeep","Civic","Corolla","Corsa","Cansado","Mouro","Bolsonaro"]

cidades = ["Pato Branco","Curitiba","Francisco Beltrao","Eneas Marques",
           "Dois Vizinhos","Vitorino","Coronel Vivida","Marmeleiro","Chapeco","Xanxere","Xaxim",
           "Sao Paulo","Rio de Janeiro","Brasilia","Palmas"]

Cursos = ["engenharia da ComPutação","Engenharia Elétrica","Engneharia Civil","Engenharia Mecanica","LEtras",
          "AGronomia","QuiMica","ConTabeis","ADMinistracao","Analise De Sistemas"]

Estados = ["PR","RJ","SP","RG","PA","PB","BA"]

Disciplinas = ["CAlculo I","CAlculo II","CAlculo III", "FIsica I","FIsica II","FIsica III","FIsica IV",
               "Geometria Analitica Algebra Linear","Equacoes Diferencias Ordinarias","Resistencia dos Materiais",
               "Calculo Numerico","Variaveis Complexas","Sistemas de Controle I","Sistemas de Controle II","Controle Digital","Instrumentação Eletroeletronica",
               "Trabalho de Conclusao do Curso I","Trabalho de Conclusao do Curso II","Sistemas Embarcados","Sistemas Digitais","REdes I","Banco de Dados I","REdes II","Banco de Dados II"]

def random_data( start):
    end = start + datetime.timedelta(days=1)
    random_date = start + (end - start) * random.randint(1,365*5)
    return random_date

remove_lower = lambda text: re.sub('[a-z,ç,é,ã]','', text)
remove_2 = lambda text: re.sub(' ','',text)
    

inicio = datetime.datetime(year=1990, month=3, day = 22)
random_data(inicio)
N_alunos = 4

for i in range(0,N_alunos):
    nome = names[random.randint(1,len(names)-1)]
    for k in range(0,random.randint(1,3)):
        nome = nome +" " + Sobrenomes[random.randint(1,len(Sobrenomes)-1)]
    
    nome_mae = names[random.randint(1,len(names)-1)]
    for k in range(0,random.randint(1,3)):
        nome_mae = nome_mae +" " + Sobrenomes[random.randint(1,len(Sobrenomes)-1)]
    
    data_nasci = random_data(inicio)
    cidade = cidades[random.randint(1,len(cidades)-1)]
    estado = Estados[random.randint(1,len(Estados)-1)]
    curso = Cursos[random.randint(1,len(Cursos)-1)]
    idade = round((datetime.datetime.now() - data_nasci).days/365)
    periodo = random.randint(1,10)