import flet
from settings import *


class NavigationBar(flet.Container):
    def __init__(self, page: flet.Page):
        self.page = page
        self.page.window_title_bar_hidden = True
        self.page.window_height = window_height
        self.page.window_width = window_width
        self.page.window_min_width = window_min_width
        self.page.window_min_height = window_min_height
        self.page.splash = flet.ProgressBar(visible=False)
        self.page.padding = 0
        self.bg_src = background
        self.destinations = []
        self.view_page = []
        self.rail = self.ret_rail()
        self.vertical = flet.VerticalDivider(width=1)
        self.operation = self.ret_operation()
        self.column = self.ret_column()
        self.view = self.ret_view()
        self.set_destinations()
        self.bg_container = self.ret_bg_container()
        super().__init__(content=self.bg_container, expand=True)

    def ret_bg_container(self):
        return flet.Container(
            content=self.view,
            image_src=self.bg_src,
            image_fit=flet.ImageFit.FILL,
            image_opacity=0.5,
            expand=True
        )

    def ret_view(self):
        return flet.Row(
            [self.rail, self.vertical, self.column],
        )

    def ret_column(self):
        return flet.Column(
            expand=True,
            controls=[
                flet.WindowDragArea(
                    content=self.operation,

                ),
            ]
        )

    def ret_operation(self):
        return flet.Row(
            alignment=flet.MainAxisAlignment.END,
            controls=[
                flet.IconButton(
                    icon=flet.icons.HORIZONTAL_RULE_ROUNDED,
                    tooltip="缩小",
                    on_click=self.narrow_window
                ),
                flet.IconButton(
                    icon=flet.icons.CROP_SQUARE,
                    tooltip="放大",
                    on_click=self.enlarge_window
                ),
                flet.IconButton(
                    icon=flet.icons.CLOSE_OUTLINED,
                    tooltip="关闭",
                    on_click=self.close_window
                )
            ]
        )

    def set_destinations(self):
        for navigation in navigations:
            self.destinations.append(
                flet.NavigationRailDestination(
                    icon_content=flet.Icon(navigation[0]),
                    selected_icon_content=flet.Icon(navigation[1]),
                    label=navigation[2]
                )
            )
            self.view_page.append(navigation[3](self.page))
        if self.rail.selected_index == 0:
            self.view.controls[2].controls.append(self.view_page[0])

    def ret_rail(self):
        return flet.NavigationRail(
            bgcolor=transparent_color,
            selected_index=0,
            label_type=flet.NavigationRailLabelType.ALL,
            min_width=100,
            group_alignment=-0.9,
            destinations=self.destinations,
            on_change=self.set_view_page,
        )

    async def set_view_page(self, e):
        self.view.controls[2].controls[1] = self.view_page[e.control.selected_index]
        await self.page.update_async()

    # @staticmethod
    async def close_window(self, e):
        await self.page.window_close_async()

    # @staticmethod
    async def narrow_window(self, e):
        self.page.window_minimized = True
        await self.page.update_async()

    async def enlarge_window(self, e):
        if not self.page.window_maximized:
            e.page.window_maximized = True
        else:
            e.page.window_maximized = False
        await e.page.update_async()


async def main(page: flet.Page):
    t = NavigationBar(page)
    await page.window_center_async()
    await page.add_async(t)


if __name__ == '__main__':
    flet.app(target=main)
