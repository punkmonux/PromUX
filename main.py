import tkinter as tk
import webbrowser

class PromotionsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Promotions Poster")

        self.groups = [
            "https://www.facebook.com/groups/1958989727511924/",
            "https://www.facebook.com/groups/517573795083336/",
            "https://www.facebook.com/groups/3086374944729173/",
            "https://www.facebook.com/groups/3196795953684516/",
            "https://www.facebook.com/groups/TEZIUTLAN/",
            "https://www.facebook.com/groups/472789587464923/",
            "https://www.facebook.com/groups/258131232555019/",
            "https://www.facebook.com/groups/1414095748868473/",
            "https://www.facebook.com/groups/193412577513204/",
            "https://www.facebook.com/groups/703059000633435/",
            "https://www.facebook.com/groups/567054217887678/",
            "https://www.facebook.com/groups/489180201136536/",
            "https://www.facebook.com/groups/471433513423613/",
            "https://www.facebook.com/groups/518518709154751/",
            "https://www.facebook.com/groups/2240298862900776/",
            "https://www.facebook.com/groups/mercadolibrenanchital/",
            "https://www.facebook.com/groups/273084012884574/",
            "https://www.facebook.com/groups/2916423398603002/",
            "https://www.facebook.com/groups/1640601779554055/",
            "https://www.facebook.com/groups/640502536071874/",
            "https://www.facebook.com/groups/663281898229744/",
            "https://www.facebook.com/groups/2187624217958656/",
            "https://www.facebook.com/groups/610766779807418/",
            "https://www.facebook.com/groups/382211381889233/",
            "https://www.facebook.com/groups/mi.ofertam/",
            "https://www.facebook.com/groups/651064371620552/",
            "https://www.facebook.com/groups/661584247198242/",
            "https://www.facebook.com/groups/4820640774679553/",
            "https://www.facebook.com/groups/VENTAYCOMPRAMORELOS/",
            "https://www.facebook.com/groups/866533960859908/",
            "https://www.facebook.com/groups/211154932755117/",
            "https://www.facebook.com/groups/881622649007432/",
            "https://www.facebook.com/groups/715076862414504/",
            "https://www.facebook.com/groups/ventasacapulco1/",
            "https://www.facebook.com/groups/123546577837087/",
            "https://www.facebook.com/groups/161988497319820/",
            "https://www.facebook.com/groups/1049700088377670/",
            "https://www.facebook.com/groups/2944944222410318/",
            "https://www.facebook.com/groups/1193452111001561/",
            "https://www.facebook.com/groups/1451474725020656/",
            "https://www.facebook.com/groups/201327830050955/",
            "https://www.facebook.com/groups/211624434445061/",
            "https://www.facebook.com/groups/196416564641469/",
            "https://www.facebook.com/groups/402236344858662/",
            "https://www.facebook.com/groups/1594456500699127/",
            "https://www.facebook.com/groups/2451070698356554/",
            "https://www.facebook.com/groups/ventasfuentesdesatelite/",
            "https://www.facebook.com/groups/525766157628821/",
            "https://www.facebook.com/groups/245387866546471/",
            "https://www.facebook.com/groups/757223334826884/",
            "https://www.facebook.com/groups/1109868969847872/",
            "https://www.facebook.com/groups/960035994008352/",
            "https://www.facebook.com/groups/1227211657711943/",
            "https://www.facebook.com/groups/389066588844167/",
            "https://www.facebook.com/groups/2044735702275689/",
            "https://www.facebook.com/groups/565195583605413/",
            "https://www.facebook.com/groups/1745072785620199/",
            "https://www.facebook.com/groups/2268316790073614/",
            "https://www.facebook.com/groups/655945524419766/",
            "https://www.facebook.com/groups/125094894506339/",
            "https://www.facebook.com/groups/537865274045534/",
            "https://www.facebook.com/groups/455083401353725/",
            "https://www.facebook.com/groups/464333674944345/",
            "https://www.facebook.com/groups/658687161365379/",
            "https://www.facebook.com/groups/745561112771821/",
            "https://www.facebook.com/groups/943167349833691/",
            "https://www.facebook.com/groups/197296447752180/",
            "https://www.facebook.com/groups/1270405566459999/",
            "https://www.facebook.com/groups/108847746166801/",
            "https://www.facebook.com/groups/1863499457030727/",
            "https://www.facebook.com/groups/463916651456051/",
            "https://www.facebook.com/groups/1033712590063539/",
            "https://www.facebook.com/groups/479848360590409/",
            "https://www.facebook.com/groups/3684239794967211/",
            "https://www.facebook.com/groups/175604546314427/",
            "https://www.facebook.com/groups/233701947881730/",
            "https://www.facebook.com/groups/1856529777961235/",
            "https://www.facebook.com/groups/4601758329897967/",
            "https://www.facebook.com/groups/539051346666703/",
            "https://www.facebook.com/groups/236428303462448/",
            "https://www.facebook.com/groups/160727912261026/",
            "https://www.facebook.com/groups/351168223495737/",
            "https://www.facebook.com/groups/1236605683435231/",
            "https://www.facebook.com/groups/2848977448695074/",
            "https://www.facebook.com/groups/675479345907448/",
            "https://www.facebook.com/groups/2884249151691064/",
            "https://www.facebook.com/groups/615459799885757/",
        ]

        self.total_groups = len(self.groups)
        self.current_group_index = 0

        # Etiqueta para mostrar el número de grupo y el total de grupos
        self.label = tk.Label(root, text="Grupo #" + str(self.current_group_index + 1) + " de " + str(self.total_groups))
        self.label.pack(pady=20)

        # Botón para abrir el grupo actual
        self.open_button = tk.Button(root, text="Abrir Grupo", command=self.open_group)
        self.open_button.pack(pady=10)

        # Botón para abrir el siguiente grupo
        self.open_next_button = tk.Button(root, text="Abrir Siguiente", command=self.open_next_group)
        self.open_next_button.pack(pady=10)

        # Botón para salir de la aplicación
        self.quit_button = tk.Button(root, text="Salir", command=self.quit_app)
        self.quit_button.pack(pady=10)

    def open_next_group(self):
        # Verificar si hay enlaces restantes en la lista
        if self.current_group_index < len(self.groups) - 1:
            # Incrementar el índice para cargar el siguiente enlace
            self.current_group_index += 1
            # Actualizar el número de grupo en la etiqueta
            self.label.config(text="Grupo #" + str(self.current_group_index + 1))
            # Abrir el enlace en una nueva pestaña del navegador
            webbrowser.open_new_tab(self.groups[self.current_group_index])
        else:
            print("No hay más enlaces para abrir.")

    def open_group(self):
        webbrowser.open_new_tab(self.groups[self.current_group_index])

    def load_next_group(self):
        self.current_group_index += 1
        if self.current_group_index >= len(self.groups):
            self.current_group_index = 0
        # Actualizar el número de grupo en la etiqueta
        self.label.config(text="Grupo #" + str(self.current_group_index + 1))
        print("Cargando siguiente grupo:", self.groups[self.current_group_index])

    def quit_app(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = PromotionsApp(root)
    root.mainloop()
