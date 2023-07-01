import flet as ft
from main import taylor,graph
def main(page: ft.Page):
    page.window_center()
    page.window_maximizable = False
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}, {tb3.value}'"
        graph(tb1.value,int(tb2.value),int(tb3.value))



    t = ft.Text()
    button = ft.ElevatedButton("Calcular", on_click=button_clicked)
    tb1 = ft.TextField(label="Función f(x)")
    tb2 = ft.TextField(label="Punto inicial (c)" )
    tb3 = ft.TextField(label="Numero de derivadas (n)")
    ct = ft.Container(
            margin=(10),
            padding=(10),
            width=500,
            height=350,
            bgcolor=ft.colors.BLUE_ACCENT,
            border_radius=5,
            animate_opacity=300
        )


    page.add(tb1,tb2,tb3,button,ct)

ft.app(target=main)