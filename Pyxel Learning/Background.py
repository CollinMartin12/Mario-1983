import pyxel

# Initialize Pyxel
pyxel.init(120, 160)

# Load images into image banks
pyxel.image(1).load(20, 40, r"C:\Users\USER\Desktop\Pyxel Learning\assets\Enemies\Classic enemies 1.png")

# Define your update and draw functions
def update():
    pass  # Implement your update logic here

def draw():
    # Clear the screen
    pyxel.cls(0)

    # Draw the image loaded into bank 1 at position (x=20, y=40)
    pyxel.blt(20, 40, 1, 0, 0, 16, 16)  # Adjust the size (16, 16) if needed

# Run the Pyxel application
pyxel.run(update, draw)


