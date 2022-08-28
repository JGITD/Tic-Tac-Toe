from tkinter import *

class TicTacToe:
    board = [None]*9
    win = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    step = 0

    def new_window(self):
        self.window = Tk()
        self.window['bg'] = '#191240'
        self.window.title('Tic Tac Toe')
        self.window.geometry('620x620+490+140')
        self.window.resizable(width = False, height = False)
        return self.window

    def show_board(self, click):
        self.buttons = [Button(bd = 0, bg = '#FFFFFF', font = ('Arial', 130), command = lambda id = i: click(id)) for i in range(0, 9)]
        x, y = 0, 0
        for i in range(9):
            self.buttons[i].place(x = x, y = y, width = 200, height = 200)
            x += 210
            if x == 630: x, y = 0, y + 210

    def check(self):
        quantity_X , quantity_O = 0, 0
        for i in range(8):
            for j in range(3):
                if self.board[self.win[i][j]] == 'X': quantity_X += 1
                elif self.board[self.win[i][j]] == 'O': quantity_O += 1
            if quantity_X == 3 or quantity_O == 3:
                for j in range(3): self.buttons[self.win[i][j]].config(fg = '#047500')
                self.board.clear()
                break
            else: quantity_X, quantity_O = 0, 0 

    def logic(self):
        win_X, win_O = {}, {}
        for i in range(8):
            quantity_X , quantity_O, id = 0, 0, -1
            for j in range(3):
                if self.board[self.win[i][j]] == 'X': quantity_X += 1
                elif self.board[self.win[i][j]] == 'O': quantity_O += 1
                else: id = self.win[i][j]
            if quantity_O == 2 and id > -1: 
                try: win_O[id] += 1
                except: win_O[id] = 1
            elif quantity_X == 2 and id > -1: 
                try: win_X[id] += 1
                except: win_X[id] = 1
        max = 0
        for o in win_O:
            if win_O[o] > max:
                max = win_O[o]
                ido = o
        max = 0
        for x in win_X:
            if win_X[x] > max:
                max = win_X[x]
                idx = x
        try: 
            return ido
        except: 
            try: 
                return idx
            except:
                return id

    def one_player(self):
        def click(id):
            if len(self.board) > 0 and self.board[id] == None:
                self.board[id] = 'X'
                self.buttons[id].config(text = 'X', fg = '#8A0000')
                self.check()
                if None in self.board:
                    id = self.logic()
                    self.board[id] = 'O'
                    self.buttons[id].config(text = 'O', fg = '#040075')
                    self.check()
        
        self.window_1.destroy()
        self.window_2 = self.new_window()
        self.show_board(click)

    def two_players(self):
        def click(id):
            if len(self.board) > 0 and self.board[id] == None:
                if self.step % 2 == 0:
                    self.board[id] = 'X'
                    self.buttons[id].config(text = 'X', fg = '#8A0000')
                    self.step += 1
                    self.check()
                else:
                    self.board[id] = 'O'
                    self.buttons[id].config(text = 'O', fg = '#040075')
                    self.step += 1
                    self.check()
                
        self.window_1.destroy()
        self.window_3 = self.new_window()
        self.show_board(click)

    def start(self):
        self.window_1 = self.new_window()

        frames = [Frame(self.window_1, bg = '#FFFFFF') for i in range(2)]

        label_1 = Label(self.window_1, text = 'Tic Tac Toe', font = ('Arial', 50), fg = '#FFFFFF', bg = '#191240')

        button_1 = Button(bd = 0, fg = '#FFFFFF', bg = '#191240', font = ('Arial', 20, 'bold'), text = '1 player', command  = self.one_player)
        button_2 = Button(bd = 0, fg = '#FFFFFF', bg = '#191240', font = ('Arial', 20, 'bold'), text = '2 players', command = self.two_players)

        frames[0].place(x = 184, y = 249, width = 252, height = 52)
        frames[1].place(x = 184, y = 319, width = 252, height = 52)

        label_1.place(x = 130, y = 95, width = 360, height = 60)

        button_1.place(x = 185, y = 250, width = 250, height = 50)
        button_2.place(x = 185, y = 320, width = 250, height = 50)

        self.window_1.mainloop()

Tic_Tac_Toe = TicTacToe()
Tic_Tac_Toe.start()