from pyrogram import Client, filters
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

app.run()