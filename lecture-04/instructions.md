# Every instruction pasted in Lecture 4

In lecture order. Paste them into the prompt box of Text Encode Qwen Image 2.1. `<image1>` is the picture being edited (first image input), `<image2>` the second reference.

## Chapter 03: Turn text-to-image into image-to-image (unit 03_008)

```text
A realistic candid photograph of a man in his thirties sitting at a wooden table in a cozy cafe. He has short dark curly hair, a neatly trimmed dark beard, brown eyes and round tortoiseshell glasses. He wears a dark green knitted wool sweater over a white collared shirt and holds a white ceramic coffee cup with both hands. Behind him is a red brick wall with wooden shelves holding books, glass jars and small potted plants. Soft warm window light comes from the left.
```

## Chapter 05: Edit with the photo in the conditioning (unit 05_006)

```text
Change his navy blue sweater to a dark green sweater.
```

## Chapter 06: Why denoise one is still editing (unit 06_004)

```text
Change his navy blue sweater to a dark green sweater, while keeping his face, hairstyle and the background exactly the same.
```

## Chapter 07: Measure changed pixels with a difference map (unit 07_010)

```text
Change his navy blue sweater to a dark green sweater.
```

## Chapter 09: Replace words on a photographed sign (unit 09_002)

```text
Replace the word "RIVER" on the large sign with "HARBOR", so the sign reads "HARBOR BAKERY". Keep the letter style, colours and everything else unchanged.
```

## Chapter 09: Replace words on a photographed sign (unit 09_004)

```text
Replace the text "Closed" on the small board in the window with "Open 24/7 - Est. 1998". Keep the board, the window and everything else unchanged.
```

## Chapter 10: Two references with named roles (unit 10_004)

```text
Dress the man from <image1> in the mustard yellow corduroy jacket from <image2>, buttoned over his white collared shirt. Keep his face, glasses, beard, hands, the coffee cup and the cafe background from <image1> unchanged.
```

## Chapter 11: One character: a turnaround sheet (unit 11_003)

```text
Create a character turnaround sheet of the man from <image1> on a plain light grey background: the same man shown three times side by side, full body, in a front view, a three-quarter view and a side profile view. Keep his face, beard, the navy field jacket, the copper scarf, the olive trousers, the boots and the brown satchel with its square brass clasp exactly as in <image1>.
```

## Chapter 12: Place the explorer in three storyboard scenes (unit 12_003)

```text
Place the explorer from <image2> on the railway platform in <image1>. He walks along the platform toward the camera, glancing at the tracks on his left. Keep his face, beard, the navy field jacket, the copper scarf, the olive trousers, the boots and the brown satchel with its square brass clasp exactly as in <image2>. Keep the platform from <image1> with its warm lamps and dusk sky.
```

## Chapter 12: Place the explorer in three storyboard scenes (unit 12_006)

```text
Place the explorer from <image2> on the hilltop in <image1>. He stands beside the stone cairn with one hand resting on it and looks out across the valley to the right. Keep his face, beard, the navy field jacket, the copper scarf, the olive trousers, the boots and the brown satchel with its square brass clasp exactly as in <image2>. Keep the hilltop from <image1> with golden sunrise light from the right.
```

## Chapter 12: Place the explorer in three storyboard scenes (unit 12_008)

```text
A realistic photograph of an adult male explorer in his forties with short dark hair and a short salt-and-pepper beard, wearing a navy blue canvas field jacket, a copper-coloured wool scarf, olive cargo trousers and brown leather boots, with a brown leather satchel with a square brass clasp. He stands beside the wooden bench of an old workshop and lifts a copper lantern in his right hand. Warm light from the window on the left.
```

## Chapter 12: Place the explorer in three storyboard scenes (unit 12_012)

```text
Place the explorer from <image2> in the workshop in <image1>. He stands beside the wooden bench, turned slightly toward the window, and lifts the copper lantern from the bench in his right hand. Keep his face, beard, the navy field jacket, the copper scarf, the olive trousers, the boots and the brown satchel with its square brass clasp exactly as in <image2>. Keep the workshop from <image1> with warm light from the window on the left.
```

## Chapter 13: Five sequential edits and a clean rollback (unit 13_003)

```text
Make him smile warmly.
```

## Chapter 13: Five sequential edits and a clean rollback (unit 13_004)

```text
Make the copper lantern glow with a warm flame.
```

## Chapter 13: Five sequential edits and a clean rollback (unit 13_005)

```text
Change the time of day to evening: blue dusk light in the window, the workshop lit mainly by the lantern.
```

## Chapter 13: Five sequential edits and a clean rollback (unit 13_007)

```text
Add a rolled paper map under his left arm.
```

## Chapter 13: Five sequential edits and a clean rollback (unit 13_008)

```text
Make him turn his head to look toward the window on the left.
```

## Chapter 13: Five sequential edits and a clean rollback (unit 13_012)

```text
Place the explorer from <image2> in the workshop in <image1>. He stands beside the wooden bench, turned slightly toward the window, lifts the copper lantern from the bench in his right hand and smiles warmly. The lantern glows with a warm flame, a rolled paper map is tucked under his left arm, and it is evening, with blue dusk light in the window. Keep his face, beard, the navy field jacket, the copper scarf, the olive trousers, the boots and the brown satchel with its square brass clasp exactly as in <image2>.
```

## Chapter 14: Relight a portrait by instruction (unit 14_002)

```text
Relight the photo as a night scene: the window on the left is dark blue, and a warm table lamp on the right side lights his face from the right, so the shadows fall to the left. Keep the man, his pose, his clothes, the coffee cup and the cafe background unchanged.
```
