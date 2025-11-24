import paths
import subprocess
import sys

from motora import Motora
from controller import Controller
from view import MainView

def main():
    # Instalação de dependências
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", 
                           "requirements.txt"])

    # Instâncias MVC
    model = Motora()
    controller = Controller()
    view = MainView()

    # Conexões MVC
    model.set_controller(controller)
    view.set_controller(controller)
    controller.set_model(model)
    controller.set_view(view)

    view._run()

if __name__ == '__main__':
    main() 
    
