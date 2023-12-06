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
print("Patchwork colors:", patchwork_colors)

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
from graphics import GraphWin

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

#Draw the patch work

#import libraries
from graphics import GraphWin, Point, Rectangle, Oval, Polygon, Line

def draw_patch(win, x, y, color, design):
    # Function to draw a single patch at the specified position with given color and design
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
    patch.draw(win)

def draw_patchwork(win, patchwork_size, colors, antepenultimate, penultimate, final):
    # Function to draw the entire patchwork based on the extracted digits
    patch_size = 100

    for row in range(patchwork_size):
        for col in range(patchwork_size):
            x = col * patch_size
            y = row * patch_size

            # Use the extracted digits to determine color and design
            color_index = (antepenultimate + row + col) % 3
            color = colors[color_index]

            design_index = (penultimate + row + col) % 2 + 1

            draw_patch(win, x, y, color, design_index)

def main():
    while True:
        # Draw the patchwork
        draw_patchwork(win, patchwork_size, colors, antepenultimate, penultimate, final)

        # Display the window until the user clicks on it
        win.getMouse()
        win.close()

        while True: # Ask the user if they want to create another patchwork
            another_patchwork = input("Do you want to create another patchwork? (yes/no): ").lower()
            if another_patchwork == 'yes' or another_patchwork == 'no':  
                break
            else:
                continue

        if another_patchwork == 'yes':
            continue
        else:
            break

if __name__ == "__main__":
    main()
