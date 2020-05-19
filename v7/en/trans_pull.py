#!/usr/bin/env python

import sys
import os

langs = []
folders = ['overview', 'get-started', 'widgets', 'porting'];
files = ['index.md'];

lang_str = ""

for lang in langs:
  lang_str += lang + ","

  for f in folders:
    cmd = "rm -r " + "../" + lang + "/" + f
    print(cmd)
    os.system(cmd);
    
  for f in files:
    cmd = "rm "  + "../" + lang + "/" + f
    print(cmd)
    os.system(cmd);
    
    
cmd = "zanata-cli pull -B -l " + lang_str
print(cmd)
os.system(cmd);


for lang in langs:
  old_link = ':github_url: https:\/\/github.com\/lvgl\/docs\/blob\/master\/v7\/en'
  new_link = ':github_url: https:\/\/github.com\/lvgl\/docs\/blob\/master\/v7\/' + lang
  cmd = "sed -i 's/{}/{}/' ../{}/**/*.txt".format(old_link, new_link, lang)
  print(cmd)
  os.system(cmd);

  cmd = "sed -i 's/{}/{}/' ../{}/*.txt".format(old_link, new_link, lang)
  print(cmd)
  os.system(cmd);


  cmd = "rename -f 's/\.txt//g' ../" + lang + "/**/*.txt"
  print(cmd)
  os.system(cmd);

  cmd = "rename -f 's/\.txt//g' ../" + lang + "/*.txt"
  print(cmd)
  os.system(cmd);

  
  
