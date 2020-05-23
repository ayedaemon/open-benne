banner = '''
     ...     ..
  .=*8888x <"?88h.
 X>  '8888H> '8888                 u.    u.      u.    u.
'88h. `8888   8888        .u     x@88k u@88c.  x@88k u@88c.      .u
'8888 '8888    "88>    ud8888.  ^"8888""8888" ^"8888""8888"   ud8888.
 `888 '8888.xH888x.  :888'8888.   8888  888R    8888  888R  :888'8888.
   X" :88*~  `*8888> d888 '88%"   8888  888R    8888  888R  d888 '88%"
 ~"   !"`      "888> 8888.+"      8888  888R    8888  888R  8888.+"
  .H8888h.      ?88  8888L        8888  888R    8888  888R  8888L
 :"^"88888h.    '!   '8888c. .+  "*88*" 8888"  "*88*" 8888" '8888c. .+
 ^    "88888hx.+"     "88888%      ""   'Y"      ""   'Y"    "88888%
        ^"**""          "YP'        By ayedaemon               "YP'

'''


print(banner)


import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--search', help='Search for comma seperated keywords (eg. key1,key2,key3)')
group.add_argument('-r', '--refresh', help='Refresh the h1 report list. Give number of pages to load')

args = parser.parse_args()

# print(args)
try:
    if args.search:
        import searcher
        searcher.my_parser(args.search)
except Exception as e:
    print(e)

try:
    if args.refresh:
        import refresh
        print("[+] Refreshing..")
        refresh.refresh_list(int(args.refresh))
        print("[+] Finished!")
except:
    pass
