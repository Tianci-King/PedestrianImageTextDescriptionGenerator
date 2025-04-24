# 用于生成行人文本描述
# 读取数据集路径为../../Market1501/bounding_box_train
# 每张图片单独的生成的文本描述存储在generated_txt文件夹中，以图片名为文件名保存
# 汇总的生成结果保存在CompletePedestrianTextDescription.json中
# 生成的文本描述包括图片名、文本描述、图片的base64编码

import os
import json
import Tools.main as tools
# import Tools.prompt_chaining_tiddec_final as prompts
import Tools.prompt_tiddec_0307 as prompts

train_folder = "../../Market1501/bounding_box_train"
N=200

if __name__ == "__main__":
    for i, filename in enumerate(os.listdir(train_folder), start=2):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"{filename} is not an image, skip.")
            continue

        # Current image path.
        image_path = os.path.join(train_folder, filename)

        # Subdirectory for storing the results of generating pedestrian text descriptions.
        # Each txt file corresponds to the description of an image.
        result_folder = "generated_txt"
        os.makedirs(result_folder, exist_ok=True)

        # File path for storing the results of generating pedestrian text descriptions.
        result_path = os.path.join(result_folder, f"{filename}.txt")

        # If the file already exists and the content is not empty, skip.
        # Avoid redundant generation of the same image.
        if os.path.exists(result_path) and os.path.getsize(result_path) > 400:
            print(f"{result_path} has already been generated, skip.")
            continue

        # Generating pedestrian text descriptions using prompt chaining.
        print(f"----------{result_path} start----------")
        print("----------step 1----------")
        step11 = tools.prompt_chain(image_path, prompts.prompt11)
        step12 = tools.prompt_chain(image_path, prompts.prompt12, step11)
        print("----------step 2----------")
        step2 = tools.prompt_chain(image_path, prompts.prompt2, step12)
        print("----------step 3----------")
        step31 = tools.prompt_chain(image_path, prompts.prompt31, step2)
        result = step31
        print(f"----------{result_path} end----------")

        # Base64 encoding of generated pedestrian images.
        image_base64 = tools.encode_image(image_path)

        # Save the generated results to a data dictionary.
        data = {
            "image_name": filename,
            "description": result,
            # "image_base64": image_base64,
        }

        # Save the generated results to a txt file.
        file = open(result_path, "w")
        print(result, file=file)
        file.close()

        # Save the generated results to a json file.
        output_file = "CompletePedestrianTextDescription.json"
        if not os.path.exists(output_file):
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump([data], f, indent=4)
        else:
            with open(output_file, "r", encoding="utf-8") as f:
                old_data = json.load(f)
            with open(output_file, "w", encoding="utf-8") as f:
                old_data.append(data)
                json.dump(old_data, f, indent=4)
                # Break the loop if needed images have been generated.
                print(f"{len(old_data)} images have been generated.")
                if len(old_data) == N:
                    print("All images have been generated.")
                    break
