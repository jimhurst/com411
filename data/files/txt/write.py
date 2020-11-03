def search(filename):
  print("Searching...")
  sections = []
  books = []
  with open (filename) as file:
    for line in file:
      if line.startswith("Section"):
        #line.split(":")
        sections.append(line.split(":"))
      else:
        books.append(line.split(":"))
      print("Done!")
      sorted = (sections, books)
      return sorted     

def save(filename, data):
  print("Saving...")
  with open (filename, "w") as file:
    file.write(f"Sections: {data}")


def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data)

run()


