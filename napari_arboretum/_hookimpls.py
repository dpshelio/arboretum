from napari_plugin_engine import napari_hook_implementation

from .plugin import Arboretum


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return Arboretum
