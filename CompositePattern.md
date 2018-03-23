# Composite

We implemented the composite pattern to handle all the drawing calls.
Previously we called the `Draw()` function on every object that should be drawn.

We made a class `DrawableComponent` which implements `Drawable`, i.e. its `operation()` handles the drawing (we think similar to Dependency Injection).

We then made two classes, `DrawableLeaf` and `DrawableComposite` which inherit from `DrawableComponent`.  
The composite has a collection that stores its children and an iterator which can be overridden if desired. 
The leaf only implements the operation, in this case a call to the objects `self.Draw()` function. 

If `Operation` is called on the composite class it first draws itself and then applies `Operation()`on all its children.

This way we could reduce the many calls of `Draw` on all the game objects to a single draw-call on the gameboard.

Theoretically a snake could also be a composite to render the head differently or similar. 
Due to time constraints we did not finish this though. 