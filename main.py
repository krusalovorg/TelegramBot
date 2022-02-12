from pyrogram import Client, filters
import os
import time

app = Client("test")
animations = {}

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
                print(item)
                if len(boofer)>0:
                    animations[anim_name].append(boofer)
                    boofer = ""
                animations[anim_name].append(item.replace("#:",""))

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
    if this_anim:
        for anim in this_anim:
            if anim.replace('.','',1).isdigit():
                time.sleep(float(anim))
            else:
                message.edit(anim)
    else:
        message.edit(message.text+"🤷")

app.run()