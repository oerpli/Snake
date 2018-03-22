# State Pattern

We implemented this pattern by separating the SnakeGameView class into multiple states. Previously, the class would handle all possible game states and differentiate between them using a lot of `if` statements and some status indicator variables like `self.GAME_OVER = True/False`.

In our new implementation, we now have two seperate classes, namely `GameRunningState` and `GameOverState`, which both inherit from the base class `State` and the `SnakeGameView` is just responsible for keeping track of which state is active. 

The `State` class requires its subclasses to implement a `start()` and a `keyPressed(self, event)` method. Each time the `setState(state)` method of the `SnakeGameView` is being called, the view sets `self.currentState` and calls the `start()` method of the respective new state.  Additionally, any key events are being forwarded to the currently active state by invoking the `keyPressed` method.