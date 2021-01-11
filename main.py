import random
import time
from turtle import *
from random import randrange
from freegames import square, vector
from tkinter import *
import numpy as np
print("Hello!, \nI hope you are fine, \nso what would you like to do today.\njust enter the number and i will open that program accordingly")
choice = input("1-Mad Libs \n2-Calculator \n3-guessing game \n4-snake \n5-dots (2players) \n")
if choice == "1":
   print("Ah! so you wanna play mad libs today sure enter some adjectives, some nouns and let's see what do we get")
   adjective1 = input("Enter a adjective: ")
   adjective2 = input("Enter another adjective: ")
   adjective3 = input("Enter another adjective: ")
   adjective4 = input("Enter another adjective: ")
   adjective5 = input("Enter another adjective: ")
   adjective6 = input("Enter another adjective: ")
   nationality = input("Enter a nationality: ")
   person = input("Enter a name: ")
   noun = input("enter a noun: ")
   noun2 = input("enter another noun: ")
   pluralnoun = input("Enter a plural noun: ")
   noun3 = input("enter another noun: ")
   number = input("Enter a number: ")
   shape = input("Enter a shape: ")
   food = input("Enter a food: ")
   food2 = input("Enter another food: ")
   number3 = input("Enter another Number: ")
   print("pizza was invented by a " + adjective1 + " " + nationality + " chef named " + person + ".")
   print("To make a pizza, you need to take a lump of " + noun + " , and make a " + adjective2 + " , " + adjective3 + " " + adjective4 + " " + noun2 + " .")
   print("Then you cover it with " + adjective5 + " sauce, " + adjective6 + " cheese, and fresh chopped " + pluralnoun + " .")
   print("Next you have to bake it in a very hot " + noun3 + ".")
   print("When it is done, cut it into " + number + " " + shape + ".")
   print("Some kids like " + food + " pizza the best, but my favourite is the " + food2 + " pizza")
   print("WOW! that's nice ok it was fun")
   print("Goodbye!")
elif choice == "2" :
     print("oh so you wanna do some calculation \nAlright \nalso there is some bug that after you get some result you may get invalid error \nsorry!")
     num1 = float(input("Enter first number: "))
     op = input("Enter operator: ")
     num2 = float(input("Enter second number"))

     if op == "+":
        print(num1 + num2)
     if op == "-":
         print(num1 - num2)
     if op == "/":
        print(num1 / num2)
     if op == "*":
         print(num1 * num2)
     if op != "+" and "-" and "/" and "*":
         print("Invalid operator ")
elif choice == "3":
    print("ok, so you wanna play some guessing games \nno problem")
    print("also let me tell you the instructions \nyou will be given 10 chance to guess the word also you can get a hint at the start but not afterwards")
    print("Alright!")
    WORDS = ("python", "guess", "easy", "difficult", "answer",  "xylophone")
    secret_word = random.choice(WORDS)
    guess = ""
    guess_count = 0
    guess_limit = 10
    out_of_guess = False
    hint1 = ""
    hint2 = ""
    hint3 = ""
    hint4 = ""
    hint5 = ""
    hint6 = ""
    if secret_word == "python":
        hint1 = input("do you need hint: ")
        if hint1 == "yes":
             print("hint is a programming language")
        else:
            print("ok")
    elif secret_word == "guess":
       hint2 = input("do you need hint: ")
       if hint2 == "yes":
           print("hint is to be guessed")
       else:
        print("ok")
    elif secret_word == "easy":
      hint3 = input("do you need hint: ")
      if hint3 == "yes":
        print("hint is not easy")
      else:
        print("ok")
    elif secret_word == "difficult":
      hint4 = input("do you need hint: ")
      if hint4 == "yes":
        print("hint is very difficult")
      else:
        print("ok")
    elif secret_word == "answer":
      hint5 = input("do you need hint: ")
      if hint5 == "yes":
        print("hint is related to question")
      else:
        print("ok")
    elif secret_word == "xylophone":
      hint6 = input("do you need hint: ")
      if hint6 == "yes":
        print("hint is a toy with which children play")
      else:
        print("ok")
    while guess != secret_word and not(out_of_guess):
        if guess_count < guess_limit:
            guess = input("Enter guess:")
            guess_count += 1
        else:
            out_of_guess = True
    if out_of_guess:
        print("well you ran out of chances. \nLet's see what word was it")
        print(secret_word)
    else:
       print("well you got it")
       print("NICE")
elif choice == "4":
    print("ok no problem we will play snakes you can play with arrow keys \nalso if you run into your self you will lose \nalso after you lose please click command+q to exit")
    print("and also the last count is your final score")
    time.sleep(13)
    """Snake, classic arcade game.

    Exercises

     1. How do you make the snake faster or slower?
     2. How can you make the snake go around the edges?
     3. How would you move the food?
     4. Change the snake to respond to arrow keys.

     """


    food = vector(0, 0)
    snake = [vector(10, 0)]
    aim = vector(0, -10)

    def change(x, y):
        "Change snake direction."
        aim.x = x
        aim.y = y

    def inside(head):
        "Return True if head inside boundaries."
        return -500 < head.x < 490 and -500 < head.y < 490

    def move():
        "Move snake forward one segment."
        head = snake[-1].copy()
        head.move(aim)

        if not inside(head) or head in snake:
           square(head.x, head.y, 9, 'red')
           update()
           return

        snake.append(head)

        if head == food:
           print('Snake:', len(snake))
           food.x = randrange(-15, 15) * 10
           food.y = randrange(-15, 15) * 10
        else:
           snake.pop(0)

        clear()

        for body in snake:
            square(body.x, body.y, 9, 'black')

        square(food.x, food.y, 9, 'green')
        update()
        ontimer(move, 100)


    setup(900, 900, 800, 0)
    hideturtle()
    tracer(False)
    time.sleep(5)
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move()
    done()
elif choice == "5":
    print("oh so you wanna play dots.\nI hope you have a friend with you.\nalso there is a error that if you are making a box \nand if the opponent made a line it would not make a box for anyone and would be discarded and would belong to no one")
    time.sleep(10)
    print("\n\nok so let's talk about instructions \nyou have too click the line between the dots to make a line and four lines = a box")
    time.sleep(8)
    size_of_board = 800
    number_of_dots = 10
    symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
    symbol_thickness = 50
    dot_color = '#7BC043'
    player1_color = '#0492CF'
    player1_color_light = '#67B0CF'
    player2_color = '#EE4035'
    player2_color_light = '#EE7E77'
    Green_color = '#7BC043'
    dot_width = 0.25*size_of_board/number_of_dots
    edge_width = 0.1*size_of_board/number_of_dots
    distance_between_dots = size_of_board / (number_of_dots)

    class Dots_and_Boxes():
        # ------------------------------------------------------------------
        # Initialization functions
        # ------------------------------------------------------------------
        def __init__(self):
            self.window = Tk()
            self.window.title('Dots_and_Boxes')
            self.canvas = Canvas(self.window, width=size_of_board, height=size_of_board)
            self.canvas.pack()
            self.window.bind('<Button-1>', self.click)
            self.player1_starts = True
            self.refresh_board()
            self.play_again()

        def play_again(self):
            self.refresh_board()
            self.board_status = np.zeros(shape=(number_of_dots - 1, number_of_dots - 1))
            self.row_status = np.zeros(shape=(number_of_dots, number_of_dots - 1))
            self.col_status = np.zeros(shape=(number_of_dots - 1, number_of_dots))

            # Input from user in form of clicks
            self.player1_starts = not self.player1_starts
            self.player1_turn = not self.player1_starts
            self.reset_board = False
            self.turntext_handle = []

            self.already_marked_boxes = []
            self.display_turn_text()

        def mainloop(self):
            self.window.mainloop()

        # ------------------------------------------------------------------
        # Logical Functions:
        # The modules required to carry out game logic
        # ------------------------------------------------------------------

        def is_grid_occupied(self, logical_position, type):
            r = logical_position[0]
            c = logical_position[1]
            occupied = True

            if type == 'row' and self.row_status[c][r] == 0:
                occupied = False
            if type == 'col' and self.col_status[c][r] == 0:
                occupied = False

            return occupied

        def convert_grid_to_logical_position(self, grid_position):
            grid_position = np.array(grid_position)
            position = (grid_position-distance_between_dots/4)//(distance_between_dots/2)

            type = False
            logical_position = []
            if position[1] % 2 == 0 and (position[0] - 1) % 2 == 0:
                r = int((position[0]-1)//2)
                c = int(position[1]//2)
                logical_position = [r, c]
                type = 'row'
                # self.row_status[c][r]=1
            elif position[0] % 2 == 0 and (position[1] - 1) % 2 == 0:
                c = int((position[1] - 1) // 2)
                r = int(position[0] // 2)
                logical_position = [r, c]
                type = 'col'

            return logical_position, type

        def mark_box(self):
            boxes = np.argwhere(self.board_status == -4)
            for box in boxes:
                if list(box) not in self.already_marked_boxes and list(box) !=[]:
                    self.already_marked_boxes.append(list(box))
                    color = player1_color_light
                    self.shade_box(box, color)

            boxes = np.argwhere(self.board_status == 4)
            for box in boxes:
                if list(box) not in self.already_marked_boxes and list(box) !=[]:
                    self.already_marked_boxes.append(list(box))
                    color = player2_color_light
                    self.shade_box(box, color)

        def update_board(self, type, logical_position):
            r = logical_position[0]
            c = logical_position[1]
            val = 1
            if self.player1_turn:
                val =- 1

            if c < (number_of_dots-1) and r < (number_of_dots-1):
                self.board_status[c][r] += val

            if type == 'row':
                self.row_status[c][r] = 1
                if c >= 1:
                    self.board_status[c-1][r] += val

            elif type == 'col':
                self.col_status[c][r] = 1
                if r >= 1:
                    self.board_status[c][r-1] += val

        def is_gameover(self):
            return (self.row_status == 1).all() and (self.col_status == 1).all()

        # ------------------------------------------------------------------
        # Drawing Functions:
        # The modules required to draw required game based object on canvas
        # ------------------------------------------------------------------

        def make_edge(self, type, logical_position):
            if type == 'row':
                start_x = distance_between_dots/2 + logical_position[0]*distance_between_dots
                end_x = start_x+distance_between_dots
                start_y = distance_between_dots/2 + logical_position[1]*distance_between_dots
                end_y = start_y
            elif type == 'col':
                start_y = distance_between_dots / 2 + logical_position[1] * distance_between_dots
                end_y = start_y + distance_between_dots
                start_x = distance_between_dots / 2 + logical_position[0] * distance_between_dots
                end_x = start_x

            if self.player1_turn:
                color = player1_color
            else:
                color = player2_color
            self.canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=edge_width)

        def display_gameover(self):
            player1_score = len(np.argwhere(self.board_status == -4))
            player2_score = len(np.argwhere(self.board_status == 4))

            if player1_score > player2_score:
                # Player 1 wins
                text = 'Winner: Player 1 '
                color = player1_color
            elif player2_score > player1_score:
                text = 'Winner: Player 2 '
                color = player2_color
            else:
                text = 'Its a tie'
                color = 'gray'

            self.canvas.delete("all")
            self.canvas.create_text(size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

            score_text = 'Scores \n'
            self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                text=score_text)

            score_text = 'Player 1 : ' + str(player1_score) + '\n'
            score_text += 'Player 2 : ' + str(player2_score) + '\n'
            # score_text += 'Tie                    : ' + str(self.tie_score)
            self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                text=score_text)
            self.reset_board = True

            score_text = 'Click to play again \n'
            self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                text=score_text)

        def refresh_board(self):
            for i in range(number_of_dots):
                x = i*distance_between_dots+distance_between_dots/2
                self.canvas.create_line(x, distance_between_dots/2, x,
                                        size_of_board-distance_between_dots/2,
                                        fill='gray', dash = (2, 2))
                self.canvas.create_line(distance_between_dots/2, x,
                                        size_of_board-distance_between_dots/2, x,
                                        fill='gray', dash=(2, 2))

            for i in range(number_of_dots):
                for j in range(number_of_dots):
                    start_x = i*distance_between_dots+distance_between_dots/2
                    end_x = j*distance_between_dots+distance_between_dots/2
                    self.canvas.create_oval(start_x-dot_width/2, end_x-dot_width/2, start_x+dot_width/2,
                                            end_x+dot_width/2, fill=dot_color,
                                            outline=dot_color)

        def display_turn_text(self):
            text = 'Next turn: '
            if self.player1_turn:
                text += 'Player1'
                color = player1_color
            else:
                text += 'Player2'
                color = player2_color

            self.canvas.delete(self.turntext_handle)
            self.turntext_handle = self.canvas.create_text(size_of_board - 5*len(text),
                                                           size_of_board-distance_between_dots/8,
                                                           font="cmr 15 bold", text=text, fill=color)


        def shade_box(self, box, color):
            start_x = distance_between_dots / 2 + box[1] * distance_between_dots + edge_width/2
            start_y = distance_between_dots / 2 + box[0] * distance_between_dots + edge_width/2
            end_x = start_x + distance_between_dots - edge_width
            end_y = start_y + distance_between_dots - edge_width
            self.canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=color, outline='')

        def display_turn_text(self):
            text = 'Next turn: '
            if self.player1_turn:
                text += 'Player1'
                color = player1_color
            else:
                text += 'Player2'
                color = player2_color

            self.canvas.delete(self.turntext_handle)
            self.turntext_handle = self.canvas.create_text(size_of_board - 5*len(text),
                                                           size_of_board-distance_between_dots/8,
                                                           font="cmr 15 bold",text=text, fill=color)

        def click(self, event):
            if not self.reset_board:
                grid_position = [event.x, event.y]
                logical_positon, valid_input = self.convert_grid_to_logical_position(grid_position)
                if valid_input and not self.is_grid_occupied(logical_positon, valid_input):
                    self.update_board(valid_input, logical_positon)
                    self.make_edge(valid_input, logical_positon)
                    self.mark_box()
                    self.refresh_board()
                    self.player1_turn = not self.player1_turn

                    if self.is_gameover():
                        # self.canvas.delete("all")
                        self.display_gameover()
                    else:
                        self.display_turn_text()
            else:
                self.canvas.delete("all")
                self.play_again()
                self.reset_board = False


    game_instance = Dots_and_Boxes()
    game_instance.mainloop()
else:
    print("this choice is not available \nYET!")
