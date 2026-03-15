#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Personal Command Center - Windows 11 Style
Widget moderno e minimalista para seu desktop
"""

import tkinter as tk
from tkinter import ttk, font
import json
import random
import requests
from datetime import datetime
from pathlib import Path
import sys

# Caminho para arquivos de dados
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
TODOS_FILE = DATA_DIR / "todos.json"
CONFIG_FILE = DATA_DIR / "config.json"

# Paleta Windows 11 - Moderna e clean
COLORS = {
    'bg': '#F3F3F3',           # Background claro
    'card': '#FFFFFF',         # Cards brancos
    'accent': '#0067C0',       # Azul Windows 11
    'text': '#1F1F1F',         # Texto escuro
    'text_secondary': '#616161',  # Texto secundário
    'success': '#0F7B0F',      # Verde
    'border': '#E0E0E0',       # Bordas sutis
    'hover': '#F9F9F9'         # Hover state
}

def load_config():
    """Carrega configurações"""
    default_config = {
        "city": "São Paulo",
        "country_code": "BR"
    }

    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        return default_config

def get_weather():
    """Obtém clima"""
    config = load_config()
    try:
        city = config['city'].replace(' ', '+')
        url = f"http://wttr.in/{city}?format=%C+%t"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text.strip()
        return "Clima indisponível"
    except:
        return "Offline"

def load_todos():
    """Carrega TODOs"""
    if TODOS_FILE.exists():
        with open(TODOS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def get_quote():
    """Frase motivacional"""
    quotes = [
        "Progresso, não perfeição",
        "Um dia de cada vez",
        "Você consegue!",
        "Foco no que importa",
        "Pequenos passos, grandes mudanças",
        "Seja a melhor versão de você hoje",
        "Discipline beats motivation",
        "A consistência é a chave"
    ]
    return random.choice(quotes)

def get_habit():
    """Hábito do dia"""
    habits = [
        "🏋️ Exercício",
        "📚 Leitura",
        "🧘 Meditação",
        "💧 Hidratação",
        "💻 Aprender algo novo"
    ]
    return random.choice(habits)

class CommandCenter(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Command Center")
        self.configure(bg=COLORS['bg'])
        self.overrideredirect(True)  # Remove bordas padrão do Windows

        # Dimensões - compacto e elegante
        width = 380
        height = 420

        # Posicionar no canto inferior direito
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = screen_width - width - 20
        y = screen_height - height - 60  # 60px para barra de tarefas

        self.geometry(f"{width}x{height}+{x}+{y}")

        # Sempre no topo mas não invasivo
        self.attributes('-topmost', False)

        # Transparência leve (Windows 11 style)
        self.attributes('-alpha', 0.97)

        # Criar interface
        self.create_widgets()

        # Fechar com ESC
        self.bind('<Escape>', lambda e: self.destroy())

        # Arrastar janela
        self.bind('<Button-1>', self.start_move)
        self.bind('<B1-Motion>', self.on_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def create_widgets(self):
        """Cria interface moderna"""

        # Container principal com padding
        main_frame = tk.Frame(self, bg=COLORS['card'], padx=20, pady=20)
        main_frame.pack(fill='both', expand=True, padx=1, pady=1)

        # === HEADER ===
        header_frame = tk.Frame(main_frame, bg=COLORS['card'])
        header_frame.pack(fill='x', pady=(0, 15))

        # Título
        title_label = tk.Label(
            header_frame,
            text="Command Center",
            font=('Segoe UI', 16, 'bold'),
            bg=COLORS['card'],
            fg=COLORS['text']
        )
        title_label.pack(side='left')

        # Botão fechar (X)
        close_btn = tk.Label(
            header_frame,
            text="✕",
            font=('Segoe UI', 14),
            bg=COLORS['card'],
            fg=COLORS['text_secondary'],
            cursor='hand2'
        )
        close_btn.pack(side='right')
        close_btn.bind('<Button-1>', lambda e: self.destroy())

        # Linha separadora
        separator = tk.Frame(main_frame, bg=COLORS['border'], height=1)
        separator.pack(fill='x', pady=(0, 15))

        # === DATA E HORA ===
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        day_name = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"][now.weekday()]

        date_label = tk.Label(
            main_frame,
            text=f"📅 {day_name}, {date_str}",
            font=('Segoe UI', 10),
            bg=COLORS['card'],
            fg=COLORS['text_secondary']
        )
        date_label.pack(anchor='w', pady=(0, 12))

        # === CLIMA ===
        weather = get_weather()
        weather_label = tk.Label(
            main_frame,
            text=f"🌤️  {weather}",
            font=('Segoe UI', 11),
            bg=COLORS['card'],
            fg=COLORS['text']
        )
        weather_label.pack(anchor='w', pady=(0, 15))

        # === FOCO DO DIA ===
        focus_frame = tk.Frame(main_frame, bg=COLORS['bg'], padx=12, pady=10)
        focus_frame.pack(fill='x', pady=(0, 12))

        focus_title = tk.Label(
            focus_frame,
            text="🎯 FOCO DO DIA",
            font=('Segoe UI', 9, 'bold'),
            bg=COLORS['bg'],
            fg=COLORS['text_secondary']
        )
        focus_title.pack(anchor='w')

        habit = get_habit()
        habit_label = tk.Label(
            focus_frame,
            text=habit,
            font=('Segoe UI', 11),
            bg=COLORS['bg'],
            fg=COLORS['text']
        )
        habit_label.pack(anchor='w', pady=(4, 0))

        # === TODOS ===
        todos_frame = tk.Frame(main_frame, bg=COLORS['bg'], padx=12, pady=10)
        todos_frame.pack(fill='both', expand=True, pady=(0, 12))

        todos_title = tk.Label(
            todos_frame,
            text="✅ TAREFAS",
            font=('Segoe UI', 9, 'bold'),
            bg=COLORS['bg'],
            fg=COLORS['text_secondary']
        )
        todos_title.pack(anchor='w', pady=(0, 6))

        todos = load_todos()
        if not todos:
            no_todo = tk.Label(
                todos_frame,
                text="Sem tarefas - Aproveite! 🎉",
                font=('Segoe UI', 10),
                bg=COLORS['bg'],
                fg=COLORS['success']
            )
            no_todo.pack(anchor='w')
        else:
            for todo in todos[:3]:  # Máximo 3 TODOs visíveis
                status = "✓" if todo.get('done', False) else "○"
                color = COLORS['success'] if todo.get('done', False) else COLORS['text']

                todo_label = tk.Label(
                    todos_frame,
                    text=f"{status} {todo['task']}",
                    font=('Segoe UI', 10),
                    bg=COLORS['bg'],
                    fg=color
                )
                todo_label.pack(anchor='w', pady=2)

        # === MOTIVAÇÃO ===
        quote = get_quote()
        quote_label = tk.Label(
            main_frame,
            text=f'💡 "{quote}"',
            font=('Segoe UI', 10, 'italic'),
            bg=COLORS['card'],
            fg=COLORS['accent'],
            wraplength=340,
            justify='left'
        )
        quote_label.pack(anchor='w', pady=(0, 15))

        # === FOOTER ===
        footer_label = tk.Label(
            main_frame,
            text="ESC para fechar",
            font=('Segoe UI', 8),
            bg=COLORS['card'],
            fg=COLORS['text_secondary']
        )
        footer_label.pack(anchor='center')

def main():
    """Inicia aplicação"""
    app = CommandCenter()
    app.mainloop()

if __name__ == "__main__":
    main()
