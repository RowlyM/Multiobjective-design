# -*- coding: utf-8 -*-
"""
This code is from the matplotlib.widgets.
"""

class MultiCursor:
    """
    Provide a vertical line cursor shared between multiple axes

    Example usage::

        from matplotlib.widgets import MultiCursor
        from pylab import figure, show, nx

        t = nx.arange(0.0, 2.0, 0.01)
        s1 = nx.sin(2*nx.pi*t)
        s2 = nx.sin(4*nx.pi*t)
        fig = figure()
        ax1 = fig.add_subplot(211)
        ax1.plot(t, s1)


        ax2 = fig.add_subplot(212, sharex=ax1)
        ax2.plot(t, s2)

        multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)
        show()

    """
    def __init__(self, canvas, axes, useblit=True, **lineprops):

        self.canvas = canvas
        self.axes = axes
        xmin, xmax = axes[-1].get_xlim()
        xmid = 0.5*(xmin+xmax)
        if useblit:
            lineprops['animated'] = True

        self.lines = [ay.axvline(xmid, visible=False, **lineprops) for ay in axes]

        self.visible = True
        self.useblit = useblit
        self.background = None
        self.needclear = False

        self.canvas.mpl_connect('motion_notify_event', self.onmove)
        self.canvas.mpl_connect('draw_event', self.clear)


    def clear(self, event):
        'clear the cursor'
        if self.useblit:
            self.background = self.canvas.copy_from_bbox(self.canvas.figure.bbox)
        for line in self.lines: line.set_visible(False)


    def onmove(self, event):
        if event.inaxes is None: return
        if not self.canvas.widgetlock.available(self): return
        self.needclear = True
        if not self.visible: return

        for line in self.lines:
            line.set_xdata( (event.xdata,event.xdata))
            line.set_visible(self.visible)
        self._update()


    def _update(self):

        if self.useblit:
            if self.background is not None:
                self.canvas.restore_region(self.background)
            for ay, line in zip(self.axes, self.lines):
                ay.draw_artist(line)
            self.canvas.blit(self.canvas.figure.bbox)
        else:

            self.canvas.draw_idle()