import customtkinter as ctk
import subprocess
from PIL import Image
import os

# Configuración inicial del tema oscuro moderno
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class XoolxiApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal grande y espaciosa
        self.title("Xoolxi Ultimate Optimizer - Edición Caballero")
        self.geometry("860x640")
        self.resizable(False, False)

        # --- FORZAR ICONO EN LA VENTANA Y BARRA DE TAREAS ---
        try:
            self.iconbitmap("logo.ico")
        except Exception:
            pass

        # --- SECCIÓN DE ENCABEZADO / LOGO ---
        self.label_title = ctk.CTkLabel(
            self, 
            text="⚔️ XOOLXI ULTIMATE OPTIMIZER ⚔️", 
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color="#e67e22"
        )
        self.label_title.pack(pady=(15, 5))

        # Subtítulo de estado transparente y confiable
        self.label_subtitle = ctk.CTkLabel(
            self, 
            text="Estado: Sistema protegido y listo para la batalla (Optimización Real)", 
            font=ctk.CTkFont(size=13),
            text_color="#a0a0a0"
        )
        self.label_subtitle.pack(pady=(0, 15))

        # --- SECCIÓN 1: BOTONES DE ACCIÓN (NORMAL Y EXTREMO) ---
        self.btn_action = ctk.CTkButton(
            self, 
            text="🛡️ EJECUTAR LIMPIEZA ESTÁNDAR", 
            command=lambda: self.liberar_ram_real(modo_extremo=False), 
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#1f6aa5",
            hover_color="#144870",
            height=42,
            width=400,
            corner_radius=8
        )
        self.btn_action.pack(pady=6)

        self.btn_extremo = ctk.CTkButton(
            self, 
            text="🔥 ACTIVAR MODO EXTREMO (Guerrero implacable)", 
            command=lambda: self.liberar_ram_real(modo_extremo=True), 
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#c0392b",
            hover_color="#962d22",
            height=42,
            width=400,
            corner_radius=8
        )
        self.btn_extremo.pack(pady=6)

        # --- SECCIÓN 2: SELECTOR PERSONALIZADO ---
        self.label_custom = ctk.CTkLabel(
            self, 
            text="Atacar un proceso o app específica por su nombre (ej: notepad.exe):", 
            font=ctk.CTkFont(size=12),
            text_color="#cccccc"
        )
        self.label_custom.pack(pady=(15, 3))

        self.entry_proceso = ctk.CTkEntry(
            self, 
            placeholder_text="Escribe aquí el nombre del proceso (con .exe)", 
            width=400,
            height=34,
            font=ctk.CTkFont(size=12)
        )
        self.entry_proceso.pack(pady=3)

        self.btn_custom = ctk.CTkButton(
            self, 
            text="🎯 Forzar Cierre de este Objetivo", 
            command=self.cerrar_proceso_personalizado, 
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color="#27ae60",
            hover_color="#1e8449",
            height=36,
            width=400,
            corner_radius=8
        )
        self.btn_custom.pack(pady=8)

        # --- SECCIÓN 3: SELLO DE CONFIANZA Y TRANSPARENCIA ---
        self.label_security = ctk.CTkLabel(
            self, 
            text="🔒 Transparencia: Usa comandos nativos (taskkill). Sin malware ni recolección de datos.", 
            font=ctk.CTkFont(size=11, slant="italic"),
            text_color="#3498db"
        )
        self.label_security.pack(pady=(10, 5))

        # Pie de página / Créditos
        self.label_footer = ctk.CTkLabel(
            self, 
            text="Creado por Fabrizio • Código abierto para la comunidad gamer", 
            font=ctk.CTkFont(size=11),
            text_color="#666666"
        )
        self.label_footer.pack(side="bottom", pady=12)

    def liberar_ram_real(self, modo_extremo):
        if modo_extremo:
            self.label_subtitle.configure(text="🔥 Modo Extremo activado: Despejando el campo de batalla...", text_color="#e74c3c")
            procesos_a_cerrar = [
                "Teams.exe", "OneDrive.exe", "Cortana.exe", 
                "YourPhone.exe", "SkypeApp.exe", "AdobeUpdateService.exe",
                "SearchIndexer.exe", "Spotify.exe"
            ]
        else:
            self.label_subtitle.configure(text="⏳ Limpiando procesos secundarios del sistema...", text_color="#f39c12")
            procesos_a_cerrar = [
                "Teams.exe", "OneDrive.exe", "Cortana.exe", "YourPhone.exe"
            ]

        self.btn_action.configure(state="disabled")
        self.btn_extremo.configure(state="disabled")
        self.update()

        cerrados_count = 0
        for proc in procesos_a_cerrar:
            try:
                resultado = subprocess.run(["taskkill", "/f", "/im", proc], capture_output=True, text=True)
                if resultado.returncode == 0:
                    cerrados_count += 1
            except Exception:
                pass

        self.label_subtitle.configure(
            text=f"✅ ¡Batalla ganada! Se neutralizaron {cerrados_count} procesos.", 
            text_color="#2ecc71"
        )
        self.btn_action.configure(state="normal")
        self.btn_extremo.configure(state="normal")

    def cerrar_proceso_personalizado(self):
        nombre_proceso = self.entry_proceso.get().strip()
        
        if not nombre_proceso:
            self.label_subtitle.configure(text="⚠️ Escribe un nombre de objetivo válido.", text_color="#e67e22")
            return

        if not nombre_proceso.lower().endswith(".exe"):
            nombre_proceso += ".exe"

        try:
            resultado = subprocess.run(["taskkill", "/f", "/im", nombre_proceso], capture_output=True, text=True)
            if resultado.returncode == 0:
                self.label_subtitle.configure(text=f"🎯 ¡Impacto! '{nombre_proceso}' ha sido eliminado.", text_color="#2ecc71")
            else:
                self.label_subtitle.configure(text=f"⚠️ Objetivo '{nombre_proceso}' no encontrado en activo.", text_color="#e67e22")
        except Exception:
            self.label_subtitle.configure(text="❌ Error al intentar ejecutar el comando.", text_color="#e74c3c")

        self.entry_proceso.delete(0, 'end')

if __name__ == "__main__":
    app = XoolxiApp()
    app.mainloop()