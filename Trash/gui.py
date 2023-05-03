import customtkinter


def run_gui():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.title("MES")
    root.geometry("1500*1500")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="MES - Manufacturing Execution System", font=("Roboto", 24))
    label.pack(pady=12, padx=10)

    tabview = customtkinter.CTkTabview(master=frame, width=870, height=500)
    tabview.pack(pady=12, padx=10)

    tab1 = tabview.add("Separador1")
#    tab2 = tabview.add("Separador2")
#    tab3 = tabview.add("Separador3")

    texto = customtkinter.CTkTextbox(master=tab1, width=650, height=450)
    texto.grid(row=0, column=0, padx=20, pady=20)
    texto.configure(state="normal")
    texto.insert("0.0",
                 "Exemplo:\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod"
                 + " tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
    texto.configure(state="disabled")

    right_frame = customtkinter.CTkFrame(master=tab1, width=200, height=450)
    right_frame.grid(row=0, column=1, padx=0, pady=0)

    check1 = customtkinter.CTkCheckBox(master=right_frame, text="Botão 1")
    check1.grid(row=0, column=0, padx=20, pady=20)

    check2 = customtkinter.CTkCheckBox(master=right_frame, text="Botão 2")
    check2.grid(row=1, column=0, padx=20, pady=20)

    check3 = customtkinter.CTkCheckBox(master=right_frame, text="Botão 3")
    check3.grid(row=2, column=0, padx=20, pady=20)

    root.mainloop()


run_gui()
