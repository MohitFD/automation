
def check_message(message):
    try:
#         if message.get("type") == "text" and "text" in message:
#             message_body = message["text"].get("body", "")
#         elif message.get("type") == "interactive":
#             interactive = message.get("interactive", {})
#             if interactive.get("type") == "button_reply":
#                 message_body = interactive["button_reply"].get("title", "")
#             elif interactive.get("type") == "list_reply":
#                 message_body = interactive["list_reply"].get("title", "")
#             else:
#                 message_body = "Unsupported interactive type"
#         else:
#             message_body = "Unsupported message type"
          if message.get("type") == "text" and "text" in message:
              message_body = message["text"].get("body", "")
          elif message.get("type") == "interactive":
              interactive = message.get("interactive", {})
              if interactive.get("type") == "button_reply":
                 message_body = interactive["button_reply"].get("title", "")
              elif interactive.get("type") == "list_reply":
                 message_body = interactive["list_reply"].get("title", "") 
              else:
                 message_body = "Unsupported interactive type"
          elif message.get("type") == "image" and "image" in message:
          # Extract image URL and caption
                    image = message["image"]
                    image_url = image.get("url", "")
                    image_caption = image.get("caption", "")
                    message_body = f"Image received: {image_url} with caption: {image_caption}"
          else:
              message_body = "Unsupported message type"
  

    except Exception as e:
        print("❌ Error:", str(e))

    return message_body