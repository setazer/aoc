from aocframework import AoCFramework


class File:

    def __init__(self, name, size: int):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'File({self.name}, {self.size})'


class Dir:

    def __init__(self, name=None, parent=None):
        self.name = name
        self.items = {}
        self._parent = parent

    def __repr__(self):
        return f'{self._parent}/{self.name}/' if self._parent else f'{self.name}'

    def __iter__(self):
        return iter(self.items)

    @property
    def size(self):
        return sum(item.size for item in self.items.values())

    def folders(self):
        for item in self.items.values():
            if isinstance(item, Dir):
                yield item
                yield from item.folders()

    def limited(self, limit=0):
        for folder in self.folders():
            if folder.size < limit:
                yield folder

    def add_child(self, name, item):
        self.items[name] = item

    def print_contents(self, path=''):
        for item in self.items.values():
            offset = f'  {path}'
            if isinstance(item, File):
                print(offset, item.name, item.size, sep=' ')
            elif isinstance(item, Dir):
                print(offset, item.name, sep=' ')
                item.print_contents(offset)

class FS(Dir):
    def parse_instructions(self, fs_data:str):
        current_dir = None
        for line in fs_data.strip().split('\n'):
            line = line.lstrip('$ ')
            if line.startswith('cd '):
                folder = line[3:]
                if folder == '..':
                    current_dir = current_dir._parent
                elif folder == '/':
                    current_dir = self
                else:
                    current_dir = current_dir.items[folder]
            elif line.startswith('ls'):
                pass
            elif line.startswith('dir'):
                folder = line[4:]
                current_dir.add_child(folder, Dir(folder, parent=current_dir))
            else:
                size, _, name = line.partition(' ')
                current_dir.add_child(name, File(name, int(size)))


class DayPart1(AoCFramework):
    test_cases = (
        ('''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k''', 95_437),
    )
    known_result = 1_141_028

    def go(self):
        fs = FS('/')
        fs.parse_instructions(self.raw_puzzle_input)
        limit = 100_000
        return sum(folder.size for folder in fs.folders() if folder.size < limit)


DayPart1()


class DayPart2(AoCFramework):
    test_cases = (
        ('''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k''', 24_933_642),
    )
    known_result = 8_278_005

    def go(self):
        fs = FS('/')
        fs.parse_instructions(self.raw_puzzle_input)
        total_size = 70_000_000
        update_size = 30_000_000
        free_size = total_size - fs.size
        target_free = update_size - free_size
        return min(folder.size for folder in fs.folders() if folder.size > target_free)


DayPart2()
