import os
import io
import requests

import gradio as gr
from PIL import Image


# Read Hugging Face token from environment for security
# Set HF_TOKEN environment variable before running, e.g.:
#   $env:HF_TOKEN = 'hf_...'
HF_TOKEN = os.environ.get("HF_TOKEN")
if not HF_TOKEN:
    raise RuntimeError("HF_TOKEN environment variable is required. Please set it before running the app.")

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# List of working Hugging Face models to try (most reliable ones)
MODELS = [
    "stabilityai/stable-diffusion-xl-base-1.0",
    "CompVis/stable-diffusion-v1-4",
    "prompthero/openjourney",
    "dreamlike-art/dreamlike-photoreal-2.0",
]


def generate_image(prompt: str) -> Image.Image:
    """Generate an image from a text prompt using Hugging Face Inference API.

    Returns a PIL.Image on success. Raises an exception on failure which Gradio will display.
    """
    prompt = (prompt or "").strip()
    if not prompt:
        raise gr.Error("Please enter a prompt.")

    print(f"\nGenerating image for prompt: {prompt}")
    print(f"Using token: {HF_TOKEN[:10]}...")
    
    # Try each model until one works
    last_error = None
    for model in MODELS:
        try:
            api_url = f"https://api-inference.huggingface.co/models/{model}"
            print(f"\nTrying model: {model}")
            
            # Make direct HTTP request to Hugging Face API
            response = requests.post(
                api_url,
                headers=headers,
                json={"inputs": prompt},
                timeout=60
            )
            
            print(f"Response status: {response.status_code}")
            
            if response.status_code == 200:
                # Convert bytes response to PIL Image
                image_bytes = response.content
                image = Image.open(io.BytesIO(image_bytes))
                print(f"✅ Successfully generated image with {model}!")
                return image
            elif response.status_code == 503:
                # Model is loading - try next model
                print(f"Model {model} is loading, trying next...")
                last_error = "Model is loading"
                continue
            elif response.status_code == 401:
                raise gr.Error("⚠️ Invalid token. Please check your Hugging Face token at https://huggingface.co/settings/tokens")
            elif response.status_code == 404:
                # Model not found, try next
                print(f"Model {model} not found (404), trying next...")
                last_error = f"Model not accessible"
                continue
            else:
                error_text = response.text
                print(f"Error with {model}: {error_text}")
                last_error = f"HTTP {response.status_code}"
                continue
                
        except requests.exceptions.RequestException as e:
            print(f"Request error with {model}: {e}")
            last_error = str(e)
            continue
        except Exception as e:
            print(f"Error with {model}: {e}")
            last_error = str(e)
            continue
    
    # If all models failed
    raise gr.Error(f"⚠️ All models failed. Last error: {last_error}. Your token may need 'Inference API' permissions. Get a new token at https://huggingface.co/settings/tokens")


with gr.Blocks(title="Text to Image Generator (Hugging Face API)") as demo:
    gr.Markdown("""
    ## 🧠 Text to Image Generator
    Type a prompt and generate an image — powered by Hugging Face Inference API.
    
    **Note:** If you get errors, you may need to create a new token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
    """)

    with gr.Row():
        prompt_input = gr.Textbox(label="Enter your prompt", placeholder="e.g. A cat riding a skateboard")
        submit_btn = gr.Button("Generate")

    output_img = gr.Image(label="Generated image")

    submit_btn.click(fn=generate_image, inputs=prompt_input, outputs=output_img)


if __name__ == "__main__":
    demo.launch()
