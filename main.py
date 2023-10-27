import os, shutil
import random
import sys


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


recipes = []
loot_tables = []
try:
    IS_RESET_LOOT = sys.argv[1].lower() == '-reset_loot'
except IndexError as e:
    IS_RESET_LOOT = False


def reset_recipes():
    folder = "data\\minecraft\\recipes"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def reset_loot():
    folder = "data\\minecraft\\loot_tables"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def randomize_loot():
    reset_loot()
    copytree("vanilla_loot_tables\\", "data\\minecraft\\loot_tables\\")

    current_dir = "vanilla_loot_tables\\blocks\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:block"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[s:]
            loot_tables.append(cut)
            f.close()
    current_dir = "vanilla_loot_tables\\chests\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:chest"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[s:]
            loot_tables.append(cut)
            f.close()
    current_dir = "vanilla_loot_tables\\entities\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:entity"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[s:]
            loot_tables.append(cut)
            f.close()
    current_dir = "vanilla_loot_tables\\chests\\village\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:chest"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[s:]
            loot_tables.append(cut)
            f.close()
    current_dir = "vanilla_loot_tables\\entities\\sheep\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:entity"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[s:]
            loot_tables.append(cut)
            f.close()
    # ------------------------------------
    # write
    # ------------------------------------
    current_dir = "data\\minecraft\\loot_tables\\blocks\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:block"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[0:s]
            f.close()
            f = open(current_dir + entry.name, 'w')
            rnd_txt = random.choice(loot_tables)
            f.write(cut + rnd_txt)
            loot_tables.remove(rnd_txt)
            f.close()
    current_dir = "data\\minecraft\\loot_tables\\chests\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:chest"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[0:s]
            f.close()
            f = open(current_dir + entry.name, 'w')
            rnd_txt = random.choice(loot_tables)
            f.write(cut + rnd_txt)
            loot_tables.remove(rnd_txt)
            f.close()
    current_dir = "data\\minecraft\\loot_tables\\entities\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:entity"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[0:s]
            f.close()
            f = open(current_dir + entry.name, 'w')
            rnd_txt = random.choice(loot_tables)
            f.write(cut + rnd_txt)
            loot_tables.remove(rnd_txt)
            f.close()

    current_dir = "data\\minecraft\\loot_tables\\chests\\village\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:chest"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[0:s]
            f.close()
            f = open(current_dir + entry.name, 'w')
            rnd_txt = random.choice(loot_tables)
            f.write(cut + rnd_txt)
            loot_tables.remove(rnd_txt)
            f.close()

    current_dir = "data\\minecraft\\loot_tables\\entities\\sheep\\"
    for entry in os.scandir(current_dir):
        if entry.name.endswith(".json") and entry.is_file():
            f = open(current_dir + entry.name, 'r')
            txt = f.read()
            type_str = '"type": "minecraft:entity"'
            s = txt.find(type_str) + len(type_str)
            cut = txt[0:s]
            f.close()
            f = open(current_dir + entry.name, 'w')
            rnd_txt = random.choice(loot_tables)
            f.write(cut + rnd_txt)
            loot_tables.remove(rnd_txt)
            f.close()


def main():
    if IS_RESET_LOOT:
        print("Resetting Loot...")
        reset_loot()
    else:
        print("Randomizing Loot...")
        randomize_loot()

    print("Done!")


if __name__ == '__main__':
    main()
