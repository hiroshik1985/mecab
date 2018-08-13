import json
import os
import glob
import MeCab

tagger = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')


dir_name = "/datasets"
mecabed_dir_name = "/datasets/mecabed_2"

json_file = "*.json"

file_names = [os.path.basename(f) for f in glob.glob(os.path.join(os.getcwd(), dir_name, json_file))]
tagger.parse('')
# print(file_names)

for n in file_names:
    f = open( os.path.join(dir_name, n))
    l = json.load(f)
    for j in l:
        content = j['content'].replace('#', '')
        surfaces = []
        if len(content) > 20:
            node = tagger.parseToNode(content)
            while node:
                hinshi = node.feature.split(',')[0]
                if hinshi != "記号":
                    surfaces.append(node.surface)
                else:
                    print(node.surface)
                node = node.next

            with open(os.path.join(mecabed_dir_name, os.path.splitext(n)[0] + ".txt"), mode='a') as m:
                m.write((' ').join(surfaces) + "\n")
                print((' ').join(surfaces))

