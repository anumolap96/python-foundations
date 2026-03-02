"""
This script recreates a visual diagram similar to the image you showed.

The idea of the image is:

"Do something to Data"
Functions operate on Values → produce New Values

We will use matplotlib to:
1. Create a blank canvas
2. Draw boxes (for libraries and function)
3. Draw arrows
4. Add text labels
5. Arrange everything properly

Run this file using:
python filename.py
"""

# Import matplotlib for drawing
import matplotlib.pyplot as plt

# Import patches module to draw rectangles, arrows, etc.
import matplotlib.patches as patches


# -------------------------------
# STEP 1: Create a figure (canvas)
# -------------------------------

# figsize controls width and height of the image (in inches)
fig, ax = plt.subplots(figsize=(14, 8))

# Turn OFF axes (no x/y grid visible)
ax.set_xlim(0, 100)   # Horizontal range
ax.set_ylim(0, 100)   # Vertical range
ax.axis("off")        # Hide axes


# --------------------------------
# STEP 2: Helper function to draw box
# --------------------------------

def draw_box(x, y, width, height, text):
    """
    This function draws a rectangle and places text inside it.

    Parameters:
    x, y        → Bottom-left position of the box
    width       → Width of the box
    height      → Height of the box
    text        → Text to display inside the box
    """

    # Create rectangle
    rect = patches.FancyBboxPatch(
        (x, y),                # Bottom-left corner
        width, height,
        boxstyle="round,pad=0.02",  # Rounded edges
        linewidth=2,
        edgecolor="black",
        facecolor="#E8F4FA"     # Light blue color
    )

    # Add rectangle to plot
    ax.add_patch(rect)

    # Add text in center of box
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",  # Horizontal alignment
        va="center",  # Vertical alignment
        fontsize=12,
        weight="bold"
    )


# --------------------------------
# STEP 3: Draw Top Title
# --------------------------------

ax.text(
    50, 95,
    "Do Something to Data",
    ha="center",
    fontsize=22,
    weight="bold"
)


# --------------------------------
# STEP 4: Draw Top 3 Boxes
# --------------------------------

draw_box(10, 70, 20, 10, "User Defined")
draw_box(40, 70, 20, 10, "Standard Library")
draw_box(70, 70, 20, 10, "3rd-Party Libraries\n(Pandas, NumPy, TensorFlow)")


# --------------------------------
# STEP 5: Draw Central Function Box
# --------------------------------

draw_box(35, 45, 30, 12, "Function")


# --------------------------------
# STEP 6: Draw Arrows from Top Boxes to Function
# --------------------------------

def draw_arrow(x1, y1, x2, y2):
    """
    Draw an arrow from (x1, y1) to (x2, y2)
    """

    ax.annotate(
        "",
        xy=(x2, y2),    # Arrow end
        xytext=(x1, y1),# Arrow start
        arrowprops=dict(
            arrowstyle="->",
            linewidth=2
        )
    )


# Arrows pointing to central function
draw_arrow(20, 70, 50, 57)
draw_arrow(50, 70, 50, 57)
draw_arrow(80, 70, 50, 57)


# --------------------------------
# STEP 7: Draw Value → Function → New Value
# --------------------------------

# Left side "Value"
ax.text(15, 50, "Value", fontsize=14, weight="bold")

# Arrow from Value to Function
draw_arrow(22, 50, 35, 51)

# Right side "New Value"
ax.text(75, 50, "New Value", fontsize=14, weight="bold")

# Arrow from Function to New Value
draw_arrow(65, 51, 75, 50)


# --------------------------------
# STEP 8: Bottom Section
# --------------------------------

# Standalone Functions
ax.text(15, 25,
        "Standalone Functions\n\nprint()\ntype()",
        fontsize=11)

# Methods of class
ax.text(45, 25,
        "Methods of Class\n\nupper()\nreplace()",
        fontsize=11)

# Operations
ax.text(75, 25,
        "Operations\n\n+  -  *  /\n==  in  or",
        fontsize=11)


# --------------------------------
# STEP 9: Show the final diagram
# --------------------------------

plt.show()