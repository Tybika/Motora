import customtkinter as tk

class MainView:
    def __init__(self):
        self.controller = None
        self.root = tk.CTk()

    def set_controller(self, controller: object):
        self.controller = controller

    def _run(self):
        button = tk.CTkButton(self.root, text='test connection',
                              command=self.controller.test_connection)
        button.grid(row=0, column=0)
        self.root.mainloop()
    
