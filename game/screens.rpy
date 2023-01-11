screen yesno_prompt(message = "Are you sure", yes_action = [], no_action = []):
    modal True
    add "#000":
        xysize (1., 1.) alpha 0.8
    vbox:
        spacing 8
        xalign 0.5 yalign 0.5
        text message:
            xalign 0.5
        textbutton "Yes":
            xalign 0.5
            action yes_action
        textbutton "No":
            xalign 0.5
            action no_action

screen choice(message = "", items = []):
    modal True
    add "#000":
        xysize (1., 1.) alpha 0.8
    vbox:
        spacing 8
        xalign 0.5 yalign 0.5
        if message:
            text message:
                xalign 0.5
            null:
                xsize 30
        for item in items:
            textbutton item[0]:
                xalign 0.5
                action item[1]

style button_text:
    hover_color "#d9dd00"
