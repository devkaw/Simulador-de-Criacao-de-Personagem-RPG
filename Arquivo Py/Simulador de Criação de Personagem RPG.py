import sqlite3
# Classe representando as características necessárias de cada personagem
class Personagem:
    # Método Construtor
    def __init__(self, nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
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
            'Carisma': self.carisma
        }
        return dicionario


# Classe que fará os sistema de opcões
class SimuladorRPG:
    # Método Construtor
    def __init__(self):
        self.conexao = sqlite3.connect('personagens.db')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personagens
                            (nome TEXT, raca TEXT, classe TEXT, equipamento TEXT, dinheiro TEXT, proficiencias TEXT, recursos_especiais TEXT, idiomas TEXT, forca TEXT, destreza TEXT, constituicao TEXT, inteligencia TEXT, sabedoria TEXT, carisma TEXT)''')


    # Todo o código caso o usuário queira adicionar um personagem
    def adicionar_personagem(self, nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma):
        novo_personagem = Personagem(nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, forca, destreza, constituicao, inteligencia, sabedoria, carisma)
        novo_personagem = novo_personagem.criacao_dicionario()
        self.cursor.execute("INSERT INTO personagens VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                          (novo_personagem['Nome'], novo_personagem['Raça'], novo_personagem['Classe'], novo_personagem['Equipamento'], novo_personagem['Dinheiro'], novo_personagem['Proficiências'], novo_personagem['Recursos Especiais'], novo_personagem['Idiomas'], novo_personagem['Força'], novo_personagem['Destreza'], novo_personagem['Constituição'], novo_personagem['Inteligência'], novo_personagem['Sabedoria'], novo_personagem['Carisma']))
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
            print("Raça:", row[1])
            print()
            print("Classe:", row[2])
            print()
            print("Equipamento:", row[3])
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
            print("Raça:", row[1])
            print()
            print("Classe:", row[2])
            print()
            print("Equipamento:", row[3])
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
            print('-' * 50)


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
            idiomas = 'Comum e um idioma adicional de sua escolha'

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
            idiomas = 'Comum e Élfico'
        
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
            idiomas = 'Comum e Anão'

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
            idiomas = 'Comum e Halfling'

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
            idiomas = 'Comum, Élfico e um idioma adicional de sua escolha'

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
            idiomas = 'Comum e Orc'

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
            idiomas = 'Comum e Infernal'

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
            idiomas = 'Comum e Dracônico'

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
            idiomas = 'Comum, Gnômico e um idioma adicional de sua escolha'

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

        elif escolha_classe == 2:
            dicionario_de_bonus['Inteligência'] += 2
            dicionario_de_bonus['Destreza'] += 1
            classe = 'Mago'
            equipamento = 'Um bordão arcano ou varinha, um livro de magias, componentes arcanos, pacote de estudioso ou pacote de aventureiro'
            dinheiro = '3d4 x 10 peças de ouro (ou seja, de 30 a 120 peças de ouro)'
            proficiencias = 'Nenhuma proficiência adicional em armaduras ou armas, mas pode lançar magias arcanas'
            recursos_especiais = 'Livro de Magias - Capacidade de aprender e lançar uma variedade de magias arcanas de diferentes escolas e níveis de poder'

        elif escolha_classe == 3:
            dicionario_de_bonus['Sabedoria'] += 2
            dicionario_de_bonus['Carisma'] += 1
            classe = 'Clérigo'
            equipamento = 'Armadura de malha, escudo, uma arma corpo a corpo simples, um símbolo sagrado, pacote de sacerdote ou pacote de explorador'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'
            proficiencias = 'Armaduras leves e médias, escudos, armas simples'
            recursos_especiais = 'Magias - Capacidade de lançar magias divinas, bem como canalizar energia divina para curar ferimentos e afastar o mal'

        elif escolha_classe == 4:
            dicionario_de_bonus['Força'] += 2
            dicionario_de_bonus['Constituição'] += 2
            classe = 'Bárbaro'
            equipamento = 'Arma corpo a corpo, duas armas corpo a corpo leves, pacote de explorador ou pacote de aventureiro, quatro machados de arremesso'
            dinheiro = '2d4 x 10 peças de ouro (ou seja, de 20 a 80 peças de ouro)'
            proficiencias = 'Armaduras leves e médias, escudos, armas simples e marciais, ferramentas de artesão (uma à escolha), veículos terrestres'
            recursos_especiais = 'Fúria - Capacidade de entrar em um estado de fúria durante o combate, concedendo vantagem em testes de Força, resistência a dano e outros benefícios'

        elif escolha_classe == 5:
            dicionario_de_bonus['Sabedoria'] += 2
            dicionario_de_bonus['Inteligência'] += 1
            classe = 'Druida'
            equipamento = 'Armadura de couro, um escudo, um foco druídico, uma arma corpo a corpo simples, pacote de explorador ou pacote de aventureiro'
            dinheiro = '2d4 x 10 peças de ouro (ou seja, de 20 a 80 peças de ouro)'
            proficiencias = 'Armaduras leves e médias (sem metal), escudos (não de metal), armas simples, armas marciais, ferramentas de cura'
            recursos_especiais = 'Transformação - Capacidade de se transformar em animais e acessar os poderes da natureza'

        elif escolha_classe == 6:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Inteligência'] += 1
            classe = 'Ladino'
            equipamento = 'Uma arma corpo a corpo simples, duas armas à distância simples, ferramentas de ladrão, pacote de ladrão'
            dinheiro = '4d4 x 10 peças de ouro (ou seja, de 40 a 160 peças de ouro)'
            proficiencias = 'Armaduras leves, armas simples, ferramentas de ladrão, veículos terrestres'
            recursos_especiais = 'Furtividade - Capacidade de se mover furtivamente e realizar ações de combate furtivas, bem como desarmar armadilhas e abrir fechaduras'

        elif escolha_classe == 7:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Carisma'] += 2
            classe = 'Bardo'
            equipamento = 'Uma arma corpo a corpo simples, uma arma à distância simples, um instrumento musical (à escolha), pacote de diplomata ou pacote de entretenimento'
            dinheiro = '3d4 x 10 peças de ouro (ou seja, de 30 a 120 peças de ouro)'
            proficiencias = 'Armaduras leves, armas simples, ferramentas de artesão (três à escolha), veículos terrestres'
            recursos_especiais = 'Magias - Capacidade de lançar magias, bem como inspirar aliados e desencorajar inimigos com seu talento musical'

        elif escolha_classe == 8:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Sabedoria'] += 1
            classe = 'Monge'
            equipamento = 'Arma corpo a corpo simples, pacote de explorador ou pacote de aventureiro'
            dinheiro = '5d4 po (ou seja, de 5 a 20 peças de ouro)'
            proficiencias = 'Armas simples, armas corpo a corpo leves, ferramentas de artesão (uma à escolha)'
            recursos_especiais = 'Ki - Capacidade de canalizar sua energia interior para realizar feitos sobre-humanos, como ataques desarmados poderosos e habilidades especiais como esquiva sobrenatural e toque tranquilo para resistir a efeitos mágicos'

        elif escolha_classe == 9:
            dicionario_de_bonus['Força'] += 2
            dicionario_de_bonus['Carisma'] += 1
            classe = 'Paladino'
            equipamento = 'Armadura de corselete ou escamas, escudo, uma arma corpo a corpo simples, cinco javelins ou qualquer arma corpo a corpo simples, pacote de sacerdote ou pacote de aventureiro'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'
            proficiencias = 'Todas as armas e armaduras, escudos, armas simples e marciais'
            recursos_especiais = 'Juramento Sagrado - Capacidade de fazer um juramento sagrado a uma causa ou divindade, concedendo poderes divinos e magias relacionadas ao juramento'

        elif escolha_classe == 10:
            dicionario_de_bonus['Destreza'] += 2
            dicionario_de_bonus['Sabedoria'] += 1
            classe = 'Patrulheiro'
            equipamento = 'Armadura de couro, duas armas corpo a corpo simples, duas armas à distância simples, um pacote de explorador e um símbolo da vida selvagem'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'
            proficiencias = 'Armaduras leves e médias (sem metal), escudos (não de metal), armas simples, armas marciais'
            recursos_especiais = 'Caçador - Capacidade de rastrear presas, sobreviver na natureza selvagem e lançar magias de proteção e combate'

        simulador.adicionar_personagem(nome, raça, classe, equipamento, dinheiro, proficiencias, recursos_especiais, idiomas, dicionario_de_bonus['Força'], dicionario_de_bonus['Destreza'], dicionario_de_bonus['Constituição'], dicionario_de_bonus['Inteligência'], dicionario_de_bonus['Sabedoria'], dicionario_de_bonus['Carisma'])
        print('='*50)

    # Todo o código caso o usuário escolha a segunda opção
    elif escolha == 2:
        simulador.remover_personagem()
        print('='*50)

    # Todo o código caso o usuário escolha a terceira opção
    elif escolha == 3:
        simulador.listar_personagens()
        print('='*50)

    continuacao = input('Você quer continuar usando o programa? Digite Y para sim e N para não: ')

print('Obrigado por usar meu programa!')
fechar = input('Digite qualquer tecla para sair... ')
simulador.fechar_conexao()