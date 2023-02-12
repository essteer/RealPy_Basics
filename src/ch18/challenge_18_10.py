import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import random

def create_poem(nouns, verbs, adjectives, prepositions, adverbs):
    """Shuffles the chosen words into a random order,
    then creates a poem according to a template and
    assigns the result to the frm_poem labels."""
    random.shuffle(nouns)
    random.shuffle(verbs)
    random.shuffle(adjectives)
    random.shuffle(prepositions)
    random.shuffle(adverbs)

    if adjectives[0][0].lower() in "aeiou":
        opener = "An"
    else:
        opener = "A"

    lbl_poem["text"] = "Your poem:"
    lbl_poem_title["text"] = f"{opener} {adjectives[0].title()} {nouns[0].title()}"
    lbl_poem_text["text"] = f"""{opener} {adjectives[0]} {nouns[0]} {prepositions[0]} the {adjectives[1]} {nouns[1]}
{adverbs[0]}, the {nouns[0]} {verbs[1]}
the {nouns[1]} {verbs[2]} {prepositions[1]} a {adjectives[2]} {nouns[2]}"""


def error_check(nouns, verbs, adjectives, prepositions, adverbs):
    """Ensures the minimum of each word type has been entered.
    Returns an error message if not, otherwise calls create_poem()."""
    if len(nouns) < 3 or len(verbs) < 3 or len(adjectives) < 3 or len(prepositions) < 3 or len(adverbs) < 1:
        lbl_poem["text"] = "Error!"
        lbl_poem_title["text"] = "Please enter unique words only, with at least:"
        lbl_poem_text["text"] = "3 nouns\n3 verbs\n3 adjectives\n3 prepositions, and\n1 adverb."
    else:
        create_poem(nouns, verbs, adjectives, prepositions, adverbs)


def generate():
    """Sorts the user's words into lists by word type,
    then runs the error_check function on them."""
    nouns = list(set(ent_nouns.get().split(",")))
    verbs = list(set(ent_verbs.get().split(",")))
    adjectives = list(set(ent_adjectives.get().split(",")))
    prepositions = list(set(ent_prepositions.get().split(",")))
    adverbs = list(set(ent_adverbs.get().split(",")))

    error_check(nouns, verbs, adjectives, prepositions, adverbs)


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = f"{lbl_poem_title['text']}\n\n{lbl_poem_text['text']}"
        output_file.write(text)


window = tk.Tk()
window.title("Make your own poem!")
window.columnconfigure(0, minsize=500, weight=1)

lbl_instruction = tk.Label(window, text="Enter your word selections, separated by commas.")

frm_words = tk.Frame(window)
frm_words.columnconfigure(1, minsize=450, weight=1)

lbl_nouns = tk.Label(frm_words, text="Nouns: ")
ent_nouns = tk.Entry(frm_words)
lbl_verbs = tk.Label(frm_words, text="Verbs: ")
ent_verbs = tk.Entry(frm_words)
lbl_adjectives = tk.Label(frm_words, text="Adjectives: ")
ent_adjectives = tk.Entry(frm_words)
lbl_prepositions = tk.Label(frm_words, text="Prepositions: ")
ent_prepositions = tk.Entry(frm_words)
lbl_adverbs = tk.Label(frm_words, text="Adverbs: ")
ent_adverbs = tk.Entry(frm_words)

btn_generate = tk.Button(window, text="Generate", relief=tk.RAISED, padx=2, command=generate)

frm_poem = tk.Frame(window, relief=tk.SUNKEN, borderwidth=2)
frm_poem.columnconfigure(0, minsize=500, weight=1)
lbl_poem = tk.Label(frm_poem, text="")
lbl_poem_title = tk.Label(frm_poem, text="")
lbl_poem_text = tk.Label(frm_poem, text="")

btn_save = tk.Button(frm_poem, text="Save to file", relief=tk.RAISED, padx=2, command=save_file)

lbl_instruction.grid(row=0, column=0, pady=5, sticky="ew")
frm_words.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
lbl_nouns.grid(row=0, column=0, sticky="e")
ent_nouns.grid(row=0, column=1, sticky="ew")
lbl_verbs.grid(row=1, column=0, sticky="e")
ent_verbs.grid(row=1, column=1, sticky="ew")
lbl_adjectives.grid(row=2, column=0, sticky="e")
ent_adjectives.grid(row=2, column=1, sticky="ew")
lbl_prepositions.grid(row=3, column=0, sticky="e")
ent_prepositions.grid(row=3, column=1, sticky="ew")
lbl_adverbs.grid(row=4, column=0, sticky="e")
ent_adverbs.grid(row=4, column=1, sticky="ew")

btn_generate.grid(row=2, column=0, pady=5)

frm_poem.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
lbl_poem.grid(row=0, column=0, pady=5, sticky="ew")
lbl_poem_title.grid(row=1, column=0, pady=5, sticky="ew")
lbl_poem_text.grid(row=2, column=0, pady=5, sticky="ew")
btn_save.grid(row=3, column=0, pady=5)

window.mainloop()
