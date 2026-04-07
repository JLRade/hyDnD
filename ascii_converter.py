import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os

try:
    from ascii_magic import AsciiArt
except ImportError:
    messagebox.showerror("Missing dependency", "Run: pip install ascii-magic")
    raise SystemExit


CHAR_PRESETS = {
    "Default":     None,
    "Dense":       " .:-=+*#%@",
    "Blocks":      " ░▒▓█",
    "Simple":      " .*#",
    "Dots":        " .oO",
}


class AsciiConverterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ASCII Art Converter")
        self.resizable(True, True)
        self.minsize(700, 500)
        self.configure(bg="#1e1e1e")

        self._image_path = None
        self._last_art = None
        self._build_ui()

    def _build_ui(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="#cccccc", font=("Segoe UI", 10))
        style.configure("TButton", background="#2d2d2d", foreground="#ffffff", font=("Segoe UI", 10), borderwidth=0, relief="flat", padding=6)
        style.map("TButton", background=[("active", "#3a3a3a")])
        style.configure("Accent.TButton", background="#5865f2", foreground="#ffffff", font=("Segoe UI", 10, "bold"), padding=6)
        style.map("Accent.TButton", background=[("active", "#4752c4")])
        style.configure("TScale", background="#1e1e1e", troughcolor="#3a3a3a")
        style.configure("TCombobox", fieldbackground="#2d2d2d", background="#2d2d2d", foreground="#ffffff", selectbackground="#5865f2")
        style.configure("TCheckbutton", background="#1e1e1e", foreground="#cccccc", font=("Segoe UI", 10))
        style.map("TCheckbutton", background=[("active", "#1e1e1e")])

        # ── Left panel ──────────────────────────────────────────────────────
        left = ttk.Frame(self, padding=16)
        left.pack(side=tk.LEFT, fill=tk.Y)

        # Image selector
        ttk.Label(left, text="Image", font=("Segoe UI", 11, "bold"), foreground="#ffffff").pack(anchor="w")
        ttk.Separator(left, orient="horizontal").pack(fill=tk.X, pady=6)

        self._thumb_label = ttk.Label(left, text="No image selected", foreground="#888888", wraplength=180, justify="center")
        self._thumb_label.pack(pady=4)

        ttk.Button(left, text="Browse file…", command=self._browse).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="Load from URL", command=self._ask_url).pack(fill=tk.X, pady=2)

        ttk.Separator(left, orient="horizontal").pack(fill=tk.X, pady=12)

        # Options
        ttk.Label(left, text="Options", font=("Segoe UI", 11, "bold"), foreground="#ffffff").pack(anchor="w")
        ttk.Separator(left, orient="horizontal").pack(fill=tk.X, pady=6)

        ttk.Label(left, text="Columns").pack(anchor="w")
        self._cols_var = tk.IntVar(value=100)
        cols_row = ttk.Frame(left)
        cols_row.pack(fill=tk.X, pady=2)
        ttk.Scale(cols_row, from_=40, to=220, orient="horizontal",
                  variable=self._cols_var, command=lambda _: self._cols_lbl.config(text=str(self._cols_var.get()))
                  ).pack(side=tk.LEFT, fill=tk.X, expand=True)
        self._cols_lbl = ttk.Label(cols_row, text="100", width=4)
        self._cols_lbl.pack(side=tk.LEFT)

        ttk.Label(left, text="Character set").pack(anchor="w", pady=(8, 0))
        self._char_var = tk.StringVar(value="Default")
        ttk.Combobox(left, textvariable=self._char_var, values=list(CHAR_PRESETS.keys()), state="readonly").pack(fill=tk.X, pady=2)

        self._mono_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(left, text="Monochrome", variable=self._mono_var).pack(anchor="w", pady=4)

        self._enhance_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(left, text="Enhance image", variable=self._enhance_var).pack(anchor="w")

        ttk.Separator(left, orient="horizontal").pack(fill=tk.X, pady=12)

        ttk.Button(left, text="Convert  ▶", style="Accent.TButton", command=self._convert).pack(fill=tk.X, pady=2)

        ttk.Separator(left, orient="horizontal").pack(fill=tk.X, pady=12)

        ttk.Label(left, text="Export", font=("Segoe UI", 11, "bold"), foreground="#ffffff").pack(anchor="w")
        ttk.Separator(left, orient="horizontal").pack(fill=tk.X, pady=6)
        ttk.Button(left, text="Save as .txt", command=lambda: self._save("txt")).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="Save as .html", command=lambda: self._save("html")).pack(fill=tk.X, pady=2)
        ttk.Button(left, text="Copy to clipboard", command=self._copy).pack(fill=tk.X, pady=2)

        # ── Right panel (output) ─────────────────────────────────────────────
        right = ttk.Frame(self, padding=(0, 16, 16, 16))
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        header = ttk.Frame(right)
        header.pack(fill=tk.X, pady=(0, 6))
        ttk.Label(header, text="Output", font=("Segoe UI", 11, "bold"), foreground="#ffffff").pack(side=tk.LEFT)
        self._status_lbl = ttk.Label(header, text="", foreground="#888888")
        self._status_lbl.pack(side=tk.RIGHT)

        text_frame = tk.Frame(right, bg="#1e1e1e")
        text_frame.pack(fill=tk.BOTH, expand=True)

        self._output = tk.Text(
            text_frame,
            font=("Courier New", 5),
            bg="#0d0d0d",
            fg="#e0e0e0",
            insertbackground="#ffffff",
            wrap="none",
            relief="flat",
            borderwidth=0,
            state="disabled",
        )
        vsb = ttk.Scrollbar(text_frame, orient="vertical", command=self._output.yview)
        hsb = ttk.Scrollbar(text_frame, orient="horizontal", command=self._output.xview)
        self._output.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self._output.pack(fill=tk.BOTH, expand=True)

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _browse(self):
        path = filedialog.askopenfilename(
            title="Select image",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp *.gif *.webp *.tiff"), ("All files", "*.*")]
        )
        if path:
            self._image_path = path
            self._url = None
            name = os.path.basename(path)
            self._thumb_label.config(text=f"📄 {name}", foreground="#5865f2")
            self._status_lbl.config(text="")

    def _ask_url(self):
        dialog = tk.Toplevel(self)
        dialog.title("Load from URL")
        dialog.configure(bg="#1e1e1e")
        dialog.geometry("400x110")
        dialog.grab_set()

        ttk.Label(dialog, text="Image URL:").pack(anchor="w", padx=16, pady=(16, 4))
        url_var = tk.StringVar()
        entry = ttk.Entry(dialog, textvariable=url_var, width=50)
        entry.pack(fill=tk.X, padx=16)
        entry.focus()

        def load():
            url = url_var.get().strip()
            if url:
                self._image_path = None
                self._url = url
                self._thumb_label.config(text=f"🌐 {url[:30]}…", foreground="#5865f2")
                self._status_lbl.config(text="")
            dialog.destroy()

        ttk.Button(dialog, text="Load", style="Accent.TButton", command=load).pack(pady=10)
        dialog.bind("<Return>", lambda _: load())

    def _convert(self):
        if not self._image_path and not getattr(self, "_url", None):
            messagebox.showwarning("No image", "Please select an image or enter a URL first.")
            return
        self._status_lbl.config(text="Converting…", foreground="#f0a500")
        self.update_idletasks()
        threading.Thread(target=self._run_conversion, daemon=True).start()

    def _run_conversion(self):
        try:
            cols = self._cols_var.get()
            mono = self._mono_var.get()
            enhance = self._enhance_var.get()
            char = CHAR_PRESETS[self._char_var.get()]

            if self._image_path:
                art = AsciiArt.from_image(self._image_path)
            else:
                art = AsciiArt.from_url(self._url)

            kwargs = dict(columns=cols, monochrome=mono, enhance_image=enhance)
            if char:
                kwargs["char"] = char

            result = art.to_ascii(**kwargs)
            self._last_art = (art, kwargs)

            self.after(0, lambda: self._display(result))
        except Exception as e:
            self.after(0, lambda: self._show_error(str(e)))

    def _display(self, text):
        self._output.config(state="normal")
        self._output.delete("1.0", tk.END)
        self._output.insert(tk.END, text)
        self._output.config(state="disabled")
        lines = text.count("\n")
        chars = len(text)
        self._status_lbl.config(text=f"{lines} lines · {chars:,} chars", foreground="#888888")

    def _show_error(self, msg):
        self._status_lbl.config(text="Error", foreground="#e05252")
        messagebox.showerror("Conversion failed", msg)

    def _save(self, fmt):
        if not self._last_art:
            messagebox.showwarning("Nothing to save", "Convert an image first.")
            return

        art, kwargs = self._last_art

        if fmt == "txt":
            path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file", "*.txt")])
            if path:
                text = art.to_ascii(**kwargs)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
                messagebox.showinfo("Saved", f"Saved to {path}")

        elif fmt == "html":
            path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML file", "*.html")])
            if path:
                html_kwargs = {k: v for k, v in kwargs.items() if k != "monochrome"}
                art.to_html_file(path, **html_kwargs)
                messagebox.showinfo("Saved", f"Saved to {path}")

    def _copy(self):
        text = self._output.get("1.0", tk.END)
        if text.strip():
            self.clipboard_clear()
            self.clipboard_append(text)
            self._status_lbl.config(text="Copied!", foreground="#57f287")
            self.after(2000, lambda: self._status_lbl.config(
                text=self._status_lbl.cget("text").replace("Copied!", "").strip() or "",
                foreground="#888888"
            ))
        else:
            messagebox.showwarning("Nothing to copy", "Convert an image first.")


if __name__ == "__main__":
    app = AsciiConverterApp()
    app.mainloop()
