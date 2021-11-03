from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import algorithms
import generators
import tools


class Asymmetrix:

    def __init__(self, root):

        root.title('Asymmetrix')

        self.mainframe = ttk.Frame(root, padding='3 3 12 12')
        self.mainframe.grid(column=0, row=0)

        self.algtask_frame = ttk.Frame(self.mainframe)
        self.algtask_frame.grid(row=10, column=10)

        # self.draw_generator_frame()
        self.draw_input_frame()
        self.draw_algorithm_frame()
        self.draw_task_frame()
        self.draw_property_a_frame()
        self.draw_property_b_frame()
        self.draw_property_c_frame()
        self.draw_property_d_frame()
        self.draw_action_frame()
        self.draw_output_frame()

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=4, pady=4)

        for child in self.algtask_frame.winfo_children():
            child.grid_configure(padx=4)

        self.update_properties()

    def draw_input_frame(self):

        self.input_frame = ttk.Labelframe(self.mainframe, text='Input')
        self.input_frame.grid(row=5, column=10)

        self.input_buttons_frame = ttk.Frame(self.input_frame)
        self.input_buttons_frame.grid(row=5, column=10, sticky='we')

        self.open_file_button = ttk.Button(
            self.input_buttons_frame, text="Open file...", command=self.open_file)
        self.open_file_button.grid(row=5, column=10, sticky='w')

        self.clear_input_button = ttk.Button(
            self.input_buttons_frame, text="Clear input", command=self.update_input)
        self.clear_input_button.grid(row=5, column=20, sticky='w')

        self.input_text = Text(self.input_frame, height=3, width=80)
        self.input_text.grid(row=10, column=10, sticky='we')

        for child in self.input_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def open_file(self):
        self.open_filename = filedialog.askopenfile()

        self.update_input(content=self.open_filename.read())

    def draw_algorithm_frame(self):

        self.algorithm_frame = ttk.Labelframe(
            self.algtask_frame, text='Algorithm')
        self.algorithm_frame.grid(row=10, column=10)

        self.algorithm_var = StringVar()
        self.algorithm_var.set('rsa')

        self.rsa_radio = ttk.Radiobutton(
            self.algorithm_frame, text='RSA', variable=self.algorithm_var, value='rsa', command=self.update_properties)
        self.elgamal_radio = ttk.Radiobutton(
            self.algorithm_frame, text='ElGamal', variable=self.algorithm_var, value='elgamal', command=self.update_properties)
        self.paillier_radio = ttk.Radiobutton(
            self.algorithm_frame, text='Paillier', variable=self.algorithm_var, value='paillier', command=self.update_properties)
        self.ecc_radio = ttk.Radiobutton(
            self.algorithm_frame, text='ECC', variable=self.algorithm_var, value='ecc', command=self.update_properties)

        self.rsa_radio.grid(row=0, column=0, sticky='nw')
        self.elgamal_radio.grid(row=0, column=1, sticky='nw')
        self.paillier_radio.grid(row=0, column=2, sticky='nw')
        self.ecc_radio.grid(row=0, column=3, sticky='nw')

        self.ecc_radio.state(['disabled'])

        for child in self.algorithm_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_task_frame(self):

        self.task_frame = ttk.Labelframe(self.algtask_frame, text='Task')
        self.task_frame.grid(row=10, column=20)

        self.task_var = StringVar()
        self.task_var.set('encrypt')

        self.encrypt_radio = ttk.Radiobutton(
            self.task_frame, text='Encrypt', variable=self.task_var, value='encrypt', command=self.update_properties)
        self.decrypt_radio = ttk.Radiobutton(
            self.task_frame, text='Decrypt', variable=self.task_var, value='decrypt', command=self.update_properties)
        self.generate_key_radio = ttk.Radiobutton(
            self.task_frame, text='Generate Key', variable=self.task_var, value='generate', command=self.update_properties)

        self.encrypt_radio.grid(row=0, column=0, sticky='nw')
        self.decrypt_radio.grid(row=0, column=1, sticky='nw')
        self.generate_key_radio.grid(row=0, column=2, sticky='nw')

        for child in self.task_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def update_properties(self):
        self.property_a_frame.grid_remove()
        self.property_b_frame.grid_remove()
        self.property_c_frame.grid_remove()
        self.property_d_frame.grid_remove()

        mode = self.task_var.get()
        algorithm = self.algorithm_var.get()

        if algorithm == 'rsa':
            if mode == 'encrypt':
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_a_frame['text'] = 'e (encryption key)'
                self.property_b_frame['text'] = 'n'
            elif mode == 'decrypt':
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_a_frame['text'] = 'd (decryption key)'
                self.property_b_frame['text'] = 'n'
            else:
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_a_frame['text'] = 'p'
                self.property_b_frame['text'] = 'q'

        elif algorithm == 'elgamal':
            if mode == 'encrypt':
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_c_frame.grid()
                self.property_d_frame.grid()
                self.property_a_frame['text'] = 'y (public key)'
                self.property_b_frame['text'] = 'g'
                self.property_c_frame['text'] = 'p'
                self.property_d_frame['text'] = 'k'
            elif mode == 'decrypt':
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_c_frame.grid()
                self.property_a_frame['text'] = 'a --- [for b, put in Input box above]'
                self.property_b_frame['text'] = 'x (private key)'
                self.property_c_frame['text'] = 'p'
            else:
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_c_frame.grid()
                self.property_a_frame['text'] = 'p'
                self.property_b_frame['text'] = 'g'
                self.property_c_frame['text'] = 'x'
        elif algorithm == 'paillier':
            if mode == 'encrypt':
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_c_frame.grid()
                self.property_a_frame['text'] = 'g'
                self.property_b_frame['text'] = 'n'
                self.property_c_frame['text'] = 'r'
            elif mode == 'decrypt':
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_c_frame.grid()
                self.property_a_frame['text'] = 'λ'
                self.property_b_frame['text'] = 'μ'
                self.property_c_frame['text'] = 'n'
            else:
                self.property_a_frame.grid()
                self.property_b_frame.grid()
                self.property_c_frame.grid()
                self.property_a_frame['text'] = 'p'
                self.property_b_frame['text'] = 'q'
                self.property_c_frame['text'] = 'g'

    def draw_property_a_frame(self):

        self.property_a_frame = ttk.Labelframe(
            self.mainframe, text='Property A')
        self.property_a_frame.grid(row=31, column=10)

        self.property_a_text = Text(self.property_a_frame, height=2, width=80)
        self.property_a_text.grid(row=10, column=10, sticky='we')

        for child in self.property_a_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_property_b_frame(self):

        self.property_b_frame = ttk.Labelframe(
            self.mainframe, text='Property B')
        self.property_b_frame.grid(row=32, column=10)

        self.property_b_text = Text(self.property_b_frame, height=2, width=80)
        self.property_b_text.grid(row=10, column=10, sticky='we')

        for child in self.property_b_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_property_c_frame(self):

        self.property_c_frame = ttk.Labelframe(
            self.mainframe, text='Property C')
        self.property_c_frame.grid(row=33, column=10)

        self.property_c_text = Text(self.property_c_frame, height=2, width=80)
        self.property_c_text.grid(row=10, column=10, sticky='we')

        for child in self.property_c_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_property_d_frame(self):

        self.property_d_frame = ttk.Labelframe(
            self.mainframe, text='Property D')
        self.property_d_frame.grid(row=34, column=10)

        self.property_d_text = Text(self.property_d_frame, height=2, width=80)
        self.property_d_text.grid(row=10, column=10, sticky='we')

        for child in self.property_d_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def draw_action_frame(self):
        self.action_frame = ttk.Frame(self.mainframe)
        self.action_frame.grid(row=40, column=10)

        ttk.Separator(self.action_frame).grid(row=10, column=10, pady=16)

        self.start_button = ttk.Button(
            self.action_frame, text='START', command=self.action_start)
        self.start_button.grid(row=20, column=10)

    def draw_output_frame(self):

        self.output_frame = ttk.Labelframe(self.mainframe, text='Output')
        self.output_frame.grid(row=80, column=10)

        self.output_text = Text(self.output_frame, height=3, width=80)
        self.output_text.grid(row=10, column=10, sticky='we')

        for child in self.output_frame.winfo_children():
            child.grid_configure(padx=8, pady=8)

    def update_input(self, content='', enabled=True):
        self.input_text.delete('1.0', END)
        self.input_text.insert('1.0', content)

    def update_output(self, content='', enabled=True):
        self.output_text.delete('1.0', END)
        self.output_text.insert('1.0', content)

    def action_start(self):
        self.input_content = self.input_text.get('1.0', END)
        self.property_a_content = tools.str_to_int(
            self.property_a_text.get('1.0', END))
        self.property_b_content = tools.str_to_int(
            self.property_b_text.get('1.0', END))
        self.property_c_content = tools.str_to_int(
            self.property_c_text.get('1.0', END))
        self.property_d_content = tools.str_to_int(
            self.property_d_text.get('1.0', END))

        mode = self.task_var.get()
        algorithm = self.algorithm_var.get()

        if (algorithm == 'rsa'):
            if (mode == 'encrypt'):
                self.output_content = algorithms.rsa_encrypt(
                    self.input_content, self.property_a_content, self.property_b_content)
            elif (mode == 'decrypt'):
                self.output_content = algorithms.rsa_decrypt(
                    self.input_content, self.property_a_content, self.property_b_content)
            else:
                self.output_content = generators.rsa_generate(
                    self.property_a_content, self.property_b_content)
        elif (algorithm == 'elgamal'):
            if (mode == 'encrypt'):
                self.output_content = algorithms.elgamal_encrypt(
                    self.input_content, self.property_a_content, self.property_b_content, self.property_c_content, self.property_d_content)
            elif (mode == 'decrypt'):
                self.output_content = algorithms.elgamal_decrypt(
                    self.property_a_content, self.input_content, self.property_b_content, self.property_c_content)
            else:
                self.output_content = generators.elgamal_generate(
                    self.property_a_content, self.property_b_content, self.property_c_content)
        elif (algorithm == 'paillier'):
            if (mode == 'encrypt'):
                self.output_content = algorithms.paillier_encrypt(
                    self.input_content, self.property_a_content, self.property_b_content, self.property_c_content)
            elif (mode == 'decrypt'):
                self.output_content = algorithms.paillier_decrypt(
                    self.input_content, self.property_a_content,  self.property_b_content, self.property_c_content)
            else:
                self.output_content = generators.paillier_generate(
                    self.property_a_content, self.property_b_content, self.property_c_content)

        self.update_output(content=self.output_content)


root = Tk()
Asymmetrix(root)
root.mainloop()
