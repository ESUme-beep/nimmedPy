# This file contains nim implementations of heavy functions used in actcom to speed it up
import nimpy

proc parse_labels(labels: seq[(int, float)]): (int, float) {.exportpy.} =
  var 
    i_highest: int = 0
    f_highest: float = 0.0
    f_lowest: float = 0.0
    f_delta: float = 0.0
    i: int = 0
  for label in labels.items:
    let value: float = label[1]
    if value > f_highest:
      f_highest = value
      i_highest = i
    elif value < f_lowest:
      f_lowest = value
    i += 1
  f_delta = f_highest - f_lowest
  return (i_highest, f_delta)