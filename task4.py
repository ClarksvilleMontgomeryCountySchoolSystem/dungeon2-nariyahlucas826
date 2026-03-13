good = r"""
 {"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
You will will walk across to freedom
"""
bad = r"""
{"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
 You will stay down in the danger
 """
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: The drawbridge crashes down just in time, and you charge across to freedom!"
    print(good)
else:
    outcome = "Doom: The drawbridge stays raised, leaving you stranded as danger closes in."
    print(bad)