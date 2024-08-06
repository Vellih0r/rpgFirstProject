import pyglet


def language():
    music = pyglet.resource.media("Static (cut).mp3")
    music.play()
    pyglet.app.run()
    input(f'''Обери мову / Choose the language:\n
>> english
>> spanish\n''')

language()