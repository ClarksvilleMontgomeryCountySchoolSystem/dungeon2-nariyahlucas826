good = r""""
 {"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
You survive dancing walls 
"""
bad = r""""
 {"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
 The darkness swallows you
 """""

torch_lit = True
if torch_lit:
    outcome = "Flicker: The warm light dances across the walls, revealing a hidden dooor and saffe path forward."
    print(good)
else:
    outcome = "Doom: Darkness swallows you whole, and every step feels like a stumble into the unkown."
    print(bad)