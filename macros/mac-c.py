from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'C', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, 'Cut', [Keycode.COMMAND, 'X']),
        (0x004000, 'Copy', [Keycode.COMMAND, 'C']),
        (0x400000, 'Paste', [Keycode.SHIFT, 'V']),      # Scroll up
        # 2nd row ----------
        (0x202000, 'Undo', [Keycode.COMMAND,'Z']),
        (0x202000, 'Redo', [Keycode.COMMAND, Keycode.SHIFT,'Z']),
        (0x400000, 'Print', 'printf'),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Run', [Keycode.F5]),
        (0x000040, 'Debug', [Keycode.CONTROL, Keycode.F5]),
        (0x000040, 'Stop', [Keycode.CONTROL, Keycode.F2]),
        # 4th row ----------
        (0x000000, 'New', [Keycode.COMMAND, 'N']),   # Adafruit in new window
        (0x800000, 'Open', [Keycode.COMMAND, 'O']),   # Digi-Key in new window
        (0x101010, 'Save', [Keycode.COMMAND, 'S']), # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w']) # Close window/tab
    ]
}
