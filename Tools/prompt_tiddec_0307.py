# 第一个任务 生成文本描述 用到的 prompt 汇总
# 注释掉的的 prompt 都是上一版本迭代前的 prompt 保留可能有作用
# 使用 prompt chaining 每一个 chain 都是一个变量
prompt11 = {
    "clothing": {
        "task_type": "Describe the clothing of the target pedestrian.",
        "instructions": "Describe the pedestrian's clothing by checking its color, texture, and type in sequence. If no clothing is detected, output 'This part is none'. Follow the steps in order without repeating previous descriptions.",
        "steps": [
            {
                "task_type": "Describe the clothing color.",
                "instructions": "Describe the dominant color or color combination of the clothing. If multiple colors or patterns are observed, mention them, but do not repeat texture or pattern details from the next step.",
                "do": "Use specific terms like 'a red jacket,' 'a pair of black and white pants,' or 'a blue and green shirt.'",
                "don't": "Avoid vague descriptions like 'normal color' or 'plain,' and do not mention texture or pattern in this step.",
                "examples": "Example: 'The pedestrian is wearing a bright yellow sweater.'",
                "user_context": "The user needs to identify the clothing color for recognition or profiling purposes.",
            },
            {
                "task_type": "Describe the clothing texture or pattern.",
                "instructions": "After identifying the color, focus on describing the texture or pattern of the clothing, such as smooth, rough, striped, or patterned. Do not repeat color descriptions from the previous step.",
                "do": "Mention specific textures like 'smooth cotton,' 'silk with floral prints,' or 'denim with a distressed look.'",
                "don't": "Avoid over-description, such as texture., and avoid vague terms like 'regular texture.'",
                "examples": "Example: 'The shirt has a soft cotton texture with a plaid pattern.'",
                "user_context": "The user is analyzing the pedestrian's clothing texture or pattern for identification purposes.",
            },
            {
                "task_type": "Describe the clothing type.",
                "instructions": "Finally, identify the type of clothing. Be specific and categorize the clothing as accurately as possible, such as jackets, dresses, pants, etc. Avoid using overly broad terms.",
                "do": "Use specific terms like 'a long-sleeved shirt,' 'a jacket,' 'a dress,' or 'a pair of knee-length shorts'",
                "don't": "Avoid vague descriptions like 'outfit' or 'clothes' without specific categorization.",
                "examples": "Example: 'The pedestrian is wearing a jacket over a T-shirt and jeans.'",
                "user_context": "The user needs to classify the pedestrian's clothing for recognition or profiling.",
            },
        ],
    },
    "gender_expression": {
        "task_type": "Describe the perceived gender of the target pedestrian.",
        "instructions": "Base your description on visible attributes such as clothing, appearance, and general societal gender norms, while remaining respectful and neutral. If the gender cannot be determined, output 'This part is none'.",
        "do": "Provide simple descriptors such as 'male' or 'female' based on visible cues.",
        "don't": "Avoid assumptions or using disrespectful or non-neutral language. Do not attempt to make complex judgments beyond the basic gender identification.",
        "examples": "Example: 'The pedestrian appears male, wearing a t-shirt and jeans.' Another example: 'The pedestrian appears female, with a dress and long hair.' If gender cannot be identified, output 'This part is none'",
        "user_context": "The user requires an unbiased observation of gender for identification purposes.",
    },
    "body_type": {
        "task_type": "Characterize the pedestrian's body type.",
        "instructions": "Describe the body type in terms of build, using terms like slim, average, or broad.",
        "do": "Provide a concise and clear categorization based on visual assessment.",
        "don't": "Avoid using judgmental or inappropriate descriptors.",
        "examples": "Example: 'The person has a broad build with a muscular frame.'",
        "user_context": "The user requires a neutral description for identification.",
    },
    "wearing_hat": {
        "task_type": "Indicate if the pedestrian is wearing a hat.",
        "instructions": "First, check if the pedestrian is wearing a hat. If no hat is detected, output 'This part is none'. If a hat is present, follow these steps: 1) Describe the hat's color and type 2) Describe its texture/pattern without repeating color/type info.",
        "steps": [
            {
                "task_type": "Describe the color and type of the hat.",
                "instructions": "Identify both the dominant color and specific hat type. Do not mention texture/pattern. Ensure type and color are distinct elements.",
                "do": "Combine color + type: 'navy blue baseball cap', 'khaki bucket hat', 'white wide-brim sunhat'",
                "don't": "Avoid vague terms like 'a hat' - specify type. Don't mention material/texture.",
                "examples": [
                    "The person wears a crimson beret",
                    "A charcoal gray fedora is visible",
                    "Bright yellow construction helmet"
                    ],
                "user_context": "The user needs to identify the color and type of the hat for focused observation.",
            },
            {
                "task_type": "Describe the texture or pattern of the hat.",
                "instructions": "Describe the texture or pattern of the hat. Do not repeat the color and type information from the previous step. If no hat is detected, output 'This part is none'.",
                "do": "Describe patterns or textures like 'woven straw', 'cotton fabric', or 'striped design'.",
                "don't": "Do not mention the color and type of the hat again in this step.",
                "examples": "Example: 'The hat is made of woven straw.The brim of the hat is wider.'",
                "user_context": "The user needs to identify patterns or textures on the hat for focused observation.",
            },
        ],
    },
    "carrying_bag": {
        "task_type": "Describe the bag the pedestrian is carrying, including its color, type and texture.",
        "instructions": "First, check if the pedestrian is carrying a bag. If no bag is detected, output 'This part is none'. If a bag is present, proceed with the following steps: First, describe the color and type of the bag, focusing on the primary color or color combination. Then, describe the pattern or texture of the bag without repeating the color and type information from the previous step.",
        "steps": [
            {
                "task_type": "Describe the color and type of the bag.",
                "instructions": "Identify bag category and dominant color. Keep type and color as separate elements.",
                "do": "Combine color + type: Use terms like 'a red handbag' or 'a blue and yellow Shoulder bag.'. Distinguish the types of bags, such as backpack, shoulder bag, and handbag. If no bag is detected, output 'This part is none'.",
                "don't": "Avoid including texture or pattern descriptions, and do not repeat color information in subsequent steps.",
                "examples": "Example: 'The pedestrian is carrying an orange and black backpack.'",
                "user_context": "The user needs to identify the color of the bag for profiling purposes.",
            },
            {
                "task_type": "Describe the texture or pattern of the bag.",
                "instructions": "Only focus on the pattern or texture of the bag. Do not repeat the color information from the previous step. If no bag is detected, output 'This part is none'.",
                "do": "Describe patterns like 'floral print', 'striped design', or 'solid color'.",
                "don't": "Do not mention the color of the bag again in this step.",
                "examples": "Example: 'The bag has a floral print on it.'",
                "user_context": "The user needs to identify patterns or textures on the bag for profiling purposes.",
            },
        ],
    },
    "wearing_glasses": {
        "task_type": "Determine if the pedestrian is wearing glasses.",
        "instructions": "First, check if the pedestrian is wearing glasses. If glasses are not detected, output 'This part is none'. If glasses are detected, describe their type, style, and any distinguishing features.",
        "do": "Mention descriptors like 'round black frames' or 'rimless glasses with thin metal arms'.If no glasses are detected, output 'This part is none'",
        "don't": "Avoid stating only 'yes' or 'no' without details.",
        "examples": "Example: 'The pedestrian is wearing black glasses.' If no glasses are detected, output 'This part is none'",
        "user_context": "The user needs to identify eyewear as a distinguishing feature.",
    },
    # 围巾
    "wearing_scarf": {
        "task_type": "Describe the scarf worn by the pedestrian.",
        "instructions": "First check if the pedestrian is wearing a scarf. If no scarf is detected, output 'This part is none'. If a scarf is present, follow the steps: First describe the color, then describe the texture/material without repeating color information.",
        "steps": [
            {
                "task_type": "Describe the scarf color.",
                "instructions": "Identify the dominant color or color combination. Avoid mentioning texture/pattern in this step.",
                "do": "Use specific terms like 'a red scarf' or 'blue and white striped' (if stripes are part of color description).If no scarf is detected, output 'This part is none'.",
                "don't": "Do not mention material/texture or repeat color in next step",
                "examples": "Example: 'The scarf has alternating black and gray bands'",
                "user_context": "User needs color information for visual identification"
            },
            {
                "task_type": "Describe the scarf texture/material.",
                "instructions": "Focus on physical characteristics: thickness, material (wool/silk/etc) or surface patterns",
                "do": "Use terms like 'knitted wool', 'silk with paisley pattern', 'thin gauzy fabric'.If no scarf is detected, output 'This part is none'.",
                "don't": "Avoid repeating color information from previous step",
                "examples": "Example: 'The scarf appears to be a thick knitted material'",
                "user_context": "User needs to identify scarf material for detailed description"
            }
        ]
    },
    # 在骑自行车
    "transportation_bicycle": {
        "task_type": "Determine the pedestrian is riding a bicycle.",
        "instructions": "Check if the pedestrian is actively riding a bicycle. Confirm by: 1) Seated on bicycle 2) Hands gripping handlebars 3) At least one foot on pedal. If all conditions met, output affirmative. If bicycle is merely present (parked/walked alongside) or not detected, output 'This part is none'.",
        "do": "Use binary output: either 'The pedestrian is riding a bicycle' or 'This part is none'",
        "don't": "Do not describe the bicycle's appearance or speculate about nearby bicycles",
        "examples": [
            "Affirmative: 'The pedestrian is riding a bicycle'",
            "Rejected (parked): 'This part is none'",
            "Rejected (walking): 'This part is none'"
        ],
        "user_context": "User needs to identify the pedestrian is riding a bicycle for pedestrian's status"
    },
    # 在骑电动车
    "transportation_electric_vehicle": {
        "task_type": "Determine the pedestrian is riding a electric vehicle.",
        "instructions": "Check if the pedestrian is actively riding a electric vehicle. Confirm by: 1) Seated on electric vehicle 2) Hands gripping handlebars 3) At least one foot on pedal. If all conditions met, output affirmative. If bicycle is merely present (parked/walked alongside) or not detected, output 'This part is none'.",
        "do": "Use binary output: either 'The pedestrian is riding a electric vehicle' or 'This part is none'",
        "don't": "Do not describe the electric vehicle's appearance or speculate about nearby electric vehicle",
        "examples": [
            "Affirmative: 'The pedestrian is riding a electric vehicle'",
            "Rejected (parked): 'This part is none'",
            "Rejected (walking): 'This part is none'"
        ],
        "user_context": "User needs to identify the pedestrian is riding a electric vehicle for pedestrian's status"
    }
}

prompt12 = {
    "light_color_temperature": {
        "task_type": "Describe the light color temperature in the surrounding environment.",
        "instructions": "Identify whether the light appears cool (bluish), warm (yellowish), or neutral. Mention any notable lighting sources if visible.",
        "do": "Provide specific details about the color tone and any variations across the environment.",
        "don't": "Avoid vague terms like 'normal' or 'standard' without further clarification.",
        "examples": "Example: 'The light in the area appears warm, with a yellowish hue from overhead streetlights.'",
        "user_context": "The user is analyzing lighting conditions for environmental assessment or identification.",
    },
    "obstructions": {
        "task_type": "Determine if the target pedestrian is partially obstructed by objects.",
        "instructions": "First, check if the pedestrian is obstructed by any objects. If no obstruction is detected, output 'This part is none'. If there are obstructions, describe them, including their type, size, and position relative to the pedestrian.",
        "do": "Provide clear descriptions such as 'a car blocks the lower body of the pedestrian' or 'the fence blocks the lower body of the pedestrian.'",
        "don't": "Avoid omitting details or using vague terms like 'some objects' without specification.",
        "examples": "Example: 'a car blocks the lower body of the pedestrian' If no obstruction is detected, output 'This part is none'",
        "user_context": "The user is focusing on potential visual barriers affecting observation of the pedestrian.",
    },
    "background": {
        "task_type": "Describe the target pedestrian's location and surrounding context.",
        "instructions": "First, check the pedestrian's specific location. Then, describe their immediate surroundings, highlighting any significant environmental elements or landmarks nearby. If no notable context can be identified, output 'This part is none'.",
        "do": "Provide detailed descriptions such as 'standing on the sidewalk' or 'there are trees around'",
        "don't": "Avoid vague generalizations like 'outdoors' or 'on a street' without elaborating.",
        "examples": "Example: 'There is a row of bicycles next to the pedestrian.' If no specific location can be identified, output 'This part is none'",
        "user_context": "The user needs to understand the pedestrian's precise location and its environmental context for situational awareness.",
    },
}

prompt2 = {
    "gestures": {
        "task_type": "Describe the gestures or hand movements made by the target pedestrian.",
        "instructions": "First, check if the pedestrian is making any hand gestures or movements. If no gestures are detected, output 'This part is none'. If gestures are present, describe the specific movement or action clearly",
        "do": "Provide clear descriptions of the gestures. Include any relevant context, such as the hand position or interaction with objects. If no gestures are detected, output 'This part is none'",
        "don't": "Avoid vague terms like 'moving hands' without further clarification. Do not generalize without providing specific details of the action.",
        "examples": "Example: 'The pedestrian raised his left hand above his head'. Another example: 'The pedestrian is carrying something in his hand'. If no gestures are detected, output 'This part is none'",
        "user_context": "The user is analyzing the pedestrian's actions or intentions based on hand gestures.",
    },
        "body_language": {
        "task_type": "Interpret the body language of the target pedestrian.",
        "instructions": "First, check for visible body language cues that suggest the pedestrian's mood or demeanor. If no discernible body language is detected, output 'This part is none'. If body language is observed, describe the overall posture, movements, and any specific gestures or positions that indicate the pedestrian's state, such as relaxed, tense, confident, or other observable cues.",
        "do": "Provide specific observations like 'the pedestrian looks relaxed, walking normally' or 'tense, running posture'. Focus on physical cues and avoid interpreting emotions without clear physical indicators. If no body language cues are detected, the output should be 'This part is none.'",
        "don't": "Avoid making assumptions about emotions or internal states without clear, visible physical cues. Do not generalize based on minimal body language information.",
        "examples": "Example: 'This pedestrian is walking relaxedly'. Another example: 'This pedestrian is running anxiously'. If no body language cues are detected, the output should be 'This part is none'",
        "user_context": "The user is seeking to infer the pedestrian's mood or attitude through body language.",
    },
    "walking_posture": {
        "task_type": "Describe the walking posture and movement of the target pedestrian.",
        "instructions": "First, assess the pedestrian's walking movement. If no walking movement is detected, output 'This part is none'. If walking, describe the pedestrian's posture, including body alignment, speed, and any significant patterns like leaning or irregular movement. Additionally, include details about arm movements and head position, such as arm swings or whether the head is tilted or looking around.",
        "steps": [
            {
                "task_type": "Describe the body posture during walking.",
                "instructions": "Describe the alignment of the pedestrian's body as they walk, such as whether they are walking straight, slightly leaning forward, or tilted in any direction. If there are any signs of imbalance or irregular posture, mention them.",
                "do": "Provide detailed descriptions like 'the pedestrian is walking with a slight forward lean' or 'the pedestrian's body is upright with minimal lean.'",
                "don't": "Avoid generalizations like 'walking normally' or 'straight posture' without further clarification.",
                "examples": "Example: 'The pedestrian is walking with a slight forward lean'",
                "user_context": "The user needs a clear understanding of the pedestrian's walking posture for movement or behavior analysis.",
            },
            {
                "task_type": "Describe the arm movements during walking.",
                "instructions": "Observe the pedestrian's arm movement while walking. Note if the arms are swinging naturally, held tightly to the body, or moving in an irregular or unusual way.",
                "do": "Describe specific arm movements like 'arms are swinging naturally' or 'arms are held close to the body.' If the arm movement is erratic or unusual, mention it.",
                "don't": "Avoid vague terms like 'arms are moving' without describing the nature of the movement.",
                "examples": "Example: 'The pedestrian's arms are swinging naturally in rhythm with their walking.'",
                "user_context": "The user needs to understand the pedestrian's arm movement to infer behavioral context or intentions.",
            },
            {
                "task_type": "Describe the head position during walking.",
                "instructions": "Evaluate the pedestrian's head position during walking. Observe if they are looking straight ahead, looking down, or scanning the environment.",
                "do": "Describe the head position clearly, such as 'the pedestrian's head is held high and they are looking straight ahead' or 'the pedestrian's head is tilted down, focusing on the ground.'",
                "don't": "Avoid vague descriptions like 'normal head position' without specifying the position or focus.",
                "examples": "Example: 'The pedestrian's head is tilted slightly upward'",
                "user_context": "The user needs to understand the pedestrian's head position to assess their situational awareness or behavior.",
            },
        ],
        "don't": ""
    },
}

prompt31 = {
    "behavior": {
        "task_type": "Analyze the behavior of the pedestrian based on static attributes.",
        "instructions": "Interpret the pedestrian's actions, gestures, and movements to describe their potential behaviors, intentions, or state of mind. Focus on static (e.g., posture)",
        "do": "Clearly require the analysis of behavior from both a static (such as posture) perspective to more comprehensively understand the target behavior.If no clear behavioral indicators are observed, output 'This part is none'",
        "don't": "Avoid overly subjective interpretation.",
        "examples": "Example: 'This pedestrian is carrying a table.' Another example: 'The pedestrian is waving'. If no clear behavioral indicators are observed, output 'This part is none'",
        "user_context": "The user is identifying behavioral patterns for situational or contextual analysis.",
    },
    "color_difference": {
        "task_type": "Detect color alterations in the pedestrian's appearance caused by environmental lighting.",
        "instructions": "Analyze how light conditions (e.g. shadows, artificial lights, sunlight) physically alter the perceived color of the pedestrian's clothing, skin, or accessories. Focus on light-induced phenomena like: color desaturation/saturation, hue shifting, brightness changes, or specular reflections that modify the original color properties.",
        "do": [
            "Identify specific lighting sources (e.g. neon signs, car headlights, sunset glow) affecting the pedestrian",
            "Describe color transformations using physical optics terms (e.g. 'the cyan jacket shows greenish tint under sodium-vapor lighting')",
            "Differentiate between material properties and lighting effects (e.g. 'reflective strips are glowing due to direct light exposure, not their inherent color')",
            "Note lighting gradients (e.g. 'the left sleeve appears darker as it moves into shadow')"
        ],
        "don't": [
            "Compare pedestrian's color with environment/other objects",
            "Mention visibility/contrast for detection purposes",
            "Assume original color without lighting evidence",
            "Describe environmental lighting without linking to pedestrian's appearance"
        ],
        "examples": [
            "The pedestrian's navy blue pants exhibit purple highlights where direct sunlight reflects off synthetic fabric texture.",
            "Overcast sky causes the orange safety vest to lose chromatic intensity, appearing closer to pale yellow.",
            "Fluorescent store lighting adds a green cast to the white sneakers, particularly noticeable in toe areas facing the light source."
        ],
        "user_context": "Accurate color perception analysis for applications requiring lighting-invariant recognition, where environmental illumination may distort true color values."
    }

}
