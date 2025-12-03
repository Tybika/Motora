import customtkinter as ctk
from CTkMenuBar import *
from CustomTkinterMessagebox import CTkMessagebox
import matplotlib.pyplot as plot
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainView:
    def __init__(self):
        self.controller = None
        self.root = ctk.CTk()
        self.home()

    def set_controller(self, controller: object):
        self.controller = controller

    def home(self):
        self.root.geometry(f"1280x720+0+0")
        self.root.title("Motora")
        menu = CTkMenuBar(master=self.root)
        menu.add_cascade("Novo atleta", command=self.register)
        menu.add_cascade("Buscar atleta", command=self.search)
        
        # Cria frames para organização 
        homeFrame = ctk.CTkFrame(self.root, fg_color="transparent",
                                      width=1280)
        self.plotFrame = ctk.CTkFrame(homeFrame, fg_color="transparent",
                                      width=1280)
        infoFrame = ctk.CTkFrame(homeFrame, fg_color="transparent",
                                 width=1280)

        # Cria widgets
        countLabel = ctk.CTkLabel(infoFrame, text="Total de registros:",
                                   bg_color="transparent")
        self.countLabel = ctk.CTkLabel(infoFrame, text="",
                                   bg_color="transparent")
        
        dateLabel = ctk.CTkLabel(infoFrame, text="Data do último registro:",
                                   bg_color="transparent")
        self.dateLabel = ctk.CTkLabel(infoFrame, text="",
                                   bg_color="transparent")
        
        # Posiciona Widgets
        countLabel.grid(row=0, column=1, sticky="e")
        self.countLabel.grid(row=0, column=2, sticky="e")

        dateLabel.grid(row=1, column=1)
        self.dateLabel.grid(row=1, column=2)

        # Posiciona frames
        infoFrame.pack()
        self.plotFrame.pack(expand=True, fill="both")

        homeFrame.pack(expand=True, fill="both")

    def register(self):
        # Cria e configura a janela
        self.r_window = ctk.CTkToplevel(self.root)
        self.r_window.title("Novo Atleta")
        self.r_window.geometry("500x400")
        self.r_window.grab_set()
        self.r_window.focus()

        # Cria frames para organização
        mainFrame = ctk.CTkFrame(self.r_window, fg_color="transparent")
        personalFrame = ctk.CTkFrame(mainFrame, fg_color="transparent")
        testFrame = ctk.CTkFrame(mainFrame, fg_color="transparent")
        buttonFrame = ctk.CTkFrame(mainFrame, fg_color="transparent")

        # Cria widgets
        personalLabel = ctk.CTkLabel(personalFrame, text = 'Dados pessoais',
                                     pady=(40), bg_color="transparent")
        
        nameLabel = ctk.CTkLabel(personalFrame, text = 'Nome completo', 
                                 bg_color="transparent")
        self.nameEntry = ctk.CTkEntry(personalFrame, width=300, 
                                      bg_color="transparent")
        
        ageLabel = ctk.CTkLabel(personalFrame, text="Idade", 
                                bg_color="transparent")
        self.ageEntry = ctk.CTkEntry(personalFrame, width=40, 
                                     bg_color="transparent")
        
        sexLabel = ctk.CTkLabel(personalFrame, text="Sexo", 
                                bg_color="transparent")
        self.sexCombo = ctk.CTkComboBox(personalFrame,
                        values=self.controller.get_sex_options())
        self.sexSwitch = ctk.StringVar(value="off")
        sexSwitch = ctk.CTkCheckBox(personalFrame, text="Em hormonioterapia",
                        variable=self.sexSwitch, onvalue="on", offvalue="off")

        weightLabel = ctk.CTkLabel(personalFrame, text="Peso (em kg)", 
                                   bg_color="transparent")
        self.weightEntry = ctk.CTkEntry(personalFrame, width=40, 
                                        bg_color="transparent")

        heigthLabel = ctk.CTkLabel(personalFrame, text="Altura (em metros)", 
                                   bg_color="transparent")
        self.heigthEntry = ctk.CTkEntry(personalFrame, width=40, 
                                        bg_color="transparent")

        testLabel = ctk.CTkLabel(testFrame,text="Dados de teste", pady=40, 
                                 bg_color="transparent")
        flexLabel = ctk.CTkLabel(testFrame, text="Flexibilidade (em cm)", 
                                 bg_color="transparent")
        self.flexEntry = ctk.CTkEntry(testFrame, bg_color="transparent")

        cardioLabel = ctk.CTkLabel(testFrame, text="Cardio (em m)", 
                                   bg_color="transparent")
        self.cardioEntry = ctk.CTkEntry(testFrame, bg_color="transparent")

        cancelButton = ctk.CTkButton(buttonFrame, text="Cancelar", fg_color="gray",
                                     bg_color="transparent",
                                     command=self.r_window.destroy)
        sendButton = ctk.CTkButton(buttonFrame, text="Salvar", 
                                   bg_color="transparent",
                                   command=self.save_athlete)

        # Configura grids
        mainFrame.columnconfigure(0, weight=1, pad=10)
        mainFrame.columnconfigure(1, weight=2, pad=10)
        mainFrame.columnconfigure(2, weight=1)

        personalFrame.rowconfigure([0,1,2,3,4,5,6,7], pad=4)

        # Posiciona widgets
        personalLabel.grid(row=0, column=0, sticky="w")
        nameLabel.grid(row=1, column=0, sticky="w", padx=(0, 20))
        self.nameEntry.grid(row=1, column=1, sticky="w", columnspan=2)

        ageLabel.grid(row=2, column=0, sticky="w", padx=(0, 20))
        self.ageEntry.grid(row=2, column=1, sticky="w")
        
        sexLabel.grid(row=3, column=0, sticky="w", padx=(0, 20))
        self.sexCombo.grid(row=3, column=1, sticky="w")
        sexSwitch.grid(row=3, column=2)

        weightLabel.grid(row=4, column=0, sticky="w", padx=(0, 20))
        self.weightEntry.grid(row=4, column=1, sticky="w")

        heigthLabel.grid(row=4, column=2, sticky="w", padx=(0, 20))
        self.heigthEntry.grid(row=4, column=4, sticky="w")

        testLabel.grid(row=5, column=0, sticky="w")
        flexLabel.grid(row=6, column=0, sticky="w", padx=(0, 20))
        self.flexEntry.grid(row=7, column=0, sticky="w", padx=(0, 20))

        cardioLabel.grid(row=6, column=1, sticky="w", padx=20)
        self.cardioEntry.grid(row=7, column=1, sticky="e", padx=20)

        cancelButton.grid(row=0, column=0, sticky="e", pady=(20, 0), padx=4)
        sendButton.grid(row=0, column=1, sticky="w", pady=(20, 0))

        # Posiciona frames
        personalFrame.grid(row=0, column=0, sticky="w")
        testFrame.grid(row=1, column=0, sticky="w")
        buttonFrame.grid(row=2, column=0, sticky='e')
        mainFrame.grid(row=0, column=0, padx=20, sticky="ew")

    def search(self):
        # Cria e configura a janela
        window = ctk.CTkToplevel(self.root)
        window.title("Buscar atleta")
        window.geometry("600x400")
        window.grab_set()
        window.focus()

        # Cria frames para organização
        mainFrame = ctk.CTkFrame(window, fg_color="transparent")
        searchFrame = ctk.CTkFrame(mainFrame, fg_color="transparent")
        self.listFrame = ctk.CTkScrollableFrame(mainFrame, width=550,
                                                fg_color="transparent")

        criteriaLabel = ctk.CTkLabel(searchFrame, text="Critério de busca",
                                     bg_color="transparent")
        self.criteriaCombo = ctk.CTkComboBox(searchFrame, 
                                    bg_color="transparent",
                                    values=self.controller.get_search_options())
        
        searchLabel = ctk.CTkLabel(searchFrame, text="Termo de busca",
                                  bg_color="transparent")
        self.searchEntry = ctk.CTkEntry(searchFrame, bg_color="transparent")
        searchButton = ctk.CTkButton(searchFrame, text="Buscar",
                                     command=self.search_result)
        
        nameLabel = ctk.CTkLabel(self.listFrame, text="Nome",
                                 bg_color="transparent")
        ageLabel = ctk.CTkLabel(self.listFrame, text="Idade", 
                           bg_color="transparent")
        flexLabel = ctk.CTkLabel(self.listFrame, bg_color="transparent", 
                        text="Aptidão para flexibilidade")
        cardioLabel = ctk.CTkLabel(self.listFrame, bg_color="transparent", 
                        text="Aptidão cardiovascular")
        
        # Configura grids
        self.listFrame.columnconfigure(0, weight=2, pad=10)
        self.listFrame.columnconfigure([1, 2, 3], weight=1, pad=10)

        searchFrame.columnconfigure(0, pad=10)
        mainFrame.rowconfigure(0, weight=1)
        mainFrame.rowconfigure(1, weight=2)

        # Posiciona widgets
        criteriaLabel.grid(row=0, column=0, sticky="w")
        self.criteriaCombo.grid(row=0, column=1, sticky="w")

        searchLabel.grid(row=1, column=0, sticky="w")
        self.searchEntry.grid(row=1, column=1, sticky="w")
        searchButton.grid(row=1, column=2, sticky="w")

        nameLabel.grid(row=0, column=0, sticky="w")
        ageLabel.grid(row=0, column=1, sticky="w")
        flexLabel.grid(row=0, column=2, sticky="w")
        cardioLabel.grid(row=0, column=3, sticky="w")

        # Posiciona frames
        searchFrame.pack(padx=10, pady=10, anchor="w")
        self.listFrame.pack(expand=True, fill="y")

        mainFrame.pack(expand=True, fill="y")

    def item_search_list(self, data:list, row:int):
        name = ctk.CTkLabel(self.listFrame, text=data[0], 
                            bg_color="transparent")
        age = ctk.CTkLabel(self.listFrame, text=data[1],
                            bg_color="transparent")        
        flex = ctk.CTkLabel(self.listFrame, text=data[5], 
                            bg_color="transparent")
        cardio = ctk.CTkLabel(self.listFrame, text=data[6], 
                              bg_color="transparent")
        
        name.grid(row=row, column=0, sticky="w")
        age.grid(row=row, column=1, sticky="w")
        flex.grid(row=row, column=2, sticky="w")
        cardio.grid(row=row, column=3, sticky="w")

    def update_search_list(self, data:list):
        children = self.listFrame.winfo_children()

        for i in range(len(children)):
            if i > 3:
                children[i].destroy()

        for i in range(len(data)):
            self.item_search_list(data[i], (i+1))
        
    def search_result(self):
        criteria = self.criteriaCombo.get().lower()
        search = self.searchEntry.get()
        id = None

        if criteria == "nome" and len(search) > 0:
            id = {"name": search}

        self.update_search_list(self.controller.get_athlete_data(id))

    def save_athlete(self):
        # Considera a checkbox para classificar segundo gênero
        # ao invés do sexo puro 
        if self.sexSwitch == "on":
            values = self.controller.get_sex_options()
            selected = self.sexCombo.get()
            selected = values.index(selected)
            sex = values[(len(values) - 1 - selected)]
        else:
            sex = self.sexCombo.get()

        complete = True
        data = [self.nameEntry.get(),
                self.ageEntry.get(),
                sex,
                self.weightEntry.get(),
                self.heigthEntry.get(),
                self.flexEntry.get(),
                self.cardioEntry.get()
                ]

        for i in range(len(data)):
            if len(data[i]) == 0:
                complete = False

        if complete:
            self.controller.save_data(data)
            self.plot_classes(self.controller.get_plot_data())
            self.update_metadata()
            self.r_window.destroy()

    def plot_classes(self, data):
        # Agrupa em vetores por característica
        age = []
        flex = []
        cardio = []
        class_flex = []
        class_cardio = []
        
        for athlete in data:
                age.append(athlete[0])
                flex.append(athlete[1])
                cardio.append(athlete[2])
                class_flex.append(athlete[3])
                class_cardio.append(athlete[4])

        # Cria nova figura, com ambas imagens
        figure = Figure()
        flex_plot = figure.add_subplot(121)
        cardio_plot = figure.add_subplot(122)

        # Cria plotagem de flexibilidade
        flex_scatter = flex_plot.scatter(age, flex, c=class_flex, cmap="viridis")
        flex_plot.set_xlabel("Idade")
        flex_plot.set_ylabel("Flexibilidade em cm")
        flex_plot.set_title("Aptidão para flexibilidade")
        flex_scale = figure.colorbar(flex_scatter, ax=flex_plot)

        # Cria plotagem de cardiovascular
        cardio_scatter = cardio_plot.scatter(age, cardio, c=class_cardio, cmap="plasma")
        cardio_plot.set_xlabel("Idade")
        cardio_plot.set_ylabel("Metros em 6min")
        cardio_plot.set_title("Aptidão cardiovascular")
        cardio_scale = figure.colorbar(flex_scatter, ax=cardio_plot)

        # Configura ticks e tórulos dos gráficos
        ticks = [0, 1, 2, 3, 4, 5]
        labels = ["M. fraco", "Fraco", "Razoável", "Bom", "M. bom", "Excelente"]

        flex_scale.set_ticks(ticks)
        flex_scale.set_ticklabels(labels)
        cardio_scale.set_ticks(ticks)
        cardio_scale.set_ticklabels(labels)

        # Limpa plot anterior do frame
        children = self.plotFrame.winfo_children()
        for child in children:
            child.destroy()

        # Cria canva e posiciona plot
        canvas = FigureCanvasTkAgg(figure, master=self.plotFrame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True, fill="both")

    def update_metadata(self):
        meta = self.controller.get_metadata()
        self.countLabel.configure(text=meta[0])
        self.dateLabel.configure(text=meta[1])

    def alert(self):
        CTkMessagebox.messagebox(title="Erro", 
                                 text="Houve um erro no processamento, tente refazer a solicitação")

    def _run(self):
        self.update_metadata()
        self.plot_classes(self.controller.get_plot_data())
        self.root.mainloop()
    
