We used the Strategy pattern for the drawing of the snakes.
This way, we can easily modify the way snakes are drawn during runtime.

For example, if a snake has eaten a special fruit, we can just change snake.ColorGenerator = BlinkingColorGenerator() so that the snake is now blinking.

We implemented the Strategy pattern using an abstract class ColorGenerator which has an abstract method getNextColor(). We have two definite implementations, SingleColorGenerator and BlinkingColorGenerator. Using a different getNextColor(), the different drawing behaviour can be achieved. 