import webview
import platformdirs
from pathlib import Path

ascii_text = r"""
__________                        ________                  _____                 
\______   \_____    ______ ______/  _____/  ____   ____    /  _  \ ______ ______  
 |     ___/\__  \  /  ___//  ___/   \  ____/ __ \ /    \  /  /_\  \\____ \\____ \ 
 |    |     / __ \_\___ \ \___ \\    \_\  \  ___/|   |  \/    |    \  |_> >  |_> >
 |____|    (____  /____  >____  >\______  /\___  >___|  /\____|__  /   __/|   __/ 
                \/     \/     \/        \/     \/     \/         \/|__|   |__|    
"""

class Api:
    def txt(self, data):
        try:
            desktop = platformdirs.user_desktop_dir()
            path = Path(desktop) / "Journal_Passwords.txt"
            with open(path, "a", encoding="utf-8") as f:
                f.write(ascii_text + "\n" + "-"*20 + "\n"*2 + data + "\n" + "-"*20 + "\n")
                
        except Exception as e:
            print(f"Error: {str(e)}")

api = Api()

webview.create_window("PassGenApp", 
                      "web-ui/index.html", 
                      js_api=api,
                      resizable=False) 
webview.start()
