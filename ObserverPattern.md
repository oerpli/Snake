# Observer Pattern

We use the Observer Pattern for handling keyboard events in our Snake game.

In the `SnakeGameView` class, we subscribe to receive keyboard events of the window by calling `self.window.bind_all("<Key>", self.keyPressed)`. The window is only responsible of keeping track of which services have subscribed to receive keyboard events/updates and call the respecive methods when the time has come. This way, every time a key event happens, our `self.keyPressed` method is being automatically called without the need for us to regularly poll for updates.