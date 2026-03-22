from nicegui import ui
#lze používat lehce class, upravujeme přes tailwindcss, https://tailwindcss.com/

def example():
    ui.notify("Button works!")

def example_2():
    ui.notify("Button works yet again!")

buttons = {
    "Button 1": example,
    "Button 2": example_2,
    "Button 3": example
}

with ui.element("div").classes("flex items-center justify-center flex-col h-screen w-full gap-5"):
    ui.label("Hello").classes("text-teal-400 text-4xl")
    ui.label("Bye!").style("color: red")

    with ui.grid(columns=3):
        # for i in range(9):
        #     ui.button(i, on_click=example)
        for name, func in buttons.items():
            ui.button(name, on_click=func)

ui.run(native=True) #bez native = True je ve webovém prohlížeči