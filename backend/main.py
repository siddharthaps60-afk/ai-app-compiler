from fastapi import FastAPI

from pipeline.intent_extractor import extract_intent
from pipeline.system_designer import generate_design
from pipeline.schema_generator import generate_schemas
from pipeline.validator import validate
from pipeline.repair_engine import repair

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }

@app.post("/generate")
def generate(data: dict):

    prompt = data.get("prompt", "")

    intent = extract_intent(prompt)

    design = generate_design(intent)

    config = generate_schemas(design)

    validation = validate(config)

    config = repair(
        config,
        validation
    )

    return {
        "intent": intent,
        "design": design,
        "config": config,
        "validation": validation
    }
