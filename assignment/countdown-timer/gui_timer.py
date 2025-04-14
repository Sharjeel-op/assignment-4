import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.root.geometry("300x150")

        self.minutes = tk.IntVar(value=1)  # default to 1 minute

        tk.Label(root, text="Set Timer (minutes):").pack(pady=5)
        self.entry = tk.Entry(root, textvariable=self.minutes, width=5, justify='center')
        self.entry.pack()

        self.time_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.time_label.pack(pady=10)

        self.start_btn = tk.Button(root, text="Start Countdown", command=self.start_timer)
        self.start_btn.pack()

        self.running = False

    def start_timer(self):
        if not self.running:
            try:
                total_secs = int(self.minutes.get()) * 60
                self.countdown(total_secs)
                self.running = True
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a valid number of minutes.")

    def countdown(self, remaining):
        mins, secs = divmod(remaining, 60)
        self.time_label.config(text=f"{mins:02d}:{secs:02d}")
        if remaining > 0:
            self.root.after(1000, self.countdown, remaining - 1)
        else:
            self.running = False
            messagebox.showinfo("Time's up!", "⏰ Time is up!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownTimer(root)
    root.mainloop()
