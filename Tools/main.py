import datetime
from openai import OpenAI
import base64
import Tools.system_prompt as system_prompt
import time

client = OpenAI(api_key="<KEY>")

# you can use the following code to load the API key from a .env file
# from dotenv import load_dotenv
# load_dotenv()

# or you can set the API key and base URL directly
# client.api_key = "your_api_key"
# client.base_url = "your_base_url"


# --------------------------------------------------------
def get_chat(text_to_input):
    """
    Returns a string output from the GPT-4 chat model given the input string.

    Args:
        text_to_input (str): The input string to be used to generate output from the GPT-4 chat model.

    Returns:
        str: The output string from the GPT-4 chat model.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": [{"type": "text", "text": text_to_input}]}
        ],
    )

    return response.choices[0].message.content


# --------------------------------------------------------


def get_embedding(text_to_embed):
    # Embed a line of text
    """
    Generates an embedding for the provided text using the specified model.

    Args:
        text_to_embed (str): The text string to be embedded.

    Returns:
        list[float]: A list of floating-point numbers representing the embedding of the input text.
    """
    attempt = 0
    max_retries = 20
    retry_delay = 3
    while attempt < max_retries:
        try:
            response = client.embeddings.create(
                model="text-embedding-ada-002", input=[text_to_embed]
            )
            # successful response
            embedding = response.data[0].embedding
            return embedding
        except Exception as e:
            print(f"try {attempt + 1}/{max_retries} failed with error: {e} \n retrying...")
            attempt += 1
            if attempt < max_retries:
                time.sleep(retry_delay)


# --------------------------------------------------------


# image to base64
def encode_image(image_path):
    """
    Encode an image file located at `image_path` as a base64 string.

    Args:
        image_path (str): The path to the image file to be encoded.

    Returns:
        str: The base64 encoded string of the image data.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def get_image_analysis_base64(base64_image, prompt):
    """
    Upload an image and generate a description or analysis using GPT-4 Vision.

    Args:
        image_path (str): The file path to the image to be analyzed.

    Returns:
        str: The output description or analysis of the image from GPT-4 Vision.
        :param base64_image:
        :param prompt:
    """
    attempt = 0
    max_retries = 10000
    retry_delay = 3
    while attempt < max_retries:
        try:
            response = client.chat.completions.create(
                model="gpt-4o",  # choose the model
                messages=[
                    {
                        "role": "system",
                        "content": str(system_prompt.system_prompt),
                    },
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": str(prompt)},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                },
                            },
                        ],
                    },
                ],
                temperature=0,
            )
            # successful response
            return response.choices[0].message.content
        except Exception as e:
            print(f"try {attempt + 1}/{max_retries} failed with error {e} \n retrying...")
            attempt += 1
            if attempt < max_retries:
                time.sleep(retry_delay)


def get_image_analysis(image_path, prompt):
    """
    Upload an image and generate a description or analysis using GPT-4 Vision.

    Args:
        image_path (str): The file path to the image to be analyzed.
        prompt (str): The prompt to give to the model to generate the description or analysis.

    Returns:
        str: The output description or analysis of the image from GPT-4 Vision.
    """
    image2base64 = encode_image(image_path)
    return get_image_analysis_base64(image2base64, prompt)


# --------------------------------------------------------


def prompt_chain(image_path, follow_up_prompts, previous_prompt=""):
    response = previous_prompt

    for i, key in enumerate(follow_up_prompts, 1):
        prompt = follow_up_prompts[key]
        print(f"Step {i} key: {key} ; prompt: {prompt}")

        if previous_prompt == "":
            full_prompt = f"Analyze the following issues: {prompt}. \n\n Take a deep breath and work on this problem step-by-step.Output directly without any additional explanation.No line breaks, no dot breaks, no markdown. "
        else:
            full_prompt = f"Base on the description of the Previous OutPut: {previous_prompt},\n\n Analyze the following issues: {prompt}. \n\n Take a deep breath and work on this problem step-by-step.Output directly without any additional explanation.No line breaks, no dot breaks, no markdown. "
        result = get_image_analysis(image_path, full_prompt)
        if result is None:
            return f"Prompt {i} failed."
        print(f"Step {i} output: {result}\n")
        response += f"{result}\n"
    return response


# -------------------------------------------------------------
def get_image_base64(prompt_temp):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_temp,
        quality="hd",
        response_format="b64_json",
        size="1024x1024",
        style="natural",
    )

    img = response.data[0].b64_json
    img_data = base64.b64decode(img)
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"{current_time}-img.jpg"
    with open(output_file, "wb") as f:
        f.write(img_data)
    return img_data


def get_image_url(prompt_temp):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt_temp,
        quality="hd",
        response_format="url",
        size="1024x1024",
        style="natural",
    )

    return response.data[0].url