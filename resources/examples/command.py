class Command:
    def execute(self, program):
        pass


class KillCommand(Command):
    def execute(self, program):
        program.kill()


class RestartCommand(Command):
    def execute(self, program):
        program.restart()


commands = [KillCommand(), RestartCommand()]
