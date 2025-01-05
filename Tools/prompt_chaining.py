# Step 1: Static Attribute Space
#
# 	1.	Pedestrian Attributes
# 	•	Clothing Color: “What is the color of the target pedestrian’s clothing? Please specify if there are multiple colors.”
# 	•	Clothing Texture: “Describe the texture or pattern of the target pedestrian’s clothing (e.g., striped, solid, checkered).”
# 	•	Clothing Type: “What type of clothing is the target pedestrian wearing (e.g., jacket, dress, pants)?”
# 	•	Gender Expression: “What is the target pedestrian’s perceived gender expression?”
# 	•	Height: “How would you describe the target pedestrian’s height—tall, short, or average?”
# 	•	Body Type: “What is the target pedestrian’s body type—slim, average, or broad?”
# 	•	Wearing a Hat?: “Is the target pedestrian wearing a hat? If so, what type and color?”
# 	•	Carrying a Backpack?: “Is the target pedestrian carrying a backpack? If yes, describe its type and color.”
# 	•	Wearing Glasses?: “Is the target pedestrian wearing glasses? If so, what type and style?”
#
# 	2.	Environmental Properties
# 	•	Light Color Temperature: “What is the light color temperature in the surrounding environment—cool (bluish), warm (yellowish), or neutral?”
# 	•	Obstructions: “Is the target pedestrian partially obstructed by any objects (e.g., trees, buildings, vehicles)? If so, what is obstructing them?”
# 	•	Location Context: “What is the target pedestrian’s location? Are there any notable environmental elements nearby?”
# 	•	Crowds: “How dense is the crowd around the target pedestrian?”
# 	•	Vehicles: “Are there any vehicles nearby? If so, what types of vehicles are present?”
# 	•	Signage: “Are there any visible signs or landmarks near the target pedestrian?”
#
# Step 2: Dynamic Attribute Space
#
# 	1.	Pedestrian Dynamics
# 	•	Gestures: “What gestures or hand movements is the target pedestrian making (e.g., waving, pointing, holding)?”
# 	•	Body Language: “What does the target pedestrian’s body language suggest (e.g., relaxed, tense, confident)?”
# 	•	Walking Posture: “How would you describe the target pedestrian’s walking posture—normal, slow, hurried, or irregular?”
#
# Step 3: Analytical Space
#
# 	1.	Pedestrian Analysis
# 	•	Behavior: “Based on the pedestrian’s static and dynamic attributes, what behavior might they be exhibiting (e.g., shopping, commuting, sightseeing)?”
# 	•	Color Contrast: “Does the target pedestrian stand out due to a noticeable color contrast with their surroundings or other pedestrians?”
# 	•	Obscured Elements: “If parts of the pedestrian are obscured, can you infer what the missing elements might be (e.g., a hidden bag or device)?”
# 	•	Physical State: “What does the target pedestrian’s physical state suggest (e.g., tired, energetic, injured)?”
# 	•	Emotional State: “What is the target pedestrian’s emotional state based on their expressions and body language (e.g., happy, frustrated, neutral)?”
# 	2.	Environment Analysis
# 	•	“Considering the environmental properties, describe the pedestrian’s interaction with the surroundings (e.g., standing in a crowded marketplace, crossing a busy road, waiting at a bus stop).”

prompt11 = {
    "clothing_color": "What is the color of the target pedestrian's clothing? Please specify if there are multiple colors.",
    "clothing_texture": "Describe the texture or pattern of the target pedestrian's clothing.",
    "clothing_type": "What type of clothing is the target pedestrian wearing?",
    "gender_expression": "What is the target pedestrian's perceived gender expression?",
    "height": "How would you describe the target pedestrian's height—tall, short, or average?",
    "body_type": "What is the target pedestrian's body type—slim, average, or broad?",
    "wearing_hat": "Is the target pedestrian wearing a hat? If so, what type and color?",
    "carrying_backpack": "Is the target pedestrian carrying a bag? If yes, describe its type and color.",
    "wearing_glasses": "Is the target pedestrian wearing glasses? If so, what type and style?",
}

prompt12 = {
    "light_color_temperature": "What is the light color temperature in the surrounding : environment—cool (bluish), warm (yellowish), or neutral?",
    "obstructions": "Is the target pedestrian partially obstructed by any objects? If so, what is obstructing them?",
    "location_context": "What is the target pedestrian's location? Are there any notable environmental elements nearby?",
}

prompt13 = {
    "crowds": "How dense is the crowd around the target pedestrian?",
    "vehicles": "Are there any vehicles nearby? If so, what types of vehicles are present?",
    "signage": "Are there any visible signs or landmarks near the target pedestrian?",
}

prompt2 = {
    "gestures": "What gestures or hand movements is the target pedestrian making (e.g., waving, pointing, holding or any other gestures)?",
    "body_language": "What does the target pedestrian's body language suggest (e.g., relaxed, tense, confident or any other body language)?",
    "walking_posture": "How would you describe the target pedestrian's walking (e.g., posture—normal, slow, hurried, or irregular or any other walking posture)?",
}

prompt31 = {
    "behavior": "Based on the pedestrian's static and dynamic attributes, what behavior might they be exhibiting?",
    "color_contrast": "Does the target pedestrian stand out due to a noticeable color contrast with their surroundings or other pedestrians?",
    "obscured_elements": "If parts of the pedestrian are obscured, can you infer what the missing elements might be (e.g., a hidden bag or device or watch or small object)?",
    "physical_state": "What does the target pedestrian's physical state suggest (e.g., tired, energetic, injured or any other physical state)?",
    "emotional_state": "What is the target pedestrian's emotional state based on their expressions and body language (e.g., happy, frustrated, neutral or any other emotional state)?",
}

prompt32 = {
    "environment_analysis": "Considering the environmental properties, describe the pedestrian's interaction with the surroundings.Briefly summarize. Do not break lines."
}

# 以下是测试 prompt

prompt = """
Step 1: Static Attribute Space

    1.	Pedestrian Attributes
	•	Clothing Color: “What is the color of the target pedestrian’s clothing? Please specify if there are multiple colors.”
	•	Clothing Texture: “Describe the texture or pattern of the target pedestrian’s clothing (e.g., striped, solid, checkered).”
	•	Clothing Type: “What type of clothing is the target pedestrian wearing (e.g., jacket, dress, pants)?”
	•	Gender Expression: “What is the target pedestrian’s perceived gender expression?”
	•	Height: “How would you describe the target pedestrian’s height—tall, short, or average?”
	•	Body Type: “What is the target pedestrian’s body type—slim, average, or broad?”
	•	Wearing a Hat?: “Is the target pedestrian wearing a hat? If so, what type and color?”
	•	Carrying a Backpack?: “Is the target pedestrian carrying a backpack? If yes, describe its type and color.”
	•	Wearing Glasses?: “Is the target pedestrian wearing glasses? If so, what type and style?”

	2.	Environmental Properties
	•	Light Color Temperature: “What is the light color temperature in the surrounding environment—cool (bluish), warm (yellowish), or neutral?”
	•	Obstructions: “Is the target pedestrian partially obstructed by any objects (e.g., trees, buildings, vehicles)? If so, what is obstructing them?”
	•	Location Context: “What is the target pedestrian’s location? Are there any notable environmental elements nearby?”
	•	Crowds: “How dense is the crowd around the target pedestrian?”
	•	Vehicles: “Are there any vehicles nearby? If so, what types of vehicles are present?”
	•	Signage: “Are there any visible signs or landmarks near the target pedestrian?”

Step 2: Dynamic Attribute Space

	1.	Pedestrian Dynamics
	•	Gestures: “What gestures or hand movements is the target pedestrian making (e.g., waving, pointing, holding)?”
	•	Body Language: “What does the target pedestrian’s body language suggest (e.g., relaxed, tense, confident)?”
	•	Walking Posture: “How would you describe the target pedestrian’s walking posture—normal, slow, hurried, or irregular?”

Step 3: Analytical Space

	1.	Pedestrian Analysis
	•	Behavior: “Based on the pedestrian’s static and dynamic attributes, what behavior might they be exhibiting (e.g., shopping, commuting, sightseeing)?”
	•	Color Contrast: “Does the target pedestrian stand out due to a noticeable color contrast with their surroundings or other pedestrians?”
	•	Obscured Elements: “If parts of the pedestrian are obscured, can you infer what the missing elements might be (e.g., a hidden bag or device)?”
	•	Physical State: “What does the target pedestrian’s physical state suggest (e.g., tired, energetic, injured)?”
	•	Emotional State: “What is the target pedestrian’s emotional state based on their expressions and body language (e.g., happy, frustrated, neutral)?”
	2.	Environment Analysis
	•	“Considering the environmental properties, describe the pedestrian’s interaction with the surroundings (e.g., standing in a crowded marketplace, crossing a busy road, waiting at a bus stop).”

Answer in more detail.
"""

prompt_bag = "Carrying a Backpack?: “Is the target pedestrian carrying a bag? If yes, describe its type and color.”"

prompt_second = """
"gestures": "What gestures or hand movements is the target pedestrian making (e.g., waving, pointing, holding or any other gestures)?",
"body_language": "What does the target pedestrian's body language suggest (e.g., relaxed, tense, confident or any other body language)?",
"walking_posture": "How would you describe the target pedestrian's walking (e.g., posture—normal, slow, hurried, or irregular or any other walking posture)?",
"behavior": "Based on the pedestrian's static and dynamic attributes, what behavior might they be exhibiting?",
"color_contrast": "Does the target pedestrian stand out due to a noticeable color contrast with their surroundings or other pedestrians?",
"obscured_elements": "If parts of the pedestrian are obscured, can you infer what the missing elements might be (e.g., a hidden bag or device or watch or small object)?",
"physical_state": "What does the target pedestrian's physical state suggest (e.g., tired, energetic, injured or any other physical state)?",
"emotional_state": "What is the target pedestrian's emotional state based on their expressions and body language (e.g., happy, frustrated, neutral or any other emotional state)?",
"environment_analysis": "Considering the environmental properties, describe the pedestrian's interaction with the surroundings.Briefly summarize. Do not break lines."
"""
