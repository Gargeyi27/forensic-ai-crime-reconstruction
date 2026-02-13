from fingerprint_encoder import FingerprintFeatureEncoder
from blood_detection import identify_blood_patterns
from ballistics import calculate_projectile
from crime_scene_mapping import map_crime_scene


def launch_demo():
    print(" Forensic AI System")

    print("\nRun modules manually:")
    print("1. Fingerprint Matching")
    print("2. Blood Pattern Detection")
    print("3. Projectile Simulation")
    print("4. Crime Scene Mapping")


if __name__ == "__main__":
    launch_demo()
