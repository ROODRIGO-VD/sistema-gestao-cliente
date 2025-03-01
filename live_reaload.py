from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os
import sys


class MyHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = self.start_process()

    def start_process(self):
        """Inicia o processo da aplicação."""
        return subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        """Reinicia a aplicação quando um arquivo .py é modificado."""
        if event.src_path.endswith(".py"):
            print(
                f"Arquivo modificado: {event.src_path}. Reiniciando aplicação...")
            self.process.terminate()  # Encerra o processo atual
            self.process = self.start_process()  # Reinicia a aplicação


if __name__ == "__main__":
    script = "app.py"  # Substitua pelo nome do seu script principal
    event_handler = MyHandler(script)
    observer = Observer()
    # Monitora o diretório atual
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)  # Mantém o script em execução
    except KeyboardInterrupt:
        observer.stop()  # Encerra o monitoramento ao pressionar Ctrl+C
    observer.join()
