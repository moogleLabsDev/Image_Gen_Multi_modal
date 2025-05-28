# Image_Gen_Multi_modal
# 🖼️ Flux Image Generator API

A FastAPI-based image generation service using the [`FluxPipeline`](https://huggingface.co/black-forest-labs/FLUX.1-dev) model from Hugging Face's `diffusers`. This API allows you to generate high-quality images from text prompts via a simple HTTP endpoint.

---

## 🚀 Features

- Generate images from natural language prompts
- CPU-compatible using `torch.float32`
- Customizable inference parameters
- Returns images as PNG files
- Defaults to a funny prompt if none is provided 😺

---

## 🧱 Requirements

Python 3.8+

### 📦 Install dependencies:

```bash
pip install -r requirements.txt



🧠 Model Used
Model: black-forest-labs/FLUX.1-dev

Pipeline: FluxPipeline from Hugging Face's diffusers

📂 Project Structure

app/
├── main.py              # FastAPI app
├── requirements.txt     # Python dependencies
└── README.md            # This file



▶️ Run Command
Make sure you are in the root directory (where the app folder is located), then run:

uvicorn app.main:app --reload



🧪 Example Usage
✅ Generate default cat image (no prompt)


curl -X POST http://127.0.0.1:8000/generate --output cat.png


🎨 Generate custom image

curl -X POST http://127.0.0.1:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
        "prompt": "A futuristic city with neon lights and flying cars",
        "height": 1024,
        "width": 1024
      }' \
  --output image.png

🛠️ Customization
You can change the default prompt or generation parameters in main.py.



📜 License
This project is provided for educational and prototyping purposes. Check the license of the model (black-forest-labs/FLUX.1-dev) before deploying commercially.


🤝 Contributions
Pull requests and feedback are welcome!
