# CrystalRET 

![GitHub release](https://img.shields.io/github/v/release/Lupix111/CrystalRET?include_prereleases&label=versione)
![License](https://img.shields.io/github/license/Lupix111/CrystalRET)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![Status](https://img.shields.io/badge/status-alpha-orange)
[![Ko-fi](https://img.shields.io/badge/Supporta-Ko--fi-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/emanuelecarlino)

> ⚠️ **Progetto in fase di sviluppo attivo — versione 0.9 alpha.** Potrebbero esserci bug e funzionalità incomplete. Ogni feedback è benvenuto!

**CrystalRET** è uno strumento open source per il monitoraggio automatico di frequenze radio, pensato per **radioamatori** e appassionati di **SDR** e **radioscanning**. Cattura le trasmissioni in tempo reale, le trascrive automaticamente con l'intelligenza artificiale e le analizza con un modello linguistico locale.
Pensato per chi va a dormire ma vuole continuare a tenere sott'occhio le proprie frequenze preferite.
---

## ✨ Funzionalità

- 🎤 **Rilevamento automatico della voce** tramite [Silero VAD](https://github.com/snakers4/silero-vad), niente più registrazioni continue, solo quando c'è davvero qualcuno che parla
- 📝 **Trascrizione automatica** con [faster-whisper](https://github.com/guillaumekynast/faster-whisper), supporto completo per l'italiano
- 🤖 **Analisi AI locale** con [Ollama](https://ollama.com), tutto gira sul tuo PC quindi non hai limiti di token
- 📻 **Compatibile con qualsiasi ricevitore radio** con uscita audio, Baofeng UV-5R, RTL-SDR, scanner, ricetrasmettitori, etc.
- 📋 **Log automatico** delle trasmissioni con timestamp e frequenza
- 🖥️ **Interfaccia grafica** intuitiva basata su Qt

---

## 📋 Requisiti

- Windows 10/11 (Linux in arrivo)
- [Ollama](https://ollama.com/download) installato con almeno un modello (es. `ollama pull mistral`)
- Un dispositivo audio di input (scheda audio USB, cavo ausiliario dal ricevitore)
- Connessione internet solo al primo avvio (per scaricare i modelli Whisper)

---

## 🚀 Installazione

### Metodo 1 — Installer (consigliato)
1. Scarica `CrystalRET_0.9_alpha_setup.exe` dalla pagina [Releases](https://github.com/Lupix111/CrystalRET/releases)
2. Esegui l'installer e segui le istruzioni
3. Assicurati di avere Ollama installato e almeno un modello scaricato (preferibilmente mistral)

### Metodo 2 — Da sorgente
```bash
git clone https://github.com/Lupix111/CrystalRET.git
cd CrystalRET
pip install -r requirements.txt
python __main__.py
```

---

## ⚙️ Configurazione rapida

1. Collega il tuo ricevitore radio al PC tramite cavo aux o adattatore USB
2. Avvia CrystalRET
3. Vai in **Impostazioni** e seleziona il dispositivo audio corretto
4. Scegli il modello Whisper (consigliato: `small` o `medium` per l'italiano)
5. Imposta la frequenza che stai monitorando nel pannello sinistro
6. Premi **Monitoraggio**, CrystalRET inizierà ad ascoltare e trascrivere automaticamente

---

## 🛠️ Tecnologie utilizzate

| Componente | Tecnologia |
|---|---|
| Interfaccia grafica | PySide6 (Qt) |
| Rilevamento voce | Silero VAD |
| Trascrizione | faster-whisper (OpenAI Whisper) |
| Analisi AI | Ollama (locale) |
| Audio | PyAudio + pydub |

---

## 🗺️ Roadmap

- [ ] Supporto Linux (Debian/Ubuntu)
- [ ] Persistenza impostazioni tra sessioni
- [ ] Supporto CUDA per trascrizione accelerata
- [ ] Integrazione diretta con RTL-SDR
- [ ] Decodifica di segnali digitali (DMR, D-STAR)
- [ ] Esportazione log in formato CSV

---

## 🤝 Contribuire

Il progetto è in fase alpha — ogni contributo è benvenuto! Apri una issue per segnalare bug o proporre funzionalità, o una pull request se vuoi contribuire direttamente.

---

## ☕ Supporta il progetto

Se CrystalRET ti è utile e vuoi supportarne lo sviluppo:

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/emanuelecarlino)

---

## 📄 Licenza

Distribuito sotto licenza **MIT**. Vedi il file [LICENSE](LICENSE) per i dettagli.

---

## 👤 Autore

**Emanuele Carlino**  
GitHub: [@Lupix111](https://github.com/Lupix111)
E-mail: em4n.carlino@gmail.com
Telegram: @Vuurjager
---

*CrystalRET è un progetto amatoriale non affiliato con alcun produttore di apparati radio.*
