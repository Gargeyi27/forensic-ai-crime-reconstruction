import numpy as np
from sklearn.metrics.pairwise import cosine_similarity as cos_sim
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import img_to_array, load_img


class FingerprintFeatureEncoder:
    def __init__(self):
        base_net = ResNet50(weights='imagenet', include_top=False)
        gap_layer = GlobalAveragePooling2D()(base_net.output)
        embedding = Dense(128, activation='relu')(gap_layer)
        self.extractor = Model(inputs=base_net.input, outputs=embedding)
        print("[SYSTEM] Feature extractor initialized successfully.")

    def preprocess_image(self, img_file):
        img = load_img(img_file, target_size=(224, 224))
        arr = img_to_array(img)
        arr = np.expand_dims(arr, axis=0)
        return tf.keras.applications.resnet50.preprocess_input(arr)

    def get_embedding(self, img_file):
        arr = self.preprocess_image(img_file)
        vector = self.extractor.predict(arr)[0]
        return vector / np.linalg.norm(vector)

    def compare_fingerprints(self, query_file, db_files):
        query_vector = self.get_embedding(query_file).reshape(1, -1)
        scores = []

        for sid, file in db_files.items():
            db_vector = self.get_embedding(file).reshape(1, -1)
            similarity = cos_sim(query_vector, db_vector)[0][0]
            scores.append((sid, similarity))

        return sorted(scores, key=lambda x: x[1], reverse=True)
