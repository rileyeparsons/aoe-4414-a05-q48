# conv_ops.py

# Usage: python3 conv_ops.py c_in h_in w_in h_pool w_pool s p

# Parameters:
#  c_in : int 
#   input channel count
#  h_in : int 
#   input height count
#  w_in : int 
#   input width count
#  h_pool : int 
#    average pooling kernel height count
#  w_pool : int 
#   average pooling kernel width count
#  s : int | float | str
#   stride of convolution filters
#  p : int | float | str
#   amount of padding on each of the four input map sides

# Output:
#  c_out : list
#  output channel count
#  h_out : list
#  output height count
#  w_out : list
#  output width count
#  adds : list
#  number of additions performed
#  muls : list
#  number of multiplications performed
#  divs : list
#  number of divisions performed

# Written by Riley Parsons

import sys
import math

# "constants"
w = 7.292115e-5

# helper functions  
def output_map_h(h_in, p, h_pool, s):
  h_out = ((h_in + 2*p - h_pool)/s) +  1
  return h_out

def output_map_w(w_in, p, w_pool, s):
  w_out = ((w_in + 2*p - w_pool)/s) +  1
  return w_out

def get_adds(h_out, w_out, c_in, h_pool, w_pool):
  adds = c_in*h_out*w_out*(h_pool*w_pool - 1)
  return adds

def get_divs(c_in, h_out, w_out):
  divs = c_in*h_out*w_out
  return divs

# main function
def conv_ops(c_in, h_in, w_in, h_pool, w_pool, s, p):
  
  c_out = c_in
  h_out = output_map_h(h_in, p, h_pool, s)
  w_out = output_map_w(w_in, p, w_pool, s)
  adds = get_adds(h_out, w_out, c_in, h_pool, w_pool)
  muls = 0
  divs = get_divs(c_in, h_out, w_out)

  print(c_out)
  print(h_out)
  print(w_out)
  print(adds)
  print(muls)
  print(divs)

  return c_out, h_out, w_out, adds, divs
  
# initialize script arguments
c_out = None
h_out = None
w_out = None
adds = None
divs = None

# parse script arguments
if len(sys.argv)==8:
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    h_pool = int(sys.argv[4])
    w_pool = int(sys.argv[5])
    s = int(sys.argv[6])
    p = int(sys.argv[7])
else:
  print('Usage: python3 conv_ops.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km')
  exit()

# write script below this line
if __name__ == '__main__':
  conv_ops(c_in, h_in, w_in, h_pool, w_pool, s, p)
else:
  conv_ops(c_in, h_in, w_in, h_pool, w_pool, s, p)