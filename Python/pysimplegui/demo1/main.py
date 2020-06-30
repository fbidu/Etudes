import PySimpleGUI as sg
layout = [[sg.Text("Hey, yo!")], [sg.Button("OK")]]

window = sg.Window("Hey!!", layout)

while True:
    event, values = window.read()

    if event == "OK":
        print("Ok to you too, dear user!")

window.close()
