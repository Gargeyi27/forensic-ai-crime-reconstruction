import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def map_crime_scene():
    evidence_points = np.random.uniform(0, 50, size=(60,3))

    clusterer = KMeans(n_clusters=5, random_state=99)
    cluster_labels = clusterer.fit_predict(evidence_points)

    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection='3d')

    for cluster_id in np.unique(cluster_labels):
        ax.scatter(
            evidence_points[cluster_labels==cluster_id,0],
            evidence_points[cluster_labels==cluster_id,1],
            evidence_points[cluster_labels==cluster_id,2],
            label=f"Cluster-{cluster_id+1}"
        )

    ax.set_title("3D Evidence Mapping")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")
    ax.legend()

    plt.show()
