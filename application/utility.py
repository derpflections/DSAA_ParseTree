import os

class utilities():
    def cls():
        os.system('cls' if os.name=='nt' else 'clear')
