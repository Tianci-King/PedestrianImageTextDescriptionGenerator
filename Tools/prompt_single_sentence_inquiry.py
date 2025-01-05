# 与 tiddec 文件中的 prompt 保持一致 区别只是不携带链上之前输出的信息而已

# prompt11 = {
#     "clothing_color": "What is the color of the target pedestrian's clothing? Please specify if there are multiple colors.",
#     "clothing_texture": "Describe the texture or pattern of the target pedestrian's clothing.",
#     "clothing_type": "What type of clothing is the target pedestrian wearing?",
#     "gender_expression": "What is the target pedestrian's perceived gender expression?",
#     "height": "How would you describe the target pedestrian's height—tall, short, or average?",
#     "body_type": "What is the target pedestrian's body type—slim, average, or broad?",
#     "wearing_hat": "Is the target pedestrian wearing a hat? If so, what type and color?",
#     "carrying_backpack": "Is the target pedestrian carrying a bag? If yes, describe its type and color.",
#     "wearing_glasses": "Is the target pedestrian wearing glasses? If so, what type and style?",
# }
prompt11 = {
    "clothing_color": {
        "task_type": "Describe the clothing color of the target pedestrian.",
        "instructions": "Detail all visible colors of the clothing, including any combinations, gradients, or patterns present.",
        "do": "Provide a clear and detailed description of the colors, mentioning if multiple colors or unique combinations are used.",
        "don't": "Avoid vague terms like 'normal' or 'plain' without additional clarification.",
        "examples": "Example: 'The shirt is light blue with white polka dots, and the pants are solid black.'",
        "user_context": "The user is looking to distinguish the pedestrian by their clothing's color characteristics.",
    },
    "clothing_texture": {
        "task_type": "Identify the texture or pattern of the target pedestrian's clothing.",
        "instructions": "Focus on describing the feel or design of the clothing, such as smooth, rough, or specific patterns.",
        "do": "Mention details like 'cotton texture with striped patterns' or 'silky material with floral prints.'",
        "don't": "Avoid omitting texture details or generalizing as 'regular.'",
        "examples": "Example: 'The dress has a silky smooth texture with a paisley print in soft hues.'",
        "user_context": "The user is analyzing pedestrian clothing patterns for detailed identification.",
    },
    "clothing_type": {
        "task_type": "Specify the type of clothing the pedestrian is wearing.",
        "instructions": "Clearly categorize the clothing into types such as jackets, dresses, jeans, or formal attire.",
        "do": "Use specific terms like 'long-sleeved shirt,' 'denim jacket,' or 'pleated skirt.'",
        "don't": "Avoid vague terms like 'outfit' without categorization.",
        "examples": "Example: 'The person is wearing a black leather jacket over a white T-shirt and ripped jeans.'",
        "user_context": "The user needs to classify clothing types for recognition purposes.",
    },
    "gender_expression": {
        "task_type": "Describe the perceived gender expression of the target pedestrian.",
        "instructions": "Base your description on clothing, appearance, and cultural norms while remaining respectful.",
        "do": "Provide descriptors such as 'masculine,' 'feminine,' or 'androgynous.'",
        "don't": "Avoid making assumptions or using disrespectful language.",
        "examples": "Example: 'The pedestrian has an androgynous appearance with short hair and neutral-toned clothing.'",
        "user_context": "The user requires an unbiased observation of gender expression.",
    },
    "height": {
        "task_type": "Estimate the height of the pedestrian.",
        "instructions": "Provide a general categorization like tall, short, or average relative to others.",
        "do": "Use relative comparisons or numerical ranges if possible.",
        "don't": "Avoid overly specific measurements without context.",
        "examples": "Example: 'The individual appears to be tall, approximately 6 feet compared to others nearby.'",
        "user_context": "The user needs to estimate height for situational awareness.",
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
        "instructions": "Specify the type, color, and any distinguishing features of the hat.",
        "do": "Include descriptors like 'a red baseball cap with a logo' or 'a beige sunhat with a ribbon.'",
        "don't": "Avoid omitting details if a hat is visible.",
        "examples": "Example: 'The person is wearing a wide-brimmed straw hat with a navy ribbon.'",
        "user_context": "The user is identifying headwear for focused observation.",
    },
    "carrying_backpack": {
        "task_type": "Describe if the pedestrian is carrying a bag.",
        "instructions": "Mention the type, color, and other notable details of the bag.",
        "do": "Use specific terms like 'a black leather backpack with metal zippers' or 'a canvas tote bag with floral prints.'",
        "don't": "Avoid generalizing as 'a bag' without further description.",
        "examples": "Example: 'The individual is carrying a green hiking backpack with multiple compartments.'",
        "user_context": "The user needs to identify baggage for profiling purposes.",
    },
    "wearing_glasses": {
        "task_type": "Determine if the pedestrian is wearing glasses.",
        "instructions": "Describe the type, style, and any unique features of the glasses.",
        "do": "Mention descriptors like 'round black frames' or 'rimless glasses with thin metal arms.'",
        "don't": "Avoid stating only 'yes' or 'no' without details.",
        "examples": "Example: 'The pedestrian is wearing rectangular glasses with thick black frames.'",
        "user_context": "The user needs to identify eyewear as a distinguishing feature.",
    },
}


# prompt12 = {
#     "light_color_temperature": "What is the light color temperature in the surrounding : environment—cool (bluish), warm (yellowish), or neutral?",
#     "obstructions": "Is the target pedestrian partially obstructed by any objects? If so, what is obstructing them?",
#     "location_context": "What is the target pedestrian's location? Are there any notable environmental elements nearby?",
# }
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
        "instructions": "Describe any objects obstructing the pedestrian, including their type, size, and position relative to the pedestrian.",
        "do": "Provide clear descriptions such as 'a parked car partially blocks the lower half of the pedestrian.'",
        "don't": "Avoid omitting details or using vague terms like 'some objects' without specification.",
        "examples": "Example: 'The pedestrian is partially obstructed by a tree branch, covering their upper body.'",
        "user_context": "The user is focusing on potential visual barriers affecting observation of the pedestrian.",
    },
    "location_context": {
        "task_type": "Describe the target pedestrian's location and surrounding context.",
        "instructions": "Detail the pedestrian's specific location and highlight any notable environmental elements nearby.",
        "do": "Mention key details such as 'standing near a fountain in a busy plaza' or 'walking along a quiet residential street.'",
        "don't": "Avoid generalizing as 'in a park' or 'on a street' without elaboration.",
        "examples": "Example: 'The pedestrian is located at the corner of a bustling intersection, near a coffee shop with outdoor seating.'",
        "user_context": "The user needs to understand the pedestrian's precise location and its environmental context for situational awareness.",
    },
}

# prompt13 = {
#     "crowds": "How dense is the crowd around the target pedestrian?",
#     "vehicles": "Are there any vehicles nearby? If so, what types of vehicles are present?",
#     "signage": "Are there any visible signs or landmarks near the target pedestrian?",
# }
prompt13 = {
    "crowds": {
        "task_type": "Assess the density of the crowd around the target pedestrian.",
        "instructions": "Describe the crowd density in the area surrounding the pedestrian, using terms like sparse, moderate, or dense. Include any noticeable patterns of movement or clustering.",
        "do": "Provide clear and specific descriptions, such as 'a sparse crowd with a few people scattered' or 'a dense crowd gathered for an event.'",
        "don't": "Avoid vague descriptions like 'there are people' without quantifying or elaborating.",
        "examples": "Example: 'The crowd is moderately dense, with groups of 5–10 people moving together along the sidewalk.'",
        "user_context": "The user is evaluating the pedestrian's visibility or navigability within the crowd.",
    },
    "vehicles": {
        "task_type": "Identify the presence and types of vehicles near the pedestrian.",
        "instructions": "Note if vehicles are present, and specify their types, such as cars, buses, bicycles, or motorcycles. Mention their proximity to the pedestrian.",
        "do": "Describe the types and positions of vehicles clearly, such as 'two cars parked nearby and a bus approaching the pedestrian's location.'",
        "don't": "Avoid generalizations like 'there are vehicles' without detailing the types or their positions.",
        "examples": "Example: 'A delivery van is parked across the street, and a bicycle is stationed near the pedestrian.'",
        "user_context": "The user is interested in the vehicle-related context for situational analysis or safety concerns.",
    },
    "signage": {
        "task_type": "Identify visible signs or landmarks near the pedestrian.",
        "instructions": "Describe any visible signage, landmarks, or notable features in the area, such as street signs, advertisements, or architectural elements.",
        "do": "Include specific details like 'a stop sign at the corner' or 'a large billboard advertising a local restaurant.'",
        "don't": "Avoid vague references like 'some signs' without specifying their nature or position.",
        "examples": "Example: 'The pedestrian is near a street sign that reads 'Main St.,' and a historical marker is visible across the road.'",
        "user_context": "The user requires information about nearby landmarks or signage for orientation or contextual understanding.",
    },
}

# prompt2 = {
#     "gestures": "What gestures or hand movements is the target pedestrian making (e.g., waving, pointing, holding or any other gestures)?",
#     "body_language": "What does the target pedestrian's body language suggest (e.g., relaxed, tense, confident or any other body language)?",
#     "walking_posture": "How would you describe the target pedestrian's walking (e.g., posture—normal, slow, hurried, or irregular or any other walking posture)?",
# }
prompt2 = {
    "gestures": {
        "task_type": "Describe the gestures or hand movements made by the target pedestrian.",
        "instructions": "Identify any specific hand movements or gestures, such as waving, pointing, holding objects, or other noticeable actions.",
        "do": "Provide clear descriptions like 'the pedestrian is waving with their right hand' or 'holding a bag with both hands.'",
        "don't": "Avoid vague terms like 'moving hands' without further clarification of the action.",
        "examples": "Example: 'The pedestrian is pointing towards a nearby building while holding a phone in their other hand.'",
        "user_context": "The user is analyzing the pedestrian's actions or intentions based on hand gestures.",
    },
    "body_language": {
        "task_type": "Interpret the body language of the target pedestrian.",
        "instructions": "Describe the pedestrian's overall demeanor, such as relaxed, tense, confident, or other observable body language cues.",
        "do": "Provide observations like 'the pedestrian appears relaxed, leaning casually against a pole' or 'tense, with arms crossed and shoulders hunched.'",
        "don't": "Avoid making assumptions about emotions without clear physical indicators.",
        "examples": "Example: 'The pedestrian's confident stance, with hands on hips and a straight posture, suggests self-assurance.'",
        "user_context": "The user is seeking to infer the pedestrian's mood or attitude through body language.",
    },
    "walking_posture": {
        "task_type": "Describe the walking posture and movement of the target pedestrian.",
        "instructions": "Characterize the pedestrian's walking style, such as normal, slow, hurried, irregular, or other notable patterns.",
        "do": "Include specific descriptions like 'walking hurriedly with a slight forward lean' or 'moving slowly and shuffling their feet.'",
        "don't": "Avoid generalizations like 'walking normally' without additional context.",
        "examples": "Example: 'The pedestrian is walking briskly, looking straight ahead with purposeful strides.'",
        "user_context": "The user needs to understand the pedestrian's movement style for tracking or behavioral analysis.",
    },
}

# prompt31 = {
#     "behavior": "Based on the pedestrian's static and dynamic attributes, what behavior might they be exhibiting?",
#     "color_contrast": "Does the target pedestrian stand out due to a noticeable color contrast with their surroundings or other pedestrians?",
#     "obscured_elements": "If parts of the pedestrian are obscured, can you infer what the missing elements might be (e.g., a hidden bag or device or watch or small object)?",
#     "physical_state": "What does the target pedestrian's physical state suggest (e.g., tired, energetic, injured or any other physical state)?",
#     "emotional_state": "What is the target pedestrian's emotional state based on their expressions and body language (e.g., happy, frustrated, neutral or any other emotional state)?",
# }
prompt31 = {
    "behavior": {
        "task_type": "Analyze the behavior of the pedestrian based on static and dynamic attributes.",
        "instructions": "Interpret the pedestrian's actions and movements to describe potential behaviors or intentions.",
        "do": "Provide detailed observations such as 'the pedestrian is frequently checking their phone, indicating distraction' or 'walking in a zigzag pattern, suggesting possible aimlessness.'",
        "don't": "Avoid overly broad conclusions like 'acting normally' without specific examples.",
        "examples": "Example: 'The pedestrian is walking purposefully towards a shop, occasionally glancing at a shopping list.'",
        "user_context": "The user is identifying behavioral patterns for situational or contextual analysis.",
    },
    "color_contrast": {
        "task_type": "Determine if the pedestrian stands out due to color contrast.",
        "instructions": "Assess whether the pedestrian's clothing or appearance is visually distinct compared to their surroundings or other pedestrians.",
        "do": "Mention contrasts like 'a bright red jacket against a mostly muted background' or 'stands out due to neon-colored sneakers.'",
        "don't": "Avoid vague statements like 'they look different' without specifying the nature of the contrast.",
        "examples": "Example: 'The pedestrian's bright yellow hoodie stands out prominently in a crowd wearing darker colors.'",
        "user_context": "The user needs to identify visual distinctiveness for recognition or attention analysis.",
    },
    "obscured_elements": {
        "task_type": "Infer missing or obscured elements of the pedestrian's appearance or belongings.",
        "instructions": "Describe what might be obscured or hidden, using visible context clues to infer potential objects or features.",
        "do": "Provide plausible inferences like 'a bulge in the pocket suggests a concealed phone' or 'partially visible strap indicates a hidden backpack.'",
        "don't": "Avoid making baseless assumptions without any visual cues.",
        "examples": "Example: 'The pedestrian's left arm is obscured, but a visible strap suggests they might be carrying a bag.'",
        "user_context": "The user is focusing on identifying hidden or partially visible elements for detailed observation.",
    },
    "physical_state": {
        "task_type": "Describe the physical state of the pedestrian.",
        "instructions": "Observe the pedestrian's posture, movements, and expressions to infer their physical condition, such as tired, energetic, or injured.",
        "do": "Provide detailed descriptions like 'slouching and dragging their feet, suggesting tiredness' or 'energetically jogging with upright posture.'",
        "don't": "Avoid general terms like 'looks okay' without supporting details.",
        "examples": "Example: 'The pedestrian appears tired, as indicated by their slow pace and frequent pauses to rest.'",
        "user_context": "The user needs to assess the pedestrian's physical condition for monitoring or assistance purposes.",
    },
    "emotional_state": {
        "task_type": "Infer the emotional state of the pedestrian based on expressions and body language.",
        "instructions": "Describe emotions such as happy, frustrated, or neutral, supported by observable cues like facial expressions and gestures.",
        "do": "Provide specific observations like 'smiling and laughing with a companion, indicating happiness' or 'frowning and crossing arms, suggesting frustration.'",
        "don't": "Avoid assumptions without clear visual or behavioral evidence.",
        "examples": "Example: 'The pedestrian's furrowed brow and quick gestures suggest frustration, possibly due to a delay.'",
        "user_context": "The user is analyzing emotional cues for situational or interpersonal assessment.",
    },
}

# prompt32 = {
#     "environment_analysis": "Considering the environmental properties, describe the pedestrian's interaction with the surroundings.Briefly summarize. Do not break lines."
# }
prompt32 = {
    "environment_analysis": {
        "task_type": "Analyze the pedestrian's interaction with the surrounding environment.",
        "instructions": "Evaluate how the pedestrian is engaging with their surroundings, considering environmental properties such as terrain, weather, or nearby elements. Provide a brief, single-line summary.",
        "do": "Describe interactions succinctly, such as 'the pedestrian is walking carefully on a wet sidewalk while avoiding puddles.'",
        "don't": "Avoid overly detailed or multiline descriptions, and do not ignore the environmental context.",
        "examples": "Example: 'The pedestrian is standing under a tree to avoid light rain while glancing at their phone.'",
        "user_context": "The user is seeking a concise summary of the pedestrian's interaction with their environment for quick analysis or reporting.",
    },
}
