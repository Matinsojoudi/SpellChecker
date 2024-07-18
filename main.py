import nltk
import difflib
import tkinter as tk

nltk.download('words')
words = set(nltk.corpus.words.words())

def get_suggestions(misspelled_word):
    suggestions = difflib.get_close_matches(misspelled_word, words, n=7, cutoff=0.1)
    return suggestions

def update_suggestions(event):
    misspelled_word = misspelled_word_entry.get()
    suggestions = get_suggestions(misspelled_word)

    suggestions_listbox.delete(0, tk.END)
    for suggestion in suggestions:
        suggestions_listbox.insert(tk.END, suggestion)


def reset():
    misspelled_word_entry.delete(0, tk.END)  # Clear the misspelled word entry
    suggestions_listbox.delete(0, tk.END)  # Clear the suggestions listbox


window = tk.Tk()
window.title('Spell Checker')

misspelled_word_entry = tk.Entry(window, width=60, font="arial")
misspelled_word_entry.pack()
misspelled_word_entry.bind('<KeyRelease>', update_suggestions)

suggestions_listbox = tk.Listbox(window, width=60, font="arial")
suggestions_listbox.pack()

reset_button = tk.Button(window, text='Reset', command=reset, width=30, background="pink", font="arial")
reset_button.pack()

window.mainloop()
