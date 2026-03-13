good = r"""
{"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
 You will escape and see escape
 """
bad = r"""
{"`-'"}
  (o o)
,--`Y'--.
``:   ;''
  / _ \
 ()' `()
 You will get caught and your chance to get away slips
 """
escaped = True
if escaped:
    outcome = "Legend: You step into the sunlight, you daring escape destined to be told for generations."
    print(good)
else:
    outcome = "Doom: The shawdows tighten around you, and the world fades as your chance slips away."
    print(bad)