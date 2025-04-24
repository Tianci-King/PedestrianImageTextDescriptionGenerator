# Prompt Design Iteration Documentation

## Version 1.0

### Issues Identified in the First 20 Checks

1. The feature `posture` only described whether a pedestrian is `walking` or `standing`, **but overlooked their actual posture**, such as leaning forward, backward, or standing upright.
2. There were **gaps in extracting color and texture**, occasionally resulting in outputs of `none`.
3. There was an error in the definition of color difference.
4. The feature `bicycle` was not documented effectively in the description.
5. Sometimes the detection and extraction failed: specifically for posture and gender.
6. Content alignment needed improvement.
7. The descriptions were not sufficiently objective.
8. The language was verbose and not concise enough.
9. There were issues with hallucinations in the text.
10. There were redundant or repetitive generations.


## Version 2.0

### I. Improvements Made Based on the Findings from Version 1.0

1. **Separated "Pedestrian Behavior" and "Posture"**:
   In prompt_2, the original "Pedestrian posture" was split into:

   - `Pedestrian Behavior` (Behavior, such as walking/standing). Walking is categorized as a **behavior**.
   - `Pedestrian Posture` (Postural adjectives, such as upright/slouched/forward tilt/backward tilt). Upright is a **postural adjective**.

   **Before** (Only behavior was included, omitting posture):

   - Pedestrian posture: Extract the posture of the pedestrian, such as "standing," "sitting," "walking," etc.	

   **After**:

   - Pedestrian Behavior: Extract the behavior of the pedestrian, such as “standing,” “sitting,” “walking,” etc.

   - Pedestrian Posture: Extract the posture of the pedestrian during the behavior, such as “walking with an upright posture,” “sitting with a slouched posture,” etc., only output "upright", "forward tilt", "backward tilt", "slouched" as adjective words.

2. **Corrected the Definition of Color Difference**:
   The contrast between clothes and the environment is not the "color difference" we initially defined. It is now explicitly defined as referring to color shifts due to lighting.

   **(New clarifying text added)**:

   - Color difference: Assess whether there are noticeable deviations in the colors of the pedestrian’s clothing, accessories, or appearance due to surrounding light conditions or external factors. **This color difference should be understood as a shift or distortion caused by lighting or reflections, not as a contrast between the clothing and the surrounding environment.** Limited to “yes,” “no.”

3. **Introduced "Presence of Transportation"** Feature:
   Added a `Presence of Transportation` field specifically to detect whether pedestrians are actively using a bicycle, noting that the focus is on whether the pedestrian is riding it, not just if a bicycle is in the image.

   **(Entire section newly added)**:

   - Presence of Transportation: Extract whether there is a bicycle actively being used by a pedestrian in the image. If a pedestrian is riding the bicycle, extract “bicycle.” If no bicycle is being used or if the bicycle is merely present in the image without active use, output “none.”

4. **Expanded Head Orientation Dimensions**:
   Considering that head orientations in the dataset are multidirectional, `looking left` and `looking right` have been added as options.

   **(New clarifying text added)**:

   - Pedestrian head: Extract the state of the pedestrian's head, only use "looking up", "looking down", "look straight ahead", **"looking left", "looking right"**.

### II. Changes that Were Not Successful

- The prompts for color, texture, and type were not successfully revised. The results were inconsistent, sometimes retaining the modifier `bright light`, while other times not. The next attempt will focus on consistently preserving color modifiers and adjectives.

### III. New Issues Found in the Second 20 Checks

- The adjective `bright` should be consistently retained, yet the checks indicated that `light` was retained while `bright` was often lost.
- Arm movements can vary, with individual actions for each hand. The initial constraints like `close to body` or `waving` were insufficient, causing one hand's actions to be described while omitting the movements of the other hand.


## Version 3.0

- The issue with the color modifier `light bright` has been resolved.
- Problems with intermittent `and` between colors were resolved for consistent formatting.
- However, sometimes extracting color or texture results in `none` or missing a color entirely. **This cannot be currently resolved through adjustments to the prompt**.

- Transportation is extracted as a new dimension, separate from behaviors or postures in previous dimensions. The prompt includes a new dimension specifically describing transportation.

- Added a new dimension for scarves, with improved keyword extraction for scarves included.

---

