import time
import logging
import threading
from pyrekordbox import Rekordbox6Database
from pyrekordbox.db6 import tables
from pypresence import Presence
from pystray import Icon, MenuItem, Menu
from PIL import Image

logging.getLogger("pyrekordbox.db6.database").setLevel(logging.ERROR)

DISCORD_CLIENT_ID = '1344323770797789336'
db = Rekordbox6Database()

# ---------- System Tray ----------
def on_quit(icon, item):
    icon.stop()
    exit(0)

def create_tray_icon():
    image = Image.open("rs/icon.png")  
    menu = Menu(MenuItem('Exit', on_quit))
    icon = Icon("Rekordbox Presence", image, "Rekordbox Presence", menu)
    icon.run()

# ---------- Rich Presence Monitor ----------
def monitor_rekordbox_history(interval_seconds=3):
    last_known_title = None
    rpc = None
    start_time = None

    try:
        rpc = Presence(DISCORD_CLIENT_ID)
        rpc.connect()
    except:
        rpc = None

    while True:
        try:
            last_played = (
                db.get_history_songs()
                .order_by(tables.DjmdSongHistory.created_at.desc())
                .first()
            )

            current_title = None
            if last_played and last_played.Content:
                current_title = last_played.Content.Title

            if current_title != last_known_title:
                if current_title:
                    start_time = int(time.time())
                    if rpc:
                        try:
                            rpc.update(
                                state="Now Playing: " + current_title,
                                large_image="icon",
                                large_text="Rekordbox DJ",
                                start=start_time
                            )
                        except:
                            try:
                                rpc.close()
                                rpc = Presence(DISCORD_CLIENT_ID)
                                rpc.connect()
                            except:
                                rpc = None
                else:
                    start_time = None
                    if rpc:
                        try:
                            rpc.clear()
                        except:
                            pass

                last_known_title = current_title

            time.sleep(interval_seconds)

        except KeyboardInterrupt:
            if rpc:
                rpc.close()
            break
        except:
            time.sleep(10)

# ---------- Run ----------
if __name__ == "__main__":
    tray_thread = threading.Thread(target=create_tray_icon, daemon=True)
    tray_thread.start()
    monitor_rekordbox_history()
