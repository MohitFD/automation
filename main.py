from fastapi import FastAPI, Request
from handle_message import handle_message
from send_message_automatic import (
    send_whatsapp_message,
    send_whatsapp_image,
    send_text_message,
)
from fastapi.staticfiles import StaticFiles
from check_message import check_message
from fastapi.responses import JSONResponse,HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

seen_messages = set()


@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("send_msg.html", {"request": request})

@app.post("/webhook")
async def zapup_webhook(request: Request):
    data = await request.json()
    try:
        event = data.get("event")
        if event != "message.received":
            return {"status": "ignored"}
        message = data["data"]["data"]["value"]["messages"][0]
        msg_id = message["id"]
        sender_number = message["from"]
        message_body = check_message(message)
        sender_names = set()
        contacts = data["data"]["data"]["value"].get("contacts", [])
        for contact in contacts:
            wa_id = contact.get("wa_id")
            name = contact.get("profile", {}).get("name", "Unknown")
            if wa_id == sender_number:
                sender_names.add(name)
        sender_names = list(sender_names)
        if msg_id in seen_messages:
            print("🔁 Duplicate message, skipping.")
            return {"status": "duplicate_skipped"}
        seen_messages.add(msg_id)

        reply = handle_message(message_body)
        # send_whatsapp_image(reply, sender_number)
        send_whatsapp_message(reply, sender_number, sender_names)

    except Exception as e:
        print("❌ Error:", str(e))

    return {"status": "ok"}


@app.post("/send-message")
async def send_message(request: Request):
    data = await request.json()
    phone = data.get("phone")
    message = data.get("message")

    if not phone or not message:
        return JSONResponse(
            status_code=400,
            content={"success": False, "message": "Phone and message are required"},
        )

    result = send_text_message(phone, message)
    return JSONResponse(status_code=200, content={"success": True, "data": result})
