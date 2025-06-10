# 🎧 Rekordbox Discord Presence

This lightweight background utility updates your **Discord Rich Presence** with the most recently played track from **Rekordbox**, and runs silently in the **system tray**.

![preview](preview.png)

---

## 💡 Features

- ✅ Automatically fetches the latest track played in Rekordbox
- ✅ Updates Discord Rich Presence with:
  - Track name
  - Elapsed time
- ✅ Runs silently in the background (no terminal window)
- ✅ Tray icon with a right-click "Exit" menu
- ✅ Resource-efficient, minimal, and clean

---

## 📦 Requirements

- Windows
- Discord
- Rekordbox
---

## 🚀 How to Use

1. Download the latest release `.exe` from the [Releases](https://github.com/yourusername/yourrepo/releases) page
3. Run the `.exe` – it will:
   - Connect to Discord
   - Show up in your system tray
   - Auto-update your Discord Rich Presence based on Rekordbox playback
4. To quit, right-click the tray icon → **Exit**

---

## 📥 Download

👉 Grab the latest `.exe` from the [Releases](https://github.com/yourusername/yourrepo/releases) tab.

---

## 🔧 Customization

If you’re compiling from source, feel free to customize:

```python
state="Now Playing: " + current_title,
large_image="icon",       
large_text="Rekordbox DJ"
