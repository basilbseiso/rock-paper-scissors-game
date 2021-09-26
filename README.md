# Rock, Paper, Scissors Game

A Python application for playing Rock, Paper, Scissors against the computer.

> NOTE: The content and instructions in this README file were referenced and adapted from Professor Rossetti's "'Rock, Paper, Scissors' Exercise" repository as well as the sample README file provided in the repository. 

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Repo Setup and Installation

Fork this [remote repository](https://github.com/basilbseiso/rock-paper-scissors-game) under your own control, and "clone" or download your remote copy onto your local computer.

Next, navigate there from the command line (assuming that you are running the following commands from the local repository's root directory):

```sh
cd rock-paper-scissors-game
```

## Environment Setup
> NOTE: Since we're going to be working with environment variables and requiring a third-party package to read them from the ".env" file, we need to use a new project-specific Python environment within which to install required packages. 

Create and activate a new project-specific Anaconda virtual environment, perhaps called "my-game-env":

```sh
conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: Make sure you are running this command from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Customization

In the root directory of your local repository, create a new file called ".env", and update the contents of the file to specify your player name (make sure to SAVE the ".env" file once you are finished):

```sh
PLAYER_NAME="Player One"
```

## Usage

Run the Python script:

```sh
python game.py
```