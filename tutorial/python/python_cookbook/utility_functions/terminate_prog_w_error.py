import sys
sys.stderr.write("It failed\n")
raise SystemError(1) # returning a non zero code