# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/09c_vision.widgets.ipynb (unless otherwise specified).

__all__ = ['HBox', 'VBox', 'widgets', 'Button', 'Checkbox', 'Dropdown', 'Layout', 'Box', 'ImagesWidget']

# Cell
from ..torch_basics import *
from ..data.all import *
from .core import *
from ipywidgets import HBox,VBox,widgets,Button,Checkbox,Dropdown,Layout,Box

# Cell
@patch
def __getitem__(self:Box, i): return self.children[i]

# Cell
class ImagesWidget:
    "A widget that displays all images in `fns` along with a `Dropdown`"
    def __init__(self, fns, opts=(), height=128, width=128):
        self.fns = fns
        box_layout = dict(width='100%', height='', overflow='scroll hidden', flex_flow='row', display='flex')
        img_layout = dict(height=f'{height}px', object_fit='contain')

        v = [VBox([
                widgets.Image(value=Image.open(fn).to_thumb(height,width).to_bytes_format(), layout=img_layout),
                Dropdown(options=('<Keep>', '<Delete>')+tuple(opts), layout={'width': 'max-content'})
            ], layout={'min_width':f'{width}px'}) for fn in fns]
        self.widget = Box(children=v, layout=box_layout)

    def _ipython_display_(self): display(self.widget)
    def values(self): return L(self.widget.children).itemgot(1).attrgot('value')
    def delete(self): return L(self.fns[i] for i,o in enumerate(self.values()) if o=='<Delete>')
    def change(self): return L(self.fns[i] for i,o in enumerate(self.values()) if not o in ('<Delete>','<Keep>'))