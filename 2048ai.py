import tkinter as tk
import random

class Game2048(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.board = [[0, 0, 0, 0] for _ in range(4)]
        self.tiles = []
        for i in range(4):
            row = []
            for j in range(4):
                tile = tk.Label(self, text="", font=("Helvetica", 32))
                tile.grid(row=i, column=j)
                row.append(tile)
            self.tiles.append(row)

        self.score_label = tk.Label(self, text="Score: 0", font=("Helvetica", 16))
        self.score_label.grid(row=5, column=0, columnspan=4)
        self.score = 0
        self.new_game_button = tk.Button(self, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=6, column=0, columnspan=4)

    def new_game(self):
        self.board = [[0, 0, 0, 0] for _ in range(4)]
        self.score = 0
        self.update_score()
        self.spawn_tile()
        self.spawn_tile()
        self.update_board()

    def spawn_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] == 0]
        if not empty_cells:
            return False
        i, j = random.choice(empty_cells)
        self.board[i][j] = 2
        self.update_tile(i, j)
        return True

    def update_tile(self, i, j):
        self.tiles[i][j]["text"] = str(self.board[i][j])
        if self.board[i][j] == 0:
            self.tiles[i][j]["bg"] = "white"
        elif self.board[i][j] == 2:
            self.tiles[i][j]["bg"] = "lightyellow"
        elif self.board[i][j] == 4:
            self.tiles[i][j]["bg"] = "lightgreen"
        elif self.board[i][j] == 8:
            self.tiles[i][j]["bg"] = "lightblue"
        elif self.board[i][j] == 16:
            self.tiles[i][j]["bg"] = "purple"
        elif self.board[i][j] == 32:
            self.tiles[i][j]["bg"] = "pink"
        elif self.board[i][j] == 64:
            self.tiles[i][j]["bg"] = "orange"
        elif self.board[i][j] == 128:
            self.tiles[i][j]["bg"] = "red"
        elif self.board[i][j] == 256:
            self.tiles[i][j]["bg"] = "lightpink"
        elif self.board[i][j] == 512:
            self.tiles[i][j]["bg"] = "lightorange"
        elif self.board[i][j] == 1024:
            self.tiles[i][j]["bg"] = "lightpurple"
        elif self.board[i][j] == 2048:
            self.tiles[i][j]["bg"] = "darkgreen"
    
    def update_score(self):
        self.score_label["text"] = "Score: {}".format(self.score)

    def move_tiles(self, direction):
        moved = False
        if direction == "up":
            for j in range(4):
                for i in range(1, 4):
                    if self.board[i][j] == 0:
                        continue
                    for k in range(i-1, -1, -1):
                        if self.board[k][j] == 0:
                            self.board[k][j] = self.board[k+1][j]
                            self.board[k+1][j] = 0
                            moved = True
                        elif self.board[k][j] == self.board[k+1][j]:
                            self.board[k][j] *= 2
                            self.board[k+1][j] = 0
                            self.score += self.board[k][j]
                            moved = True
                        else:
                            break
            self.update_board()
        elif direction == "down":
            for j in range(4):
                for i in range(2, -1, -1):
                    if self.board[i][j] == 0:
                        continue
                    for k in range(i+1, 4):
                        if self.board[k][j] == 0:
                            self.board[k][j] = self.board[k-1][j]
                            self.board[k-1][j] = 0
                            moved = True
                        elif self.board[k][j] == self.board[k-1][j]:
                            self.board[k][j] *= 2
                            self.board[k-1][j] = 0
                            self.score += self.board[k][j]
                            moved = True
                        else:
                            break
            self.update_board()
        elif direction == "left":
            for i in range(4):
                for j in range(1, 4):
                    if self.board[i][j] == 0:
                        continue
                    for k in range(j-1, -1, -1):
                        if self.board[i][k] == 0:
                            self.board[i][k] = self.board[i][k+1]
                            self.board[i][k+1] = 0
                            moved = True
                        elif self.board[i][k] == self.board[i][k+1]:
                            self.board[i][k] *= 2
                            self.board[i][k+1] = 0
                            self.score += self.board[i][k]
                            moved = True
                        else:
                            break
            self.update_board()
        elif direction == "right":
            for i in range(4):
                for j in range(2, -1, -1):
                    if self.board[i][j] == 0:
                        continue
                    for k in range(j+1, 4):
                        if self.board[i][k] == 0:
                            self.board[i][k] = self.board[i][k-1]
                            self.board[i][k-1] = 0
                            moved = True
                        elif self.board[i][k] == self.board[i][k-1]:
                            self.board[i][k] *= 2
                            self.board[i][k-1] = 0
                            self.score += self.board[i][k]
                            moved = True
                        else:
                            break
                self.update_board()
            return moved

    def update_board(self):
        for i in range(4):
            for j in range(4):
                self.update_tile(i, j)
        self.update_score()

    def game_over(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return False
                if i > 0 and self.board[i][j] == self.board[i-1][j]:
                    return False
                if i < 3 and self.board[i][j] == self.board[i+1][j]:
                    return False
                if j > 0 and self.board[i][j] == self.board[i][j-1]:
                    return False
                if j < 3 and self.board[i][j] == self.board[i][j+1]:
                    return False
        return True

    def key_pressed(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.move_tiles(event.keysym.lower())
            if self.game_over():
                self.game_over_label = tk.Label(self, text="Game Over!", font=("Helvetica", 32))
                self.game_over_label.grid(row=5, column=0, columnspan=4)
            else:
                self.spawn_tile()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    root.title("2048")
    app = Game2048(master=root)
    root.bind("<Key>", app.key_pressed)
    app.mainloop()
