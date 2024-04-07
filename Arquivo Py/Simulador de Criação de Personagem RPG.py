# Classe representando as características necessárias de cada personagem
class Personagem:
    # Método Construtor
    def __init__(self, nome, raça, classe, equipamento, dinheiro):
        self.nome = nome
        self.raça = raça
        self.classe = classe
        self.equipamento = equipamento
        self.dinheiro = dinheiro

    # Criação do nosso dicionário pra colocar na lista dos personagens
    def criacao_dicionario(self):
        dicionario = {
            'Nome': self.nome,
            'Raça': self.raça,
            'Classe': self.classe,
            'Equipamento': self.equipamento,
            'Dinheiro': self.dinheiro
        }
        return dicionario


# Classe que fará os sistema de opcões
class SimuladorRPG:
    # Método Construtor
    def __init__(self):
        self.personagens = []

    # Todo o código caso o usuário queira adicionar um personagem
    def adicionar_personagem(self, nome, raça, classe, equipamento, dinheiro):
        novo_personagem = Personagem(nome, raça, classe, equipamento, dinheiro)
        novo_personagem = novo_personagem.criacao_dicionario()
        self.personagens.append(novo_personagem)
        print(f'Personagem {nome} criado com sucesso!')

    # Todo o código caso o usuário queira remover um personagem
    def remover_personagem(self):
        print('Personagens Criados:')
        print('-'*50)
        for personagem in self.personagens:
            print(f'''
Nome: {personagem['Nome']}
Raça: {personagem['Raça']}
Classe: {personagem['Classe']}
Equipamento: {personagem['Equipamento']}
Dinheiro: {personagem['Dinheiro']}
''')
            print('-'*50)

        nome_remocao = input('Digite o nome do personagem que deseja remover: ')

        encontrado = False
        for personagem in self.personagens:
            if nome_remocao == personagem['Nome']:
                self.personagens.remove(personagem)
                print('Personagem removido com sucesso!')
                encontrado = True
                break  

        if not encontrado:
            print(f"Personagem '{nome_remocao}' não foi encontrado.")

    # Todo o código caso o usuário queira listar os personagens
    def listar_personagens(self):
        if not self.personagens:
            print('Não há personagens criados!')
            return
        
        print('Personagens Criados:')
        print('-'*50)
        for personagem in self.personagens:
            print(f'''
Nome: {personagem['Nome']}
Raça: {personagem['Raça']}
Classe: {personagem['Classe']}
Equipamento: {personagem['Equipamento']}
Dinheiro: {personagem['Dinheiro']}
''')
            print('-'*50)


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
''')
        escolha_raça = int(input('Digite a opção escolhida: '))
        if escolha_raça == 1:
            raça = 'Humano'

        elif escolha_raça == 2:
            raça = 'Elfo'
        
        elif escolha_raça == 3:
            raça = 'Anão'

        elif escolha_raça == 4:
            raça = 'Halfling'

        elif escolha_raça == 5:
            raça = 'Meio-elfo'

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
''')
        escolha_classe = int(input('Digite a opção escolhida: '))
        if escolha_classe == 1:
            classe = 'Guerreiro'
            equipamento = 'Armadura, Arma corpo a corpo, Arma à distância, Pacote de aventureiro'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'

        elif escolha_classe == 2:
            classe = 'Mago'
            equipamento = 'Bastão arcano ou varinha, Livro de magias, Componentes arcanos, Pacote de aventureiro'
            dinheiro = '25 peças de ouro, um foco arcano ou componentes para um, mochila, 10 peças de ouro'
        
        elif escolha_classe == 3:
            classe = 'Clérigo'
            equipamento = 'Armadura, Escudo, Símbolo sagrado, Mochila ou bolsa de componentes, Pacote de aventureiro'
            dinheiro = '5d4 x 10 peças de ouro (ou seja, de 50 a 200 peças de ouro)'

        elif escolha_classe == 4:
            classe = 'Bárbaro'
            equipamento = 'Armadura, Arma corpo a corpo, Pacote de aventureiro, Fonte de alimento portátil'
            dinheiro = '2d4 x 10 peças de ouro (ou seja, de 20 a 80 peças de ouro)'

        elif escolha_classe == 5:
            classe = 'Druida'
            equipamento = 'Armadura leve, Escudo, Foco druídico, Arma corpo a corpo simples, Pacote de aventureiro'
            dinheiro = '2d4 x 10 peças de ouro (ou seja, de 20 a 80 peças de ouro)'

        simulador.adicionar_personagem(nome, raça, classe, equipamento, dinheiro)
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