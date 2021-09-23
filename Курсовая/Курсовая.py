import tkinter as tk
  
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x200')

  
def printInput():

    input_string = inputtxt.get(1.0, "end-1c")

    ru_dictionary = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю',
                 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    en_dictionary = ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'sch', "'", 'i', "'", 'e', 'yu',
                 'ya', 'A', 'B', 'V', 'G', 'D', 'E', 'YO', 'ZH', 'Z', 'I', 'Y', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'H', 'C', 'CH', 'SH', 'SCH', "'", 'I', "'", 'E', 'YU', 'YA']

    result = []

    for char in input_string:
        if char in ru_dictionary:
            ru_dictionary.index(char)
            result.append(en_dictionary[ru_dictionary.index(char)])
        elif char in en_dictionary:
            en_dictionary.index(char)
            result.append(ru_dictionary[en_dictionary.index(char)])
        else:
            result.append(char)
    result = ''.join(result)
    lbl.config(text = "Транслитерация: "+result)

inputtxt = tk.Text(frame,
                   height = 5,
                   width = 20)

inputtxt.pack()

printButton = tk.Button(frame,
                        text = "Старт", 
                        command = printInput)
printButton.pack()

lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()

