# Task-1 Tic Tac Toe AI

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



# Task-2 YOLOv5 Object Detection System

## Overview

This project implements an object detection system using the YOLOv5 model. It leverages the power of deep learning to identify and localize objects in real-time video streams. The application is built with Streamlit for an interactive web interface and OpenCV for video processing.

## Features

- **Real-Time Object Detection:** Detect and visualize objects from your webcam feed.
- **User-Friendly Interface:** Control the video stream using a simple sidebar in the Streamlit application.
- **Lightweight and Efficient:** Utilizes the YOLOv5s model for fast and accurate detection.

## Technologies Used

- **Python:** Main programming language for development.
- **PyTorch:** For loading and running the YOLOv5 model.
- **OpenCV:** For video capturing and processing.
- **Streamlit:** To create the web interface.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required packages:
   ```bash
   pip install torch torchvision torchaudio
   pip install opencv-python streamlit
   ```

### Running the Application

1. Run the Streamlit application:
   ```bash
   streamlit run your_script_name.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application.

3. Use the control panel to start or stop the video stream and view real-time object detection results.
