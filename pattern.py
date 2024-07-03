import turtle
import random

class BarnsleyFernDrawer:
    def __init__(self, iterations=50000, scale=50, speed=0):
        """
        Initialize the BarnsleyFernDrawer with initial parameters.
        
        iterations: The number of points to plot.
        scale: The scale factor for the drawing.
        speed: The drawing speed of the turtle.
        """
        self.iterations = iterations
        self.scale = scale
        self.speed = speed
        self.t = turtle.Turtle()
        self.t.speed(speed)
        self.t.penup()
        self.t.hideturtle()
        self.x, self.y = 0, 0  # Starting point

    def transform(self, x, y):
        """
        Apply one of the four transformation rules to the point (x, y).
        
        x: The x-coordinate of the point.
        y: The y-coordinate of the point.
        """
        r = random.random()
        if r < 0.01:
            return 0, 0.16 * y
        elif r < 0.86:
            return 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6
        elif r < 0.93:
            return 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6
        else:
            return -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

    def draw_point(self, x, y):
        """
        Draw a point at the transformed coordinates (x, y).
        
        x: The x-coordinate of the point.
        y: The y-coordinate of the point.
        """
        self.t.goto(x * self.scale, y * self.scale - 300)  # Scale and position the point
        self.t.dot(2, "green")  # Draw a green dot

    def draw_fern(self):
        """Iteratively draw the Barnsley fern."""
        for _ in range(self.iterations):
            self.x, self.y = self.transform(self.x, self.y)
            self.draw_point(self.x, self.y)

    def start_drawing(self):
        """Start the drawing process."""
        turtle.bgcolor("black")
        self.t.color("green")
        self.draw_fern()
        turtle.done()
    
    def set_colors(self, background_color="black", fern_color="green"):
        """
        Set the colors for the background and the fern.
        
        background_color: The color of the background.
        fern_color: The color of the fern.
        """
        turtle.bgcolor(background_color)
        self.t.color(fern_color)

    def start_drawing_with_colors(self, background_color="black", fern_color="green"):
        """Start the drawing process with custom colors."""
        self.set_colors(background_color, fern_color)
        self.draw_fern()
        turtle.done()

# Create an instance of BarnsleyFernDrawer with parameters to extend drawing time and start drawing
fern = BarnsleyFernDrawer(iterations=50000, scale=60, speed=0)
fern.start_drawing_with_colors(background_color="black", fern_color="lime")
