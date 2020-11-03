def search(file_name):
  print("Searching...")
  sections = []
  books = []
  with open(file_name) as file:
    for line in file:
      if (line.startswith("Section")):
        parts = line.split(":")
        sections.append(parts[1].replace('\n',''))
      else:
        books.append(line.replace('\n'))
  print("Done!")
  return (sections, books)

def save(file_name, data):
    print("Saving...")
    with open(file_name, "w") as file:
      file.write("Section: ")
      file.write(f"Section: {data[0]}")
      file.write(f"books: {data[1]}")
    
def run():
    data = search("data/files/txt/books.txt")
    save("data/files/txt/section-books2.txt", data)

run()
