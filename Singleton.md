# Singleton Pattern
The GameBoard class was modified to implement the Singleton pattern.
Due to Python not having private methods we implemented it the following way:

The singleton pattern ensures that of a class only one instance is created.
There should be only one game board at a time, so it's a good idea to apply this pattern there.

* Encapsulate the `GameBoard` class in a private inner class `__GameBoard`
* Move every function from the previous class to this private inner class
* In the normal `GameBoard` class create a new constructor that calls the constructor of the inner class if the instance has not yet been assigned
* If a new Game is started, previously a new GameBoard has been created. We changed this to a `NewGame()` method of the private `__BoardGame` method which changes the current instance to reflect the state of a new game
* We redirect all calls to the `GameBoard` class to the instance of the private inner class using `__getattr__`


In the current state we did not implement a synchronized behavior. We do not know if this is necessary in Python (as we're new to the language).
We will try to add networking functionality to our game today in the evening - maybe then we have to add this. 