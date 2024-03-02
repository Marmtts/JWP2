ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.


def main():
    """Rozgrywka w kółko i krzyżyk."""
    print('Witaj w grze kółko i krzyżyk!')
    gameBoard = getBlankBoard()  # Utwórz słownik planszy KIK.
    currentPlayer, nextPlayer = X, O  # X wykonuje ruch jako pierwszy, O jako następny.
    while True:
        print(getBoardStr(gameBoard))  # Wyświetl planszę na ekranie.

        # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
        move = None
        while not isValidSpace(gameBoard, move):
            print(f'Jaki jest ruch gracza {currentPlayer}? (1-9)')
            move = input()
        updateBoard(gameBoard, move, currentPlayer)  # Wykonanie ruchu.
        # Sprawdzenie, czy gra jest zakończona:
        if isWinner(gameBoard, currentPlayer):  # Sprawdzenie, kto wygrał.
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' wygrał grę!')
            break
        elif isBoardFull(gameBoard):  # Sprawdzenie remisu.
            print(getBoardStr(gameBoard))
            print('Gra zakończyła się remisem!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Zmiana gracza.
    print('Dziękuję za grę!')


def getBlankBoard():
    """Tworzy nową, pustą planszę gry w kółko i krzyżyk."""
    board = {}  # Plansza jest reprezentowana przez słownik Pythona.
    for space in ALL_SPACES:
        board[space] = BLANK  # Wszystkie pola na początku są puste.
    return board


def getBoardStr(board):
    """Zwraca tekstową reprezentację planszy."""
    return f'''
            {board['1']}|{board['2']}|{board['3']} 1 2 3 
            -+-+- 
            {board['4']}|{board['5']}|{board['6']} 4 5 6 
            -+-+- 
            {board['7']}|{board['8']}|{board['9']} 7 8 9'''
def isValidSpace(board, space):
    """Zwraca True, jeśli pole na planszy ma prawidłowy numer i pole jest puste."""
    if space is None:
        return False
    return space in ALL_SPACES or board[space] == BLANK
def isWinner(board, player):
    """Zwraca True, jeśli gracz jest zwycięzcą tej planszy KIK."""
    b, p = board, player # Krótsze nazwy jako "składniowy cukier".
    # Sprawdzenie, czy trzy takie same znaki występują w wierszach, kolumnach i po przekątnych.
    return ((b['1'] == b['2'] == b['3'] == p) or # poziomo na górze
            (b['4'] == b['5'] == b['6'] == p) or # poziomo w środku
            (b['7'] == b['8'] == b['9'] == p) or # poziomo u dołu
            (b['1'] == b['4'] == b['7'] == p) or # pionowo z lewej
            (b['2'] == b['5'] == b['8'] == p) or # pionowo w środku
            (b['3'] == b['6'] == b['9'] == p) or # pionowo z prawej
            (b['3'] == b['5'] == b['7'] == p) or # przekątna 1
            (b['1'] == b['5'] == b['9'] == p)) # przekątna 2

def isBoardFull(board):
    """Zwraca True, jeśli wszystkie pola na planszy są zajęte."""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False # Jeśli nawet jedno pole jest puste, zwracaj False.
    return True # Nie ma wolnych pól, zatem zwróć True.
def updateBoard(board, space, mark):
    """Ustawia pole na planszy na podany znak."""
    board[space] = mark

if __name__ == '__main__':
    main() # Wywołaj main(), jeśli ten moduł został uruchomiony, a nie zaimportowany.