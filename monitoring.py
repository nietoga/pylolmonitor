import psutil


def is_lol_runing() -> bool:
    patterns_to_validate = ["league", "riot"]

    for p in psutil.process_iter():
        try:
            process_name = p.name().lower()
            process_command = " ".join(p.cmdline()).lower()

            for pattern in patterns_to_validate:
                if pattern in process_name or pattern in process_command:
                    return True
        except psutil.AccessDenied:
            pass

    return False
