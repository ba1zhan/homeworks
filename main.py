import flet as ft



def main(page: ft.Page):
    page.title = 'Мое первое приложение!'
    page.theme_mode = ft.ThemeMode.LIGHT
    text_hello = ft.Text(value='Hello World')
    text_time = ft.TimePicker

    # text_hello.value = 'Hello'
    # text_hello.color = ft.Colors.GREEN_900


    def text_name(_):
        name = name_input.value.strip()


        if name:
            text_hello.color = None
            text_hello.value = f'Hello {name}'
            name_input.value = None
        else:
            text_hello.value = 'Введите имя!'
            text_hello.color = ft.Colors.RED

    def switch_icon(_):


        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK


    elevated_button = ft.ElevatedButton('send', on_click=text_name, icon=ft.Icons.SEND)

    name_input = ft.TextField(label='Введите что нибудь!', on_submit=text_name)

    thememode_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=switch_icon)


    page.add(text_hello,  name_input ,  elevated_button, thememode_button, text_time)




ft.app(target=main)