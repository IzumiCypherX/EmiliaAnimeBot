from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)

with i:
    strinsess = i.export_session_string()
    print("\nString Session Generated. Copy and keep it Confidentially\n")
    print(f"\n{stringsess}\n")