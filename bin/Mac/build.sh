#!/bin/bash
# Build for Mac

case "$1" in
"algorithm" | "algo")
    pyinstaller ../../algorithm.py -F
    ;;
"visualizer" | "vis")
    pyinstaller ../../visualizer.py -F
    ;;
"gui")
    pyinstaller ../../gui.py -F
    ;;
"all")
    pyinstaller ../../algorithm.py -F
    pyinstaller ../../visualizer.py -F
    pyinstaller ../../gui.py -F
    ;;
"help" | "h")
    echo -e "Build options:
    all                 Build all components
    algorithm or algo   Build algorithm
    visualizer or vis   Build visualizer
    gui                 Build gui
    help or h           Show help"
    ;;
*)
    echo "Options are incorrect. Use h for help"
    ;;
esac