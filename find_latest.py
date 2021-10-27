import os, os.path
  
  
def find_latest(start_dir):
      latest_time = 0
      latest_file = None
      for root, subdirs, files in os.walk(start_dir):
          for name in files:
              modified_time = os.path.getmtime(os.path.join(root, name))
              if (modified_time > latest_time):
                  latest_file = os.path.join(root, name)
                  latest_time = modified_time
      return os.path.abspath(latest_file)

      
      
      
      
