from menu.menu import *

if __name__ == '__main__':
    nba_menu = Menu()
    # Load data in advance
    nba_menu.load_data()
    nba_menu.run()
