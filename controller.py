from PyQt5.QtWidgets import *
from view import Ui_RockPaperScissors
import random
import sys

player_score = 0
computer_score = 0

class controller(QMainWindow, Ui_RockPaperScissors):
   """
   This class is responsible for handling the GUI of the Rock Paper
   Scissors game.
   """

   def __init__(self, *args, **kwargs):
       """
       Constructor for the Controller class. Sets up the GUI
       and connects the buttons to their corresponding methods.
       """
       super().__init__(*args, **kwargs)
       self.setupUi(self)

       self.Text_Output.setText('LETS PLAY = Rock - Paper - Scissor')

       self.Rock_Button.clicked.connect(lambda: self.rockchoice())

       self.Paper_Button.clicked.connect(lambda: self.paperchoice())

       self.Scissors_Button.clicked.connect(lambda: self.scissorschoice())

       self.compscore.setText(str(computer_score))
       self.myscore.setText(str(player_score))

       self.quitbutton.clicked.connect(lambda: sys.exit())

   def rockchoice(self):
       """
       This method is called when the Rock button is clicked. It
       generates a random choice for the computer and compares it
       to the player's choice. The appropriate score is incremented
       and the result is displayed to the user.
       """
       response = "rock"
       choices = ["rock", "paper", "scissor"]
       computer_guess = random.choice(choices)
       self.Text_Output.setText("Computer is " + computer_guess +
             ". You are " + response + ". ")
       if response == "rock":
           if computer_guess == "scissor":
               global player_score
               player_score += 1
               self.myscore.setText(str(player_score))
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You win.")
           elif computer_guess == "rock":
               self.Text_Output.setText("Computer is " + computer_guess +
             ". You are " + response + ". " + "You tie.")
           else:
               global computer_score
               computer_score += 1
               self.compscore.setText(str(computer_score))
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You lose.")

   def paperchoice(self):
       """
       This method is called when the Paper button is clicked. It
       generates a random choice for the computer and compares it
       to the player's choice. The appropriate score is incremented
       and the result is displayed to the user.
       """
       response = "paper"
       choices = ["rock", "paper", "scissor"]
       computer_guess = random.choice(choices)
       self.Text_Output.setText("Computer is " + computer_guess +
             ". You are " + response + ". ")
       if response == "paper":
           if computer_guess == "scissor":
               global computer_score
               computer_score += 1
               self.compscore.setText(str(computer_score))
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You lose.")
           elif computer_guess == "paper":
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You tie.")
           else:
               global player_score
               player_score += 1
               self.myscore.setText(str(player_score))
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You win.")

   def scissorschoice(self):
       """
       This method is called when the Scissors button is clicked. It
       generates a random choice for the computer and compares it
       to the player's choice. The appropriate score is incremented
       and the result is displayed to the user.
       """
       response = "scissor"
       choices = ["rock", "paper", "scissor"]
       computer_guess = random.choice(choices)
       self.Text_Output.setText("Computer is " + computer_guess +
             ". You are " + response + ". ")
       if response == "scissor":
           if computer_guess == "paper":
               global player_score
               player_score += 1
               self.myscore.setText(str(player_score))
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You win.")
           elif computer_guess == "scissor":
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You tie.")
           else:
               global computer_score
               computer_score += 1
               self.compscore.setText(str(computer_score))
               self.Text_Output.setText("Computer is " + computer_guess +
                                        ". You are " + response + ". " + "You lose.")