good = r"""
 {"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
You will go through the gaurds
"""
bad = r"""
 {"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
 The gaurd will catch you
 """
guard_awake = False
if not guard_awake:
    outcome = "Shadow: You slip silently past the slumped guard, your footsteps softer than dust."
    print(good)
else:
    outcome = "Doom: The guard's eyes snap open, and the alarm bell shatters the silence."
    print(bad)