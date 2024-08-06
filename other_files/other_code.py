import pyglet


def language():
    print(f'''Обери мову / Choose the language:\n
>> english
>> spanish\n''')
    music = pyglet.resource.media("Static (cut).mp3")
    music.play()
    pyglet.app.run()

language()