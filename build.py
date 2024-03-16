import PyInstaller.__main__

PyInstaller.__main__.run(
    [
        "--onefile",
        "--windowed",
        *["--icon", "rat.ico"],
        *["--name", "lolnotifier"],
        *["--add-data", "rat.ico:."],
        *["--add-data", ".env:."],
        "main.py",
    ]
)
