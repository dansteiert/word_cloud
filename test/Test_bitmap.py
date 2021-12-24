from wordcloud.wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np
import os
base_dir = os.path.join("C:\\Users\\ohrwu\\Downloads")
freq = {np.array(Image.open(os.path.join(base_dir, 'hops.jpg'))): f for i, f in zip(["hops.jpg", "hops2.jpg"], [0.8, 0.2])}


wc = WordCloud()
wc.generate_from_bitmap_frequencies(frequencies=freq)
plt.imshow(wc.recolor(colormap=sns.dark_palette(color=color, as_cmap=True)), interpolation="bilinear")

import wordcloud.query_integral_image