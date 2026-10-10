
import tkinter as tk

def logic_gate(gate, a, b=None):
    if gate == "AND":
        return a & b
    elif gate == "OR":
        return a | b
    elif gate == "NOT":
        return 1 - a
    elif gate == "NAND":
        return 1 - (a & b)
    elif gate == "NOR":
        return 1 - (a | b)
    elif gate == "XOR":
        return a ^ b
    elif gate == "XNOR":
        return 1 - (a ^ b)


def half_adder(a, b):
    return a ^ b, a & b


def full_adder(a, b, cin):
    total = a + b + cin
    return total % 2, total // 2


root = tk.Tk()
root.title("Digital Logic Simulator")
root.geometry("650x790")
root.configure(bg="#171923")

BG = "#171923"
PANEL = "#252a3a"
ACCENT = "#a78bfa"
TEXT = "#f4f4f5"
WIRE = "#a78bfa"

mode = tk.StringVar(value="AND")
a_value = tk.IntVar(value=0)
b_value = tk.IntVar(value=0)
cin_value = tk.IntVar(value=0)

tk.Label(
    root, text="DIGITAL LOGIC SIMULATOR",
    font=("Arial", 20, "bold"), bg=BG, fg=ACCENT
).pack(pady=(18, 4))

tk.Label(
    root, text="Interactive ECE Project",
    font=("Arial", 11), bg=BG, fg="#a1a1aa"
).pack(pady=(0, 12))

input_frame = tk.Frame(root, bg=PANEL, padx=15, pady=12)
input_frame.pack(fill="x", padx=25, pady=6)

tk.Label(
    input_frame, text="INPUTS",
    font=("Arial", 12, "bold"), bg=PANEL, fg=TEXT
).grid(row=0, column=0, columnspan=3, pady=(0, 8))


def toggle_input(variable, button):
    variable.set(1 - variable.get())
    button.config(text=str(variable.get()))
    calculate()


tk.Label(input_frame, text="A", bg=PANEL, fg=TEXT).grid(
    row=1, column=0, padx=35
)

a_button = tk.Button(
    input_frame, text="0", width=5,
    font=("Arial", 13, "bold"), bg=ACCENT, fg=BG,
    command=lambda: toggle_input(a_value, a_button)
)
a_button.grid(row=2, column=0, padx=35)

tk.Label(input_frame, text="B", bg=PANEL, fg=TEXT).grid(
    row=1, column=1, padx=35
)

b_button = tk.Button(
    input_frame, text="0", width=5,
    font=("Arial", 13, "bold"), bg=ACCENT, fg=BG,
    command=lambda: toggle_input(b_value, b_button)
)
b_button.grid(row=2, column=1, padx=35)

tk.Label(input_frame, text="Carry-in", bg=PANEL, fg=TEXT).grid(
    row=1, column=2, padx=35
)

cin_button = tk.Button(
    input_frame, text="0", width=5,
    font=("Arial", 13, "bold"), bg=ACCENT, fg=BG,
    command=lambda: toggle_input(cin_value, cin_button)
)
cin_button.grid(row=2, column=2, padx=35)

gate_frame = tk.Frame(root, bg=BG)
gate_frame.pack(pady=10)

tk.Label(
    gate_frame, text="SELECT A LOGIC GATE",
    font=("Arial", 12, "bold"), bg=BG, fg=TEXT
).pack(pady=(0, 7))

gate_buttons = tk.Frame(gate_frame, bg=BG)
gate_buttons.pack()


def select_mode(new_mode):
    mode.set(new_mode)
    calculate()


gates = ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"]

for i, gate in enumerate(gates):
    tk.Button(
        gate_buttons, text=gate, width=8,
        bg=PANEL, fg=TEXT, activebackground=ACCENT,
        command=lambda g=gate: select_mode(g)
    ).grid(row=i // 4, column=i % 4, padx=4, pady=4)

tk.Label(
    root, text="OR SELECT AN ADDER",
    font=("Arial", 12, "bold"), bg=BG, fg=TEXT
).pack(pady=(5, 7))

adder_frame = tk.Frame(root, bg=BG)
adder_frame.pack()

tk.Button(
    adder_frame, text="Half Adder", width=15,
    bg="#374151", fg=TEXT,
    command=lambda: select_mode("HALF ADDER")
).grid(row=0, column=0, padx=6)

tk.Button(
    adder_frame, text="Full Adder", width=15,
    bg="#374151", fg=TEXT,
    command=lambda: select_mode("FULL ADDER")
).grid(row=0, column=1, padx=6)

diagram_frame = tk.Frame(root, bg=PANEL)
diagram_frame.pack(fill="x", padx=25, pady=12)

tk.Label(
    diagram_frame, text="CIRCUIT DIAGRAM",
    font=("Arial", 12, "bold"), bg=PANEL, fg=TEXT
).pack(pady=(8, 2))

canvas = tk.Canvas(
    diagram_frame, width=560, height=165,
    bg=PANEL, highlightthickness=0
)
canvas.pack(padx=5, pady=5)


def draw_circuit():
    canvas.delete("all")

    selected = mode.get()
    a = a_value.get()
    b = b_value.get()
    cin = cin_value.get()

    if selected == "HALF ADDER":
        canvas.create_text(
            280, 18, text="HALF ADDER",
            fill=ACCENT, font=("Arial", 12, "bold")
        )

        canvas.create_text(55, 57, text=f"A = {a}", fill=TEXT)
        canvas.create_text(55, 105, text=f"B = {b}", fill=TEXT)

        for y in [57, 105]:
            canvas.create_line(85, y, 175, y, fill=WIRE, width=2)

        canvas.create_rectangle(
            175, 35, 275, 75, outline=TEXT, width=2
        )
        canvas.create_text(
            225, 55, text="XOR",
            fill=TEXT, font=("Arial", 11, "bold")
        )

        canvas.create_rectangle(
            175, 90, 275, 130, outline=TEXT, width=2
        )
        canvas.create_text(
            225, 110, text="AND",
            fill=TEXT, font=("Arial", 11, "bold")
        )

        canvas.create_line(275, 55, 340, 55, fill=WIRE, width=2)
        canvas.create_line(275, 110, 340, 110, fill=WIRE, width=2)

        s, c = half_adder(a, b)

        canvas.create_text(
            405, 55, text=f"SUM = {s}",
            fill=ACCENT, font=("Arial", 11, "bold")
        )
        canvas.create_text(
            405, 110, text=f"CARRY = {c}",
            fill=ACCENT, font=("Arial", 11, "bold")
        )

    elif selected == "FULL ADDER":
        canvas.create_text(
            280, 18, text="FULL ADDER",
            fill=ACCENT, font=("Arial", 12, "bold")
        )

        canvas.create_text(55, 48, text=f"A = {a}", fill=TEXT)
        canvas.create_text(55, 82, text=f"B = {b}", fill=TEXT)
        canvas.create_text(55, 116, text=f"Cin = {cin}", fill=TEXT)

        for y in [48, 82, 116]:
            canvas.create_line(85, y, 165, y, fill=WIRE, width=2)

        canvas.create_rectangle(
            165, 35, 275, 130, outline=TEXT, width=2
        )
        canvas.create_text(
            220, 82, text="FULL\nADDER",
            fill=TEXT, font=("Arial", 11, "bold")
        )

        canvas.create_line(275, 65, 340, 65, fill=WIRE, width=2)
        canvas.create_line(275, 105, 340, 105, fill=WIRE, width=2)

        s, c = full_adder(a, b, cin)

        canvas.create_text(
            425, 65, text=f"SUM = {s}",
            fill=ACCENT, font=("Arial", 11, "bold")
        )
        canvas.create_text(
            425, 105, text=f"CARRY = {c}",
            fill=ACCENT, font=("Arial", 10, "bold")
        )

    else:
        canvas.create_text(
            30, 48, text=f"A={a}",
            fill=TEXT, font=("Arial", 10)
        )
        canvas.create_line(55, 52, 180, 52, fill=WIRE, width=2)

        if selected == "NOT":
            canvas.create_polygon(
                180, 30, 180, 75, 235, 52,
                outline=TEXT, fill="#374151", width=2
            )
            canvas.create_oval(
                232, 47, 242, 57, outline=TEXT, width=2
            )
            canvas.create_text(
                200, 52, text="NOT", fill=TEXT,
                font=("Arial", 8)
            )
            canvas.create_line(242, 52, 400, 52, fill=WIRE, width=2)
            result = logic_gate("NOT", a)

        else:
            canvas.create_text(
                30, 108, text=f"B={b}",
                fill=TEXT, font=("Arial", 10)
            )
            canvas.create_line(55, 108, 180, 108, fill=WIRE, width=2)

            canvas.create_rectangle(
                180, 30, 285, 125, outline=TEXT, width=2
            )
            canvas.create_text(
                232, 77, text=selected,
                fill=TEXT, font=("Arial", 11, "bold")
            )
            canvas.create_line(285, 77, 400, 77, fill=WIRE, width=2)
            result = logic_gate(selected, a, b)

        canvas.create_text(
            460, 52 if selected == "NOT" else 77,
            text=f"OUT = {result}",
            fill=ACCENT, font=("Arial", 11, "bold")
        )


output_frame = tk.Frame(root, bg=PANEL, padx=15, pady=10)
output_frame.pack(fill="x", padx=25, pady=(0, 12))

tk.Label(
    output_frame, text="OUTPUT",
    font=("Arial", 11, "bold"), bg=PANEL, fg="#a1a1aa"
).pack()

result_label = tk.Label(
    output_frame, text="Select a gate to begin",
    font=("Arial", 16, "bold"), bg=PANEL, fg=ACCENT
)
result_label.pack(pady=6)


def calculate():
    a = a_value.get()
    b = b_value.get()
    cin = cin_value.get()
    selected = mode.get()

    if selected == "HALF ADDER":
        s, c = half_adder(a, b)
        result_label.config(text=f"SUM = {s}     CARRY = {c}")

    elif selected == "FULL ADDER":
        s, c = full_adder(a, b, cin)
        result_label.config(text=f"SUM = {s}     CARRY-OUT = {c}")

    elif selected == "NOT":
        result = logic_gate("NOT", a)
        result_label.config(text=f"NOT {a} = {result}")

    else:
        result = logic_gate(selected, a, b)
        result_label.config(text=f"{a} {selected} {b} = {result}")

    draw_circuit()


for variable in (a_value, b_value, cin_value):
    variable.trace_add("write", lambda *_: calculate())

calculate()
root.mainloop()
