from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse
import torch
from diffusers import FluxPipeline
from io import BytesIO

app = FastAPI()

# Load the model once at startup
pipe = FluxPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-dev",
    torch_dtype=torch.float32
).to("cpu")

# New default prompt
DEFAULT_PROMPT = (
    "A cute cartoon cat holding a board. On the board, it is written: 'You forgot to pass the prompt'."
)

# Input model with new default prompt
class GenerationInput(BaseModel):
    prompt: str = Field(default=DEFAULT_PROMPT, description="Text prompt for image generation")
    height: int = Field(default=1024, description="Image height in pixels")
    width: int = Field(default=1024, description="Image width in pixels")
    guidance_scale: float = Field(default=3.5, description="Guidance scale for generation")
    num_inference_steps: int = Field(default=50, description="Number of inference steps")
    max_sequence_length: int = Field(default=512, description="Max token sequence length")
    seed: int = Field(default=0, description="Seed for reproducibility")

@app.post("/generate", summary="Generate image from prompt")
def generate_image(data: GenerationInput):
    try:
        generator = torch.Generator("cpu").manual_seed(data.seed)

        image = pipe(
            data.prompt,
            height=data.height,
            width=data.width,
            guidance_scale=data.guidance_scale,
            num_inference_steps=data.num_inference_steps,
            max_sequence_length=data.max_sequence_length,
            generator=generator
        ).images[0]

        buffer = BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)

        return StreamingResponse(buffer, media_type="image/png")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
