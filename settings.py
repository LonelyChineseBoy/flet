from flet import icons
from views.home import ViewPage as HomeViewPage
from views.music import ViewPage as MusicViewPage
from views.user_settings import ViewPage as SettingsViewPage

navigations = [
    [icons.HOME_MAX_SHARP, icons.ADD_HOME_WORK_SHARP, "首页", HomeViewPage],
    [icons.MUSIC_VIDEO_OUTLINED, icons.MY_LIBRARY_MUSIC_ROUNDED, "音乐", MusicViewPage],
    [icons.SETTINGS_SUGGEST_OUTLINED, icons.SETTINGS_SUGGEST_SHARP, "设置", SettingsViewPage],
]

background = "./assets/bgimg.png"
transparent_color = "surface,0.0"

window_height = 450
window_width = 800
window_min_width = 800
window_min_height = 450

api = {
    # 随机返回一句网易云音乐热评
    "hot_comment": "https://v.api.aa1.cn/api/api-wenan-wangyiyunreping/index.php?aa1=json",
}
