import random

class User:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def throwCard(self):
        while True:
            card = input('Выберите карту или введите "lose", чтобы забрать все карты со стола: ')
            if card in self.hand:
                self.hand.remove(card)
                return card
            elif card == 'lose':
                return 'lose'
            else:
                print('Такой карты в руке нет!')
                continue

class Deck:
    def __init__(self):
        self.deck = ['09_heart', '09_spades', '09_diamonds', '09_clubs',
                    '10_heart', '10_spades', '10_diamonds', '10_clubs',
                    '11_heart', '11_spades', '11_diamonds', '11_clubs', #JACK\Валет
                    '12_heart', '12_spades', '12_diamonds', '12_clubs', #QUEEN\Королева
                    '13_heart', '13_spades', '13_diamonds', '13_clubs', #KING\Король
                    '14_heart', '14_spades', '14_diamonds', '14_clubs'] #ACE\Туз

    def giveCard(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def getSize(self):
        return len(self.deck)

class Rules:
    def __init__(self, trump=None):
        self.trump = trump

    def checkStatus(self, attack_card, defend_card):
        if (attack_card[3:] == defend_card[3:]) or defend_card[3:] == self.trump:
            if (int(attack_card[:2]) < int(defend_card[:2]) or (attack_card[3:] != self.trump and defend_card[3:] == self.trump)):
                return 1
            else:
                print('Вы не можете отбиться младшей картой!')
                return 0
        else:
            print('Ваша карта должна быть той же масти или козырем!')
            return 0

class Game(Rules):
    def __init__(self):
        trump = random.choice(['heart', 'spades', 'diamonds', 'clubs'])
        super().__init__(trump)
        print('Козырь этой игры: ', self.trump)

    def play(self):
        #Создаем колоду для игры
        deck = Deck()

        #Создаем первого игрока
        _name = input('Введите имя игрока 1: ')
        _hand = []
        for i in range(6):
            _hand.append(deck.giveCard())
        player1 = User(_name, _hand)

        #Создаем второго игрока
        _name = input('Введите имя игрока 2: ')
        _hand = []
        for i in range(6):
            _hand.append(deck.giveCard())
        player2 = User(_name, _hand)

        winner = player1
        loser = player2
        while (deck.getSize() != 0) and (len(player1.hand) != 0 or len(player2.hand) != 0):
                while len(winner.hand) < 6:
                    if deck.getSize() == 0:
                        print('В колоде закончились карты')
                        break
                    else:
                        winner.hand.append(deck.giveCard())

                while len(loser.hand) < 6:
                    if deck.getSize() == 0:
                        print('В колоде закончились карты')
                        break
                    else:
                        loser.hand.append(deck.giveCard())

                #attack_card = ''
                #defend_card = ''
                table_cards = []

                #создаем проигравшего и победившего игрока. ходить всегда будет победивший

                print(f'\nИгрок {winner.name} атакует')
                print(sorted(winner.hand))
                attack_card = winner.throwCard()
                while attack_card == 'lose':
                    print('Вы не можете забрать карты, так как вы атакуете')
                    attack_card = winner.throwCard()
                table_cards.append(attack_card)

                print(f'\nИгрок {loser.name} отбивает {attack_card}')
                print(sorted(loser.hand))
                while True:
                    defend_card = loser.throwCard()
                    table_cards.append(defend_card)
                    if defend_card == 'lose':
                        for i in table_cards:
                            loser.hand.append(i)
                        print('Вы забрали все карты со стола')
                        break
                    elif self.checkStatus(attack_card=attack_card, defend_card=defend_card) == 0:
                        continue
                    elif self.checkStatus(attack_card=attack_card, defend_card=defend_card) == 1:
                        print('Вы отбили карту')
                        table_cards.append(defend_card)
                        tmp = winner
                        winner = loser
                        loser = tmp
                        break
        print(f'Игра окончена! Победил игрок {winner}')

game = Game()
game.play()