import tkinter as tk
from tkinter import messagebox, ttk


class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Calificaciones")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.students = {}

        # Estilo de fuente
        self.font_style = ("CASTELLAR", 10)

        # Widgets principales
        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y campos de entrada
        tk.Label(self.root, text="DNI:", font=self.font_style, bg="#f0f0f0").grid(row=0, column=0, padx=5, pady=5,
                                                                                  sticky="w")
        self.dni_entry = tk.Entry(self.root, font=self.font_style)
        self.dni_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Apellidos:", font=self.font_style, bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5,
                                                                                        sticky="w")
        self.surname_entry = tk.Entry(self.root, font=self.font_style)
        self.surname_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Nombre:", font=self.font_style, bg="#f0f0f0").grid(row=2, column=0, padx=5, pady=5,
                                                                                     sticky="w")
        self.name_entry = tk.Entry(self.root, font=self.font_style)
        self.name_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Nota:", font=self.font_style, bg="#f0f0f0").grid(row=3, column=0, padx=5, pady=5,
                                                                                   sticky="w")
        self.grade_entry = tk.Entry(self.root, font=self.font_style)
        self.grade_entry.grid(row=3, column=1, padx=5, pady=5)

        # Botones
        tk.Button(self.root, text="Introducir Alumno", font=self.font_style, command=self.add_student,
                  bg="#b3e5fc").grid(row=4, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Eliminar Alumno", font=self.font_style, command=self.delete_student,
                  bg="#ffcdd2").grid(row=4, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Consultar Alumno", font=self.font_style, command=self.query_student,
                  bg="#c8e6c9").grid(row=5, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Modificar Nota", font=self.font_style, command=self.modify_grade, bg="#ffcc80").grid(
            row=5, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Mostrar Alumnos", font=self.font_style, command=self.show_students,
                  bg="#d1c4e9").grid(row=6, column=0, padx=5, pady=5)
        tk.Button(self.root, text="Suspensos", font=self.font_style, command=self.show_failed, bg="#e1bee7").grid(row=6,
                                                                                                                  column=1,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        tk.Button(self.root, text="Aprobados", font=self.font_style, command=self.show_passed, bg="#b2dfdb").grid(row=7,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        tk.Button(self.root, text="MH", font=self.font_style, command=self.show_candidates_mh, bg="#ffe0b2").grid(row=7,
                                                                                                                  column=1,
                                                                                                                  padx=5,
                                                                                                                  pady=5)

    def calculate_calification(self, grade):
        if grade < 5:
            return "SS"
        elif grade < 7:
            return "AP"
        elif grade < 9:
            return "NT"
        else:
            return "SB"

    def add_student(self):
        dni = self.dni_entry.get()
        surname = self.surname_entry.get()
        name = self.name_entry.get()
        try:
            grade = float(self.grade_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Nota debe ser un número válido.")
            return

        if dni in self.students:
            messagebox.showerror("Error", "El DNI ya existe.")
            return

        self.students[dni] = {
            "surname": surname,
            "name": name,
            "grade": grade,
            "calification": self.calculate_calification(grade)
        }
        messagebox.showinfo("Éxito", "Alumno añadido correctamente.")

    def delete_student(self):
        dni = self.dni_entry.get()
        if dni in self.students:
            del self.students[dni]
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
        else:
            messagebox.showerror("Error", "DNI no encontrado.")

    def query_student(self):
        dni = self.dni_entry.get()
        if dni in self.students:
            student = self.students[dni]
            messagebox.showinfo("Consulta Alumno",
                                f"DNI: {dni}\nApellidos: {student['surname']}\nNombre: {student['name']}\nNota: {student['grade']}\nCalificación: {student['calification']}")
        else:
            messagebox.showerror("Error", "DNI no encontrado.")

    def modify_grade(self):
        dni = self.dni_entry.get()
        try:
            new_grade = float(self.grade_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Nota debe ser un número válido.")
            return

        if dni in self.students:
            self.students[dni]["grade"] = new_grade
            self.students[dni]["calification"] = self.calculate_calification(new_grade)
            messagebox.showinfo("Éxito", "Nota modificada correctamente.")
        else:
            messagebox.showerror("Error", "DNI no encontrado.")

    def show_students(self):
        output = "DNI\tAPELLIDOS, NOMBRE\tNOTA\tCALIFICACIÓN\n"
        for dni, data in self.students.items():
            output += f"{dni}\t{data['surname']}, {data['name']}\t{data['grade']}\t{data['calification']}\n"
        self.show_output(output)

    def show_failed(self):
        output = "Alumnos Suspensos:\n"
        for dni, data in self.students.items():
            if data['grade'] < 5:
                output += f"{dni}\t{data['surname']}, {data['name']}\t{data['grade']}\t{data['calification']}\n"
        self.show_output(output)

    def show_passed(self):
        output = "Alumnos Aprobados:\n"
        for dni, data in self.students.items():
            if data['grade'] >= 5:
                output += f"{dni}\t{data['surname']}, {data['name']}\t{data['grade']}\t{data['calification']}\n"
        self.show_output(output)

    def show_candidates_mh(self):
        output = "Candidatos a Matrícula de Honor:\n"
        for dni, data in self.students.items():
            if data['grade'] == 10:
                output += f"{dni}\t{data['surname']}, {data['name']}\t{data['grade']}\t{data['calification']}\n"
        self.show_output(output)

    def show_output(self, text):
        output_window = tk.Toplevel(self.root)
        output_window.title("Resultado")
        text_area = tk.Text(output_window, wrap=tk.WORD, width=80, height=20, font=self.font_style)
        text_area.insert(tk.END, text)
        text_area.config(state=tk.DISABLED)
        text_area.pack(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManager(root)
    root.mainloop()

