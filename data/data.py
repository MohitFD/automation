greetings = {
    "message": "how are you?",
    "header": "Welcome to FixingDots",
    "footer": "Select One",
    "buttons": [
        {"id": "1", "title": "Looking for Machine"},
        {"id": "2", "title": "Services"},
        {"id": "3", "title": "Enquiry"},
    ],
}

machines_data = {
    "message": "Select a machine for more information.",
    "header": "Machine Selection",
    "footer": "Please choose a machine.",
    "buttons": [
        {
            "id": "1",
            "title": "Bulldozer",
            "description": "Heavy-duty earth-moving machine.",
        },
        {
            "id": "2",
            "title": "Excavator",
            "description": "Used for digging and demolition tasks.",
        },
        {
            "id": "3",
            "title": "Crane",
            "description": "Lifts and moves heavy materials vertically.",
        },
    ],
}
machine1_data = {
    "message": "BullDozer is used for pushing large quantities of soil, sand, or other materials.",
    "header": "BULLDOZER",
    "footer": "Please choose a machine.",
    "media_type": "image",  # Media type is an image
    "media_url": "https://images.pexels.com/photos/276267/pexels-photo-276267.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "caption": "your caption for image or video media types",
    "file_name": "testFileName",
}
services_data = {
    "message": "Select a service you would like to know more about.",
    "header": "Service Options",
    "footer": "Please choose a service.",
    "buttons": [
        {
            "id": "1",
            "title": "Engine Repair",
            "description": "Our engine repair service covers everything from diagnostics to full repair.",
        },
        {
            "id": "2",
            "title": "Tire Replacement",
            "description": "Get your tires replaced with high-quality ones suited for your vehicle.",
        },
        {
            "id": "3",
            "title": "Oil Change",
            "description": "Regular oil changes to keep your engine running smoothly.",
        },
    ],
}

enquiry_data = {
    "message": "Please select the type of enquiry.",
    "header": "Enquiry Options",
    "footer": "Let us know your enquiry type.",
    "buttons": [
        {
            "id": "1",
            "title": "Availability",
            "description": "Check the availability of vehicles or services.",
        },
        {
            "id": "2",
            "title": "Pricing",
            "description": "Get pricing details for our vehicles and services.",
        },
        {
            "id": "3",
            "title": "Booking an Appointment",
            "description": "Schedule a time for a vehicle inspection or service.",
        },
    ],
}

responses = {
    "hello": greetings,
    "hi": greetings,
    "looking for machine": machines_data,
    "services": services_data,
    "enquiry": enquiry_data,
    "bulldozer": machine1_data,
}
