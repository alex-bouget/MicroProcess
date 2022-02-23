import os
import subprocess
import threading
from typing import List

"""
MicroProcess
Class for interact with a sub-process.
"""


class MicroProcess:
    _arg: str or list
    """Argument for call the process"""

    _process: subprocess.Popen
    """sub-process"""

    _thread: threading.Thread
    """Thread for test the out process"""

    _stdout: List[str]
    """List of all return of the process"""

    def __init__(self, arg: str or list):
        """Constructor"""
        self._arg = arg
        self._process = subprocess.Popen(
            self._arg,
            shell=True,
            bufsize=64,
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        self._stdout = []
        self._thread = threading.Thread(target=self._thread_get_st)
        self._thread.start()

    def _thread_get_st(self):
        """Thread call for get the out's process"""
        for line in self._process.stdout:
            self._stdout.append("".join(str(line.rstrip())[2:-1]))
            self._process.stdout.flush()

    def send_line(self, line: str):
        """Send a command to the process"""
        self._process.stdin.write(line.encode() + os.linesep.encode())
        self._process.stdin.flush()

    def get_out(self) -> str or None:
        """Get the new line of the out's process"""
        if len(self._stdout) > 0:
            get = str(self._stdout[0])
            del self._stdout[0]
            return get
        return None
