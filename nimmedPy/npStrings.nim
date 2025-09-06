# This file contains fast nim functions for string processing
import strutils
import os
import nimpy

proc doc_sort(doc_dir_paths: seq[string], include_links: bool): seq[string]{.exportpy.} =
  var 
    docs: seq[string]
    urls: seq[string]
  for doc_dir in doc_dir_paths:
    let doc_dir: string = doc_dir
    for kind, path in os.walkDir(doc_dir):
      case kind:
        of pcDir:
          continue
        of pcFile:
          if "links" in path and include_links:
            let link_file: File = open(path)
            defer: link_file.close()
            urls.add(readAll(link_file))
          else:
            docs.add(path)
        else:
          continue
  if urls.len() > 0: result = docs & urls
  else: result = docs
  return result

proc string_cleaner(input: string): string{.exportpy.} =
  for letter in input:
    let letter: char = letter
    case letter:
      of '{', '}', '[', ']', '\\', '"', '*', '~':
        continue
      else:
        result.add(letter)
  return result
      
