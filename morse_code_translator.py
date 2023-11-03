import tkinter as tk

morse_code_dict = {
    'A': '.-', 'N': '-.', '0': '-----',
    'B': '-...', 'O': '---', '1': '.----',
    'C': '-.-.', 'P': '.--.', '2': '..---',
    'D': '-..', 'Q': '--.-', '3': '...--',
    'E': '.', 'R': '.-.', '4': '....-',
    'F': '..-.', 'S': '...', '5': '.....',
    'G': '--.', 'T': '-', '6': '-....',
    'H': '....', 'U': '..-', '7': '--...',
    'I': '..', 'V': '...-', '8': '---..',
    'J': '.---', 'W': '.--', '9': '----.',
    'K': '-.-', 'X': '-..-',
    'L': '.-..', 'Y': '-.--',
    'M': '--', 'Z': '--..',
    ' ': ' '
}

reverse_morse_dict = {v: k for k, v in morse_code_dict.items()}

def english_to_morse():
    text = input_text.get().upper()
    morse_text = ''

    for char in text:
        if char in morse_code_dict:
            morse_text += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_text += ' '
        else:
            morse_text += '# '

    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, morse_text)
    output_text.config(state=tk.DISABLED)

def morse_to_english():
    text = input_text.get()
    english_text = ''

    morse_characters = text.split(' ')
    for morse_char in morse_characters:
        if morse_char in reverse_morse_dict:
            english_text += reverse_morse_dict[morse_char]
        elif morse_char == '':
            english_text += ' '
        else:
            english_text += '# '

    output_text.config(state=tk.NORMAL)
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, english_text)
    output_text.config(state=tk.DISABLED)

def clear_input():
    input_text.set("")

app = tk.Tk()
app.title("Morse Code Translator")

input_text = tk.StringVar()
input_label = tk.Label(app, text="Enter Text:", font=("Arial", 16))
input_entry = tk.Entry(app, textvariable=input_text, font=("Arial", 16))
input_label.pack()
input_entry.pack()

output_label = tk.Label(app, text="Translation:", font=("Arial", 16))
output_label.pack()

output_text = tk.Text(app, wrap=tk.WORD, font=("Arial", 14), height=5, width=40)
output_text.pack()
output_text.config(state=tk.DISABLED)

delete_button = tk.Button(app, text="Delete", command=clear_input, font=("Arial", 14))
delete_button.pack()

to_morse_button = tk.Button(app, text="English to Morse", command=english_to_morse, font=("Arial", 14))
to_english_button = tk.Button(app, text="Morse to English", command=morse_to_english, font=("Arial", 14))
to_morse_button.pack()
to_english_button.pack()

app.mainloop()
