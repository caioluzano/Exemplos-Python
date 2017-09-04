from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("ConversordeNomes.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "ConvNomesRaizen",
    options = options,
    version = "1.0",
    description = 'Converta o nome das empresas',
    executables = executables
)
