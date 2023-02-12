import tkinter as tk

window = tk.Tk()
text_box = tk.Text()
text_box.pack()

# text_box.get()
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     text_box.get()
# TypeError: Text.get() missing 1 required positional argument: 'index1'
# text_box.get("1.0")
# 'H'
# text_box.get("1.0", "1.7")
# 'Hello'
# text_box.get("2.0, 2.99")
# Traceback (most recent call last):
#   File "<pyshell#23>", line 1, in <module>
#     text_box.get("2.0, 2.99")
#   File "C:\Python311\Lib\tkinter\__init__.py", line 3767, in get
#     return self.tk.call(self._w, 'get', index1, index2)
# _tkinter.TclError: bad text index "2.0, 2.99"
# text_box.get("2.0", tk.END)
# 'World\n'
# text_box.get("1.0", tk.END)
# 'Hello\nWorld\n'
# text_box.delete("1.0")
# text_box.delete("1.0", "1.4")
# text_box.get("1.0")
# '\n'
# text_box.delete("1.0")
# text_box.delete("1.0", tk.END)
# text_box.insert("1.0", "Hello")
# text_box.insert("2.0", "\nWorld")
# text_box.insert(tk.END, "Put me at the end!")
# text_box.delete("2.0", tk.END)
# text_box.insert("2.0", "\nWorld")
# text_box.insert(tk.END, "\nPut me at the end!")
# text_box.destroy()
# window.destroy()
