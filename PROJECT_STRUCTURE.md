# NeuroVision Detailed Directory & Architecture Guide

This document provides a comprehensive overview of every important folder and directory in the **NeuroVision** project structure.

---

## Directory Overview

```text
neurovision/
├── frontend/             # Client-side user interface
├── backend/              # Server-side API & WebSockets
├── ai_models/            # Machine learning & deep learning models
├── datasets/             # Data samples for training & evaluation
├── uploads/              # Input files uploaded by users
├── outputs/              # System-generated outputs & visualizations
├── database/             # Persistent SQLite database storage
└── docs/                 # Documentation & reference materials
```

---

## Detailed Directory Descriptions

### 1. `frontend/`
Contains the complete React single-page application built with Vite and Tailwind CSS.
- **`src/components/`**: Modular, reusable UI components (`Header`, `StatusCard`, `ModuleCard`, `WebSocketTester`).
- **`src/pages/`**: Main application page layouts (`Dashboard.jsx`).
- **`src/layouts/`**: High-level page layout templates.
- **`src/services/`**: Centralized API service functions (`api.js`) for REST backend communication.
- **`src/hooks/`**: Custom React hooks (`useHealthCheck.js`, `useWebSocket.js`) managing state and side-effects.
- **`src/utils/`**: Helper utilities and configuration constants (`constants.js`).
- **`src/assets/`**: Static images, brand logos, and custom icons.
- **`public/`**: Static public files served directly by Vite (e.g. `favicon.svg`).

---

### 2. `backend/`
Contains the Python FastAPI web application supporting REST endpoints and WebSocket protocols.
- **`app/api/`**: API route definitions segregated by module:
  - `health`: System health status endpoint (`/api/health`)
  - `vision`: Placeholder endpoints for image pattern analysis
  - `video`: Placeholder endpoints for video sequence analysis
  - `audio`: Placeholder endpoints for audio spectrogram analysis
  - `multimodal`: Placeholder endpoints for cross-modal fusion
  - `analytics`: Placeholder endpoints for analytical query history
- **`app/core/`**: Configuration management (`config.py`) parsing environment variables and CORS settings.
- **`app/database/`**: Database engine setup (`connection.py`) and table initialization logic (`init_db.py`).
- **`app/models/`**: SQLAlchemy ORM entity definitions (`system_log.py`).
- **`app/schemas/`**: Pydantic request and response schemas (`health.py`).
- **`app/services/`**: Business logic layer separating API routes from core data processing.
- **`app/websocket/`**: Asynchronous WebSocket connection manager (`manager.py`) and websocket endpoint (`endpoint.py`).
- **`app/main.py`**: FastAPI application entry point configuring middleware, routers, and CORS.

---

### 3. `ai_models/`
Dedicated storage for trained deep learning weight files (`.pth`, `.onnx`, `.h5`) and model architecture definitions.
- **`vision/`**: Convolutional Neural Network (CNN) checkpoints for image feature extraction.
- **`video/`**: 3D-CNN / LSTM checkpoints for temporal video frame analysis.
- **`audio/`**: Audio classification checkpoints trained on mel-spectrogram representations.
- **`multimodal/`**: Fusion layer models synthesizing cross-modal embeddings.
- **`explainable_ai/`**: Grad-CAM, SHAP, and LIME attribution helper modules.

---

### 4. `datasets/`
Contains sample datasets, reference benchmarks, and test evaluation samples.
- **`vision/`**: Benchmark images for vision model testing.
- **`audio/`**: Benchmark audio clips for acoustic model testing.
- **`video/`**: Benchmark video clips for frame-sequence testing.

---

### 5. `uploads/`
Temporary and persistent storage for files uploaded by end users through the frontend interface.
- **`images/`**: Uploaded image files awaiting analysis.
- **`videos/`**: Uploaded video files awaiting frame decomposition.
- **`audio/`**: Uploaded WAV/MP3 files awaiting spectrogram conversion.

---

### 6. `outputs/`
Storage for system-generated visual outputs, predictions, and XAI heatmaps.
- **`predictions/`**: Exported JSON prediction reports and confidence metrics.
- **`heatmaps/`**: Grad-CAM visual heatmaps overlaying input images/frames.
- **`spectrograms/`**: Generated mel-spectrogram visual representations of audio files.
- **`processed_videos/`**: Video output files with real-time bounding box/heatmap overlays.

---

### 7. `database/`
Storage location for the SQLite development database file (`neurovision.db`), storing historical analysis logs, model metadata, and execution time metrics.

---

### 8. `docs/`
Houses technical design documents, architectural diagrams, MCA project reports, and API references.
