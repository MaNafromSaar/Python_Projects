import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Initial values
time = 0
wave = []

# Create a larger figure
fig = plt.figure(figsize=(14, 8))

# Create subplots for the circles and the wave
ax1 = plt.subplot2grid((8, 14), (0, 0), colspan=7, rowspan=7)
ax2 = plt.subplot2grid((8, 14), (0, 7), colspan=7, rowspan=7)

# Adjust the subplots region to leave some space for the sliders
plt.subplots_adjust(left=0.3)

# Create sliders for speed and number of epicircles
ax_slider1 = plt.axes([0.05, 0.1, 0.03, 0.65])
ax_slider2 = plt.axes([0.1, 0.1, 0.03, 0.65])

slider1 = Slider(ax_slider1, 'Speed', 0.01, 0.3, valinit=0.05, orientation='vertical')
slider2 = Slider(ax_slider2, 'Epicircles', 1, 250, valinit=5, valstep=1, orientation='vertical')

# Create a slider for the rotation direction
ax_slider3 = plt.axes([0.15, 0.1, 0.03, 0.65])
slider3 = Slider(ax_slider3, 'Clockwise %', 0, 100, valinit=0, orientation='vertical')

# Animation update function
def update(i):
    global time
    ax1.clear()
    ax2.clear()

    x = 0
    y = 0

    max_radius = 0  # Keep track of the maximum radius

    # Calculate the number of circles for each category
    total_circles = int(slider2.val)
    clockwise_circles = int(total_circles * slider3.val / 100)
    counterclockwise_circles = total_circles - clockwise_circles

    # Create lists for clockwise and counterclockwise circles
    directions = [1] * clockwise_circles + [-1] * counterclockwise_circles

    for i, direction in enumerate(directions):
        prevx = x
        prevy = y

        n = i * 2 + 1
        radius = 75 * (4 / (n * np.pi))
        x += radius * np.cos(n * time * direction)
        y += radius * np.sin(n * time * direction)

        # Draw the circle and the line
        circle = plt.Circle((prevx, prevy), radius, color='b', fill=False)
        ax1.add_artist(circle)
        ax1.plot([prevx, x], [prevy, y], color='r')

        # Update the maximum radius
        max_radius = max(max_radius, radius)

    wave.insert(0, y)

    # Draw the wave
    ax2.plot(range(len(wave)), [y for y in wave], color='g')

    # Draw the line indicating the last epicircle position to a y value on the wave plot
    ax1.plot([x, 200], [y, wave[0]], color='g')

    if len(wave) > 120:
        wave.pop()

    time += slider1.val

    # Set equal aspect ratio for the circles subplot
    ax1.set_aspect('equal', adjustable='datalim')

    # Set the limits of the subplot
    ax1.set_xlim(-max_radius-150, max_radius+150)
    ax1.set_ylim(-max_radius-200, max_radius+200)

# Create the animation
ani = FuncAnimation(fig, update, frames=range(100), repeat=True)

plt.show()
