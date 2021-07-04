import PySimpleGUI

layout = [[PySimpleGUI.Text('Hello World')], [PySimpleGUI.Button('Ok')]]

# Create the window
window = PySimpleGUI.Window('Demo', layout)

while True:
    event, value = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == 'Ok' or event == PySimpleGUI.WIN_CLOSED:
        break

window.close()