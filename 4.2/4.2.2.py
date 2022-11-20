

file_name = 'input.4.2.txt'

with open(file_name, encoding="latin1") as f:
            text = f.read()
            indents = text.split(">")

for indent in indents:  #indent - отсуп, абзац
    print(indent)
