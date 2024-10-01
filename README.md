# Tic Tac Toe AI

## Overview

This project is a simple Tic Tac Toe game built using Python's Tkinter library. It allows a user to play against an AI opponent, which employs the Minimax algorithm to make optimal moves. The game features a graphical user interface (GUI) for an engaging experience.

## Features

- **Single Player Mode:** Play against an AI that uses strategic decision-making to provide a challenge.
- **User-Friendly GUI:** Built with Tkinter, the interface is intuitive and easy to use.
- **Game Logic:** 
  - Win conditions are checked for both players.
  - Draws are handled appropriately when no moves are left.
- **Reset Functionality:** Easily restart the game without needing to relaunch the application.

## How It Works

- The board is represented as a list of nine spaces, initialized as empty.
- The user plays as 'X', and the AI plays as 'O'.
- The AI uses the Minimax algorithm to determine the best move, optimizing its chances of winning or blocking the player.
- The game checks for winners after each move, displaying a message box when the game concludes.

## Technologies Used

- **Python:** The primary programming language used.
- **Tkinter:** The standard GUI toolkit for Python, used to create the graphical interface.
