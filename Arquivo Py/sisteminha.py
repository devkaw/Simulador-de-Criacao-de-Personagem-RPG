import sqlite3
import random
import os
from time import sleep as mimindo

# Classe representando as características necessárias de cada personagem
class Personagem:
    # Método Construtor
    def __init__(self, nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma, antecedente, itens_do_pacote, vida, lvl, xp):
        self.nome = nome
        self.raça = raça
        self.classe = classe
        self.equipamento = equipamento
        self.dinheiro = dinheiro
        self.proficiencias = proficiencias
        self.recursos_especiais = recursos_especiais
        self.idiomas = idiomas
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.antecedente = antecedente
        self.itens_do_pacote = itens_do_pacote
        self.vida = vida
        self.lvl = lvl
        self.xp = xp

    # Criação do nosso dicionário pra colocar na lista dos personagens
    def criacao_dicionario(self):
        dicionario = {
            'Nome': self.nome,
            'Raça': self.raça,
            'Classe': self.classe,
            'Equipamento': self.equipamento,
            'Dinheiro': self.dinheiro,
            'Proficiências': self.proficiencias,
            'Recursos Especiais': self.recursos_especiais,
            'Idiomas': self.idiomas,
            'Força': self.forca,
            'Destreza': self.destreza,
            'Constituição': self.constituicao,
            'Inteligência': self.inteligencia,
            'Sabedoria': self.sabedoria,
            'Carisma': self.carisma,
            'Antecedente': self.antecedente,
            'Itens do pacote que você possui': self.itens_do_pacote,
            'Vida': self.vida,
            'Nível': self.lvl,
            'XP': self.xp
        }
        return dicionario


# Classe que fará os sistema de opcões
class SimuladorRPG:
    # Método Construtor
    def __init__(self):
        self.conexao = sqlite3.connect('personagens.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personagens
                            (nome TEXT, raca TEXT, classe TEXT, equipamento TEXT, dinheiro TEXT, proficiencias TEXT, recursos_especiais TEXT, idiomas TEXT, forca TEXT, destreza TEXT, constituicao TEXT, inteligencia TEXT, sabedoria TEXT, carisma TEXT, antedente TEXT, itens_do_pacote TEXT, vida INT, lvl INT, xp INT)''')


    # Todo o código caso o usuário queira adicionar um personagem
    def adicionar_personagem(self, nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma, antecedente, itens_do_pacote, vida):
        novo_personagem = Personagem(nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma, antecedente, itens_do_pacote, vida, 1, 0)
        novo_personagem = novo_personagem.criacao_dicionario()
        self.cursor.execute("INSERT INTO personagens VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (novo_personagem['Nome'], novo_personagem['Raça'], novo_personagem['Classe'], novo_personagem['Equipamento'], novo_personagem['Dinheiro'], novo_personagem['Proficiências'], novo_personagem['Recursos Especiais'], novo_personagem['Idiomas'], novo_personagem['Força'], novo_personagem['Destreza'], novo_personagem['Constituição'], novo_personagem['Inteligência'], novo_personagem['Sabedoria'], novo_personagem['Carisma'], novo_personagem['Antecedente'], novo_personagem['Itens do pacote que você possui'], novo_personagem['Vida']), novo_personagem['Nível'], novo_personagem['XP'])
        self.conexao.commit()
        print(f'Personagem {nome} criado com sucesso!')

    # Todo o código caso o usuário queira remover um personagem
    def remover_personagem(self):
        selecao = self.cursor.execute('SELECT * FROM personagens')
        dados = selecao.fetchall()

        if not dados:
            print('Não há personagens criados!')
            return
        
        print('Personagens Criados:')
        print('-'*50)
        for row in dados:
            print("Nome:", row[0])
            print()
            print("Pontos de Vida:", row[16])
            print()
            print("Raça:", row[1])
            print()
            print("Classe:", row[2])
            print()
            print("Equipamento:", row[3])
            print()
            print("Itens do pacote que você possui:", row[15])
            print()
            print("Dinheiro:", row[4])
            print()
            print("Proficiências:", row[5])
            print()
            print("Recursos Especiais:", row[6])
            print()
            print("Idiomas:", row[7])
            print(f"""Bônus de Atributo:
Bônus de Força: +{row[8]} 
Bônus de Destreza: +{row[9]} 
Bônus de Constituição: +{row[10]} 
Bônus de Inteligência: +{row[11]}
Bônus de Sabedoria: +{row[12]} 
Bônus de Carisma: +{row[13]}""")
            print()
            print("Antecedente:", row[14])
            print()
            print('Nível:', row[17])
            print()
            print('XP:', row[18])
            print()
            print('-' * 50)
        nome_remocao = input('Digite o nome do personagem que deseja remover: ')

        encontrado = False
        for personagem in dados:
            if nome_remocao == personagem[0]:
                self.cursor.execute("DELETE FROM personagens WHERE nome=?", (nome_remocao,))
                self.conexao.commit()
                print('Personagem removido com sucesso!')
                encontrado = True
                break  

        if not encontrado:
            print(f"Personagem '{nome_remocao}' não foi encontrado.")

    # Todo o código caso o usuário queira listar os personagens
    def listar_personagens(self):
        selecao = self.cursor.execute('SELECT * FROM personagens')
        dados = selecao.fetchall()

        if not dados:
            print('Não há personagens criados!')
            return
        
        print('Personagens Criados:')
        print('-'*50)
        for row in dados:
            print("Nome:", row[0])
            print()
            print("Pontos de Vida:", row[16])
            print()
            print("Raça:", row[1])
            print()
            print("Classe:", row[2])
            print()
            print("Equipamento:", row[3])
            print()
            print("Itens do pacote que você possui:", row[15])
            print()
            print("Dinheiro:", row[4])
            print()
            print("Proficiências:", row[5])
            print()
            print("Recursos Especiais:", row[6])
            print()
            print("Idiomas:", row[7])
            print()
            print(f"""Bônus de Atributo:
  Bônus de Força: +{row[8]} 
  Bônus de Destreza: +{row[9]} 
  Bônus de Constituição: +{row[10]} 
  Bônus de Inteligência: +{row[11]}
  Bônus de Sabedoria: +{row[12]} 
  Bônus de Carisma: +{row[13]}""")
            print()
            print("Antecedente:", row[14])
            print()
            print('Nível:', row[17])
            print()
            print('XP:', row[18])
            print()
            print('-' * 50)

    # Todo o código caso o usuário escolha girar um dado
    def girar_dado(self):
        print('''
Escolha o dado que você deseja girar:

1) Dado de 20 lados
2) Dado de 12 lados
3) Dado de 10 lados
4) Dado de 8 lados
5) Dado de 6 lados
6) Dado de 4 lados
''')
        escolha_do_dado = int(input('Digite a sua escolha: '))
        if escolha_do_dado == 1:
            nome_dado = 'd20'
            dado = random.randint(1, 20)
        
        elif escolha_do_dado == 2:
            nome_dado = 'd12'
            dado = random.randint(1, 12)

        elif escolha_do_dado == 3:
            nome_dado = 'd10'
            dado = random.randint(1, 10)

        elif escolha_do_dado == 4:
            nome_dado = 'd8'
            dado = random.randint(1, 8)
        
        elif escolha_do_dado == 5:
            nome_dado = 'd6'
            dado = random.randint(1, 6)

        elif escolha_do_dado == 6:
            nome_dado = 'd4'
            dado = random.randint(1, 4)

        print(f'Você girou um {nome_dado}. O resultado foi {dado}.')

    # Todo o código caso o usuário queira fechar o programa
    def fechar_conexao(self):
        self.conexao.close()

    # Todo o código caso o usuário ganhe XP
    def ganhar_xp(self, num_xp):
        selecao = self.cursor.execute('SELECT * FROM personagens')
        dados = selecao.fetchall()

        if not dados:
            print('Não há personagens criados!')
            return
        
        print('Personagens Criados:')
        print('-'*50)
        for row in dados:
            print("Nome:", row[0])
            print()
            print("Pontos de Vida:", row[16])
            print()
            print("Raça:", row[1])
            print()
            print("Classe:", row[2])
            print()
            print("Equipamento:", row[3])
            print()
            print("Itens do pacote que você possui:", row[15])
            print()
            print("Dinheiro:", row[4])
            print()
            print("Proficiências:", row[5])
            print()
            print("Recursos Especiais:", row[6])
            print()
            print("Idiomas:", row[7])
            print(f"""Bônus de Atributo:
Bônus de Força: +{row[8]} 
Bônus de Destreza: +{row[9]} 
Bônus de Constituição: +{row[10]} 
Bônus de Inteligência: +{row[11]}
Bônus de Sabedoria: +{row[12]} 
Bônus de Carisma: +{row[13]}""")
            print()
            print("Antecedente:", row[14])
            print()
            print('Nível:', row[17])
            print()
            print('XP:', row[18])
            print()
            print('-' * 50)
        nome_recebedor = input(f'Digite o nome do personagem que deseja receber {num_xp} de XP: ')

        encontrado = False
        for personagem in dados:
            if nome_recebedor == personagem[0]:
                self.cursor.execute("UPDATE personagens SET xp = xp + ? WHERE nome = ?", (num_xp, nome_recebedor))
                self.conexao.commit()
                print(f'{num_xp} de XP foi adicionado ao personagem com sucesso!')
                encontrado = True
                break  

        if not encontrado:
            print(f"Personagem '{nome_recebedor}' não foi encontrado.")
            return

        selecao_xp = self.cursor.execute('SELECT xp FROM personagens WHERE nome = ?', (nome_recebedor,))
        dados_de_xp = selecao_xp.fetchone()[0]

        novo_nivel = None
        if dados_de_xp >= 355000:
            novo_nivel = 20
        elif dados_de_xp >= 305000:
            novo_nivel = 19
        elif dados_de_xp >= 265000:
            novo_nivel = 18
        elif dados_de_xp >= 225000:
            novo_nivel = 17
        elif dados_de_xp >= 195000:
            novo_nivel = 16
        elif dados_de_xp >= 165000:
            novo_nivel = 15
        elif dados_de_xp >= 140000:
            novo_nivel = 14
        elif dados_de_xp >= 120000:
            novo_nivel = 13
        elif dados_de_xp >= 100000:
            novo_nivel = 12
        elif dados_de_xp >= 85000:
            novo_nivel = 11
        elif dados_de_xp >= 64000:
            novo_nivel = 10
        elif dados_de_xp >= 48000:
            novo_nivel = 9
        elif dados_de_xp >= 34000:
            novo_nivel = 8
        elif dados_de_xp >= 23000:
            novo_nivel = 7
        elif dados_de_xp >= 14000:
            novo_nivel = 6
        elif dados_de_xp >= 6500:
            novo_nivel = 5
        elif dados_de_xp >= 2700:
            novo_nivel = 4
        elif dados_de_xp >= 900:
            novo_nivel = 3
        elif dados_de_xp >= 300:
            novo_nivel = 2
        else:
            novo_nivel = 1

        self.cursor.execute("UPDATE personagens SET lvl = ? WHERE nome = ?", (novo_nivel, nome_recebedor))
        self.conexao.commit()
        print(f'Agora seu nível é {novo_nivel}')
        print('-'*50)
