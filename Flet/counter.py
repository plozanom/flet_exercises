#A manual counter app
import flet as ft

def main(page: ft.Page):

    page.title = "Flet counter example" #The app title 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Vertical alignment of the controls on the center of the app 

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e): #This method decrease the value of 'txt_number' by 1
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e): #This method increase the value of 'txt_number' by 1
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)