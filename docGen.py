import os

def gen_docs():
    subdirectories = []
    m = dict()
    for dir in os.listdir('.'):
        if dir[0] == '.' or not os.path.isdir(dir):
            continue
        try:
            with open(f"{dir}/tags.txt", "r") as file:
                content = file.read()
                tags = content.split(' ')
                for tag in tags:
                    name = tag[1:]
                    if not name in m:
                        m[name] = []
                    m[name].append(dir)
        except FileNotFoundError:
            print(f"Error: The file '{dir}/tags.txt' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    try:
        with open(f"README.md", "w") as file:
            for k in m:
                file.write(f"## {k}\n")
                for v in m[k]:
                    file.write(f" - [{v}](<{v}>)\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    gen_docs()
