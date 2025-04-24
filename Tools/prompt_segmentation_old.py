# 第三个任务 关键词提取所用到的 prompt 汇总

# 1. Upper Body Clothing
prompt_1 = """Extract ONLY upper body clothing features from the text:
Upper Body Clothing
    Clothing Color (Upper Body): Extract FULL color descriptions including modifiers like "bright", "light", "dark", etc. (e.g., "bright green", "light blue"). Multiple colors should be space-separated without connectors.
    Clothing Material: Extract material terms only (e.g., "smooth", "cotton"). Output "none" if unspecified.
    Clothing Type: Standard base garment name (e.g., "shirt" from "short-sleeved plaid shirt").

Special Cases:
- For dresses: When "dress" is detected in description, fill both upper and lower body clothing sections with the same values.
- Multi-color: "red white" not "red and white"
- Preserve compound colors: "blue-green" → "blue-green"
- Never simplify "dark black" to "black"
- Never simplify "bright white" to "white" or "light white" to "white"

Example Input: "man in light grey wool sweater"
Output: 
{"Upper Body Clothing": {"Clothing Color": "light grey", "Clothing Material": "wool", "Clothing Type": "sweater"}}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Upper Body Clothing": {"Clothing Color":"", "Clothing Material":"", "Clothing Type":""}}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 2. Lower Body Clothing
prompt_2 = """Extract ONLY lower body clothing features:
Lower Body Clothing
    Clothing Color: Extract FULL color descriptions including modifiers like "bright", "light", "dark", etc. (e.g., "bright green", "light blue"). Multiple colors should be space-separated without connectors. (e.g., "dark black" not just "black").
    Clothing Material: Extract material terms only (e.g., "smooth"). Output "none" if unspecified.
    Clothing Type: Standard base garment name (e.g., "pants" from "short-sleeved long pants").

Special Cases:
- For dresses: When "dress" is detected in description, fill both upper and lower body clothing sections with the same values.
- Never simplify "dark black" to "black"
- Never simplify "bright white" to "white" or "light white" to "white"
- Multi-color: "red white" not "red and white"
- Preserve compound colors: "blue-green" → "blue-green"

Example Input: "woman in beige linen skirt"
Output: {"Lower Body Clothing":{"Clothing Color":"beige","Clothing Material":"linen","Clothing Type":"skirt"}}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Lower Body Clothing": {"Clothing Color":"", "Clothing Material":"", "Clothing Type":""}}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""


# 3. Pedestrian gender
prompt_3 = """Determine pedestrian's gender:
Pedestrian gender: Extract "male", "female", or "none".
Output ONLY "male", "female" or "none" based on:
- Explicit gender references
- Clothing/style cues
- Pronoun usage

Example Input: "The pedestrian appears female"
Output: {"Pedestrian gender":"female"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Pedestrian gender":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 4. Body type
prompt_4 = """Extract body type:
Pedestrian body type: Extract only "average", "slim", "broad", or "none".
ONLY allow: "average", "slim", "broad", "none"

Example Input: "athletic build man"
Output: {"Pedestrian body type":"broad"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Pedestrian body type":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 5. Hat
prompt_5 = """Detect hat presence:
Wearing a hat: Output the hat color if present; otherwise "none".
- Output color with modifiers if present
- "none" if no hat

Example Input: "red baseball cap"
Output: {"Wearing a hat":"red"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Wearing a hat":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 6. Bag
prompt_6 = """Detect carried bag:
Carrying a bag: Output the bag color if present; otherwise "none".
- Output color with modifiers if present
- "none" if no bag

Example Input: "black leather backpack"
Output: {"Carrying a bag":"black"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Carrying a bag":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 7. Glasses
prompt_7 = """Check eyewear:
Wearing glasses: Output "yes" or "none".
- "yes" if glasses present
- "none" otherwise

Example Input: "person with thick-rimmed glasses"
Output: {"Wearing glasses":"yes"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Wearing glasses":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 8. Ambient lighting
prompt_8 = """Determine lighting condition:
Ambient lighting: Extract only "neutral", "warm", or "cold".

# Mandatory Rules
1. Output must be compact JSON containing only the key "Ambient lighting"
2. The final value must be one of the following:
   - "neutral" (neutral light/default value)
   - "warm" (warm tone)
   - "cold" (cold tone)

# Fuzzy Condition Handling Protocol
When mixed descriptions appear:
   a) If "neutral" is included, prioritize "neutral"
   b) Match the first hit in the following keyword order:
      1. warm → contains "warm"/"golden"/"sunset" etc.
      2. cold → contains "cool"/"cold"/"blueish" etc.
      3. Other cases → "neutral"

# Verification Examples
Input: "lighting between neutral and cool"
Output: {"Ambient lighting":"neutral"}

Input: "slightly warm tones with neutral base"
Output: {"Ambient lighting":"warm"}

Input: "cold daylight but looks neutral"
Output: {"Ambient lighting":"neutral"}

# Special Case Handling
Input: "The light appears neutral to slightly cool"
Output: {"Ambient lighting":"neutral"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Ambient lighting":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 9. Behavior
prompt_9 = """Extract movement action:
Pedestrian Behavior: Extract actions like "standing", "sitting", "walking".
- Use present participle: "standing", "walking", "running"

Example Input: "person is walking"
Output: {"Pedestrian Behavior":"walking"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Pedestrian Behavior":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 10. Posture
prompt_10 = """Determine body posture:
Pedestrian Posture: Extract only "upright", "forward tilt", "backward tilt", "slouched".
ONLY allow: "upright", "forward tilt", "backward tilt", "slouched"

1. "upright" - completely vertical without any tilt
2. "forward tilt" - significant forward leaning (e.g., bending over/leaning forward)
3. "backward tilt" - significant backward leaning
4. "left tilt" - significant lateral leaning
5. "right tilt" - significant lateral leaning
6. "slouched" - non-upright relaxed posture (including slight lateral tilt)

Priority rules:
- "upright" takes precedence over all other descriptions
- "forward tilt" and "backward tilt" take precedence over "left tilt" and "right tilt"
- Compound descriptions (e.g., "balanced but not upright") → slouched

Example Input: "leaning left with balanced posture"
Output: {"Pedestrian Posture":"left tilt"}

Example 2 Input: "person is leaning forward"
Output: {"Pedestrian Posture":"forward tilt"}

Example 3 Input: "Slight lean to the left" and "not entirely upright."
Output: {"Pedestrian Posture":"slouched"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Pedestrian Posture":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 11. Arm position
prompt_11 = """Analyze arm movement:
Extract arm movement details with precision:

# Mandatory Rules
1. Basic Judgment:
   - When the movements of both arms are consistent, directly output "swinging" or "close to the body"
   - When there is a discrepancy, use the format: "left: [state], right: [state]"

2. State Lexicon (only allowed):
   swinging         # Natural swinging state
   close to the body    # Close to the body/stationary state
   holding object   # Holding an object state

3. Priority Logic:
   - The holding object state takes precedence over other descriptions
   - When both hands are different, clearly specify left and right positioning
   - When left and right are not specified, default to directly output

# Discrepancy Handling Protocol
Trigger side-specific descriptions when the following keywords are detected:
   - "left"/"right" explicit directional words both present
   - Single-sided action verbs ("holding in left hand")

# Format Requirements
- State phrases use lowercase letters
- Left and right descriptions are separated by commas
- Keep the maximum string length ≤50 characters

Example Input: "arms crossed"
Output: {"Pedestrian arms":"close to the body"}

Example 2 Input: "left arm holding bag, right arm swinging"
Output: {"Pedestrian arms":"left: holding object, right: swinging"}

Example 3 Input: "right hand in pocket"
Output: {"Pedestrian arms":""close to the body"}

Example 4 Input: "arms partially swinging"
Output: {"Pedestrian arms":"swinging"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Pedestrian arms":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 12. Head orientation
prompt_12 = """Detect head direction:
ONLY allow: "looking up", "looking down", "look straight ahead", "looking left", "looking right"

1. Physical head rotation takes precedence over neck tilt.
2. Visual focus priority (e.g., direction of looking at an object).
3. Tilt does not alter direction judgment by default.

New rules:
- If there is no obvious text, appropriate reasoning can be conducted.Such as "tilted right" + "focusing on right-side object" → "looking right".
- Detect "look straight ahead" when there is no clear directional description.

Example Input: "head turned left"
Output: {"Pedestrian head":"looking left"}

Example 2 Input: "head slightly tilted to the right"
Output: {"Pedestrian head":"looking right"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Pedestrian head":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 13. Transportation
prompt_13 = """Check active transportation:
- "bicycle" ONLY if being ridden
- "none" otherwise

Example Input: "person pushing bike"
Output: {"Presence of Transportation":"none"}

Example 2 Input: "person riding bike"
Output: {"Presence of Transportation":"bicycle"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Presence of Transportation":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""

# 14. Color distortion
prompt_14 = """Detect color anomalies:
Color difference: Output "yes" or "no" based on color distortion from external factors.
- Only allow: "yes", "no"

Example Input: "colors distorted by neon lights"
Output: {"Color difference":"yes"}

Output a compact JSON object with EXACTLY these keys in camelCase:
{"Color difference":""}

Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""


system_prompt = """
You are a structured data extraction specialist. Strictly extract pedestrian features from text according to these rules:

# Output Requirements
Output MUST be pure JSON without any ```json markers or extra text
Ensure the output is a valid JSON object in a compact format without any additional explanations, escape characters, newline characters, or backslashes.
No Markdown, no line breaks, no dot breaks.
"""
