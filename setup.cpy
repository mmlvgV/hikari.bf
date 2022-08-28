if __name__ == "__main__":
    import os

    if os.name != "nt":
        import uvloop

        uvloop.install()

    import src.core.main

    from src.modules.config import TOKEN, PREFIX

    bot = src.core.main.Bot(TOKEN, prefix=PREFIX)

    bot.initiate()
