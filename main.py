import paths
import subprocess
import sys
import os

from motora import Motora
from controller import Controller
from view import MainView

def main():
    # Instalação de dependências
    if not os.path.exists('deps.txt'):
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", 
                                "requirements.txt"])
        with open("deps.txt", "x") as file:
            pass

    # Instâncias MVC
    model = Motora()
    controller = Controller()
    view = MainView()

    # Conexões MVC
    model.set_controller(controller)
    view.set_controller(controller)
    controller.set_model(model)
    controller.set_view(view)

    # Inicalização da GUI
    view._run()

if __name__ == '__main__':
    main() 
    
