import os
from file_system import Dir, File

cwd = os.path.dirname(os.path.abspath(__file__))
with open(f"{cwd}/input.txt") as f:
	data = [l.strip().split(" ") for l in f.read().splitlines()]

root = Dir(parent=None, name="/", files=[], dirs=[])
curr_dir = root
for elegible_dirs in data:
	match elegible_dirs:
		case ["$", "cd", "/"]:
			curr_dir=root
		case ["$", "cd", ".."]:
			curr_dir=curr_dir.parent
		case ["$", "cd", subdir]:
			curr_dir = curr_dir.get_dir_by_name(subdir)
		case ["$","ls"]:
			pass
		case ["dir", name]:
			if name not in [d.name for d in curr_dir.dirs]:
				curr_dir.dirs.append(Dir(name=name, parent=curr_dir))
		case [size, name]:
			if name not in [f.name for f in curr_dir.files]:
				curr_dir.files.append(File(name=name, size=int(size)))

space_needed = 30000000 - (70000000 - root.get_size())
elegible_dirs: list[Dir] = []
root.append_elegible_subdirs(elegible_dirs, lambda d: d.get_size() >= space_needed)
print(min([d.get_size() for d in elegible_dirs]))
