# Snake
A Snake implementation in Python for the TU Delft ATHENS course "Software Design Patterns" held by [@sback](https://github.com/sback).

The goal was to start first program a simple game in some OO language and gradually improve the codebase, using OO design patterns.
Brief summary of the patterns used and how they contributed to code that is easier to understand: [Google Docs](https://docs.google.com/presentation/d/1p_ECGe20TdSAOnC4rWm2I0OjiMBNA0nRQEcUfm8tG3I/edit?usp=sharing)

## Features
* Periodic boundaries
* Local multiplayer with up to 4 players (Arrow keys, `WSAD`, `IKJL`, `TGFH`)
* Fancy colors
* Coming soon(ish): Networked multiplayer

## Is it any good?
Yes.

![](https://raw.githubusercontent.com/oerpli/Snake/master/screencap.gif)

## Getting started
* Install Python 3.x, e.g. via [Anaconda](https://www.anaconda.com/download/#download)
* If for some reason your Python distribution of choice does not come with TkInter included, use `pip install TkInter` to install it. 
* Install `matplotlib` with `pip install matplotlib`
* Go to the `./src/` directory and run `./python SnakeGameView.py`(on macOS you might have to use `pip3` and `python3` instead of `python`as it comes with the deprecated Python 2.x 
* A window should open. Focus it and play with the arrow keys.
* To play multiplayer snake press `1` to `4` and control the additional snakes with: `WSAD`, `IKJL`, `TGFH`


## Built with
* Python 3
* TkInter


## Contributors
* Thomas Jirout [@Schiru](https://github.com/schiru)
* Abraham Hinteregger [@oerpli](https://github.com/oerpli)
