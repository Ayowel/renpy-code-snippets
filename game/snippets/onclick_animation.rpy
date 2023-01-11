# @author Ayowel
# @label ClickAnimationSupport
#
# The ClickEffect class must be called with the name of the animated image
# to display when the player clicks and may be called with an optional
# duration after which the image may be removed (for memory management)
init python:
    from renpy.display.layout import Container
    class ClickEffect(Container):
        def __init__(self, child_image, child_duration = 10, **kwargs):
            Container.__init__(self, **kwargs)
            self.child_image = child_image
            self.child_duration = child_duration

        def event(self, ev, x, y, st):
            if ev._type == 1026: # mouse up event
                # Cleanup finished animations
                removal_list = []
                for c in self.children:
                    if c.st + self.child_duration < st:
                        removal_list.append(c)
                for c in removal_list:
                    self.remove(c)
                # Add animation at cursor
                self.add(Transform(self.child_image, xpos = x, ypos = y))
                # Update visual
                renpy.redraw(self, 0)
