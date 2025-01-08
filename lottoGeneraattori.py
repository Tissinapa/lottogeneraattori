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
        if self.gameMode == None or self.gameMode == '1':
            if len(self.numbers) > 1 and len(self.additionalNumbers) >= 1:
                self.numbers.clear()
                self.additionalNumbers.clear()
            
            print("Anna numero väliltä 1 - 30 ")
            while(len(self.numbers) <= 6):
                user_numb_input = input()
                #Lisää tarkistus
                self.numbers.append(user_numb_input)
            self.numbers.sort()
            print(f'Annoit numerot {self.numbers}')
        
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
    while(user_input != 0):
        user_input = menu()
        if user_input == "1":
            game.generate_Numbers()
        elif user_input == "2":
            game.selectOwnNumbers()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
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