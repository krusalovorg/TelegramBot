from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import os, time, random

app = Client("test")
animations = {}
random_symbol_ = ["🤍", "🖤", "🤎", "💜", "💙", "💚", "💛", "🧡", "❤", "️", "💕", "💞", "💓", "💗", "💖", "💝", "💣",
                  '🤮', '🤢', '🥳', '🤠', '🤕', '🤒', '🤯', '😵', '😷', '😴', '🥴', '🤤', '🥶', '🧐', '🥺', '😦', '😕','👹', '😤',
                  '🤡', '🥱', '💩', '😫', '😩', '😓', '😞', '😣', '😖', '😠', '🤬', '😈', '👺', '👻', '👽', '👾', '🤖',
                  '😺', '😸', '😹', '😻', '💋', '🙊', '🙉', '🙈', '😾', '😿', '🙀', '😽', '😼', '💌', '💯', '💢', '💥',
                  '💫', '💦', '💨', '🕳', '🤚', '👋', '💤', '💭', '🗯', '💬', '💣']
random_ov_ = ['🍆','🥕']

print("start..")
def load_anims():
    path = "./anims/"
    if not os.path.exists("anims"):
        os.mkdir("anims")
    files = [_ for _ in os.listdir("anims/") if _.endswith(".anim")]
    for file in files:
        anim = open(path+file, 'r', encoding="utf-8")
        anim_name = file.split(".")[0]
        animations[anim_name] = []
        this_anim = []
        for line in anim.read().splitlines():
            this_anim.append(line)
        boofer = ""
        for index, item in enumerate(this_anim):
            if not item.startswith("#:"):
                if len(boofer)>0:
                    boofer += "\n"+item
                else:
                    boofer += item
            else:
                if len(boofer)>0:
                    animations[anim_name].append(boofer)
                    boofer = ""
                anim_value = item.replace("#:", "")
                anim_value = anim_value.replace(" ", "")
                animations[anim_name].append(anim_value)

            if index == len(this_anim)-1:
                animations[anim_name].append(boofer)
                boofer = ""

load_anims()
print(animations)

#@app.on_message(filters.chat)
#def public(client, message):
#    print("===============")
#    print(message.chat.title+":",message.text)

@app.on_message(filters.command("anim", prefixes=".") & filters.me)
def private(client, message):
    cmd = message.text.split(".anim ", maxsplit=1)[1]
    this_anim = animations.get(cmd)
    while_anim = 1
    replace_symbol_ = ""
    compile_anim_ = []
    if this_anim:
        while_anim_index = 0
        print(compile_anim_)
        compile_anim_ = [i for i in this_anim]
        for index,anim in enumerate(this_anim):
            print(compile_anim_)
            if anim.find("=") > -1:
                variable = anim.split("=")
                key = variable[0]
                value = variable[1]
                compile_anim_.remove(anim)
                if key == "while":
                    while_anim += int(value)
                elif value == "random":
                    replace_symbol_ = {"key":key,"value":random_symbol_}
                elif value == "random_ov":
                    replace_symbol_ = {"key":key,"value":random_ov_}

        while while_anim_index < while_anim:
            print(len(compile_anim_), compile_anim_)
            for anim in compile_anim_:
                if anim.replace('.','',1).isdigit():
                    time.sleep(float(anim))
                else:
                    if replace_symbol_ == "":
                        message.edit(anim.replace(" ", "⠀"))
                    else:
                        replace_key = replace_symbol_.get("key")
                        replace_value = replace_symbol_.get("value")
                        random_value = random.choice(replace_value)
                        anim_string = anim.replace(replace_key, random_value)
                        try:
                            message.edit(anim_string)
                        except:
                            True
            while_anim_index += 1
    else:
        message.edit(message.text+"🤷")


@app.on_message(filters.command("write", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".write ", maxsplit=1)[1]
    text = orig_text
    tbp = ""  # to be printed
    typing_symbol = "▒"

    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            time.sleep(0.05)  # 50 ms

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            time.sleep(0.05)

        except FloodWait as e:
            time.sleep(e.x)

cmd_cho = ".повтор "
@app.on_message(filters.command("повтор", prefixes=".") & filters.me)
def repeate(_, msg):
    words = msg.text.split(" ")

    if len(words) < 2:
        msg.edit("Не верный синтаксис: .повтор <количество: num> <текст: string>")
        return

    try:
        nums = int(words[1])
    except:
        msg.edit("Число не должно быть с буквами")
        return
    text = msg.text.replace(f"{cmd_cho}{nums} ", "")

    for i in range(nums):
        msg.edit(text * (i+1))
        time.sleep(0.05)

SPACE = '❄'
STRAR = '🎄'
random_toys = ['🍊','🦌','🍾','⛄','✨','🎉']


def toy(line):
    tmp = ''
    index = random.randint(0, len(line)-1)

    for i in range(len(line)):
        tmp += line[i] if i != index else random.choice(random_toys)

    return tmp

cmd_tree = ".елка "
@app.on_message(filters.command("елка", prefixes=".") & filters.me)
def tree(_, msg):
    words = msg.text.split(" ")

    if len(words) < 1:
        msg.edit("Не верный синтаксис: .елка <высота: num> #<ширина: num>")
        return

    try:
        rows = int(words[1])
    except:
        msg.edit("Число не должно быть с буквами")
        return

    res = ""

    spaces = rows-1
    stars = 1

    # if len(words) == 2:
    #     try:
    #         stars = int(words[2])
    #     except:
    #         msg.edit("Не верный синтаксис: .елка <высота: num> <ширина: num>")
    #         return
    # else:
    #     stars = 2

    for i in range(rows):
        print((SPACE*spaces) +
            ((STRAR*stars) if (i % 2) != 0 else toy(STRAR*stars)) +
            (SPACE*spaces))
        res += ((SPACE*spaces) +
            ((STRAR*stars) if (i % 2) != 0 else toy(STRAR*stars)) +
            (SPACE*spaces))+"\n"
        msg.edit(res)

        stars += 2
        spaces -= 1
        time.sleep(0.05)

app.run()