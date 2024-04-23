import sqlite3
import random
# Classe representando as características necessárias de cada personagem
class Personagem:
    # Método Construtor
    def __init__(self, nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma, antecedente, itens_do_pacote, vida):
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
            'Vida': self.vida
        }
        return dicionario


# Classe que fará os sistema de opcões
class SimuladorRPG:
    # Método Construtor
    def __init__(self):
        self.conexao = sqlite3.connect('personagens.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personagens
                            (nome TEXT, raca TEXT, classe TEXT, equipamento TEXT, dinheiro TEXT, proficiencias TEXT, recursos_especiais TEXT, idiomas TEXT, forca TEXT, destreza TEXT, constituicao TEXT, inteligencia TEXT, sabedoria TEXT, carisma TEXT, antedente TEXT, itens_do_pacote TEXT, vida TEXT)''')


    # Todo o código caso o usuário queira adicionar um personagem
    def adicionar_personagem(self, nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma, antecedente, itens_do_pacote, vida):
        novo_personagem = Personagem(nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma, antecedente, itens_do_pacote, vida)
        novo_personagem = novo_personagem.criacao_dicionario()
        self.cursor.execute("INSERT INTO personagens VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (novo_personagem['Nome'], novo_personagem['Raça'], novo_personagem['Classe'], novo_personagem['Equipamento'], novo_personagem['Dinheiro'], novo_personagem['Proficiências'], novo_personagem['Recursos Especiais'], novo_personagem['Idiomas'], novo_personagem['Força'], novo_personagem['Destreza'], novo_personagem['Constituição'], novo_personagem['Inteligência'], novo_personagem['Sabedoria'], novo_personagem['Carisma'], novo_personagem['Antecedente'], novo_personagem['Itens do pacote que você possui'], novo_personagem['Vida']))
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

# Todo o código para a criação do menu
simulador = SimuladorRPG()
print('Bem vindo ao Simulador de Criação de Personagem RPG! Aqui vai o menu de opções para você:')
continuacao = 'y'
while continuacao.lower() == 'y':
    print('''
1) Adicionar um personagem
2) Remover um personagem
3) Listar os personagens criados
4) Rolar dados
''')
    escolha = int(input('Digite a opção escolhida: '))
    print('='*50)

    # Todo o código caso o usuário escolha a primeira opção
    if escolha == 1:
        nome = input('Digite o nome que deseja dar ao seu personagem: ')
        print('-'*50)
        print(f'''
Escolha a sua raça!

1) Humano: Versáteis e adaptáveis, os humanos são encontrados em todos os cantos do mundo de D&D, 
mostrando grande diversidade cultural e habilidades variadas.

2) Elfo: Elegantes e graciosos, os elfos são conhecidos por sua longevidade e conexão 
com a natureza, muitas vezes sendo habilidosos em magia e arco e flecha.

3) Anão: Robustos e resistentes, os anões são mestres em trabalhar com metais e pedras, 
além de serem conhecidos por sua ferocidade em batalha e seu amor por cerveja.

4) Halfling: Pequenos e ágeis, os halflings são conhecidos por sua sorte inata e habilidade em se esquivar de perigos, 
além de serem famosos por sua paixão por comida e conforto doméstico.

5) Meio-elfo: Uma mistura das características humanas e élficas, os meio-elfos são diplomáticos por natureza e muitas vezes encontram-se confortáveis tanto em comunidades 
humanas quanto em ambientes élficos, sendo adaptáveis e versáteis em suas habilidades.
            
6) Meio-orc: Filhos de humanos e orcs, os meio-orcs são frequentemente marginalizados devido à sua origem, mas possuem 
uma força física impressionante e uma determinação feroz, tornando-se guerreiros temíveis e resilientes.

7) Tiefling: Descendentes de humanos e seres infernais, os tieflings possuem traços demoníacos visíveis, como chifres, 
cauda e olhos incandescentes. Apesar da desconfiança que frequentemente enfrentam, os tieflings são dotados de uma astúcia natural e um potencial para a magia infernal.

8) Draconato: Descendentes de dragões, os draconatos exibem traços dragônicos como escamas, asas e sopro elemental. 
Eles possuem uma forte ligação com a linhagem de seus ancestrais dracônicos e são conhecidos por sua honra e determinação em alcançar seus objetivos.

9) Gnomo: Conhecidos por sua engenhosidade e curiosidade, os gnomos são seres pequenos e ágeis, muitas vezes dotados 
de uma afinidade natural com a magia e uma habilidade especial para criar dispositivos mecânicos.
''')
        escolha_raça = int(input('Digite a opção escolhida: '))
        if escolha_raça == 1:
            raça = 'Humano'
            dicionario_de_bonus = {
                'Força': 1,
                'Destreza': 1,
                'Constituição': 1,
                'Inteligência': 1,
                'Sabedoria': 1,
                'Carisma': 1
            }
            idiomas = 'Comum, um idioma adicional de sua escolha'

        elif escolha_raça == 2:
            raça = 'Elfo'
            dicionario_de_bonus = {
                'Força': 0,
                'Destreza': 2,
                'Constituição': 0,
                'Inteligência': 0,
                'Sabedoria': 1,
                'Carisma': 0
            }
            idiomas = 'Comum, Élfico'
        
        elif escolha_raça == 3:
            raça = 'Anão'
            dicionario_de_bonus = {
                'Força': 2,
                'Destreza': 0,
                'Constituição': 2,
                'Inteligência': 0,
                'Sabedoria': 0,
                'Carisma': 0
            }
            idiomas = 'Comum, Anão'

        elif escolha_raça == 4:
            raça = 'Halfling'
            dicionario_de_bonus = {
                'Força': 0,
                'Destreza': 2,
                'Constituição': 0,
                'Inteligência': 0,
                'Sabedoria': 0,
                'Carisma': 0
            }
            idiomas = 'Comum, Halfling'

        elif escolha_raça == 5:
            raça = 'Meio-elfo'
            dicionario_de_bonus = {
                'Força': 0,
                'Destreza': 1,
                'Constituição': 0,
                'Inteligência': 1,
                'Sabedoria': 0,
                'Carisma': 2
            }
            idiomas = 'Comum, Élfico, um idioma adicional de sua escolha'

        elif escolha_raça == 6:
            raça = 'Meio-orc'
            dicionario_de_bonus = {
                'Força': 2,
                'Destreza': 0,
                'Constituição': 1,
                'Inteligência': 0,
                'Sabedoria': 0,
                'Carisma': 0
            }
            idiomas = 'Comum, Orc'

        elif escolha_raça == 7:
            raça = 'Tiefling'
            dicionario_de_bonus = {
                'Força': 0,
                'Destreza': 0,
                'Constituição': 0,
                'Inteligência': 1,
                'Sabedoria': 0,
                'Carisma': 2
            }
            idiomas = 'Comum, Infernal'

        elif escolha_raça == 8:
            raça = 'Draconato'
            dicionario_de_bonus = {
                'Força': 2,
                'Destreza': 0,
                'Constituição': 0,
                'Inteligência': 0,
                'Sabedoria': 0,
                'Carisma': 1
            }
            idiomas = 'Comum, Dracônico'

        elif escolha_raça == 9:
            raça = 'Gnomo'
            dicionario_de_bonus = {
                'Força': 0,
                'Destreza': 0,
                'Constituição': 0,
                'Inteligência': 2,
                'Sabedoria': 0,
                'Carisma': 0
            }
            idiomas = 'Comum, Gnômico, um idioma adicional de sua escolha'
        print('-'*50)
        if 'um idioma adicional de sua escolha' in idiomas:
            print('''
Lista de Idiomas!
                  
1) Anão: O idioma falado por anões.
                  
2) Élfico: O idioma dos elfos.
                  
3) Halfling: O idioma dos halflings (também conhecido como linguagem dos pequenos).
                  
4) Infernal: O idioma das criaturas infernais e dos tieflings.
                  
5) Dracônico: O idioma dos dragões e de algumas criaturas draconianas.
                  
6) Gnômico: O idioma dos gnomos.
                  
7) Orc: O idioma dos orcs e de algumas outras criaturas brutais.
''')
            print('-'*50)
            print(f'O seus idiomas por enquanto são: {idiomas}')
            idioma_adicional = int(input('Você precisa escolher um idioma adicional, digite o número correspondente a ele aqui: '))
            if idioma_adicional == 1:
                idiomas = idiomas.replace('um idioma adicional de sua escolha', 'Anão')

            elif idioma_adicional == 2:
                idiomas = idiomas.replace('um idioma adicional de sua escolha', 'Élfico')

            elif idioma_adicional == 3:
                idiomas = idiomas.replace('um idioma adicional de sua escolha', 'Halfling')

            elif idioma_adicional == 4:
                idiomas = idiomas.replace('um idioma adicional de sua escolha', 'Infernal')

            elif idioma_adicional == 5:
                idiomas = idiomas.replace('um idioma adicional de sua escolha', 'Dracônico')

            elif idioma_adicional == 6:
                idiomas = idiomas.replace('um idioma adicional de sua escolha', 'Gnômico')

            elif idioma_adicional == 7:
                idiomas = idiomas.replace('um idioma adicional de sua escolha', 'Orc')

        print('-'*50)
        print('''
Escolha sua classe!
              
1) Guerreiro: Mestres em combate corpo a corpo e em armas, os guerreiros são poderosos e versáteis, capazes de 
se adaptar a uma variedade de situações de combate e liderar o grupo para a vitória.

2) Mago: Possuidores de conhecimento arcano, os magos manipulam os elementos e lançam poderosos feitiços para 
controlar o campo de batalha, desencadeando magias devastadoras contra seus inimigos.

3) Clérigo: Escolhidos pelos deuses para servir como seus agentes na terra, os clérigos possuem habilidades 
divinas que lhes permitem curar ferimentos, banir o mal e fortalecer seus aliados, enquanto também podem ser proficientes em combate.

4) Bárbaro: Guiados pela fúria, os bárbaros são combatentes selvagens e implacáveis que entram em um estado 
de frenesi durante o combate, desferindo golpes poderosos e resistindo a ferimentos que destruiriam outros combatentes.

5) Druida: Guardiões da natureza, os druidas têm uma forte ligação com o mundo natural, sendo capazes de se 
transformar em animais, conjurar criaturas da natureza e canalizar os poderes dos elementos para proteger o equilíbrio da vida selvagem e da civilização.
              
6) Ladino: Especialistas em furtividade e astúcia, os ladinos são mestres em habilidades de combate furtivo e desarmado, capazes de desarmar 
armadilhas, roubar tesouros e surpreender seus inimigos com golpes precisos e mortais.

7) Mago: Possuidores de conhecimento arcano, os magos manipulam os elementos e lançam poderosos feitiços para controlar o campo de batalha, 
desencadeando magias devastadoras contra seus inimigos.

8) Monge: Treinados nas artes marciais e na disciplina espiritual, os monges são mestres em combate desarmado e em armas simples, 
além de possuírem habilidades sobre-humanas de velocidade, agilidade e resistência.

9) Paladino: Cavaleiros devotos de uma causa sagrada, os paladinos são guerreiros justos e honrados que lutam contra o mal e 
protegem os inocentes. Eles são abençoados com poderes divinos que os capacitam a curar ferimentos, banir o mal e conjurar magias sagradas.

10) Patrulheiro: Sobreviventes habilidosos e mestres rastreadores, os patrulheiros são especialistas em explorar territórios selvagens 
e caçar suas presas. Eles possuem uma ligação especial com a natureza e são capazes de rastrear criaturas, sobreviver em ambientes hostis e lançar magias de proteção e combate.
''')
        escolha_classe = int(input('Digite a opção escolhida: '))
        if escolha_classe == 1:
            dicionario_de_bonus['Força'] += 2
            dicionario_de_bonus['Constituição'] += 2
            classe = 'Guerreiro'
            equipamento = 'Armadura de cota de malha, armadura de couro ou corselete, escudo, uma arma corpo a corpo simples, um arco curto e um aljavade flechas ou uma arma corpo a corpo simples e uma arma à distância simples, pacote de aventureiro'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'
            proficiencias = 'Todas as armas e armaduras, escudos, armas simples e marciais'
            recursos_especiais = 'Ações de Combate - Capacidade de realizar múltiplas ações de combate, bem como outros talentos específicos de guerreiro'
            vida = 10 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 2:
            dicionario_de_bonus['Inteligência'] += 2
            dicionario_de_bonus['Destreza'] += 1
            classe = 'Mago'
            equipamento = 'Um bordão arcano ou varinha, um livro de magias, componentes arcanos, pacote de estudioso'
            dinheiro = '3d4 x 10 peças de ouro (ou seja, de 30 a 120 peças de ouro)'
            proficiencias = 'Nenhuma proficiência adicional em armaduras ou armas, mas pode lançar magias arcanas'
            recursos_especiais = 'Livro de Magias - Capacidade de aprender e lançar uma variedade de magias arcanas de diferentes escolas e níveis de poder'
            vida = 6 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 3:
            dicionario_de_bonus['Sabedoria'] += 2
            dicionario_de_bonus['Carisma'] += 1
            classe = 'Clérigo'
            equipamento = 'Armadura de malha, escudo, uma arma corpo a corpo simples, um símbolo sagrado, pacote de sacerdote'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'
            proficiencias = 'Armaduras leves e médias, escudos, armas simples'
            recursos_especiais = 'Magias - Capacidade de lançar magias divinas, bem como canalizar energia divina para curar ferimentos e afastar o mal'
            vida = 8 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 4:
            dicionario_de_bonus['Força'] += 2
            dicionario_de_bonus['Constituição'] += 2
            classe = 'Bárbaro'
            equipamento = 'Arma corpo a corpo, duas armas corpo a corpo leves, pacote de explorador, quatro machados de arremesso'
            dinheiro = '2d4 x 10 peças de ouro (ou seja, de 20 a 80 peças de ouro)'
            proficiencias = 'Armaduras leves e médias, escudos, armas simples e marciais, ferramentas de artesão, veículos terrestres'
            recursos_especiais = 'Fúria - Capacidade de entrar em um estado de fúria durante o combate, concedendo vantagem em testes de Força, resistência a dano e outros benefícios'
            vida = 12 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 5:
            dicionario_de_bonus['Sabedoria'] += 2
            dicionario_de_bonus['Inteligência'] += 1
            classe = 'Druida'
            equipamento = 'Armadura de couro, um escudo, um foco druídico, uma arma corpo a corpo simples, pacote de aventureiro'
            dinheiro = '2d4 x 10 peças de ouro (ou seja, de 20 a 80 peças de ouro)'
            proficiencias = 'Armaduras leves e médias (sem metal), escudos (não de metal), armas simples, armas marciais, ferramentas de cura'
            recursos_especiais = 'Transformação - Capacidade de se transformar em animais e acessar os poderes da natureza'
            vida = 8 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 6:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Inteligência'] += 1
            classe = 'Ladino'
            equipamento = 'Uma arma corpo a corpo simples, duas armas à distância simples, ferramentas de ladrão, pacote de ladrão'
            dinheiro = '4d4 x 10 peças de ouro (ou seja, de 40 a 160 peças de ouro)'
            proficiencias = 'Armaduras leves, armas simples, ferramentas de ladrão, veículos terrestres'
            recursos_especiais = 'Furtividade - Capacidade de se mover furtivamente e realizar ações de combate furtivas, bem como desarmar armadilhas e abrir fechaduras'
            vida = 8 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 7:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Carisma'] += 2
            classe = 'Bardo'
            equipamento = 'Uma arma corpo a corpo simples, uma arma à distância simples, um instrumento musical, pacote de entretenimento'
            dinheiro = '3d4 x 10 peças de ouro (ou seja, de 30 a 120 peças de ouro)'
            proficiencias = 'Armaduras leves, armas simples, ferramentas de artesão, veículos terrestres'
            recursos_especiais = 'Magias - Capacidade de lançar magias, bem como inspirar aliados e desencorajar inimigos com seu talento musical'
            vida = 8 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 8:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Sabedoria'] += 1
            classe = 'Monge'
            equipamento = 'Arma corpo a corpo simples, pacote de explorador'
            dinheiro = '5d4 po (ou seja, de 5 a 20 peças de ouro)'
            proficiencias = 'Armas simples, armas corpo a corpo leves, ferramentas de artesão'
            recursos_especiais = 'Ki - Capacidade de canalizar sua energia interior para realizar feitos sobre-humanos, como ataques desarmados poderosos e habilidades especiais como esquiva sobrenatural e toque tranquilo para resistir a efeitos mágicos'
            vida = 8 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 9:
            dicionario_de_bonus['Força'] += 2
            dicionario_de_bonus['Carisma'] += 1
            classe = 'Paladino'
            equipamento = 'Armadura de corselete ou escamas, escudo, uma arma corpo a corpo simples, cinco javelins ou qualquer arma corpo a corpo simples, pacote de aventureiro'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'
            proficiencias = 'Todas as armas e armaduras, escudos, armas simples e marciais'
            recursos_especiais = 'Juramento Sagrado - Capacidade de fazer um juramento sagrado a uma causa ou divindade, concedendo poderes divinos e magias relacionadas ao juramento'
            vida = 10 + dicionario_de_bonus['Constituição']

        elif escolha_classe == 10:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Sabedoria'] += 1
            classe = 'Patrulheiro'
            equipamento = 'Armadura de couro, duas armas corpo a corpo simples, duas armas à distância simples, um pacote de explorador e um símbolo da vida selvagem'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'
            proficiencias = 'Armaduras leves e médias (sem metal), escudos (não de metal), armas simples, armas marciais'
            recursos_especiais = 'Caçador - Capacidade de rastrear presas, sobreviver na natureza selvagem e lançar magias de proteção e combate'
            vida = 10 + dicionario_de_bonus['Constituição']

        if 'pacote de aventureiro' in equipamento:
            itens_do_pacote = 'Uma mochila, um cantil, 10 dias de ração de viagem, uma aljava com 20 flechas, uma tocha, pederneiras e 10 metros de corda de cânhamo.'

        elif 'pacote de estudioso' in equipamento:
            itens_do_pacote = 'Uma mochila, 10 folhas de papel pergaminho, um tinteiro, uma pena, um livro de referência sobre o assunto de sua especialização e trajes comuns.'

        elif 'pacote de sacerdote' in equipamento:
            itens_do_pacote = 'Uma mochila, uma aljava com 20 flechas, uma estola, incenso, um sacrifício religioso e trajes comuns.'

        elif 'pacote de explorador' in equipamento:
            itens_do_pacote = 'Uma mochila, um cantil, alimento de viagem para 10 dias, um par de botas de viagem resistentes, um chapéu de abas largas e trajes comuns.'

        elif 'pacote de ladrão' in equipamento:
            itens_do_pacote = 'Uma mochila, um manto de ladrão, uma bolsa com 1.000 balas de gude, um conjunto de cartões marcados, alimentação para uma semana e trajes finos.'

        elif 'pacote de entretenimento' in equipamento:
            itens_do_pacote = 'Uma mochila, um instrumento musical de sua escolha, 10 folhas de papel pergaminho, um tinteiro, uma pena e trajes comuns.'

        print('-'*50)
        print('-'*50)
        print('''
Escolha seu antecedente!
    
1) Acólito: Um acólito é uma pessoa que dedicou sua vida ao serviço de uma divindade, seja como clérigo, monge, ou de outra forma religiosa. 
Eles possuem conhecimento profundo sobre sua fé e são capazes de influenciar os outros com suas palavras e convicções.
              
2) Artífice de Guilda: Um artífice de guilda é um membro respeitado de uma guilda de artesãos, seja como ferreiro, carpinteiro, 
ou qualquer outra profissão. Eles são habilidosos em seu ofício e têm boas relações dentro da comunidade de artesãos.
              
3) Charlatão: Um charlatão é um trapaceiro e manipulador, habilidoso em enganar os outros para seu próprio benefício. 
Eles são mestres em disfarce e podem facilmente se passar por outra pessoa ou inventar histórias convincentes para alcançar seus objetivos.
              
4) Criminoso: Um criminoso é alguém que vive à margem da lei, envolvido em atividades ilegais como roubo, contrabando, ou extorsão. 
Eles são hábeis em se esconder nas sombras e enganar as autoridades.
              
5) Erudito: Um erudito é alguém que passou anos estudando em bibliotecas e academias, adquirindo conhecimento sobre uma variedade de assuntos. 
Eles são especialistas em suas áreas de estudo e têm uma vasta compreensão do mundo ao seu redor.

6) Fazendeiro: Um fazendeiro é alguém que trabalha na terra, cultivando colheitas e criando animais para sustento próprio ou para o comércio. 
Eles são familiarizados com a vida no campo e têm habilidades práticas de sobrevivência.
              
7) Herói Popular: Um herói popular é alguém que ganhou fama e reconhecimento dentro de uma comunidade específica, seja por atos de heroísmo, 
talento artístico, ou qualquer outra realização notável. Eles têm uma rede de contatos e aliados dentro dessa comunidade e são capazes de 
influenciar os outros com sua reputação.
              
8) Nobre: Um nobre é alguém nascido em uma família de alta classe, com riqueza, poder e influência. Eles são bem-educados e têm uma compreensão 
profunda da história e da política de seu mundo. Eles estão acostumados a receber respeito e obediência dos outros e têm acesso a recursos significativos.

9) Órfão: Um órfão é alguém que cresceu sem pais ou família, sobrevivendo nas ruas ou em instituições de caridade. Eles aprenderam a se virar por conta 
própria desde cedo e desenvolveram habilidades de sobrevivência e furtividade para enfrentar os desafios da vida nas ruas.
              
10) Plebeu: Um plebeu é alguém de origem humilde, trabalhando como artesão, comerciante, ou em outra profissão comum. Eles são habilidosos em seu ofício 
e têm uma compreensão prática do mundo ao seu redor. Apesar de não terem status ou privilégios, são respeitados por suas habilidades e trabalho árduo.
''')
        escolha_antecedente = int(input('Digite a opção escolhida: '))
        if escolha_antecedente == 1:
            antecedente = 'Acólito'
            proficiencias += ', Conhecimento de Religião, Persuasão.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 2:
            antecedente = 'Artífice de Guilda'
            proficiencias += ', Ferramentas de Artesão, Persuasão.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 3:
            antecedente = 'Charlatão'
            proficiencias += ', Fraude e Falsificação, Enganação.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 4:
            antecedente = 'Criminoso'
            proficiencias += ', Furtividade, Enganação.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 5:
            antecedente = 'Erudito'
            proficiencias += ', História, Intuição.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 6:
            antecedente = 'Fazendeiro'
            proficiencias += ', Agricultura e Animais, Sobrevivência.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 7:
            antecedente = 'Herói Popular'
            proficiencias += ', Falar e Influenciar, Persuasão.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 8:
            antecedente = 'Nobre'
            proficiencias += ', História, Persuasão.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 9:
            antecedente = 'Órfão'
            proficiencias += ', Furtividade, Sobrevivência.'
            idiomas += ', um idioma à sua escolha.'

        elif escolha_antecedente == 10:
            antecedente = 'Plebeu'
            proficiencias += ', Ferramentas de Artesão, Persuasão.'
            idiomas += ', um idioma à sua escolha.'

        print('-'*50)
        if 'um idioma à sua escolha' in idiomas:
            print('''
Lista de Idiomas!
                  
1) Anão: O idioma falado por anões.
                  
2) Élfico: O idioma dos elfos.
                  
3) Halfling: O idioma dos halflings (também conhecido como linguagem dos pequenos).
                  
4) Infernal: O idioma das criaturas infernais e dos tieflings.
                  
5) Dracônico: O idioma dos dragões e de algumas criaturas draconianas.
                  
6) Gnômico: O idioma dos gnomos.
                  
7) Orc: O idioma dos orcs e de algumas outras criaturas brutais.
''')
            print('-'*50)
            print(f'O seus idiomas por enquanto são: {idiomas}')
            idioma_adicional = int(input('Você precisa escolher um idioma adicional, digite o número correspondente a ele aqui: '))
            if idioma_adicional == 1:
                idiomas = idiomas.replace('um idioma à sua escolha', 'Anão')

            elif idioma_adicional == 2:
                idiomas = idiomas.replace('um idioma à sua escolha', 'Élfico')

            elif idioma_adicional == 3:
                idiomas = idiomas.replace('um idioma à sua escolha', 'Halfling')

            elif idioma_adicional == 4:
                idiomas = idiomas.replace('um idioma à sua escolha', 'Infernal')

            elif idioma_adicional == 5:
                idiomas = idiomas.replace('um idioma à sua escolha', 'Dracônico')

            elif idioma_adicional == 6:
                idiomas = idiomas.replace('um idioma à sua escolha', 'Gnômico')

            elif idioma_adicional == 7:
                idiomas = idiomas.replace('um idioma à sua escolha', 'Orc')
        print('-'*50)

        simulador.adicionar_personagem(nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, dicionario_de_bonus['Força'], dicionario_de_bonus['Destreza'], dicionario_de_bonus['Constituição'], dicionario_de_bonus['Inteligência'], dicionario_de_bonus['Sabedoria'], dicionario_de_bonus['Carisma'], antecedente, itens_do_pacote, vida)
        print('='*50)

    # Todo o código caso o usuário escolha a segunda opção
    elif escolha == 2:
        simulador.remover_personagem()
        print('='*50)

    # Todo o código caso o usuário escolha a terceira opção
    elif escolha == 3:
        simulador.listar_personagens()
        print('='*50)

    elif escolha == 4:
        simulador.girar_dado()
        print('='*50)

    continuacao = input('Você quer continuar usando o programa? Digite Y para sim e N para não: ')

print('Obrigado por usar meu programa!')
fechar = input('Digite qualquer tecla para sair... ')
simulador.fechar_conexao()