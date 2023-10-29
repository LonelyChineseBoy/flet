import flet


class ViewPage(flet.Container):
    def __init__(self, page: flet.Page):
        self.page = page

        self.res_view = flet.ResponsiveRow(
            controls=[
                flet.Text("settings")
            ]
        )
        super().__init__(expand=True, content=self.res_view, bgcolor=flet.colors.RED)
