from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from openai import OpenAI
import os
from typing import Optional
import uvicorn
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Diet Recipe Generator", description="Get personalized dinner recipes based on your dietary preferences")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

class RecipeRequest(BaseModel):
    dietary_preference: str

class RecipeResponse(BaseModel):
    recipe: str
    ingredients: list[str]
    instructions: list[str]

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-recipe", response_model=RecipeResponse)
async def generate_recipe(
    dietary_preference: str = Form(...)
):
    """Generate a dinner recipe based on dietary preferences"""
    
    # Get API key from environment variables
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai_api_key:
        raise HTTPException(status_code=500, detail="OpenAI API key not found. Please set OPENAI_API_KEY in your .env file.")
    
    try:
        client = OpenAI(api_key=openai_api_key)
        
        # Create a prompt based on dietary preference
        dietary_instructions = {
            "vegetarian": "vegetarian (no meat, but dairy and eggs are okay)",
            "vegan": "vegan (no meat, dairy, eggs, or any animal products)",
            "no_restrictions": "no dietary restrictions"
        }
        
        preference = dietary_instructions.get(dietary_preference, dietary_preference)
        
        prompt = f"""Generate a simple, delicious dinner recipe that is {preference}. 
        
        Please provide:
        1. A catchy recipe name
        2. A brief description (1-2 sentences)
        3. List of ingredients (with quantities)
        4. Simple step-by-step cooking instructions
        
        Make it something that can be prepared in 30-45 minutes with common ingredients. 
        Format your response clearly with sections for Name, Description, Ingredients, and Instructions."""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant that creates simple, delicious recipes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.7
        )
        
        recipe_text = response.choices[0].message.content
        
        # Parse the recipe into structured format
        lines = recipe_text.strip().split('\n')
        ingredients = []
        instructions = []
        
        in_ingredients = False
        in_instructions = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if 'ingredient' in line.lower() and ':' in line:
                in_ingredients = True
                in_instructions = False
                continue
            elif 'instruction' in line.lower() and ':' in line:
                in_ingredients = False
                in_instructions = True
                continue
            elif line.lower().startswith(('name:', 'description:', 'recipe name:')):
                in_ingredients = False
                in_instructions = False
                continue
                
            if in_ingredients and line.startswith(('•', '-', '*')):
                ingredients.append(line[1:].strip())
            elif in_instructions and (line.startswith(('•', '-', '*')) or line[0].isdigit()):
                if line[0].isdigit() and '.' in line:
                    instructions.append(line.split('.', 1)[1].strip())
                else:
                    instructions.append(line[1:].strip() if line.startswith(('•', '-', '*')) else line)
        
        # If parsing failed, return the raw text
        if not ingredients and not instructions:
            ingredients = ["See recipe text below"]
            instructions = [recipe_text]
        
        return RecipeResponse(
            recipe=recipe_text,
            ingredients=ingredients,
            instructions=instructions
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recipe: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
