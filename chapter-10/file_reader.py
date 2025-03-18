from pathlib import Path

path = Path('/workspaces/python-crash-course/chapter-10/pi_digits.txt')

contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines()