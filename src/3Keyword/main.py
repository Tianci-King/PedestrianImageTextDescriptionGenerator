# 用于生成关键词结构化数据
# 结果保存在keyword_segment.json中
from random import choices
import sys
import os
from os import path

d = path.dirname(__file__)
parent_path = os.path.dirname(os.path.dirname(d))
sys.path.append(parent_path)

import Tools.prompt_segmentation as prompt
import Tools.main as tools
import json
import copy

# 初始化关键词结构模板
KEYWORD_TEMPLATE = {
    "Upper Body Clothing": {
        "Clothing Color": "",
        "Clothing Material": "",
        "Clothing Type": "",
    },
    "Lower Body Clothing": {
        "Clothing Color": "",
        "Clothing Material": "",
        "Clothing Type": "",
    },
    "Pedestrian gender": "",
    "Pedestrian body type": "",
    "Wearing a hat": "",
    "Carrying a bag": "",
    "Wearing a scarf": "",
    "Wearing glasses": "",
    "Ambient lighting": "",
    "Pedestrian Behavior": "",
    "Pedestrian Posture": "",
    "Pedestrian arms": "",
    "Pedestrian head": "",
    "Presence of Transportation": "",
    "Color difference": "",
}

# 加载prompt列表（已拆分为prompt_1到prompt_14,一个prompt对应一个关键词）
PROMPT_LIST = [
    prompt.prompt_1,
    prompt.prompt_2,
    prompt.prompt_3,
    prompt.prompt_4,
    prompt.prompt_5,
    prompt.prompt_6,
    prompt.prompt_7,
    prompt.prompt_8,
    prompt.prompt_9,
    prompt.prompt_10,
    prompt.prompt_11,
    prompt.prompt_12,
    prompt.prompt_13,
    prompt.prompt_14,
    prompt.prompt_15
]


def merge_results(base_dict, new_dict):
    """深度合并字典，将 GPT生成的内容"""
    for key in new_dict:
        # 仅处理base_dict中存在的key
        if key not in base_dict:
            continue

        current_base = base_dict[key]
        current_new = new_dict[key]

        # 处理嵌套字典（Upper/Lower Body Clothing）
        if isinstance(current_base, dict) and isinstance(current_new, dict):
            for sub_key in current_new:
                # 仅当base子键值为空时更新
                if sub_key in current_base and current_base[sub_key] == "":
                    current_base[sub_key] = current_new[sub_key]

        # 处理字符串类型字段
        elif isinstance(current_base, str) and current_base == "":
            base_dict[key] = current_new


def choice(step):
    if step == 1:
        return [0]  # clothing
    elif step == 2:
        return [0]  # clothing
    elif step == 3:
        return [1]  # 年龄
    elif step == 4:
        return [2]  # clothing和年龄
    elif step == 5:
        return [3]  # hat
    elif step == 6:
        return [4]  # bag
    elif step == 7:
        return [5]  # glasses
    elif step == 8:
        return [9]  # 色温
    elif step == 9:  # behavior
        return [10, 11, 12, 13, 14, 15]
    elif step == 10:  # posture
        return [10, 11, 12, 13, 14, 15]
    elif step == 11:  # arms
        return [10, 11, 12, 13, 14, 15]
    elif step == 12:  # head
        return [10, 11, 12, 13, 14, 15]
    elif step == 13:  # transportation
        return [7, 8]
    elif step == 14:  # color difference
        return [16]
    elif step == 15:  # scarf
        return [6]


if __name__ == "__main__":
    outfile = "keyword_1060_c3s2_140994_00_500.json"
    if not os.path.exists(outfile):
        with open(outfile, "w") as file:
            json.dump([], file, indent=4)
    with open(outfile, "r") as file:
        data = json.load(file)

    start = len(data)
    flag = 0
    now = 0

    with open("/home/wtc/PedestrianImageTextDescriptionGenerator/src/3Keyword/1060_c3s2_140994_00_500.json", "r",
              encoding="utf-8") as f:
        input_text = json.load(f)

    for text in input_text:
        now += 1
        if flag < start:
            print(f"跳过第{now}个文本")
            flag += 1
            continue

        print(f"处理第{now}个文本")
        flag = False
        # 对当前文本切片
        text_lines = text["description"][:-1].split("\n")
        if len(text_lines) != 17:
            print(text["image_path"])
            flag = True

        keyword_result = copy.deepcopy(KEYWORD_TEMPLATE)
        response = ""
        # 分步提取每个属性
        for step, single_prompt in enumerate(PROMPT_LIST, 1):
            try:
                if not flag:
                    # 选择当前步骤所需要的描述所在的切片
                    input_description = ""
                    slice_list = choice(step)
                    for slice_index in slice_list:
                        input_description += text_lines[slice_index]
                    print("input_description:", input_description)
                else:
                    # 文本长度不符合要求，全部
                    input_description = text["description"]
                    print("input_description:", input_description)

                # 调用API获取单个属性结果
                response = tools.get_key(
                    single_prompt + "\nFollowing text:\n" + input_description
                )
                partial_result = json.loads(response)
                print("response:", response)
                # 深度合并结果
                merge_results(keyword_result, partial_result)
                print(f"步骤{step}/15 完成")
            except Exception as e:
                print(f"步骤{step}/15 出错: {str(e)}")
                print(response)
                continue

        # 构建最终结果
        new_json = {
            "image_name": text["image_path"],
            "description": text["description"],
            "keyword": keyword_result,
        }

        data.append(new_json)

        # 保存进度
        with open(outfile, "w") as file:
            json.dump(data, file, indent=4)
            print(f"当前已生成{len(data)}条数据")
