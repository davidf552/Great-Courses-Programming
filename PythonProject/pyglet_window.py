import pyglet
from pyglet.window import key

window = pyglet.window.Window(width=400, height=300, caption="TestWindow")

label = pyglet.text.Label('Nothing pressed so far',
                          font_name="Times New Roman",font_size=18,x=50, y=150)


@window.event
def on_draw():
    window.clear()
    label.draw()

@window.event
def on_key_press(symbol,modifiers):
    if symbol == key.A:
        key_pressed = "a"
    elif symbol == key.LEFT:
        key_pressed = "left"
    elif symbol == key.RETURN:
        key_pressed = "return"
    else:
        key_pressed = 'unknown'
    global label
    label = pyglet.text.Label('You pressed the '+key_pressed+' key!',font_name = "Times New Roman", font_size=18,
                              x=50,y=150)
@window.event
def on_mouse_motion (x,y,dx,dy):
    global label
    label = pyglet.text.Label('Mouse click at position ('+str(x)+', '+str(y)+')',
                              font_name="Times New Roman", font_size=18,
                              x=50, y=150
                              )
pyglet.app.run()