import asyncio
import websockets


async def run_client():
    uri = "ws://localhost:8765"

    async with websockets.connect(uri) as websocket:
        await websocket.send("Привет, сервер!")
        print("Отправлено серверу: Привет, сервер!")

        for _ in range(5):
            message = await websocket.recv()
            print(f"Получено: {message}")

if __name__ == "__main__":
    asyncio.run(run_client())
