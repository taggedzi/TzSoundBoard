import os
import pygame
# import mutagen # added for playback length etc. possible slider to indicate play position.

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
        self.sounds = []
        self.main_window = tkinter.Tk()
        self.main_window.geometry("500x300+150+150")
        self.main_window.title('TzSoundBoard')
        self.create_menu()
        self.tools = self.set_tool_frame()
        self.sound_frame = self.set_sound_frame()
        self.set_volume(100)

    def set_tool_frame(self):
        tools = tkinter.LabelFrame(self.main_window, text="Tools", borderwidth=1, relief="groove", width=200, padx=5,
                                   pady=5)
        tools.grid(row=0, column=0, sticky="ne")

        # add volume controlls
        self.volume = tkinter.Scale(tools, label="Volume", orient=tkinter.VERTICAL, from_=100, to=0, command=self.set_volume)
        self.volume.grid(row=1, column=0)

        # add: add_sound controls.
        button = tkinter.Button(tools, text="Add New Sound", height=2, command=self.pick_file)
        button.grid(row=0, column=0)
        return tools

    def set_sound_frame(self):
        sound_frame = tkinter.Frame(self.main_window, padx=5, pady=5)
        sound_frame.grid(row=0, column=1, sticky="nsew")
        return sound_frame

    def main(self):
        self.main_window.mainloop()

    def close(self):
        self.main_window.destroy()

    def pick_file(self):
        file_path = filedialog.askopenfilename(initialdir='./', title="Select file", filetypes=self.MUSIC_FILE_TYPES)
        if file_path:
            new_sound = Sound(file_path, os.path.basename(file_path), "")
            self.sounds.append(new_sound)
            total_sounds = len(self.sounds) - 1
            rows = int(total_sounds / 4)
            if total_sounds % 4 == 0:
                col = 0
            else:
                col = int(total_sounds % 4)
            button = tkinter.Button(self.sound_frame, text=os.path.basename(file_path), height=10, width=20)
            button.grid(row=rows, column=col)
            button.config(command=new_sound.play)
        else:
            raise NotImplementedError("No file Selected")

    def create_menu(self):
        self.menu = tkinter.Menu(self.main_window)
        self.main_window.config(menu=self.menu)

        file = tkinter.Menu(self.menu)
        file.add_command(label="Add Sound Effect", command=self.pick_file)
        file.add_command(label="Exit", command=self.close)
        self.menu.add_cascade(label="File", menu=file)

    def set_volume(self, value):
        self.volume.set(value)
        Sound.set_volume(value)


class Sound(object):

    def __init__(self, sound_path, label, image_path):
        self.__sound_path = None
        self.__label = None
        self.__image_path = None
        self.is_playing = False
        self.sound_path = sound_path
        self.label = label
        self.image_path = image_path

    def play(self):
        pygame.mixer.music.load(self.sound_path)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    @classmethod
    def set_volume(cls, value):
        value = int(value)
        print("is called: {}".format(value))
        if value == 0:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(value/100)

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


pygame.mixer.init()
wc = WindowController()
wc.main()
