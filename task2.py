good = r"""
 {"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
You will go through the door
"""
bad = r"""
 {"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
You won't pass through the doors
"""
has_key = True
if has_key:
    outcome = "Click: The lock turns smoothly, and the door creeks open"
    print(good)
else:
    outcome = "Doom: The handle refuses to budge, and shadows begin to close in behind you."
    print(bad)