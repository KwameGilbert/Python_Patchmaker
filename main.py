# Prompt user for input

def get_valid_size():
    while True:
        try:
            size = int(input("Enter patchwork size (5, 7, or 9): "))
            if size in [5, 7, 9]:
                return size
            else:
                print("Invalid size. Please enter 5, 7, or 9.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_valid_colors():
    colors = []
    while len(colors) < 3:
        color = input(f"Enter color {len(colors) + 1} (red, green, blue, magenta, orange, yellow, cyan): ").lower()
        if color in ['red', 'green', 'blue', 'magenta', 'orange', 'yellow', 'cyan'] and color not in colors:
            colors.append(color)
        else:
            print("Invalid color. Please enter a unique color from the given options.")
    return colors

# Example usage:
patchwork_size = get_valid_size()
patchwork_colors = get_valid_colors()

print("Patchwork size:", patchwork_size)
print("Patchwork patchwork_colors:", patchwork_colors)

# Example usage for student number input:
student_number = input("Enter your student number: ")

#Extract digits from student number:

def extract_digits(student_number):
    try:
        antepenultimate_digit = int(student_number[-3])
        penultimate_digit = int(student_number[-2])
        final_digit = int(student_number[-1])
        return antepenultimate_digit, penultimate_digit, final_digit
    except ValueError:
        print("Invalid student number format. Please make sure it contains only digits.")

antepenultimate, penultimate, final = extract_digits(student_number)

print("Antepenultimate digit: ", antepenultimate)
print("Penultimate digit: ", penultimate)
print("Final digit: ", final)

#Setup graphics window
from graphics import GraphWin, Point, Rectangle, Oval, Polygon, Line, Text

def setup_graphics_window(patchwork_size):
    # Calculate the window size based on the patchwork size
    window_size = patchwork_size * 100

    # Create a graphics window
    win = GraphWin("Patchwork", window_size, window_size)
    
    # Set a white background
    win.setBackground("white")

    return win

graphics_window = setup_graphics_window(patchwork_size)

# You can now use `graphics_window` for drawing patches and displaying the patchwork.
# Don't forget to close the window when you're done: `graphics_window.close()`

#Draw the patchwork

#import libraries


def draw_patch(graphics_window, x, y, color, design):
    # Function to draw a single patch at the specified position with a given colour and design
    patch_size = 100

    if design == 1:
        # Draw a rectangle
        patch = Rectangle(Point(x, y), Point(x + patch_size, y + patch_size))
    elif design == 2:
        # Draw an oval
        patch = Oval(Point(x, y), Point(x + patch_size, y + patch_size))
    else:
        # Draw a polygon (triangle)
        patch = Polygon(Point(x, y), Point(x + patch_size, y), Point(x + patch_size / 2, y + patch_size))
  
    patch.setFill(color)
    patch.draw(graphics_window)
    
    return patch

def draw_patchwork(graphics_window, patchwork_size, patchwork_colors, antepenultimate, penultimate, final):
    # Function to draw the entire patchwork based on the extracted digits
    patch_size = 100
    patches = []

    for row in range(patchwork_size):
        for col in range(patchwork_size):
            x = col * patch_size
            y = row * patch_size

            # Use the extracted digits to determine the colour and design
            color_index = (antepenultimate + row + col) % 3
            color = patchwork_colors[color_index]

            design_index = (penultimate + row + col) % 2 + 1

            patch = draw_patch(graphics_window, x, y, color, design_index)
            patches.append(patch)

    return patches



##Allow mouse and keyboard inputs and edits

def create_button(graphics_window, x, y, label):
    # Function to create a button at the specified position with a label
    button = Rectangle(Point(x, y), Point(x + 60, y + 30))
    button.setFill("black")
    button.draw(graphics_window)

    text = Text(Point(x + 30, y + 15), label)
    text.setTextColor("white")
    text.setSize(12)
    text.draw(graphics_window)

    return button

def handle_mouse_click(patches, buttons, click_point):
    # Function to handle mouse click events
    for patch in patches:
        if patch.getP1().getX() <= click_point.getX() <= patch.getP2().getX() and \
                patch.getP1().getY() <= click_point.getY() <= patch.getP2().getY():
            # Toggle the selection of the clicked patch
            if patch.getWidth() == 1
                patch.setWidth(1)  # Deselect
                patch.setOutline("white")
            else:
                patch.setWidth(3)  # Select
                patch.setOutline("black")

    for button in buttons:
        if button.getP1().getX() <= click_point.getX() <= button.getP2().getX() and \
                button.getP1().getY() <= click_point.getY() <= button.getP2().getY():
            return button.getText()  # Return the label of the clicked button

    return None

def main():
    while True:
        try:
            # Draw the patchwork
            patches = draw_patchwork(graphics_window, patchwork_size, patchwork_colors, antepenultimate, penultimate, final)

            # Create buttons for the selection mode
            ok_button = create_button(graphics_window, 10, 10, "OK")
            close_button = create_button(graphics_window, graphics_window.getWidth() - 70, 10, "Close")

            # Initial mode is selection mode
            mode = "selection"

            while True:
                click_point = graphics_window.getMouse()

                if mode == "selection":
                    button_clicked = handle_mouse_click(patches, [ok_button, close_button], click_point)

                    if button_clicked == "OK":
                        mode = "edit"
                        ok_button.undraw()
                        close_button.undraw()
                        continue
                    elif button_clicked == "Close":
                        graphics_window.close()
                        break

                elif mode == "edit":
                    key_pressed = graphics_window.getKey()
                    if key_pressed == "s":
                        mode = "selection"
                        ok_button.draw(graphics_window)
                        close_button.draw(graphics_window)
                    elif key_pressed == "d":
                        for patch in patches:
                            patch.setWidth(1)
                            patch.setOutline("white")
                    elif key_pressed == "p":
                        for patch in patches:
                            if patch.getWidth() == 3:
                                design_index = penultimate
                                patch.undraw()
                                patch = draw_patch(graphics_window, patch.getP1().getX(), patch.getP1().getY(), patch.getFill(), design_index)
                                patches[patches.index(patch)] = patch
                    elif key_pressed == "f":
                        for patch in patches:
                            if patch.getWidth() == 3:
                                design_index = final
                                patch.undraw()
                                patch = draw_patch(graphics_window, patch.getP1().getX(), patch.getP1().getY(), patch.getFill(), design_index)
                                patches[patches.index(patch)] = patch
                    elif key_pressed == "q":
                        for patch in patches:
                            if patch.getWidth() == 3:
                                design_index = 0
                                patch.undraw()
                                patch = draw_patch(graphics_window, patch.getP1().getX(), patch.getP1().getY(), patch.getFill(), design_index)
                                patches[patches.index(patch)] = patch
                    elif key_pressed in colors:
                        for patch in patches:
                            if patch.getWidth() == 3:
                                color = key_pressed
                                patch.undraw()
                                patch = draw_patch(graphics_window, patch.getP1().getX(), patch.getP1().getY(), color, patch.getOutlineWidth())
                                patches[patches.index(patch)] = patch
                    elif key_pressed == "x":
                        # Your custom operation (use your imagination)
                        pass

        except ValueError as e:
                print(f"Error: {e}")
                # Continue to the next iteration of the loop if there's an error

if __name__ == "__main__":
    main()
