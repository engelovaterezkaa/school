import asyncio

async def make_coffee():
    print("Coffee making in proccess.....dumbass....")
    await asyncio.sleep(3)
    print("Your caffein load is ready.")
    return "gloglo fee"

async def make_yoghurt():
    print("Making yoghurt...")
    await asyncio.sleep(2) #await: dělej to bokem a pokračuj s kódem
    print("Yoghurt ready.")
    return "yummy ghrt"

async def make_breakfast():
    coffee, yoghurt = await asyncio.gather(
        make_coffee(),
        make_yoghurt()
    )
    print(f"Breakfast is ready: {coffee} + {yoghurt}")

asyncio.run(make_breakfast())