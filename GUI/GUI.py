import flet as ft
from main import taylor
def main(page: ft.Page):
    page.window_center()
    page.window_maximizable = False
    page.window_height = 500
    page.window_width = 500
    page.title = "Método de Taylor"
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}, {tb3.value}'"
        taylor(tb1.value, float(tb2.value), int(tb3.value))


    t = ft.Text()
    button = ft.ElevatedButton("Calcular", on_click=button_clicked)
    tb1 = ft.TextField(label="Función f(x)")
    tb2 = ft.TextField(label="Punto inicial (c)" )
    tb3 = ft.TextField(label="Numero de derivadas (n)")

    page.add(tb1,tb2,tb3,button)

ft.app(target=main)