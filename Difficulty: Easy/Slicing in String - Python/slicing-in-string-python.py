# Function to join given bound_by and tag
def join_middle(bound_by, tag_name):
  n = len(bound_by)//2
  # complete the statement below to return the string as required
  return bound_by[0 : n] + tag_name + bound_by[ n: ]