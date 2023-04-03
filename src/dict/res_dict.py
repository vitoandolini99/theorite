import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

resolution_dictionary = {
    "960": (960, 540),
    "fullscreen": (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
}

