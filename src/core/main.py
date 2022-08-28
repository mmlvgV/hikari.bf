import os
import hikari
import brainfuck


path = "./src/cogs/"


class Bot(hikari.GatewayBot):
    def __init__(self, token: str, *, prefix) -> None:
        super().__init__(token, banner=None)

        self.token = token
        self.prefix = prefix

    def adjust(self) -> None:
        self.event_manager.subscribe(hikari.MessageCreateEvent, self.message)

    def initiate(self) -> None:
        self.adjust(), super().run()

    async def message(self, event: hikari.MessageCreateEvent) -> None:
        if event.is_bot or not event.content:
            return

        for _file in os.listdir(path):
            if not _file.endswith(".bf"):
                return

            _format = self.prefix + _file[:-3]

            if event.content.startswith(_format):
                with open(path + _file, "r") as book:
                    script = str(book.read().encode("utf-8"))
                    content = brainfuck.evaluate(script)

                    await event.message.respond(content, reply=True)
