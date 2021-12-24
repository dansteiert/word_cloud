from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np
import os
base_dir = os.path.join("C:\\Users\\ohrwu\\Downloads")

# need to order input! list of tuples

# [((Bitmap, Shape of Bitmap with #), Frequency)]
freq = [((Image.open(os.path.join(base_dir, i)).convert("RGBA"), s), f) for (s, i, f) in zip(["###", "#"],["Hops.jpg", "Hops_2.jpg"], [0.8, 0.2])]
# freq = [((i[0], i[1]), j) for i, j in freq]
# set freq
color="rocket"
wc = WordCloud()
wc.generate_from_bitmap_frequencies(frequencies=freq)
plt.imshow(wc.recolor(colormap=sns.dark_palette(color=color, as_cmap=True)), interpolation="bilinear")

import wordcloud.query_integral_image