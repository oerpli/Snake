# Commander pattern (somewhat)

We implemented a `Commander`class that handles all key classes of the whole game. 
It is used in the base class of the game states (`State.py`) as each state of the game has to react to keyboard input.

The concrete implementation is as follows:

* The super class constructor of the states initialize the commander for the state
* In the constructor of the state the keys are registered to the commander of the base class
* If a key is pressed during the game, the keyhandler of the current state is called which delegates calling the right function to its commander.
* As Python supports function pointers we do not use an Invoker or similar. The correct function (and its optional arguments) is retrieved by the commander and are called directly.
* As our game would not need any undo functionality we chose to not implement the full blown pattern.

