from subprocess import check_output, STDOUT, Popen, PIPE
from ewe.logging import logger
from ewe.exceptions import ShellNotFoundError
from pathlib import Path


class Command:
    def __init__(self, command: str, shell: str = 'bash', silent: bool = False) -> None:
        self.command = command.split(' ')
        self.shell = shell
        self.silent = silent

        self.shell_executable = self.find_shell_executable()

    def run(self) -> int:
        if 'bash' in str(self.shell_executable):
            self.run_bash_command()

    def run_bash_command(self) -> int:
        command = (str(self.shell_executable), '-c', f'\"{self.command}\"')
        logger.debug(f'running {self.command}')
        process = Popen(
            self.command,
            shell=True,
            executable=str(self.shell_executable),
            stdout=PIPE,
            stderr=PIPE,
        )
        exit_code = process.wait()
        if exit_code != 0:
            print(process.stderr.read().decode('utf-8'))
            raise SystemExit(1)
        print(process.stdout.read().decode('utf-8'))
        return 0

    def find_shell_executable(self) -> Path:
        logger.debug(f'finding exectuable for shell "{self.shell}"')
        if Path(f'/usr/bin/{self.shell}').exists:
            return Path(f'/usr/bin/{self.shell}')
        elif Path(f'/bin/{self.shell}').exists:
            return Path(f'/bin/{self.shell}')

        raise ShellNotFoundError(f'shell {self.shell} not found')
