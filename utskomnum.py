from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (1, 0.694, 1) 

# --- Fungsi matematika ---
def f(x):
    return x**4 - 5*x**2 + 4

def f_prim(x):
    return 4*x**3 - 10*x

class NewtonLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # --- Bagian input parameter ---
        input_layout = GridLayout(cols=2, row_default_height=35, size_hint_y=0.25, spacing=5)

        # Label dan input sejajar
        input_layout.add_widget(Label(text="x₀:", color=(0, 0, 0), font_size=16, halign="right"))
        self.x0_input = TextInput(text='2.1', multiline=False, size_hint_y=None, height=30,
                                  background_color=(0.949, 0.494, 0.820, 1), foreground_color=(0, 0, 0))
        input_layout.add_widget(self.x0_input)

        input_layout.add_widget(Label(text="ε (toleransi):", color=(0, 0, 0), font_size=16, halign="right"))
        self.e_input = TextInput(text='0.001', multiline=False, size_hint_y=None, height=30,
                                 background_color=(0.949, 0.494, 0.820, 1), foreground_color=(0, 0, 0))
        input_layout.add_widget(self.e_input)

        input_layout.add_widget(Label(text="n (maks iterasi):", color=(0, 0, 0), font_size=16, halign="right"))
        self.n_input = TextInput(text='10', multiline=False, size_hint_y=None, height=30,
                                 background_color=(0.949, 0.494, 0.820, 1), foreground_color=(0, 0, 0))
        input_layout.add_widget(self.n_input)

        self.add_widget(input_layout)

        # --- Tombol hitung ---
        self.calc_button = Button(
            text="🔹 Hitung Akar (Newton-Raphson)",
            size_hint=(1, 0.1),
            background_color=(0.949, 0.494, 0.820, 1),
            color=(1, 1, 1),
            font_size=16
        )
        self.calc_button.bind(on_press=self.hitung)
        self.add_widget(self.calc_button)

        # --- Area hasil (besar di bawah, dengan tabel) ---
        self.result_layout = GridLayout(cols=5, spacing=4, size_hint_y=None)
        self.result_layout.bind(minimum_height=self.result_layout.setter('height'))

        # Scroll view untuk tabel
        scroll = ScrollView(size_hint=(1, 0.65))
        scroll.add_widget(self.result_layout)
        self.add_widget(scroll)

    def clear_table(self):
        self.result_layout.clear_widgets()

    def add_header(self):
        headers = ["Iterasi", "xᵢ", "f(xᵢ)", "f'(xᵢ)", "|xᵢ₊₁−xᵢ|"]
        for h in headers:
            self.result_layout.add_widget(Label(
                text=f"[b]{h}[/b]",
                markup=True,
                color=(0, 0, 0),
                size_hint_y=None,
                height=30
            ))

    def add_row(self, data, color=(0, 0, 0)):
        for val in data:
            self.result_layout.add_widget(Label(
                text=str(val),
                color=color,
                font_size=14,
                size_hint_y=None,
                height=25
            ))

    def hitung(self, instance):
        try:
            x0 = float(self.x0_input.text)
            e = float(self.e_input.text)
            n = int(self.n_input.text)
        except ValueError:
            self.clear_table()
            self.add_row([" Input tidak valid"], color=(0, 0, 0))
            return

        self.clear_table()
        self.add_header()

        for i in range(1, n + 1):
            fx = f(x0)
            fpx = f_prim(x0)

            if fpx == 0:
                self.add_row([f"Turunan nol di iterasi {i}"], color=(0, 0, 0))
                break

            x1 = x0 - (fx / fpx)
            selisih = abs(x1 - x0)

            self.add_row([
                i,
                f"{x0:.6f}",
                f"{fx:.6f}",
                f"{fpx:.6f}",
                f"{selisih:.6f}"
            ])

            if selisih < e:
                self.add_row([" Akar:", f"x = {x1:.6f}", f"({i} iterasi)"], color=(1, 0, 0))
                break

            x0 = x1
        else:
            self.add_row([" Tidak konvergen", f"x terakhir = {x1:.6f}"], color=(0, 0, 0))
            

class NewtonCal(App):
    def build(self):
        self.title = 'UTS Komnum - Newton-Raphson'
        return NewtonLayout()


if __name__ == '__main__':
    NewtonCal().run()