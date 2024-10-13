# hierarchical_clustering.py
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

# 生成隨機數據
data = np.random.rand(100, 2)

# 應用層次聚類
linked = linkage(data, 'single')

# 繪製樹狀圖
dendrogram(linked)
plt.show()