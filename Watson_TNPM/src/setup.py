from cx_Freeze import setup, Executable

base = None

executables = [Executable("server.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },    
}

setup(
    name = "suyash",
    options = options,
    version = "1.0",
    description = 'Cognitive product support',
    executables = executables
)