import flet


class ViewPage(flet.Container):
    def __init__(self, page):
        self.page = page
        self.contaier = flet.Text("")
        super().__init__(content=self.contaier, expand=True)
