import customtkinter as ctk
from tkinter import scrolledtext, messagebox
from analysis import investment_advisor
from utils import export_to_pdf, export_to_csv
from company_list import companies  # 💥 NEW

# --- GUI Setup ---
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("700x500")
app.title("📊 AI Investment Advisor")

# --- UI Elements ---

title_label = ctk.CTkLabel(app, text="AI Investment Advisor", font=("Arial", 24, "bold"))
title_label.pack(pady=10)

# Dropdown menu for company selection
company_names = list(companies.keys())
selected_company = ctk.StringVar(value=company_names[0])

company_dropdown = ctk.CTkOptionMenu(app, values=company_names, variable=selected_company)
company_dropdown.pack(pady=10)

# Output Box
output_box = scrolledtext.ScrolledText(app, height=15, width=75, font=("Consolas", 12))
output_box.pack(padx=10, pady=10)

# Analyze Button
def analyze():
    company = selected_company.get()
    ticker = companies.get(company)
    output_box.delete('1.0', ctk.END)

    if not ticker:
        messagebox.showerror("Error", f"Could not find ticker for {company}")
        return

    result = investment_advisor(company, ticker, verbose=False)

    if result["price_delta"] is None:
        output = result["decision"]
    else:
        output = f"""📈 {result['company']} ({result['symbol']})

🧠 Sentiment: {result['sentiment']} ({round(result['score'], 3)})
📉 Price Change: {round(result['price_delta'], 2)}%
💡 Advice: {result['decision']}"""

    output_box.insert(ctk.END, output)

analyze_button = ctk.CTkButton(app, text="Analyze", command=analyze)
analyze_button.pack(pady=10)

# Export Buttons
button_frame = ctk.CTkFrame(app)
button_frame.pack(pady=10)

export_pdf = ctk.CTkButton(button_frame, text="Export as PDF", command=lambda: export_to_pdf(output_box.get("1.0", "end-1c")))
export_pdf.pack(side="left", padx=10)

export_csv = ctk.CTkButton(button_frame, text="Export as CSV", command=lambda: export_to_csv(output_box.get("1.0", "end-1c")))
export_csv.pack(side="left", padx=10)

# Run App
app.mainloop()


