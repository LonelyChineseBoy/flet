import flet
import requests
import settings
import asyncio


class ChangeHotComment(flet.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.change_hot_comment = flet.Text(selectable=True, size=20, text_align=flet.TextAlign.CENTER)
        return self.change_hot_comment

    async def did_mount_async(self):
        self.running = True
        asyncio.create_task(self.update_Text())

    async def will_unmount_async(self):
        self.running = False

    async def update_Text(self):
        while self.running:
            response = requests.get(url=settings.api['hot_comment'])
            if "wangyiyunreping" in response.text:
                self.change_hot_comment.value = response.json()[0]['wangyiyunreping']
            # self.change_hot_comment.value = ''
            await self.update_async()
            await asyncio.sleep(10)


class ViewPage(flet.Container):
    def __init__(self, page: flet.Page):
        self.page = page
        self.hot_comment = flet.Container(
            alignment=flet.alignment.center,
            content=ChangeHotComment()
        )
        self.res_view = flet.ResponsiveRow(
            controls=[
                self.hot_comment,
            ]
        )
        super().__init__(expand=True, content=self.res_view)