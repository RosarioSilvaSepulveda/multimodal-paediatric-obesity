# Using Multimodal Machine Learning for analysing paediatric obesity in Mexico

¡Hola! Hi! Hej!

This repository contains the code and some of the data required to reproduce the results of my degree project for the MSc in Health Informatics at Karolinska Institutet, the project was titled: 

### **Using Multimodal Machine Learning for analysing multifactorial causes of disease: the case of childhood overweight and obesity in Mexico**
***Department:*** Learning, Informatics, Management & Ethics (LIME)
- ***Author:*** Rosario Silva Sepulveda, MSc
- ***Supervisor:*** Magnus Boman, PhD
- ***Examiner:*** Sabine Koch, PhD

The methods adhere to the work of Carbonell et al. (Carbonell, Boman & Laukka), which involves an experimental, exploratory, and data-driven approach to comparing supervised and unsupervised Machine Learning classifiers with unimodal and multimodal approaches. 

Carbonell et al.'s GitHub repository is available at: https://github.com/marferca/multimodal-emotion-recognition

Their repository contains data and code that support the findings of the following article:

> Fernández Carbonell M, Boman M, Laukka P. 2021. Comparing supervised and unsupervised approaches to multimodal emotion recognition. PeerJ Computer Science 7:e804 https://doi.org/10.7717/peerj-cs.804

The data analised in the project was obtained from the 2018 instance of the Mexican National Health and Nutrition Survey (Encuesta Nacional de Salud y Nutrición de México). The authorship credits of the data are of INEGI (Instituto Nacional de Estadística y Geografía).
> Source: INEGI, Encuesta Nacional de Salud y Nutrición 2018. Available here: https://www.inegi.org.mx/programas/ensanut/2018/

***Note:*** The analysis, transformation and interpretation of the data do not represent an oficial posture, nor has it been endorsed, integrated, sponsored or supported by INEGI.

## Reproducing the results
### Getting the code
You can download a copy of all the files in this repository by cloning the git repository:

```git clone https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity```

### Setting up a Python virtual environment
In progress...

### Getting the ENSANUT files
In progress...

## Results
### Supervised Learning
- Early Fusion: [Modelling](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/early_fusion/code/early_fusion_modeling_unimodal.ipynb) | [Feature Importance](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/early_fusion/code/model_interpretation_early_fusion_unimodal.ipynb)
- Late Fusion: [Fusion Techniques](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/fusion_techniques.ipynb)
  - Modality 1. Home environment: [Modelling](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m1_modeling.ipynb) | [Feature Importance](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m1_model_interpretation.ipynb)
  - Modality 2. Household income and expenses: [Modelling](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m2_modeling.ipynb) | [Feature Importance](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m2_model_interpretation.ipynb)
  - Modality 3. Health information: [Modelling](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m3_modeling.ipynb) | [Feature Importance](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m3_model_interpretation.ipynb)
  - Modality 4. Biometrics: [Modelling](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m4_modeling.ipynb) | [Feature Importance](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m4_model_interpretation.ipynb)
  - Modality 5. Knowledge on nutritional information: [Modelling](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m5_modeling.ipynb) | [Feature Importance](https://github.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/blob/main/3_supervised_learning/late_fusion/code/m5_model_interpretation.ipynb)

### Unsupervised Learning
- Traditional approach: [Before dimensionality reduction]() | [After dimensionality reduction]()
- Exploratory approach: You can interactively visualize the data and inspect the results [here](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/RosarioSilvaSepulveda/multimodal-paediatric-obesity/main/4_unsupervised_learning/exploratory_approach/tf_embedding_projector/projector_config.json).
