import argparse
import json

# replace placeholder
def replace(tgt, jsonFile):
    with open(jsonFile, 'r', encoding='utf-8') as f:
        event = json.load(f)
    for i in range(len(tgt)):
        if '$进攻玩家$' in tgt[i]:
            tgt[i] = tgt[i].replace('$进攻玩家$',event[i]['进攻玩家名称'])
        if '$玩家$' in tgt[i] and '玩家名称' in event[i].keys():
            tgt[i] = tgt[i].replace('$玩家$', event[i]['玩家名称'])
        elif '$玩家$' in tgt[i] and not '玩家名称' in event[i].keys() and '开雾英雄' in event[i].keys():
            tgt[i] = tgt[i].replace('$玩家$',event[i]['开雾英雄'])
        if '$受敌玩家$' in tgt[i]:
            tgt[i] = tgt[i].replace('$受敌玩家$',event[i]['受敌玩家名称'])
        if '$队伍$' in tgt[i]:
            tgt[i] = tgt[i].replace('$队伍$',event[i]['队伍'])
        if '$开雾玩家$' in tgt[i]:
            tgt[i] = tgt[i].replace('$开雾玩家$',event[i]['开雾玩家'])
        if '$受敌方$' in tgt[i]:
            tgt[i] = tgt[i].replace('$受敌方$',event[i]['受敌方'])
        if '$进攻方$' in tgt[i]:
            tgt[i] = tgt[i].replace('$进攻方$',event[i]['进攻方'])
    return tgt

def set_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_src_path", type=str, default="data/adaptive/adaptive1_train.src")
    parser.add_argument("--train_tgt_path", type=str, default="data/adaptive/adaptive1_train.tgt")
    parser.add_argument("--train_json_path", type=str, default="data/adaptive/adaptive1_train.json")
    parser.add_argument("--valid_src_path", type=str, default="data/adaptive/adaptive1_valid.src")
    parser.add_argument("--valid_tgt_path", type=str, default="data/adaptive/adaptive1_valid.tgt")
    parser.add_argument("--valid_json_path", type=str, default="data/adaptive/adaptive1_valid.json")
    parser.add_argument("--test_src_path", type=str, default="data/general/general_test_seen.src")
    parser.add_argument("--test_tgt_path", type=str, default="data/general/general_test_seen.tgt")
    parser.add_argument("--test_json_path", type=str, default="data/general/general_test_seen.json")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = set_args()
    final_dict = {}
    train = []
    valid = []
    test = []
    # train
    with open(args.train_src_path, 'r', encoding='utf-8') as f1:
        train_src = f1.readlines()
        train_src = [line.strip("\n") for line in train_src]
    with open(args.train_tgt_path, 'r', encoding='utf-8') as f2:
        train_tgt = f2.readlines()
        train_tgt = [line.strip("\n") for line in train_tgt]
    train_tgt = replace(train_tgt, args.train_json_path)
    for i in range(len(train_src)):
        dict = {}
        dict["src"] = train_src[i]
        dict["tgt"] = train_tgt[i]
        train.append(dict)

    # valid
    with open(args.valid_src_path, 'r', encoding='utf-8') as f3:
        valid_src = f3.readlines()
        valid_src = [line.strip("\n") for line in valid_src]
    with open(args.valid_tgt_path, 'r', encoding='utf-8') as f4:
        valid_tgt = f4.readlines()
        valid_tgt = [line.strip("\n") for line in valid_tgt]
    valid_tgt = replace(valid_tgt, args.valid_json_path)
    for i in range(len(valid_src)):
        dict = {}
        dict["src"] = valid_src[i]
        dict["tgt"] = valid_tgt[i]
        valid.append(dict)

    # test
    with open(args.test_src_path, 'r', encoding='utf-8') as f5:
        test_seen_fs_src = f5.readlines()
        test_seen_fs_src = [line.strip("\n") for line in test_seen_fs_src]
    with open(args.test_tgt_path, 'r', encoding='utf-8') as f6:
        test_seen_fs_tgt = f6.readlines()
        test_seen_fs_tgt = [line.strip("\n") for line in test_seen_fs_tgt]
    test_seen_fs_tgt = replace(test_seen_fs_tgt, args.test_json_path)
    for i in range(len(test_seen_fs_tgt)):
        dict = {}
        dict["src"] = test_seen_fs_src[i]
        dict["tgt"] = test_seen_fs_tgt[i]
        test.append(dict)

    final_dict = {}
    final_dict["train"] = train
    final_dict["valid"] = valid
    final_dict["test"] = test
    final_str = json.dumps(final_dict, indent=4, ensure_ascii=False)
    with open('adaptive1.json','w', encoding='utf-8') as f:
        f.write(final_str)



