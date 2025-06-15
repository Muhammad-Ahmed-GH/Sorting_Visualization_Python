from shared import *

def draw_bars(data, color_array):
    canvas.delete("all")
    canvas_height = 400
    canvas_width = 600
    bar_width = canvas_width / len(data)
    for i, val in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - val
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    root.update()