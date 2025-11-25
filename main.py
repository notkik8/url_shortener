from fastapi import FastAPI

from string import ascii_letters, digits
from random import choice

app = FastAPI()

SYMBOLS = ascii_letters + digits


def generate_slug():
    slug = ""
    for _ in range(6):
        slug += choice(SYMBOLS)
    return slug


@app.get("/shortener")
async def make_url_shorter():
    slug = generate_slug()
    return {slug}


@app.get("/{some_slug}")
async def redirect_to_url(slug: str):
    return {"balls"}