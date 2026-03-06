import matplotlib.pyplot as plt
import time

def draw_array(ax, arr, highlight_index=None, found_index=None):
    ax.clear()
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, 2)
    ax.axis("off")

    for i, value in enumerate(arr):
        # Decide color
        if i == found_index:
            color = "green"
        elif i == highlight_index:
            color = "red"
        else:
            color = "lightblue"

        # Draw rectangle
        rect = plt.Rectangle((i, 0.8), 1, 0.6, fill=True, color=color, edgecolor="black")
        ax.add_patch(rect)

        # Value inside box
        ax.text(i + 0.5, 1.1, str(value), ha="center", va="center", fontsize=12, weight="bold")

        # Index below box
        ax.text(i + 0.5, 0.6, str(i), ha="center", va="center", fontsize=10)

    plt.pause(0.8)


def linear_search_visual(arr, target):
    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 3))

    for i in range(len(arr)):
        draw_array(ax, arr, highlight_index=i)
        ax.set_title(f"Checking index {i}")

        if arr[i] == target:
            draw_array(ax, arr, found_index=i)
            ax.set_title(f"Element {target} FOUND at index {i}")
            plt.pause(2)
            plt.ioff()
            plt.show()
            return i

    ax.set_title(f"Element {target} NOT FOUND")
    plt.pause(2)
    plt.ioff()
    plt.show()
    return -1


# ---------------- MAIN ---------------- #

array = [5, 3, 7, 1, 9, 4, 8]
target = 9

result = linear_search_visual(array, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")