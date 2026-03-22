import asyncio
import httpx

url = "https://catass.com/cat"

async def fetch_cat(id):
    async with httpx.AsyncClinet() as client:
        response = await client.get(url)

        filename = f"cat{id}.jpg"
        with open(filename, "w") as f:
            f.write(response.content)
        
        return filename

async def main():
    cats = [] #list
    for i in range(1, 6):
        cats.append(fetch_cat(i))
    #cats = [fetch_cat(i) for i in range(1, 6)] (alternativní zápis)

    filenames = await asyncio.gather(*cats) #rozbalí list cats(, který byl vyplněn), zobrazí položky

    print(f"Downloading {len(filenames)} cats")

asyncio.run(main())