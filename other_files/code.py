import pyglet


def language():
    music = pyglet.resource.media("Static (cut).mp3")
    music.play()
    print(f'''Обери мову / Choose the language:\n
>> english
>> spanish\n''')
    pyglet.app.run()

language()