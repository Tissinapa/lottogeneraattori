import random
class LotteryGame:
    def __init__(self):
        self.gameMode = None
        self.numbers = []
        self.additionalNumbers = []
        
        
    def gameModes(self):
            games = ["Lotto", "Vikinglotto", "Eurojackpot"]
            while True:
                
                print("1) Lotto")
                print("2) Vikinglotto")
                print("3) Eurojackpot")
                game_input = input("Valintasi: ")
                print()
                if game_input == "1" or game_input == "2" or game_input == "3":
                    print(f'Pelataan peliä **{games[int(game_input) - 1]}**')
                    print()
                    self.gameMode = game_input
                    return 
                print("Annoit virheellisen syötteen. ")
        
    # Lotto 30 numeroa arv.7 + 1 lisänumero
    # Vikinglotto 48 numeroa arv.6 + 1 lisänumero (1-30)
    # Eurojackpot 50 Päänumeroa arv. 5 numeroa + 12 tähtinumerosta arv.2 tähti numeroa
    def generate_Numbers(self):
        #Lotto
        if self.gameMode == None or self.gameMode == '1':
            if len(self.numbers) > 1 and len(self.additionalNumbers) >= 1:
                self.numbers.clear()
                self.additionalNumbers.clear()
            gen_random_numb = random.sample(range(1,31),7)
            gen_rand_addi_numb =random.sample(range(1,31),1)
            self.numbers.extend(gen_random_numb)
            self.additionalNumbers.extend(gen_rand_addi_numb)
            self.numbers.sort()
            print(f'Arvotaan Lottonumerot. ')
            
        #Vikinglotto
        elif self.gameMode == "2":
            if len(self.numbers) > 1 and len(self.additionalNumbers) >= 1:
                self.numbers.clear()
                self.additionalNumbers.clear()
            gen_random_numb = random.sample(range(1,49),6)
            gen_rand_addi_numb =random.sample(range(1,49),1)
            self.numbers.extend(gen_random_numb)
            self.additionalNumbers.extend(gen_rand_addi_numb)
            self.numbers.sort()
            print(f'Arvotaan Vikinglottonumerot. ')
        #Eurojackpot
        elif self.gameMode == "3":
            if len(self.numbers) > 1 and len(self.additionalNumbers) >= 1:
                self.numbers.clear()
                self.additionalNumbers.clear()
            gen_random_numb = random.sample(range(1,51),5)
            gen_rand_addi_numb = random.sample(range(1,13),2)
            self.numbers.extend(gen_random_numb)
            self.additionalNumbers.extend(gen_rand_addi_numb)
            self.numbers.sort()
            print(f'Arvotaan Eurojackpotnumerot. ')
        
        return print(f'Ohjelma genereoi numerot {self.numbers} ja lisänumerot {self.additionalNumbers}\n')
    
    def selectOwnNumbers(self):
        user_numb_input = None

        # Lotto
        if self.gameMode is None or self.gameMode == '1':
            if len(self.numbers) > 1 and len(self.additionalNumbers) >= 1:
                self.numbers.clear()
                self.additionalNumbers.clear()

            print("Anna numero väliltä 1 - 30 ")
            while len(self.numbers) < 7:
                try:
                    user_numb_input = int(input())
                    if 1 <= user_numb_input <= 30:
                        if user_numb_input not in self.numbers:
                            self.numbers.append(user_numb_input)
                        else:
                            print("Tämä numero on jo annettu! Anna toinen numero.")
                    else:
                        print("Annoit väärän numeron!")
                except ValueError:
                    print("Syötteen täytyy olla kokonaisluku!")
            
            print("Anna lisänumero väliltä 1 - 30: ")
            while True:
                try:
                    user_numb_input = int(input())
                    if 1 <= user_numb_input <= 30:
                        if user_numb_input not in self.numbers and user_numb_input not in self.additionalNumbers:
                            self.additionalNumbers.append(user_numb_input)
                            break
                        else:
                            print("Tämä numero on jo annettu! Anna toinen numero.")
                    else:
                        print("Annoit väärän numeron!")
                except ValueError:
                    print("Syötteen täytyy olla kokonaisluku!")
            
            self.numbers.sort()
            print(f'Annoit numerot {self.numbers} ja lisänumerot {self.additionalNumbers}\n')

        # Vikinglotto
        elif self.gameMode == '2':
            if len(self.numbers) > 1 and len(self.additionalNumbers) >= 1:
                self.numbers.clear()
                self.additionalNumbers.clear()

            print("Anna numero väliltä 1 - 49 ")
            while len(self.numbers) < 6:
                try:
                    user_numb_input = int(input())
                    if 1 <= user_numb_input <= 48:
                        if user_numb_input not in self.numbers:
                            self.numbers.append(user_numb_input)
                        else:
                            print("Tämä numero on jo annettu! Anna toinen numero.")
                    else:
                        print("Annoit väärän numeron!")
                except ValueError:
                    print("Syötteen täytyy olla kokonaisluku!")
            
            print("Anna lisänumero väliltä 1 - 49: ")
            while True:
                try:
                    user_numb_input = int(input())
                    if 1 <= user_numb_input <= 48:
                        if user_numb_input not in self.numbers and user_numb_input not in self.additionalNumbers:
                            self.additionalNumbers.append(user_numb_input)
                            break
                        else:
                            print("Tämä numero on jo annettu! Anna toinen numero.")
                    else:
                        print("Annoit väärän numeron!")
                except ValueError:
                    print("Syötteen täytyy olla kokonaisluku!")
            
            self.numbers.sort()
            print(f'Annoit numerot {self.numbers} ja lisänumerot {self.additionalNumbers}\n')

        # Eurojackpot
        elif self.gameMode == '3':
            if len(self.numbers) > 1 and len(self.additionalNumbers) >= 1:
                self.numbers.clear()
                self.additionalNumbers.clear()

            print("Anna numero väliltä 1 - 50 ")
            while len(self.numbers) < 5:
                try:
                    user_numb_input = int(input())
                    if 1 <= user_numb_input <= 50:
                        if user_numb_input not in self.numbers:
                            self.numbers.append(user_numb_input)
                        else:
                            print("Tämä numero on jo annettu! Anna toinen numero.")
                    else:
                        print("Annoit väärän numeron!")
                except ValueError:
                    print("Syötteen täytyy olla kokonaisluku!")
            
            print("Anna 2 lisänumeroa väliltä 1 - 50: ")
            while len(self.additionalNumbers) < 2:
                try:
                    user_numb_input = int(input())
                    if 1 <= user_numb_input <= 50:
                        if user_numb_input not in self.numbers and user_numb_input not in self.additionalNumbers:
                            self.additionalNumbers.append(user_numb_input)
                        else:
                            print("Tämä numero on jo annettu! Anna toinen numero.")
                    else:
                        print("Annoit väärän numeron!")
                except ValueError:
                    print("Syötteen täytyy olla kokonaisluku!")
            
            self.numbers.sort()
            self.additionalNumbers.sort()
            print(f'Annoit numerot {self.numbers} ja lisänumerot {self.additionalNumbers}\n')

        return    

    def simulateWinningNumbers(self, iterations):
        correct_numbers = 0
        correct_additional_numbers = 0
        if not self.numbers and self.additionalNumbers:
            print("Anna ensin numerot")
            return
        print(f'Simuloidaan {iterations} rivin voittonumerot.....\n')
        
        
        for _ in range(iterations):
            # Lotto
            if self.gameMode == None or self.gameMode == '1':
                gen_random_numb = random.sample(range(1,31),7)
                gen_rand_addi_numb = random.sample(range(1,31),1)
            # Vikinglotto
            elif self.gameMode == '2':
                gen_random_numb = random.sample(range(1,49),6)
                gen_rand_addi_numb = random.sample(range(1,49),1)
            # Eurojackpot
            elif self.gameMode == '3':
                gen_random_numb = random.sample(range(1,50),5)
                gen_rand_addi_numb = random.sample(range(1,50),2)
        
        
        for num in gen_random_numb:
            if num in self.numbers:
                correct_numbers += 1
        
        for addi_num in gen_rand_addi_numb:
            if addi_num in self.additionalNumbers:
                correct_additional_numbers += 1
        
        print(f"Simulaation aikana {iterations} rivistä löytyi:")
        print(f"- Oikein osuneita päänumeroita: {correct_numbers}")
        print(f"- Oikein osuneita lisänumeroita: {correct_additional_numbers}\n")
        
        return 
    def bruteforceWin(self):
        
        attempts = 0  # Laskee yritykset

        print("Etsitään niin kauan kunnes saat kaikki oikein, tässä voi mennä hetki...\n")

        while True:
            attempts += 1

            # Lotto
            if self.gameMode == None or self.gameMode == '1':  # Lotto
                gen_random_numb = random.sample(range(1, 31), 7)
                gen_rand_addi_numb = random.sample(range(1, 31), 1)

            elif self.gameMode == '2':  # Vikinglotto
                gen_random_numb = random.sample(range(1, 49), 6)
                gen_rand_addi_numb = random.sample(range(1, 49), 1)

            elif self.gameMode == '3':  # Eurojackpot
                gen_random_numb = random.sample(range(1, 51), 5)
                gen_rand_addi_numb = random.sample(range(1, 13), 2)

            else:
                print("Pelitilaa ei ole valittu.")
                return

            
            main_match = set(gen_random_numb) == set(self.numbers)
            additional_match = set(gen_rand_addi_numb) == set(self.additionalNumbers)

           
            if main_match and additional_match:
                print(f"Kaikki numerot osuivat oikein! Voiton saaminen kesti {attempts} yritystä.")
                print(f"Voittorivi: {gen_random_numb} ja lisänumerot: {gen_rand_addi_numb}\n")
                break
        return
def menu():
    
    print("1) Generoi sekalaiset numerot")
    print("2) Käytä omia numeroita")
    print("3) Simuloi voittoja")
    print("4) Brute force voitto!!")
    print("5) Valitse peli")
    print("0) lopeta")
    user_input = input("Valintasi: ")
    print()
    return user_input.lower()



def main():
    game = LotteryGame()
    
    user_input = None
    iterations = 0
    while(user_input != 0):
        user_input = menu()
        if user_input == "1":
            game.generate_Numbers()
        elif user_input == "2":
            game.selectOwnNumbers()
        elif user_input == "3":
            iterations = int(input("Monta riviä arvotaan? "))
            game.simulateWinningNumbers(iterations)
        elif user_input == "4":
            game.bruteforceWin()
        elif user_input == "5":
            game.gameModes()
        elif user_input == "0":
            break
        else:
            print("Annoit virheellisen syötteen. ")
if __name__ == "__main__":
    print("*** Lotto generaattori ***")
    print("Tällä ohjelmalla voit simuloida lottonumeroita ja kokeilla onneasi.")
    print("Ohjelma valitsee oletuksena peliksi suomessa pelattavaa *LOTTO*")
    print("Voi myös valita myös Vikinglotto tai Eurojackpot pelin")
    print()
    main()