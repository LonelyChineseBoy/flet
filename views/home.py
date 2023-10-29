import flet


class ViewPage(flet.Container):
    def __init__(self, page):
        self.page = page
        self.contaier = flet.Text("主页组件位置")
        super().__init__(content=self.contaier, expand=True,bgcolor=flet.colors.RED,width=300)
