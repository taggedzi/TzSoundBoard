import os
import pygame
import mutagen # added for playback length etc. possible slider to indicate play position.

try:
    # python 3
    import tkinter
    from tkinter import filedialog
except ImportError:
    # python 2
    import Tkinter as tkinter


class WindowController(object):
    MUSIC_FILE_TYPES = (("MP3 files", "*.mp3"),
                        ("WAV files", "*.wav"),
                        ("OGG files", "*.ogg"))

    def __init__(self):
        self.menu = None
        self.volume = None
        self.volume_callback = lambda x: print(x)
        self.pick_file_callback = lambda x: print(x)
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300+150+150")
        self.main_window.title('TzSoundBoard')
        self.volume_controls(3, 0)
        self.create_menu()

    def main(self):
        self.main_window.mainloop()

    def close(self):
        self.main_window.destroy()

    def add_button(self, label, row, col, callback):
        button = tkinter.Button(self.main_window, text=label, height=10, width=20, command=callback)
        button.grid(row=row, column=col)

    def pick_file(self):
        file_path = filedialog.askopenfilename(initialdir='./', title="Select file", filetypes=self.MUSIC_FILE_TYPES)
        self.pick_file_callback(file_path)

    def set_pick_file_callback(self, callback):
        self.pick_file_callback = callback

    def create_menu(self):
        self.menu = tkinter.Menu(self.main_window)
        self.main_window.config(menu=self.menu)

        file = tkinter.Menu(self.menu)
        file.add_command(label="Add Sound Effect", command=self.pick_file)
        file.add_command(label="Exit", command=self.close)
        self.menu.add_cascade(label="File", menu=file)

    def set_volume(self, value):
        value = int(value)
        print("is called: {}".format(value))
        if value == 0:
            self.volume = 0
        else:
            self.volume = value / 100
        self.volume_callback(self.volume)

    def set_volume_callback(self, callback):
        self.volume_callback = callback

    def volume_controls(self, row, col):
        scale = tkinter.Scale(self.main_window, label="Volume", orient=tkinter.HORIZONTAL, from_=0, to=100, command=self.set_volume)
        scale.grid(row=row, column=col)


class TzSoundBoard(object):

    def __init__(self):
        self.column = 0
        self.row = 0

# my = TzSoundBoard()


class Sound(object):

    def __init__(self, sound_path, label, image_path):
        self.__sound_path = None
        self.__label = None
        self.__image_path = None
        self.sound_path = sound_path
        self.label = label
        self.image_path = image_path
        pygame.mixer.init()

    def play(self, file_to_play):
        pygame.mixer.music.load(file_to_play)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def set_volume(self, value):
        value = int(value)
        print("is called: {}".format(value))
        if value == 0:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(value/100)

    def generate_button(self, window, file_to_play):
        return tkinter.Button(window, text=self.label, height=10, width=20,
                              command=lambda: self.play(file_to_play)).grid(row=self.row, column=self.column)

    @property
    def sound_path(self):
        return self.__sound_path

    @sound_path.setter
    def sound_path(self, sound_path):
        self.__sound_path = sound_path

    @sound_path.deleter
    def sound_path(self):
        del self.__sound_path

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    @label.deleter
    def label(self):
        del self.__label

    @property
    def image_path(self):
        return self.__image_path

    @image_path.setter
    def image_path(self, image_path):
        self.__image_path = image_path

    @image_path.deleter
    def image_path(self):
        del self.__image_path


def double(val):
    print(str(val), str(val))


wc = WindowController()
wc.set_pick_file_callback(double)
wc.set_volume_callback(double)
wc.main()