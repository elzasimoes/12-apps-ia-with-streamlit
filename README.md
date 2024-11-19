
# Artificial Intelligence Application with Streamlit

This application was developed as part of the course "Streamlit: Create 12 Web Applications for Artificial Intelligence" on Udemy. The aim is to explore concepts of Artificial Intelligence and Machine Learning, focusing on topics such as linear regression, time series, classification, and genetic algorithms.

## Topics Covered
- **Linear Regression**: Predicting continuous values based on independent variables.
- **Time Series**: Analyzing and forecasting sequential data over time.
- **Classification**: Algorithms for categorizing data.
- **Distributions**: Analysis of Poisson and Normal distributions.
- **Association Rules**: Identifying patterns in large datasets.
- **Genetic Algorithms**: Optimization based on evolutionary processes.
- **Generative AI**: Generating new data or information.
- **Technical Analysis and Data Visualization**: Tools for financial data analysis and interactive charts.

## Tools Used
- **Transformers**: NLP models for tasks like translation and summarization.
- **Diffusers**: Models for generating images and text.
- **Huggingface-hub**: Access to pre-trained models from Huggingface.
- **Scikit-learn**: Machine Learning library with implementations for supervised and unsupervised models.
- **Torch**: Deep learning framework for building neural networks.
- **Tokenizers**: Text processing tool for NLP.
- **Safetensors**: Efficient manipulation of tensors.
- **Geneticalgorithm**: Implementation of genetic algorithms.
- **MLxtend**: Extensions for machine learning, such as association rules.
- **NumPy**: Fundamental library for numerical computing.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Static chart generation.
- **Plotly**: Interactive data visualization.

## How to Run

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2.1 Installing PyTorch.

### ROCM 6.0 (Linux only)
```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/rocm6.0
```
### CUDA 11.8
```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118
```
### CUDA 12.1
```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu121
```

### CPU only
```bash
pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cpu
```

3. Run the application:
   ```bash
   streamlit run streamlit_app.py
   ```

4. Access the application in your browser.

## Next steps:

- Performance Optimization:
- Implement query caching to speed up frequently accessed data
- Add interactivity with sliders, dropdowns, or dynamic charts.
- Unit tests
- Logging and Monitoring






