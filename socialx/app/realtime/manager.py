from typing import Dict
from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        # user_id -> websocket
        self.active_connections: Dict[int, WebSocket] = {}

    # =========================
    # CONNECT USER
    # =========================
    async def connect(self, user_id: int, websocket: WebSocket):

        await websocket.accept()
        self.active_connections[user_id] = websocket

    # =========================
    # DISCONNECT USER
    # =========================
    def disconnect(self, user_id: int):

        if user_id in self.active_connections:
            del self.active_connections[user_id]

    # =========================
    # SEND NOTIFICATION
    # =========================
    async def send_notification(self, user_id: int, data: dict):

        if user_id in self.active_connections:
            await self.active_connections[user_id].send_json({
                "type": "notification",
                "data": data
            })

    # =========================
    # SEND TYPING
    # =========================
    async def send_typing(self, user_id: int, data: dict):

        if user_id in self.active_connections:
            await self.active_connections[user_id].send_json({
                "type": "typing",
                "data": data
            })

    # =========================
    # SEND TO USER
    # =========================
    async def send_to_user(self, user_id: int, message: dict):

        if user_id in self.active_connections:
            websocket = self.active_connections[user_id]
            await websocket.send_json(message)

    # =========================
    # BROADCAST
    # =========================
    async def broadcast(self, message: dict):

        for ws in self.active_connections.values():
            await ws.send_json(message)

    # =========================
    # CHECK ONLINE STATUS
    # =========================
    def is_online(self, user_id: int) -> bool:

        return user_id in self.active_connections


manager = ConnectionManager()