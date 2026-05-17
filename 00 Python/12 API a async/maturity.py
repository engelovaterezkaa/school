import asyncio
import json

async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print("...World!")

asyncio.run(main())

seznam = ["Vajgl", "Anisi", "NayNay", "Zoph"]

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

with open("data.json", "w") as file:
    json.dump(seznam, file, indent=4)
    json.dump(thisdict, file, indent=4)
