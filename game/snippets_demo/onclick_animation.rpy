image click_disappearing_effect:
    # The animated image that will be displayed
    "#00f"
    xysize (30, 30) anchor (0.5, 0.5)
    alpha 1
    pause 0.2
    linear 1 alpha 0

screen click_effect_screen():
    # The screen that actually shows the animation
    zorder 10
    default click = ClickEffect(child_image = "click_disappearing_effect", child_duration = 2)
    add click

init python:
    # One or the other, if in doubt use the first one
    config.overlay_screens.append("click_effect_screen")
    #config.always_shown_screens.append("click_effect_screen")
