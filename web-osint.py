
import webbrowser
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Cliquez sur un bouton pour ouvrir une page web :")
        self.label.pack(side="top")

        self.google_button = tk.Button(self, text="Google", command=self.open_google)
        self.google_button.pack(side="left")

        self.github_Gdork_button = tk.Button(self, text="Github Gist", command=self.open_github_gdork)
        self.github_Gdork_button.pack(side="left")

        self.idcrawl_button = tk.Button(self, text="IDCrawl", command=self.open_idcrawl)
        self.idcrawl_button.pack(side="left")

        self.usersearch_button = tk.Button(self, text="Usersearch.org", command=self.open_usersearch)
        self.usersearch_button.pack(side="left")

        self.socialsearcher_button = tk.Button(self, text="Social Searcher", command=self.open_socialsearcher)
        self.socialsearcher_button.pack(side="left")

        self.ipapi_button = tk.Button(self, text="IP API", command=self.open_ipapi)
        self.ipapi_button.pack(side="left")

        self.DNSLookup_button = tk.Button(self, text="DNS Lookup", command=self.open_DNSLookup)
        self.DNSLookup_button.pack(side="left")

        self.blackbirdosint_button = tk.Button(self, text="blackbird-osint", command=self.open_blackbirdosint)
        self.blackbirdosint_button.pack(side="left")

    def open_google(self):
        webbrowser.open("https://www.google.com")

    def open_idcrawl(self):
        webbrowser.open("https://www.idcrawl.com")

    def open_usersearch(self):
        webbrowser.open("https://www.usersearch.org")

    def open_github_gdork(self):
        webbrowser.open("https://gist.github.com/ikuamike/c2611b171d64b823c1c1956129cbc055")

    def open_socialsearcher(self):
        webbrowser.open("https://www.social-searcher.com")

    def open_ipapi(self):
        webbrowser.open("https://ipapi.co")

    def open_DNSLookup(self):
        webbrowser.open("https://mxtoolbox.com/DNSLookup.aspx")

    def open_blackbirdosint(self):
        webbrowser.open("https://blackbird-osint.herokuapp.com")


root = tk.Tk()
app = Application(master=root)
app.mainloop()

