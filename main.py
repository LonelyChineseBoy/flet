import flet
from settings import *


class NavigationBar(flet.Container):
    def __init__(self, page: flet.Page):
        self.page = page
        self.bg_src = background
        self.destinations = []
        self.view_page = []
        self.rail = flet.NavigationRail(
            bgcolor=transparent_color,
            selected_index=0,
            label_type=flet.NavigationRailLabelType.ALL,
            min_width=100,
            group_alignment=-0.9,
            destinations=self.destinations,
            on_change=lambda e: self.set_view_page(e),
        )

        self.vertical = flet.VerticalDivider(width=1)
        self.operation = flet.Row(
            alignment=flet.MainAxisAlignment.END,
            controls=[
                flet.IconButton(
                    icon=flet.icons.HORIZONTAL_RULE_ROUNDED,
                    tooltip="缩小"
                ),
                flet.IconButton(
                    icon=flet.icons.CROP_SQUARE,
                    tooltip="放大"
                ),
                flet.IconButton(
                    icon=flet.icons.CLOSE_OUTLINED,
                    tooltip="关闭"
                )
            ]
        )
        self.column = flet.Column(
            expand=True,
            controls=[
                flet.WindowDragArea(
                    content=self.operation,
                ),
            ]
        )
        self.view = flet.Row(
            [self.rail, self.vertical,self.column],
            expand=True
        )

        self.set_destinations()
        self.bg_container = flet.Container(
            content=self.view,
            image_src=self.bg_src,
            image_fit=flet.ImageFit.FILL,
            image_opacity=0.5,
            expand=True
        )
        super().__init__(content=self.bg_container, expand=True)

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

    def set_view_page(self, e):
        self.view.controls[2].controls[1] = self.view_page[e.control.selected_index]
        self.page.update()


def main(page: flet.Page):
    page.window_title_bar_hidden = True
    page.window_height = window_height
    page.window_width = window_width
    page.window_min_width = window_min_width
    page.window_min_height = window_min_height
    progress_bar = flet.ProgressBar(visible=False)
    page.splash = progress_bar
    page.padding = 0
    t = NavigationBar(page)
    page.window_center()
    page.add(t)


if __name__ == '__main__':
    flet.app(target=main)
