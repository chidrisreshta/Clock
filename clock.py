import tkinter as tk
from datetime import datetime
import time
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Clock App")
        self.root.geometry("300x250")
        self.root.resizable(False, False)

        # Clock
        self.clock_label = tk.Label(root, text="", font=("Arial", 16))
        self.clock_label.pack(pady=10)
        self.update_clock()

        # Stopwatch
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 30))
        self.stopwatch_label.pack(pady=20)

        self.start_time = None
        self.running = False
        self.elapsed_time = 0

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start", width=8, command=self.start_stopwatch)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", width=8, command=self.stop_stopwatch)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", width=8, command=self.reset_stopwatch)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text="Current Time: " + now)
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        while self.running:
            time.sleep(0.1)
            self.elapsed_time = time.time() - self.start_time
            mins, secs = divmod(int(self.elapsed_time), 60)
            hours, mins = divmod(mins, 60)
            self.stopwatch_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")

    def start_stopwatch(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            threading.Thread(target=self.update_stopwatch, daemon=True).start()

    def stop_stopwatch(self):
        if self.running:
            self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()
