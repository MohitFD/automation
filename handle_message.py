from data.data import responses

def handle_message(message_body):
    message_body = message_body.lower()

    if message_body in responses:
        reply = responses[message_body]
    else:
        reply = f"You said: {message_body}"

    return reply
