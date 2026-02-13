\# Dataset and Methodology Description — AI-Based Crime Scene Reconstruction and Forensic Investigation System



\## 1. Introduction



This project presents an AI-driven forensic investigation system designed to assist crime scene analysis using deep learning, computer vision, and machine learning techniques. The system aims to automate forensic evidence analysis, improve investigation efficiency, and support crime scene reconstruction using intelligent data-driven methods.



The project integrates multiple forensic analysis modules including:



\- Fingerprint identification using deep learning

\- Blood stain detection using computer vision

\- Ballistic trajectory simulation using physics modeling

\- 3D crime scene reconstruction using clustering techniques



The system demonstrates the application of artificial intelligence in digital forensics and investigative workflows.



---



\## 2. Dataset Overview



The project uses real-world forensic image datasets to train and evaluate AI models for evidence detection and feature extraction.



\### Dataset Characteristics

\- Type: Image dataset

\- Domain: Forensic evidence analysis

\- Data format: RGB images

\- Data modality: Visual forensic evidence



\### Dataset Categories

The dataset consists of multiple types of forensic data:



\- Fingerprint images for biometric identification

\- Crime scene images for blood pattern detection

\- Evidence images for spatial analysis



These datasets enable training and testing of AI models for forensic evidence recognition and crime scene analysis.



---



\## 3. Dataset Source



The datasets used in this project were obtained from publicly available sources including:



\- Real Fingerprint Dataset (biometric fingerprint images)

\- Open-source forensic and crime scene image datasets

\- Public research datasets for computer vision applications



All datasets are used strictly for academic and educational purposes.



No sensitive personal identity data or real investigation data was used.



---



\## 4. Dataset Size and Distribution



\- Total dataset size: approximately 1000+ images

\- Training set: approximately 80%

\- Testing set: approximately 20%



The dataset was split to ensure reliable model evaluation and generalization performance.



---



\## 5. Data Preprocessing Pipeline



A structured preprocessing pipeline was implemented to prepare the dataset for deep learning and computer vision tasks.



\### Image Preprocessing Steps

\- Image resizing to 224×224 pixels for CNN input compatibility

\- Image normalization using ResNet50 preprocessing function

\- Noise reduction and image cleaning

\- Pixel intensity scaling

\- Feature vector generation using deep neural networks

\- Data partitioning into training and testing sets



These preprocessing steps ensure consistency and improve model performance.



---



\## 6. Methodology and System Architecture



The system follows a modular AI architecture where each component performs a specific forensic analysis task.



\### 6.1 Fingerprint Matching using Deep Learning



A deep learning-based fingerprint identification system was developed using a Convolutional Neural Network (CNN) built on a pre-trained ResNet50 architecture.



Instead of traditional image classification, the model performs feature embedding extraction to capture unique fingerprint characteristics such as ridge patterns, structural variations, and texture details.



\#### Approach:

\- Transfer learning using ResNet50

\- Feature embedding generation

\- High-dimensional feature representation

\- Similarity comparison using cosine similarity



\#### Objective:

\- Identify closest fingerprint matches from database

\- Automate suspect identification process

\- Reduce manual forensic comparison effort



---



\### 6.2 Blood Stain Detection using Computer Vision



The system includes a computer vision module that analyzes crime scene images to detect potential blood stain regions.



\#### Approach:

\- Image conversion to HSV color space

\- Red spectrum segmentation

\- Mask generation for evidence highlighting

\- Visual output generation



\#### Objective:

\- Identify potential blood evidence automatically

\- Assist investigators in evidence localization

\- Reduce manual inspection time



---



\### 6.3 Ballistics and Projectile Trajectory Simulation



A physics-based simulation module was implemented to model projectile motion based on firing parameters such as velocity and angle.



\#### Approach:

\- Mathematical modeling of projectile motion

\- Parameter-based simulation

\- Trajectory visualization



\#### Objective:

\- Estimate possible shooter positions

\- Analyze weapon dynamics

\- Support crime event reconstruction



---



\### 6.4 3D Crime Scene Reconstruction and Evidence Mapping



A spatial analysis module was developed to visualize evidence distribution in three-dimensional space.



\#### Approach:

\- Generation of spatial evidence points

\- Clustering using K-Means algorithm

\- 3D visualization of evidence groups



\#### Objective:

\- Understand spatial relationships between evidence

\- Provide structured crime scene visualization

\- Support investigative decision making



---



\## 7. Machine Learning and AI Techniques Used



The project incorporates multiple artificial intelligence techniques:



\- Transfer learning using ResNet50

\- Convolutional Neural Networks (CNN)

\- Feature embedding extraction

\- Cosine similarity-based matching

\- HSV color segmentation

\- Unsupervised clustering using K-Means

\- Scientific computing and visualization

\- Physics-based modeling



---



\## 8. Purpose of Dataset Usage



The dataset supports the following research objectives:



\- Training fingerprint feature extraction models

\- Evaluating similarity-based identification methods

\- Testing forensic evidence detection algorithms

\- Supporting crime scene reconstruction experiments

\- Demonstrating AI applications in forensic investigation



---



\## 9. Performance and Evaluation Considerations



Model outputs are evaluated based on:



\- Similarity score comparison

\- Evidence detection accuracy

\- Visual validation of results

\- Reconstruction quality



Future work may include quantitative evaluation metrics such as precision, recall, and accuracy.



---



\## 10. Ethical Considerations



\- Dataset used strictly for academic research

\- No personal identity data included

\- No real forensic investigation usage

\- Compliance with public dataset licensing policies

\- System intended for research demonstration only



---



\## 11. Limitations



\- Limited dataset size

\- Simplified 3D reconstruction approach

\- Basic color-based blood detection

\- Simulation-based crime scene modeling



Future improvements will address these limitations using larger datasets and advanced models.



---



\## 12. Future Improvements



\- Deep learning-based blood pattern classification

\- Advanced 3D scene reconstruction using depth estimation

\- Real-time evidence detection

\- Integration with forensic databases

\- Deployment as interactive investigation tool



