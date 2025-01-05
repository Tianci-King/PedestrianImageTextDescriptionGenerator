import os
import json
import Tools.main as tools
import Tools.prompt_chaining_tiddec_final as prompts

train_folder = "../Market1501/bounding_box_train"

if __name__ == "__main__":
    for i, filename in enumerate(os.listdir(train_folder), start=2):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"{filename} is not an image, skip.")
            continue

        # Current image path.
        image_path = os.path.join(train_folder, filename)

        # Subdirectory for storing the results of generating pedestrian text descriptions.
        # Each txt file corresponds to the description of an image.
        result_folder = "generated_result"
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

        # Determine whether the pedestrian's color appears altered due to environmental lighting.
        color_dif = tools.get_image_analysis(
            image_path,
            """
            "color_difference_yes_or_no": {
                "task_type": "Determine if the pedestrian's color appears altered due to environmental lighting.",
                "instructions": "Assess whether the pedestrian's clothing, accessories, or appearance appear different in color due to the surrounding light conditions. For example, lighting could cause colors to appear lighter, darker, or shift to a different hue. Focus on whether the color change is noticeable due to lighting and respond with 'yes' or 'no'.",
                "do": "Respond with 'yes' if there is a noticeable color shift due to lighting, and 'no' if there is no noticeable color change. All lowercase.",
                "don't": "Do not provide any additional descriptions or explanations. Only respond with 'yes' or 'no' ",
                "examples": "Example: yes Another example: no",
                "user_context": "The user is evaluating how environmental lighting affects the pedestrian's color perception for recognition, safety, or situational analysis.",
            },
            """,
        )

        # Base64 encoding of generated pedestrian images.
        image_base64 = tools.encode_image(image_path)

        # Save the generated results to a data dictionary.
        data = {
            "image_name": filename,
            "description": result,
            "color_dif": color_dif,
            "image_base64": image_base64,
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
