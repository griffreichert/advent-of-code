

"""

What input can I get:
- command
    - cd
        - go into a dir
        - go out of a dir
        - go to home
    - ls (skip these)
- object
    - directory
        - name
        - parent
        - children
            - directories
            - files
    - file
        - name
        - parent
        - size

"""

class File:
    def __init__(self, name, parent, size=0):
        self.name = name
        self.parent = parent
        self.size = int(size)

    def print_me(self):
        pad = ''.join(['  ' for i in range(self.parent.level)])
        print(f'{pad}  . {self.name} ({self.size})')
    
    def find_size(self):
        return self.size

class Directory:
    def __init__(self, name, parent=None, level=0):
        self.name = name
        self.parent = parent
        self.children = []
        self.level = level

    def add_dir(self, name):
        self.children.append(Directory(name, self, self.level + 1))

    def add_file(self, name, size):
        self.children.append(File(name, self, size))
    
    def print_me(self):
        pad = ''.join(['  ' for i in range(self.level)])
        print(f'{pad}- {self.name}')
        for c in self.children:
            c.print_me()
    
    def find_dir(self, name):
        for d in self.children:
            if d.name == name and isinstance(d, Directory):
                return d
        return self.parent

    def find_size(self):
        return sum([c.find_size() for c in self.children])


# Part 1
def find_under_n(dir, n):
    return find_under_n_helper(dir, [], n)

def find_under_n_helper(dir, res, n):
    dir_size = dir.find_size()
    if dir_size < n:
        res.append(dir_size)
    for d in dir.children:
        if isinstance(d, Directory): 
            # recursively find child directories less than n   
            find_under_n_helper(d, res, n)
    return res

# Part 2
def find_above_n(dir, n):
    return find_above_n_helper(dir, [], n)

def find_above_n_helper(dir, res, n):
    dir_size = dir.find_size()
    if dir_size >= n:
        res.append(dir_size)
    for d in dir.children:
        if isinstance(d, Directory):    
            # recursively find child directories greater than n   
            find_above_n_helper(d, res, n)
    return res

home_dir = Directory('home')
# point to current directory
cwd = home_dir

# build folder structure
with open('../data/day7.txt', 'r') as f:
    for line in f:
        instr = line.replace('\n', '')
        if instr == '$ ls' or instr == '$ cd /':
            continue
        # command
        if instr[0] == '$':
            _, dir_name = instr.split('cd ')
            # will return name of dir if dir in list of children, otherwise it will return the parent dir if ..
            cwd = cwd.find_dir(dir_name)
        # file or directory
        else:
            a, b = instr.split(' ')
            if a.isnumeric():
                cwd.add_file(b, a)
            elif a == 'dir':
                cwd.add_dir(b)

home_dir.print_me()

print(f'\nPart 1\n{sum(find_under_n(home_dir, 100000))}')

unused = 70000000 - home_dir.find_size()
print(f'\nPart 1\n{min(find_above_n(home_dir, (30000000 - unused)))}')