from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query

from app.realtime.manager import manager
from app.auth.jwt import decode_token  # نفترض عندك JWT system


router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Query(...)
):

    # 1. فك التوكن
    try:
        payload = decode_token(token)
        user_id = payload["user_id"]

    except:
        await websocket.close()
        return

    # 2. تسجيل الاتصال
    await manager.connect(user_id, websocket)

    try:
        while True:
            data = await websocket.receive_json()

            await manager.send_to_user(
                user_id,
                {
                    "type": "echo",
                    "data": data
                }
            )

    except WebSocketDisconnect:
        manager.disconnect(user_id)
        async def send_typing_indicator(receiver_id: int, user_id: int, is_typing: bool):

    await manager.send_to_user(
        receiver_id,
        {
            "type": "typing",
            "user_id": user_id,
            "is_typing": is_typing
        }
    )