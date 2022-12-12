#This row contains a textfield and a button when click on it shows the data in the text field

import flet as ft


def main(page: ft.Page):

    name = ft.TextField(label="Your name")

    def button_clicked(e):
        page.add(ft.Text(name.value))

    page.add(
    ft.Row(controls=[
        name,
        ft.ElevatedButton(text="Say my name!", on_click=button_clicked)
    ])
)

ft.app(target=main)