import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")


root = customtkinter.CTk()
root.title("MES")
root.geometry("1500*1500")

"""
def login():

    if entry1.get() == "abc" and entry2.get() == "abc":
        print("1234")
"""

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="MES - Manufacturing Execution System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

tabview = customtkinter.CTkTabview(master=frame, width=870, height=500)
tabview.pack(pady=12, padx=10)

tab1 = tabview.add("Separador1")
tab2 = tabview.add("Separador2")
tab3 = tabview.add("Separador3")

Texto = customtkinter.CTkTextbox(master=tab1, width=650, height=450)
Texto.grid(row=0, column=0, padx=20, pady=20)
Texto.configure(state="normal")
Texto.insert("0.0", "Exemplo:\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod"
             + " tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
Texto.configure(state="disabled")

Right_Frame = customtkinter.CTkFrame(master=tab1, width=200, height=450)
Right_Frame.grid(row=0, column=1, padx=0, pady=0)

Check1 = customtkinter.CTkCheckBox(master=Right_Frame, text="Botão 1")
Check1.grid(row=0, column=0, padx=20, pady=20)

Check2 = customtkinter.CTkCheckBox(master=Right_Frame, text="Botão 2")
Check2.grid(row=1, column=0, padx=20, pady=20)

Check3 = customtkinter.CTkCheckBox(master=Right_Frame, text="Botão 3")
Check3.grid(row=2, column=0, padx=20, pady=20)

""""
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="******")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)
"""

root.mainloop()
