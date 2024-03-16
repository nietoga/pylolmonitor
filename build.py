import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "--onefile",
        "--windowed",
        *["--icon", "rat.png"],
        *["--name", "lolnotifier"],
        *["--add-data", "rat.png:."],
        "main.py",
    ]
)
