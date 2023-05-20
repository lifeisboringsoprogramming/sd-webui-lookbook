from modules import script_callbacks
from img2lookbook import make_ui


def on_ui_tabs():
    return [(make_ui(), "img2lookbook", "extension_sd_webui_img2lookbook")]


script_callbacks.on_ui_tabs(on_ui_tabs)
