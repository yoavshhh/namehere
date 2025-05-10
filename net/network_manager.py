import platform
from net.peer import Peer

class NetworkManager:
    def __init__(self):
        self.peer = Peer()
        if platform.system() == "Windows":
            self.allow_port_windows(9999)

    def sync(self):
        # Placeholder for sync logic
        pass
    
    def allow_port_windows(self, port: int, name: str, protocol: str="tcp"):
        """allow port in windows systems

        Args:
            port (int): Port number to allow
            name (str): Name of the rule
            protocol (str, optional): The protocol type to allow. Defaults to "tcp".
        """        
        try:
            import subprocess
            import ctypes
            cmd = (
                f'netsh advfirewall firewall add rule '
                f'name="{name}" dir=in action=allow protocol={protocol} localport={port}'
            )

            # This will prompt UAC if not elevated
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", "cmd.exe", f'/c {cmd}', None, 1
            )
        except subprocess.CalledProcessError as e:
            print("Failed to add firewall rule:", e)