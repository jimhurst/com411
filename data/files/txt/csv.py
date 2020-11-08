def search(file_name):
  print("Searching...")
  data = {}

  with open(file_name) as file:
    section_name = ""
    for line in file:
      if (line.startswith("Section")):
        parts = line.splitt(":")
        section_name = parts[1].strip()
      else:
        data[section_name] = line.strip()
    
