# NeuroVision: Installation and Setup Guide
## Windows Deployment Manual for MCA Major Project Demonstration

This guide provides step-by-step instructions to set up, configure, and execute the **NeuroVision: Intelligent Multimodal Pattern Analysis Using Deep Learning** platform on a Windows workstation.

---

## 1. Prerequisites

Before installing, ensure the host system has the following software installed:

* **Operating System**: Windows 10 or Windows 11 (64-bit).
* **Python**: Python 3.10 to Python 3.14 (Verified on Python 3.14.4).
  * Ensure the *"Add Python to PATH"* option was checked during Python installation.
* **Node.js**: Node.js v18.0.0 or higher (v20+ recommended).
* **Package Manager**: npm (bundled with Node.js).
* **Git**: Optional (for version management).
* **Web Browser**: Google Chrome, Microsoft Edge, or Mozilla Firefox with Web Audio API support.

Verify installations via Windows Command Prompt or PowerShell:
```cmd
python --version
node --version
npm --version
```

---

## 2. Project Directory Structure

The project root directory is located at:
```text
D:\MY PROJECT\neurovision
```

Directory structure overview:
```text
D:\MY PROJECT\neurovision\
├── backend\                 # Python FastAPI backend & AI engine
│   ├── app\                 # REST API, models, pipelines, services
│   ├── database\            # SQLite database (neurovision.db)
│   ├── tests\               # Pytest automated test suites
│   ├── venv\                # Python Virtual Environment
│   └── requirements.txt     # Python backend dependencies
├── frontend\                # React + Vite frontend application
│   ├── src\                 # React components, pages, visualizers, styles
│   ├── package.json         # Frontend Node dependencies
│   └── vite.config.js       # Vite configuration
├── uploads\                 # Temporary staging for uploads
├── README.md                # Project master documentation
├── INSTALLATION.md          # This installation manual
├── API_DOCUMENTATION.md     # REST and WebSocket specifications
├── MODEL_DOCUMENTATION.md   # AI and deep learning specifications
└── PROJECT_ARCHITECTURE.md  # Architectural blueprints & Mermaid diagrams
```

---

## 3. Backend Installation & Setup

### Step 3.1: Open Terminal in Backend Directory
Open **Windows PowerShell** or **Command Prompt**:
```powershell
cd "d:\MY PROJECT\neurovision\backend"
```

### Step 3.2: Verify / Create Virtual Environment
A virtual environment named `venv` is configured in `backend/venv`. If creating a new one:
```powershell
python -m venv venv
```

### Step 3.3: Activate the Virtual Environment
In PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```
*Note: If PowerShell shows an Execution Policy restriction, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and retry, or use Command Prompt (`venv\Scripts\activate.bat`).*

### Step 3.4: Install Python Dependencies
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3.5: Environment Variables Configuration
The backend contains a `.env` file pre-configured for local execution:
```env
PROJECT_NAME="NeuroVision Backend"
API_V1_STR="/api"
PORT=8000
HOST="127.0.0.1"
ENVIRONMENT="development"
CORS_ORIGINS=["http://localhost:5173", "http://127.0.0.1:5173"]
DATABASE_URL="sqlite:///./database/neurovision.db"
```

### Step 3.6: Database Verification
The backend automatically connects to the SQLite database at `backend/database/neurovision.db`.
**DO NOT delete or reset `neurovision.db`**, as it contains existing verified records and system audit logs.

### Step 3.7: Start the FastAPI Backend Server
```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
Upon successful launch, the terminal displays:
```text
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     [STARTUP] NeuroVision Multi-Modal AI Engine initialized
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## 4. Frontend Installation & Setup

### Step 4.1: Open Second Terminal in Frontend Directory
Open a **new** terminal window:
```cmd
cd /d "d:\MY PROJECT\neurovision\frontend"
```

### Step 4.2: Install Node Dependencies
```cmd
npm install
```

### Step 4.3: Start the Vite Development Server
```cmd
npm run dev
```
Upon successful launch, the terminal displays:
```text
  VITE v5.4.21  ready in 450 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

---

## 5. Running the Complete Application

To run the complete platform, keep both terminals running simultaneously:

| Component | Terminal Directory | Execution Command | URL / Address |
| :--- | :--- | :--- | :--- |
| **Backend API** | `d:\MY PROJECT\neurovision\backend` | `.\venv\Scripts\python.exe -m uvicorn app.main:app --port 8000 --reload` | `http://localhost:8000` |
| **Frontend UI** | `d:\MY PROJECT\neurovision\frontend` | `npm run dev` | `http://localhost:5173` |

### Accessing the System
1. Open your browser and navigate to **`http://localhost:5173`**.
2. The Top Status Bar will show **`System Online`** with a green pulsating indicator, confirming active communication with the backend.
3. Interactive Swagger API documentation is available at **`http://localhost:8000/docs`**.
4. WebSocket live bus connects at **`ws://localhost:8000/ws`**.

### 5.1 Launching Guided Evaluator Demo Mode
To start the guided evaluation walkthrough:
1. In the top navigation bar or the main dashboard header, click the glowing **`DEMO MODE`** / **`GUIDED DEMO MODE`** button (or navigate to `Guided Demo Mode` in the left sidebar).
2. The 10-step evaluator demonstration interface opens with real-time hardware telemetry, live camera frame analysis, audio recording, Explainable AI heatmaps, and multimodal fusion.
3. Use the **`Next Step`** and **`Previous Step`** controls to navigate through the evaluation milestones.

---

## 6. AI Model Setup & Loading Behavior

NeuroVision utilizes pretrained deep learning weights and PyTorch model architectures:
* **MobileNetV2**: ImageNet-1K pretrained weights (cached automatically in PyTorch torch-cache).
* **SSDLite MobileNetV3**: Object detection weights (80 COCO classes).
* **Audio Spectrogram Transformer (AST)**: MIT AudioSet weights via HuggingFace transformers.
* **Whisper-tiny**: Speech-to-text recognition weights.
* **Multimodal Fusion**: Cross-attention concatenation network initialized with PyTorch.

*Note: On first startup, if weights are not yet cached, PyTorch will download model checkpoints from official repositories (`download.pytorch.org` and `huggingface.co`). An active internet connection is required only during the first initialization.*

---

## 7. Database Setup & Integrity

* **Database Engine**: SQLite 3.
* **Database File Path**: `d:\MY PROJECT\neurovision\backend\database\neurovision.db`.
* **Tables**:
  * `analysis_records`: Stores individual analysis results, prediction labels, confidence metrics, processing latency, and execution timestamps.
  * `system_logs`: Records system lifecycle events and operational telemetry.
* **Data Preservation Guarantee**: The database persists all historical records across restarts without deletion or truncation.

---

## 8. Executing the Test Suites

To verify platform stability before demonstration, run the backend automated test suite:

```powershell
cd "d:\MY PROJECT\neurovision\backend"
& ".\venv\Scripts\python.exe" -m pytest -o pythonpath=. -v
```
**Expected Result**: All 101 tests pass (100% pass rate) across vision, video, audio, fusion, XAI, database, WebSockets, and negative error scenarios.

---

## 9. Troubleshooting Common Issues

### Issue 1: Port 8000 or 5173 Already in Use
* **Cause**: A previous server instance is still running in the background.
* **Fix**:
  ```cmd
  netstat -ano | findstr :8000
  taskkill /PID <PID_NUMBER> /F
  ```
  *(Repeat for port 5173 if needed).*

### Issue 2: Microphone Permission Denied in Real-Time Audio
* **Cause**: Browser security policy prevents microphone access on untrusted domains.
* **Fix**: Ensure you access the frontend via `http://localhost:5173` (localhost is treated as secure context). Click the microphone icon in your browser address bar and choose *"Always allow"*.

### Issue 3: PowerShell Script Execution Restricted
* **Cause**: Windows PowerShell security policy restricts script execution by default.
* **Fix**: Run in PowerShell:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```

---

## 10. Clean Shutdown Procedure

1. **Frontend**: In the frontend terminal, press `Ctrl + C`, then type `y` and press `Enter`.
2. **Backend**: In the backend terminal, press `Ctrl + C`. Uvicorn will cleanly terminate running worker threads and release the database connection.
