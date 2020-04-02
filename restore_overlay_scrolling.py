from gi.repository import GObject, Gedit

class RestoreOverlayScrollingPlugin(GObject.Object, Gedit.ViewActivatable):

    view = GObject.property(type=Gedit.View)

    def __init__(self):
        GObject.Object.__init__(self)

    def _set_overlay_scrolling(self, value):
        self.view.get_parent().set_overlay_scrolling(value)

    def do_activate(self):
        self._set_overlay_scrolling(True)

    def do_deactivate(self):
        self._set_overlay_scrolling(False)
