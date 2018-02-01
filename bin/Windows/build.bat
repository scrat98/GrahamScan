:: Build for Windows

IF "%1"=="algorithm" pyinstaller ../../algorithm.py -F
IF "%1"=="algo"      pyinstaller ../../algorithm.py -F

IF "%1"=="visualizer" pyinstaller ../../visualizer.py -F
IF "%1"=="vis"        pyinstaller ../../visualizer.py -F

IF "%1"=="gui" pyinstaller ../../gui.py -F

IF "%1"=="all" (
    pyinstaller ../../algorithm.py -F
    pyinstaller ../../visualizer.py -F
    pyinstaller ../../gui.py -F
)

IF "%1"=="help" (
    echo "Build options:"
    echo "  all                 Build all components"
    echo "  algorithm or algo   Build algorithm"
    echo "  visualizer or vis   Build visualizer"
    echo "  gui                 Build gui"
    echo "  help or h           Show help"
)
IF "%1"=="h" (
    echo "Build options:"
    echo "  all                 Build all components"
    echo "  algorithm or algo   Build algorithm"
    echo "  visualizer or vis   Build visualizer"
    echo "  gui                 Build gui"
    echo "  help or h           Show help"
) ELSE (
    echo "Options are incorrect. Use h for help"
)