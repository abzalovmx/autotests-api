import asyncio
import websockets


async def handler(websocket):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for i in range(1, 6):
            reply = f"{i} Сообщение пользователя: {message}"
            await websocket.send(reply)


async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("WebSocket сервер запущен на ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
