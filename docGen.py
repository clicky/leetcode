import os

def gen_docs():
    subdirectories = []
    t = dict()
    s = dict()
    for dir in os.listdir('.'):
        if dir[0] == '.' or not os.path.isdir(dir) or dir[:5] == 'Notes':
            continue
        try:
            with open(f"{dir}/tags.txt", "r") as file:
                content = file.read()
                tags = content.split(' ')
                for tag in tags:
                    name = tag[1:]
                    if not name in t:
                        t[name] = []
                    t[name].append(dir)
        except FileNotFoundError:
            print(f"Error: The file '{dir}/tags.txt' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        for f in os.listdir(dir):
            if os.path.isfile(f"{dir}/{f}"):
                extension = f.split('.')[1]
                language = x2l(extension)
                if language:
                    if not dir in s:
                        s[dir] = []
                    s[dir].append(language)
    try:
        with open(f"README.md", "w") as file:
            tags = list(t.keys())
            tags.sort()
            for k in tags:
                file.write(f"## {k}\n")
                for v in t[k]:
                    file.write(f"- [{v}](https://leetcode.com/problems/{v.split(' - ')[1].lower().replace(' ', '-')})\n")
                    ls = "    - [ "
                    for l in s[v]:
                        ls += f"[{l}](<{v}/solution.{l2x(l)}>) | "
                    file.write(ls[:-2] + "]\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def x2l(x: str) -> str:
    if x == 'py':
        return 'Python'
    elif x == 'cpp':
        return 'C++'
    elif x == 'java':
        return 'Java'
    else:
        return None

def l2x(l: str) -> str:
    if l == 'Python':
        return 'py'
    elif l == 'C++':
        return 'cpp'
    elif l == 'Java':
        return 'java'
    else:
        return None

if __name__ == '__main__':
    gen_docs()
