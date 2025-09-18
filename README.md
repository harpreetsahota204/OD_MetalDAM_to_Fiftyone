# Dataset Card for OD_MetalDAM


The OD_MetalDAM (Metallography Dataset from Additive Manufacturing) is a specialized computer vision dataset containing 42 high-resolution scanning electron microscope (SEM) images of metal microstructures from additive manufacturing processes. 

Each image includes pixel-level semantic segmentation masks identifying five distinct metallurgical phases and features: Matrix, Austenite, Martensite/Austenite, Precipitate, and Defects.

This is a [FiftyOne](https://github.com/voxel51/fiftyone) dataset with 42 samples.

## Installation

If you haven't already, install FiftyOne:

```bash
pip install -U fiftyone
```

## Usage

```python
import fiftyone as fo
from fiftyone.utils.huggingface import load_from_hub

# Load the dataset
# Note: other available arguments include 'max_samples', etc
dataset = load_from_hub("harpreetsahota/OD_MetalDAM")

# Launch the App
session = fo.launch_app(dataset)
```

## Dataset Details

### Dataset Description

The OD_MetalDAM dataset is a comprehensive metallography dataset specifically designed for computer vision applications in materials science and additive manufacturing quality control. 

The dataset consists of 42 carefully curated scanning electron microscope (SEM) images of metal microstructures, each accompanied by detailed pixel-level segmentation masks and rich metadata.

Key features of the dataset:
- **High-resolution SEM images**: Each micrograph is captured at various magnifications (5,000x to 15,000x)

- **Pixel-level annotations**: Five distinct classes representing different metallurgical phases and features

- **Comprehensive metadata**: Including magnification levels, scale bar measurements, and pixel counts for each phase

- **Pre-processed images**: Images are cropped to remove information bands, ensuring clean training data

- **Semantic segmentation masks**: Color-coded masks for easy visualization and model training

The dataset addresses the critical need for automated microstructure analysis in additive manufacturing, where understanding phase distributions, defect detection, and material characterization are essential for quality assurance and process optimization.

- **Curated by:** ArcelorMittal and DaSCI (Andalusian Research Institute in Data Science and Computational Intelligence)

- **Funded by:** ArcelorMittal

- **Shared by:** Harpreet Sahota

- **Language(s) (NLP):** en

- **Dataset License:** MIT License

### Dataset Sources


- **Repository:** https://github.com/ari-dasci/OD-MetalDAM


## Uses

### Direct Use

The OD_MetalDAM dataset is intended for:

1. **Semantic Segmentation Model Training**: Train deep learning models to automatically segment and classify different metallurgical phases in SEM images

2. **Quality Control in Additive Manufacturing**: Develop automated inspection systems for detecting defects and analyzing microstructure quality

3. **Materials Science Research**: Study phase distributions, grain boundaries, and microstructural features in metal alloys

4. **Computer Vision Algorithm Development**: Benchmark and evaluate segmentation algorithms on high-resolution microscopy data

5. **Educational Purposes**: Teach materials characterization and computer vision techniques in metallurgy

6. **Transfer Learning**: Pre-train models for other microscopy or materials science applications

### Out-of-Scope Use

This dataset should NOT be used for:

1. **Medical diagnosis or healthcare applications**: The dataset is specific to metal microstructures and not suitable for biological or medical imaging

2. **Real-time production monitoring**: With only 42 samples, the dataset may not capture all possible variations in production environments

3. **Other material types**: The dataset is specific to metal alloys from additive manufacturing and may not generalize to ceramics, polymers, or composites

4. **Macro-scale defect detection**: The dataset focuses on microstructural features and is not suitable for detecting large-scale manufacturing defects

5. **Standalone production decisions**: Models trained on this dataset should be validated with domain experts before deployment in critical manufacturing processes

## Dataset Structure


Each sample in the dataset contains:

### Image Data

- **filepath**: Path to the cropped SEM micrograph (JPEG format)

- **mask**: Semantic segmentation mask (PNG format) with pixel values corresponding to class labels

### Segmentation Classes

- **0 - Matrix**: Background matrix material (base metal structure)

- **1 - Austenite**: Austenite phase regions

- **2 - Martensite/Austenite**: Mixed or transitional phase regions

- **3 - Precipitate**: Precipitate particles and inclusions

- **4 - Defect**: Defects, voids, and artifacts

### Metadata Fields

- **micron_bar**: Scale bar value in micrometers (μm)

- **magnification**: SEM magnification level (5000x, 10000x, or 15000x)

- **label0_pixels**: Pixel count for Matrix phase

- **label1_pixels**: Pixel count for Austenite phase

- **label2_pixels**: Pixel count for Martensite/Austenite phase

- **label3_pixels**: Pixel count for Precipitate phase

- **label4_pixels**: Pixel count for Defect phase

- **total_pixels**: Total image pixels after cropping

### Image Specifications

- **Resolution**: Varies between 1024×703 and 1280×895 pixels (after cropping)

- **Format**: JPEG for images, PNG for segmentation masks

- **Color**: Grayscale SEM images, color-coded segmentation masks

## Dataset Creation

### Curation Rationale

The OD_MetalDAM dataset was created to address several critical challenges in additive manufacturing and materials science:

1. **Automation Need**: Manual analysis of microstructures is time-consuming and subject to human error

2. **Quality Assurance**: Additive manufacturing processes require rigorous quality control to ensure material properties

3. **Standardization**: Provide a benchmark dataset for developing and comparing computer vision algorithms in metallography

4. **Research Advancement**: Enable machine learning research in materials characterization

5. **Industrial Application**: Bridge the gap between academic research and industrial quality control needs

### Source Data

#### Data Collection and Processing


The data collection and processing pipeline involved:

1. **Sample Preparation**: Metal samples from additive manufacturing processes were prepared using standard metallographic techniques

2. **SEM Imaging**: High-resolution images captured using scanning electron microscopy at multiple magnifications

3. **Expert Annotation**: Metallurgists and materials scientists manually annotated each image to identify different phases

4. **Data Preprocessing**: 
   - Original images contained information bands that were cropped out
   - Segmentation masks were generated with consistent color coding
   - Metadata was extracted and stored in SQL database format
5. **Quality Control**: Each annotation was reviewed for accuracy and consistency

6. **Format Conversion**: Data converted to FiftyOne-compatible format for easy access and visualization

#### Who are the source data producers?

The source data was produced by:
- **ArcelorMittal**: Global steel manufacturing company providing metal samples and domain expertise

- **DaSCI (Andalusian Research Institute)**: Research institute providing computer vision and data science expertise

- **Materials Scientists**: Expert metallurgists who performed the microscopy and initial analysis

- **Research Engineers**: Technical staff who prepared samples and operated SEM equipment

### Annotations


#### Annotation process

The annotation process followed these steps:

1. **Initial Segmentation**: Expert metallurgists manually segmented each SEM image using specialized image analysis software

2. **Phase Identification**: Each region was classified into one of five categories based on visual characteristics and domain knowledge

3. **Pixel-level Precision**: Annotations were performed at pixel level to capture fine grain boundaries and small features

4. **Validation**: Multiple experts reviewed annotations for consistency

5. **Color Coding**: Segmentation masks were generated with consistent color mapping for visualization

#### Who are the annotators?

Annotations were created by:

- Professional metallurgists with expertise in additive manufacturing

- Materials science researchers from DaSCI and ArcelorMittal

- Domain experts with specific knowledge of steel microstructures and phase identification

#### Personal and Sensitive Information

The dataset does not contain any personal, sensitive, or private information. All data consists of:

- Technical microscopy images of metal samples

- Scientific measurements and metadata

- No human subjects or personal identifiers

- No location-specific or proprietary process information

## Bias, Risks, and Limitations

### Technical Limitations

1. **Limited Sample Size**: With 42 samples, the dataset may not capture all possible microstructural variations

2. **Specific Material System**: Dataset focuses on specific steel alloys used in additive manufacturing

3. **Magnification Range**: Limited to 5,000x-15,000x magnification, may not capture nano-scale or macro-scale features

4. **2D Representation**: SEM images provide 2D views of 3D microstructures

### Potential Biases

1. **Manufacturing Process**: Samples may be biased toward specific additive manufacturing techniques

2. **Material Composition**: Limited to certain alloy compositions used by ArcelorMittal

3. **Quality Distribution**: May not represent the full spectrum of quality variations in production

### Risks

1. **Overfitting**: Small dataset size increases risk of model overfitting

2. **Domain Shift**: Models may not generalize to different alloys, manufacturing processes, or imaging conditions

3. **Annotation Subjectivity**: Some phase boundaries may be ambiguous and subject to expert interpretation

### Recommendations

Users should be made aware of the risks, biases and limitations of the dataset. Recommendations include:

1. **Data Augmentation**: Apply appropriate augmentation techniques to increase training data diversity

2. **Transfer Learning**: Use pre-trained models and fine-tune on this dataset for better performance

3. **Domain Validation**: Validate models on independent datasets from your specific application domain

4. **Expert Review**: Have domain experts review model predictions before deployment

5. **Ensemble Methods**: Combine multiple models to improve robustness

6. **Continuous Learning**: Update models as more data becomes available from production environments

7. **Cross-validation**: Use appropriate cross-validation strategies given the limited sample size


## Glossary

- **SEM**: Scanning Electron Microscopy - High-resolution imaging technique for surface analysis

- **Austenite**: Face-centered cubic crystal structure phase of steel

- **Martensite**: Body-centered tetragonal crystal structure formed by rapid cooling

- **Precipitate**: Secondary phase particles that form within the metal matrix

- **Matrix**: Primary continuous phase in the microstructure

- **Additive Manufacturing**: 3D printing process for metals using layer-by-layer deposition

- **Microstructure**: Microscopic structure of a material revealing grains, phases, and defects

- **Magnification**: Degree of enlargement of the microscope image

- **Micron Bar**: Scale reference showing actual size in micrometers (μm)

## More Information

For additional information about the dataset:

- **GitHub Repository**: https://github.com/ari-dasci/OD-MetalDAM

- **FiftyOne Documentation**: https://docs.voxel51.com/

- **Materials Science Background**: Consult metallography textbooks and additive manufacturing literature

- **Technical Support**: Open issues on the GitHub repository

## Dataset Card Authors

- Harpreet Sahota - Dataset conversion to FiftyOne format and Hugging Face integration
- Original dataset creators from ArcelorMittal and DaSCI

## 📖 Citation

If you use this dataset in your research, please cite:

**BibTeX:**

```bibtex
@misc{metaldam2024,
  title={MetalDAM: Metallography Dataset from Additive Manufacturing},
  author={{ArcelorMittal} and {DaSCI Andalusian Research Institute}},
  year={2024},
  url={https://github.com/ari-dasci/OD-MetalDAM},
  note={FiftyOne dataset available at: https://huggingface.co/datasets/harpreetsahota/OD_MetalDAM}
}
```

**APA:**

ArcelorMittal & DaSCI Andalusian Research Institute. (2024). *MetalDAM: Metallography Dataset from Additive Manufacturing* [Data set]. GitHub. https://github.com/ari-dasci/OD-MetalDAM


## 📄 License

The dataset is licensed under the MIT License, but the code is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Original Dataset**: ArcelorMittal & DaSCI Andalusian Research Institute
- **FiftyOne Integration**: Harpreet Sahota

## 🙏 Acknowledgments

- ArcelorMittal for providing the metallography images and domain expertise
- DaSCI Andalusian Research Institute for dataset curation and annotation
- FiftyOne team for the excellent visualization framework

---

**Note**: This dataset is intended for research and educational purposes in materials science and computer vision. For production use, please validate models with domain experts.