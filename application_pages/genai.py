import streamlit as st
import torch
from diffusers import EulerDiscreteScheduler, StableDiffusionPipeline

st.set_page_config(page_title='IA Generativa', layout='wide')
st.title('Gerador de Imagens com Stable Diffusion')


def generate_images(
    prompt, negative_prompt, num_images_per_prompt, num_inference_steps, height, width, seed, guidance_scale
):
    """
    Generate images using the Stable Diffusion model.

    This function utilizes a pre-trained Stable Diffusion model to generate images
    based on the provided prompts and configuration parameters. The generation
    process can be influenced by various factors such as the number of images,
    inference steps, image dimensions, random seed, and guidance scale.

    Args:
        prompt (str): The text prompt to guide the image generation.
        negative_prompt (str): The text prompt to discourage certain features in the image.
        num_images_per_prompt (int): Number of images to generate per prompt.
        num_inference_steps (int): Number of inference steps for the generation process.
        height (int): Height of the generated images.
        width (int): Width of the generated images.
        seed (int): Random seed for reproducibility.
        guidance_scale (float): Scale for guidance during image generation.

    Returns:
        list: A list of generated images.
    """
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    pretrained_model_or_path = 'stabilityai/stable-diffusion-2-1-base'
    scheduler = EulerDiscreteScheduler.from_pretrained(pretrained_model_or_path, subfolder='scheduler')
    pipeline = StableDiffusionPipeline.from_pretrained(pretrained_model_or_path, scheduler=scheduler).to(device)
    generator = torch.Generator(device=device).manual_seed(seed)
    images = pipeline(
        prompt=prompt,
        num_images_per_prompt=num_images_per_prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_inference_steps,
        height=height,
        width=width,
        generator=generator,
        guidance_scale=guidance_scale,
    )['images']
    return images


st.header('Configurações da Geração da Imagem')
prompt = st.text_area('Prompt', '')
negative_prompt = st.text_area('Negative Prompt', '')
num_images_per_prompt = st.slider('Número de Imagens', min_value=1, max_value=5, value=1)
num_inference_steps = st.number_input('Número de Passos de Inferência', min_value=1, max_value=100, value=50)
height = st.selectbox('Altura da Imagem', [256, 512, 768, 1024], index=1)
width = st.selectbox('Largura da Imagem', [256, 512, 768, 1024], index=1)
seed = st.number_input('Seed', min_value=0, max_value=99999, value=42)
guidance_scale = st.number_input('Escala de Orientação', min_value=1.0, max_value=20.0, value=7.5)
generate_button = st.button('Gerar Imagem')

if generate_button and prompt:
    with st.spinner('Gerando Imagens...'):
        images = generate_images(
            prompt, negative_prompt, num_images_per_prompt, num_inference_steps, height, width, seed, guidance_scale
        )
        cols = st.columns(len(images))
        for idx, (col, img) in enumerate(zip(cols, images)):
            with col:
                st.image(img, caption=f'Imagem {idx + 1}', use_column_width=True, output_format='auto')
