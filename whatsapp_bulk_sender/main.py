import pywhatkit
import pandas as pd
import time
import pyautogui


# Step 1: Load your CSV
contacts = pd.read_csv("contact.csv", encoding="utf-8",dtype={"phone": str})

# Step 2: Loop through all rows
for index, row in contacts.iterrows():
    try:
        name = str(row["name"]).strip()
        phone = str(row["phone"]).strip().replace(" ", "").replace("\u202a", "")
        message = str(row["message"]).strip()

        # Debug print to check actual phone number format
        print(f"📤 Sending to {name} → {phone} | Length: {len(phone)}")

        # Step 3: Send WhatsApp message
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone,
            message=message,
            wait_time=20,
            tab_close=False 
        )

        time.sleep(6)

        pyautogui.press("enter")

        print(f" Message sent to {name}!\n")
        time.sleep(15) 

    except Exception as e:
        print(f" Failed to send to {name}: {e}\n")
