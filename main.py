Note = '\033[7:30m  JOGO DA VELHA  \033[m\n\033[7:30m    A   B   C    \033[m\n\033[7:30m 1  A1  B1  C1   \033[m\n\033[7:30m 2  A2  B2  C2   \033[m\n\033[7:30m 3  A3  B3  C3   \033[m'
print(Note)
print(' ')
#JOGADOR 1 ESCOLHE========================================================================================================
J1_1 = (input('Player 1 escolha uma posição: ')).upper()
print(' ')
Note = Note.replace(J1_1, '\033[31mX \033[7:30m')
print(Note)
print(' ')
#JOGADOR 2 ESCOLHE-----------------------------------------------------------------------------------------------------
J2_1 = (input('Player 2 escolha uma posição: ')).upper()
print(' ')
Note = Note.replace(J2_1, '\033[34mO \033[7:30m')
print(Note)
print(' ')
