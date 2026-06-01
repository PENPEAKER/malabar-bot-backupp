from flask import Flask, request, send_from_directory
app = Flask(__name__)
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('images', filename)
from dotenv import load_dotenv
import os
import requests
from products import PRODUCTS, SHOP_CONTACT
user_states = {}
last_product = {}

load_dotenv()



VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

ACCESS_TOKEN = "EAAW5xvVGUWYBRglR16ta1laXFORReaygFuFDXZBYCmYHYMXw1njqng07LurEHn7NeoZC94kHehgFR1FfPjZAAwyBP2Ucb5f3JxEdxrL95PfHKVjShPccW2IXYog0zccfYeSSBoKyWQjdlErFhwHkkMyDZBE8rao9eZA6bZAAp8tORbZB1bRda7LkrrhXrHbKPYb1rZA2cGvgSCGUbEP1Piw7bLL007UvpGAA1uVjrqjdYY9aZBaHSdezZAfnsal0oPQE0L8U9cIpFq5aBJItfQ6ZAVk4tI6"
PHONE_NUMBER_ID = "1151563918036377"

WHATSAPP_URL = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"


# ==============================
# SEND WHATSAPP MESSAGE
# ==============================

def send_message(to, message):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)


# ==============================
# SEND IMAGE
# ==============================

def send_image(to, image_name, caption=""):

    image_url = f"https://consuming-washable-neatly.ngrok-free.dev/images/{image_name}"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "image",
        "image": {
            "link": image_url,
            "caption": caption
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)


# ==============================
# SEND MAIN LIST MENU
# ==============================

def send_main_list_menu(to):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",

            "header": {
                "type": "text",
                "text": "🔥 MUSTHAFA MALABAR PLUS"
            },

            "body": {
                "text": "Choose a category 👇"
            },

            "footer": {
                "text": "Powered by MALABAR BOT"
            },

            "action": {
                "button": "View Categories",

                "sections": [
                    {
                        "title": "Categories",

                        "rows": [
                            {
                                "id": "tv",
                                "title": "📺 Smart TVs"
                            },

                            {
                                "id": "fridge",
                                "title": "❄️ Refrigerators"
                            },

                            {
                                "id": "washing",
                                "title": "🧺 Washing Machines"
                            },

                            {
                                "id": "ac",
                                "title": "🌬️ Air Conditioners"
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)

# ==============================
# SEND PRODUCT BUTTONS
# ==============================

def send_product_buttons(to):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",

            "body": {
                "text": "Choose an option 👇"
            },

            "footer": {
                "text": "MALABAR BOT"
            },

            "action": {
                "buttons": [

                    {
                        "type": "reply",
                        "reply": {
                            "id": "buy",
                            "title": "🛒 Buy Now"
                        }
                    },

                    {
                        "type": "reply",
                        "reply": {
                            "id": "call",
                            "title": "📞 Call Shop"
                        }
                    },

                    {
                        "type": "reply",
                        "reply": {
                            "id": "menu",
                            "title": "🏠 Main Menu"
                        }
                    }

                ]
            }
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)

# ==============================
# MAIN MENU
# ==============================

def send_main_menu(to):

    menu = """

🔥 *WELCOME TO MUSTHAFA MALABAR PLUS* 🔥

Please choose a category 👇

1️⃣ Smart TVs
2️⃣ Refrigerators
3️⃣ Washing Machines
4️⃣ Air Conditioners
5️⃣ Other Products

Send the number to continue.
"""

    send_message(to, menu)


# ==============================
# SMART TV BUTTON MENU
# ==============================

def smart_tv_menu(to):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",

            "header": {
                "type": "text",
                "text": "📺 SMART TV OPTIONS"
            },

            "body": {
                "text": "Choose TV Size 👇"
            },

            "footer": {
                "text": "MALABAR BOT"
            },

            "action": {
                "button": "View TVs",

                "sections": [
                    {
                        "title": "Smart TVs",

                        "rows": [
                            {
                                "id": "tv32",
                                "title": "32 Inch TV",
                                "description": "3 Year Warranty"
                            },

                            {
                                "id": "tv43",
                                "title": "43 Inch TV",
                                "description": "3 Year Warranty"
                            },

                            {
                                "id": "tv50",
                                "title": "50 Inch TV",
                                "description": "3 Year Warranty"
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)

# ==============================
# FRIDGE MENU
# ==============================

def fridge_menu(to):

    msg = """

❄️ *REFRIGERATOR OPTIONS*

━━━━━━━━━━━━━━━

1️⃣ Single Door

2️⃣ Double Door

3️⃣ Side By Side

━━━━━━━━━━━━━━━

↩️ 0 → Back to Main Menu

🏠 home → Main Menu

━━━━━━━━━━━━━━━

💬 Reply with option number
"""

    send_message(to, msg)


# ==============================
# SMART FRIDGE BUTTON MENU
# ==============================

def fridge_menu(to):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",

            "header": {
                "type": "text",
                "text": "❄️ REFRIGERATOR OPTIONS"
            },

            "body": {
                "text": "Choose Refrigerator 👇"
            },

            "footer": {
                "text": "MALABAR BOT"
            },

            "action": {
                "button": "View Fridges",

                "sections": [
                    {
                        "title": "Refrigerators",

                        "rows": [
                            {
                                "id": "fridge1",
                                "title": "Single Door",
                                "description": "Full & Compressor Warranty"
                            },

                            {
                                "id": "fridge2",
                                "title": "Double Door",
                                "description": "Full & Compressor Warranty"
                            },

                            {
                                "id": "fridge3",
                                "title": "Side By Side",
                                "description": "Premium Model"
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)

# ==============================
# WASHING MACHINE MENU
# ==============================

def washing_menu(to):

    msg = """

🧺 *WASHING MACHINE OPTIONS*

1️⃣ Semi Automatic
2️⃣ Top Load
3️⃣ Front Load

Reply with option number.
"""

    send_message(to, msg)

# ==============================
# WASHING MACHINE BUTTON MENU
# ==============================

def washing_menu(to):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",

            "header": {
                "type": "text",
                "text": "🧺 WASHING MACHINE OPTIONS"
            },

            "body": {
                "text": "Choose Washing Machine 👇"
            },

            "footer": {
                "text": "MALABAR BOT"
            },

            "action": {
                "button": "View Machines",

                "sections": [
                    {
                        "title": "Washing Machines",

                        "rows": [
                            {
                                "id": "washing1",
                                "title": "Semi Automatic",
                                "description": "11KG Capacity"
                            },

                            {
                                "id": "washing2",
                                "title": "Top Load",
                                "description": "10KG Capacity"
                            },

                            {
                                "id": "washing3",
                                "title": "Front Load",
                                "description": "Premium Model"
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)    

    


# ==============================
# AC MENU
# ==============================

def ac_menu(to):

    msg = """

🌬️ *AIR CONDITIONER OPTIONS*

1️⃣ 1 Ton
2️⃣ 1.5 Ton
3️⃣ 2 Ton

Reply with option number.
"""

    send_message(to, msg)

# ==============================
# AC BUTTON MENU
# ==============================

def ac_menu(to):

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",

            "header": {
                "type": "text",
                "text": "🌬️ AC OPTIONS"
            },

            "body": {
                "text": "Choose Air Conditioner 👇"
            },

            "footer": {
                "text": "MALABAR BOT"
            },

            "action": {
                "button": "View ACs",

                "sections": [
                    {
                        "title": "Air Conditioners",

                        "rows": [
                            {
                                "id": "ac1",
                                "title": "1 Ton AC",
                                "description": "Inverter Model"
                            },

                            {
                                "id": "ac2",
                                "title": "1.5 Ton AC",
                                "description": "Inverter Model"
                            },

                            {
                                "id": "ac3",
                                "title": "2 Ton AC",
                                "description": "Premium Model"
                            }
                        ]
                    }
                ]
            }
        }
    }

    response = requests.post(
        WHATSAPP_URL,
        headers=headers,
        json=data
    )

    print(response.text)

# ==============================
# OTHER PRODUCTS
# ==============================

def other_products(to):

    msg = """

🛍️ *OTHER PRODUCTS*

• Mixer
• Fan
• Light
• Iron Box
• Bed
• SOFA
• Home Theatre

""" + SHOP_CONTACT

    send_message(to, msg)


# ==============================
# PRODUCT DETAILS
# ==============================

def send_product_details(to, title, old_price, offer_price):

    msg = f"""

🔥 *{title}*

━━━━━━━━━━━━━━

💎 Premium Product
✅ Warranty Available
⚡ Latest Model

💰 MRP: ~~₹{old_price}~~

🔥 OFFER PRICE
👉 ₹{offer_price}

━━━━━━━━━━━━━━

📞 SHOP CONTACT

☎️ 0466 359 3100
📱 8089503133
📱 9645931333

📍 MALABAR PLUS

✨ Super offer available now
"""

    send_message(to, msg)


# ==============================
# WEBHOOK VERIFY
# ==============================

@app.route("/webhook", methods=["GET"])
def verify():

    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if token == VERIFY_TOKEN:
        return challenge

    return "Verification failed"


# ==============================
# RECEIVE MESSAGES
# ==============================

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json()

    try:

        value = data["entry"][0]["changes"][0]["value"]

        if "messages" not in value:
            return "OK", 200

        message = value["messages"][0]

        sender = message["from"]

        # =========================
        # NORMAL TEXT MESSAGE
        # =========================

        if message["type"] == "text":

            text = message["text"]["body"].strip().lower()

        # =========================
        # LIST BUTTON REPLY
        # =========================

        elif message["type"] == "interactive":

            interactive = message["interactive"]

            if interactive["type"] == "list_reply":
                text = interactive["list_reply"]["id"]

            elif interactive["type"] == "button_reply":
                text = interactive["button_reply"]["id"]

            else:
                return "OK", 200

        else:
            return "OK", 200
        
# =========================
# BUY BUTTON
# =========================

        if text == "buy":

                product = last_product.get(sender, "Unknown Product")

                owner_message = f"""
            🔥 MALABAR BOT OWNER ALERT

            📱 Customer: {sender}

            🛒 Interested Product:
            {product}
            """

                send_message(
                    "919961930333",
                    owner_message
                )

                send_message(
                    sender,
                    "✅ Thank you for your interest.\n\nOur sales team will contact you shortly."
                )

                return "OK", 200

# =========================
# CALL SHOP BUTTON
# =========================

        if text == "call":

            send_message(
                sender,
                "📞 *Call MUSTHAFA MALABAR PLUS*\n\n☎️ 9645931333"
            )

            return "OK", 200
        
                # =========================
# MAIN MENU BUTTON
# =========================

        if text == "menu":

            user_states[sender] = "main"

            send_main_list_menu(sender)

            return "OK", 200

            product = last_product.get(sender, "Unknown Product")

            owner_message = f"""
        🔥 MALABAR BOT OWNER ALERT

📱 Customer: {sender}

🛒 Interested Product:
{product}
"""
            
            print("MESSAGE:", text)

            send_message(
                "919961930333",
                owner_message
            )

            send_message(
                sender,
                "✅ Thank you for your interest.\n\nOur sales team will contact you shortly."
            )

            return "OK", 200

        print("MESSAGE:", text)

        

                # GET USER STATE
        state = user_states.get(sender, "main")

        # =========================
        # MAIN MENU
        # =========================

        if state == "main":

            if text in ["hi", "hello", "menu", "start"]:
                user_states[sender] = "main"
                send_main_list_menu(sender)

            elif text == "tv":

                smart_tv_menu(sender)
                user_states[sender] = "tv"

            elif text == "fridge":

                fridge_menu(sender)
                user_states[sender] = "fridge"

            elif text == "washing":

                washing_menu(sender)
                user_states[sender] = "washing"

            elif text == "ac":

                ac_menu(sender)
                user_states[sender] = "ac"

            elif text == "5":

                other_products(sender)

            else:

                send_main_list_menu(sender)




# =========================
# TV MENU
# =========================

        elif state == "tv":

            if text == "0" or text == "home":

                user_states[sender] = "main"
                send_main_list_menu(sender)            
            

            if text == "tv32":

                last_product[sender] = "32 Inch Smart TV"

                send_image(
                    sender,
                    "tv32_new.jpg",
                    "📺 *32 Inch Smart TV*\n\n❌ Old Price: ₹18,000\n\n✅ Offer Price: ₹10,800\n\n🛡 Warranty: 3 Years\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)


            elif text == "tv43":

                last_product[sender] = "43 Inch Smart TV"

                send_image(
                    sender,
                    "tv43_new.jpg",
                    "📺 *43 Inch Smart TV*\n\n❌ Old Price: ₹28,000\n\n✅ Offer Price: ₹17,800\n\n🛡 Warranty: 3 Years\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            elif text == "tv50":

                last_product[sender] = "50 Inch Smart TV"

                send_image(
                    sender,
                    "tv50_new.jpg",
                    "📺 *50 Inch Smart TV*\n\n❌ Old Price: ₹48,000\n\n✅ Offer Price: ₹27,800\n\n🛡 Warranty: 3 Years\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            else:

                smart_tv_menu(sender)



# =========================
# FRIDGE MENU
# =========================

        elif state == "fridge":

            if text == "0" or text == "home":

                user_states[sender] = "main"
                send_main_list_menu(sender)

            if text == "fridge1":

                last_product[sender] = "Single Door Refrigerator"

                send_image(
                    sender,
                    "fridge1_new.jpg",
                    "🧊 *Single Door Refrigerator*\n\n❌ Old Price: ₹17,500\n\n✅ Offer Price: ₹11,500\n\n🛡  1 Year Full Warranty\n\n🛡 10 year compressor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            elif text == "fridge2":

                last_product[sender] = "Double Door Refrigerator"

                send_image(
                    sender,
                    "fridge2_new.jpg",
                    "🧊 *Double Door Refrigerator*\n\n❌ Old Price: ₹33,000\n\n✅ Offer Price: ₹19,800\n\n🛡  1 Year Full Warranty\n\n🛡 10 year compressor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            elif text == "fridge3":

                last_product[sender] = "Side By Side Refrigerator"

                send_image(
                    sender,
                    "fridge3_new.jpg",
                    "🧊 *Side By Side Refrigerator*\n\n❌ Old Price: ₹160,000\n\n✅ Offer Price: ₹58,000\n\n🛡  1 Year Full Warranty \n\n🛡 10 year compressor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            else:

                fridge_menu(sender)

 

# =========================
# WASHING MACHINE MENU
# =========================

        elif state == "washing":

            if text == "0" or text == "home":

                user_states[sender] = "main"
                send_main_list_menu(sender)

            if text == "washing1":

                last_product[sender] = "Semi Automatic Washing Machine"

                send_image(
                    sender,
                    "washing1_new.jpg",
                    "🧺 *Semi Automatic Washing Machine 11KG*\n\n❌ Old Price: ₹21,000\n\n✅ Offer Price: ₹14,800\n\n🛡  1 Year Full Warranty\n\n🛡 5 year Motor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            elif text == "washing2":

                last_product[sender] = "Top Load Washing Machine"

                send_image(
                    sender,
                    "washing2_new.jpg",
                    "🧺 *Top Load Washing Machine 10KG*\n\n❌ Old Price: ₹38,000\n\n✅ Offer Price: ₹21,500\n\n🛡  1 Year Full Warranty\n\n🛡 5 year Motor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            elif text == "washing3":

                last_product[sender] = "Front Load Washing Machine"

                send_image(
                    sender,
                    "washing3_new.jpg",
                    "🧺 *Front Load Washing Machine 10KG*\n\n❌ Old Price: ₹48,000\n\n✅ Offer Price: ₹26,500\n\n🛡 1 Year Full Warranty\n\n🛡 5 year Motor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            else:

                washing_menu(sender)
# =========================
# AC MENU
# =========================

        elif state == "ac":

            if text == "0" or text == "home":

                user_states[sender] = "main"
                send_main_list_menu(sender)

            if text == "ac1":

                last_product[sender] = "1 Ton Inverter AC"

                send_image(
                    sender,
                    "ac1_new.jpg",
                    "❄️ *1 Ton Inverter AC*\n\n❌ Old Price: ₹33,500\n\n✅ Offer Price: ₹23,500\n\n🛡 1 Year Full Warranty\n\n🛡 5 year compressor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            elif text == "ac2":

                last_product[sender] = "1.5 Ton AC"

                send_image(
                    sender,
                    "ac2_new.jpg",
                    "❄️ *1.5 Ton AC*\n\n❌ Old Price: ₹48,000\n\n✅ Offer Price: ₹28,500\n\n🛡  1 Year Full Warranty \n\n🛡 5 year compressor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            elif text == "ac3":

                last_product[sender] = "2 Ton AC"

                send_image(
                    sender,
                    "ac3_new.jpg",
                    "❄️ *2 Ton AC*\n\n❌ Old Price: ₹58,000\n\n✅ Offer Price: ₹31,800\n\n🛡  1 Year Full Warranty \n\n🛡 5 year compressor warranty\n\n⚡ Limited Stock Available\n\n📞 Contact:\n\n☎️ 0466 359 3100\n\n📱 8089503133\n\n📱 9645931333"
                )

                send_product_buttons(sender)

            else:

                ac_menu(sender)
    except Exception as e:
        print("ERROR:", e)

    return "OK", 200


# ==============================
# RUN SERVER
# ==============================

if __name__ == "__main__":
    app.run(port=5000, debug=True)

# ==============================
# RUN SERVER
# ==============================

#if __name__ == "__main__":
 #   app.run(port=5000, debug=True)