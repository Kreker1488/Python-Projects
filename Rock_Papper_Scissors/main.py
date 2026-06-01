import os


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.move = None

    def make_move(self):
        """Игрок делает ход"""
        while True:
            self.move = input(f"{self.name}, твой ход (камень, ножницы, бумага): ").lower()
            if self.move in ['камень', 'ножницы', 'бумага']:
                return self.move
            else:
                print("Неверный ввод! Попробуй ещё раз.")

    def add_point(self):
        """Добавить очко игроку"""
        self.score += 1

    @staticmethod
    def clear_console():
        """Очистка консоли (скрывает ход первого игрока)"""
        os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self):
        self.player1 = Player("Игрок 1")
        self.player2 = Player("Игрок 2")
        self.winner = None

    def determine_winner(self, move1, move2):
        """Определяет победителя раунда"""
        if move1 == move2:
            return None  # Ничья

        winning_pairs = {
            'камень': 'ножницы',
            'ножницы': 'бумага',
            'бумага': 'камень'
        }

        if winning_pairs[move1] == move2:
            return self.player1
        else:
            return self.player2

    def show_score(self):
        """Показать текущий счёт"""
        print("\n" + "=" * 30)
        print(f"СЧЁТ: {self.player1.name} {self.player1.score} : {self.player2.score} {self.player2.name}")
        print("=" * 30 + "\n")

    def play_round(self):
        """Один раунд игры"""
        # Ход первого игрока
        self.player1.make_move()

        # Очищаем консоль, чтобы скрыть ход
        Player.clear_console()
        print("Ход первого игрока скрыт! Теперь ход второго игрока.\n")

        # Ход второго игрока
        self.player2.make_move()

        # Определяем победителя раунда
        winner = self.determine_winner(self.player1.move, self.player2.move)

        # Выводим ходы
        print(f"\n{self.player1.name} показал: {self.player1.move}")
        print(f"{self.player2.name} показал: {self.player2.move}")

        # Начисляем очки
        if winner == self.player1:
            self.player1.add_point()
            print(f"\n🏆 {self.player1.name} выиграл раунд! 🏆")
        elif winner == self.player2:
            self.player2.add_point()
            print(f"\n🏆 {self.player2.name} выиграл раунд! 🏆")
        else:
            print("\n🤝 Ничья! 🤝")

        # Показываем счёт
        self.show_score()

        return winner

    def play_game(self):
        """Основная игра до 3 побед"""
        print("\nДОБРО ПОЖАЛОВАТЬ В ИГРУ 'КАМЕНЬ-НОЖНИЦЫ-БУМАГА'")
        print("Правила: играем до 3 побед!\n")
        input("Нажми Enter, чтобы начать...")
        Player.clear_console()

        round_num = 1
        while self.player1.score < 3 and self.player2.score < 3:
            print(f"\n--- РАУНД {round_num} ---")
            self.play_round()
            round_num += 1

        # Объявляем победителя игры
        self.show_final_winner()

    def show_final_winner(self):
        """Объявить победителя игры"""
        print("\n" + "🎉" * 15)
        if self.player1.score == 3:
            print(f"ПОБЕДИТЕЛЬ ИГРЫ: {self.player1.name} со счётом {self.player1.score}:{self.player2.score} 🏆")
        else:
            print(f"ПОБЕДИТЕЛЬ ИГРЫ: {self.player2.name} со счётом {self.player2.score}:{self.player1.score} 🏆")
        print("🎉" * 15 + "\n")
        print("Спасибо за игру! 👋")


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.play_game()
