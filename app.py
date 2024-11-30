from flask import Flask, request, jsonify, send_file
from diffusers import StableDiffusionPipeline
import torch
from io import BytesIO
from PIL import Image
import os

app = Flask(__name__)

# Load Stable Diffusion model
print("Loading Stable Diffusion model...")
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")  # Use GPU for faster generation
print("Model loaded successfully!")

# Image generation route
@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        genre = data.get('genre', '')
        
        # Combine genre and prompt
        full_prompt = f"{genre}, {prompt}"

        # Generate image
        image = pipe(full_prompt).images[0]

        # Save image to memory
        img_io = BytesIO()
        image.save(img_io, format='PNG')
        img_io.seek(0)

        return send_file(img_io, mimetype='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
