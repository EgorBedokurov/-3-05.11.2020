#спизжено, переделано под словарь, пришлось поизучать "словарь"
chess_board={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
print('Сможете ли вы определить ход коня на шахматной доске?')
hor1 = int(input('где стоит конь - номер ряда по горизонтали (цифра) '))
vert1 = str(input('где стоит коньвведите номер по вертикали (буква) '))
hor2 = int(input('куда Вы хотите передвинут его по горизонтали (цифра) '))
vert2 = str(input('куда Вы хотите передвинут его по вертикали (буква) '))
vert3=chess_board.get(vert1)
vert4=chess_board.get(vert2)
dif_hor = abs(hor1 - hor2)
dif_vert = abs(vert3 - vert4)
if dif_hor == 1 and dif_vert == 2 or dif_hor == 2 and dif_vert == 1:
    print('да, такой ход возможен, \nу вас хорошее пространственное мышление ')
else:
    print('нет, такой ход не возможен, \nпоработайте над своим пространственным мышлением')

