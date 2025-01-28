import asyncio

def on():
    print("on")

def off():
    print("off")


async def cycle(on_off):
    if on_off[0] > 0:
        on()
        asyncio.sleep(on_off[0])
        off()
        asyncio.sleep(on_off[1])
    else:
        off()

    return None

async def next_time(gear):
    match gear:
        case 1:
            return 1,1
        case _:
            return 0,0

async def main():
    on_off = (0,0)
    gear = 1
    while True:
        _, on_off = await cycle(on_off), await next_time(gear)

if __name__ == "__main__":
    asyncio.run(main())