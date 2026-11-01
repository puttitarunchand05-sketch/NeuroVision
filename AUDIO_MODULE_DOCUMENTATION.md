# NeuroVision — Audio Analysis Module Documentation

## 1. Overview
The **Audio Analysis Module** (Module 03) delivers deep learning acoustic pattern recognition, speech-to-text linguistic transcription, and psychoacoustic spectral feature extraction within the NeuroVision intelligent multimodal analysis ecosystem.

### Key Capabilities
- **Sound Event Classification**: Powered by the **Audio Spectrogram Transformer (AST)** (`MIT/ast-finetuned-audioset-10-10-0.4593`), recognizing 527 AudioSet sound classes (speech, music, instruments, vehicles, animals, machinery, environmental ambient sounds).
- **Speech Recognition (ASR)**: Local, offline speech-to-text powered by **OpenAI Whisper** (`openai/whisper-tiny`), automatically transcribing spoken dialogue and detecting languages.
- **Acoustic Visualizations**: High-resolution dark-themed spectrogram plots (Waveform, STFT linear spectrogram, Mel-frequency psychoacoustic spectrogram, and 13-band MFCC heatmap).
- **Segment Timeline Analysis**: Granular temporal division of longer audio into uniform segments (2.0s - 6.0s) with interval timestamps and individual sound class predictions.
- **Evidence-Based Acoustic Insights**: Synthesizes spectral centroid, dynamic range (RMS dB), zero-crossing rate (noisiness vs harmonicity), and multi-segment variations into plain language.
- **Multi-Format Export**: One-click download of structured JSON and tabular CSV reports.

---

## 2. Supported Audio Formats & Constraints
- **Supported Formats**: `WAV`, `MP3`, `FLAC`, `OGG`, `M4A`
- **Magic Bytes Validation**: Validates binary headers (`RIFF/WAVE`, `fLaC`, `OggS`, `ID3/MPEG`, `ftypM4A`) preventing file extension spoofing.
- **Maximum File Size**: 50 MB
- **Duration Limits**: Minimum 0.1s (100ms) to Maximum 600.0s (10 minutes)
- **Sample Rate Processing**: All audio streams are safely decoded, resampled to 16,000 Hz, converted to mono, and normalized.

---

## 3. Required Python Packages & Windows Setup

### Required Dependencies
```text
soundfile>=0.12.0
librosa>=0.10.0
torchaudio>=2.2.0
transformers>=4.38.0
scipy>=1.12.0
matplotlib>=3.8.0
torch>=2.2.0
fastapi>=0.110.0
```

### Installation on Windows (PowerShell)
```powershell
cd "d:\MY PROJECT\neurovision\backend"

# Activate Python Virtual Environment
.\venv\Scripts\Activate.ps1

# Install audio analysis dependencies
pip install soundfile librosa torchaudio transformers scipy matplotlib
```

---

## 4. How to Run the Application

### Start the Backend (FastAPI + Uvicorn)
```powershell
cd "d:\MY PROJECT\neurovision\backend"
.\venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
- API Base URL: `http://localhost:8000`
- Interactive Swagger Docs: `http://localhost:8000/docs`

### Start the Frontend (Vite + React)
```powershell
cd "d:\MY PROJECT\neurovision\frontend"
npm run dev
```
- Frontend UI: `http://localhost:5173`

---

## 5. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/audio` | Audio module capabilities, limits, and supported formats |
| `GET` | `/api/audio/status` | Readiness and device status of AST and Whisper models |
| `POST` | `/api/audio/analyze` | Upload audio file, run preprocessing, AST classification, feature extraction, and Whisper transcription |
| `POST` | `/api/audio/transcribe` | Upload audio file for standalone speech recognition |
| `GET` | `/api/audio/result/{job_id}` | Retrieve cached results of a completed audio analysis job |
| `GET` | `/api/audio/report/{job_id}?format=json\|csv` | Download structured analysis report in JSON or CSV format |

### Example Response (`POST /api/audio/analyze`)
```json
{
  "job_id": "aaa174456c8b",
  "success": true,
  "filename": "sample.wav",
  "duration_seconds": 3.0,
  "classification": {
    "model": "Audio Spectrogram Transformer (AST)",
    "model_id": "MIT/ast-finetuned-audioset-10-10-0.4593",
    "dataset": "AudioSet (527 Sound Classes)",
    "predictions": [
      { "label": "Sine wave", "confidence": 0.818, "confidence_percentage": 81.8 },
      { "label": "Dial tone", "confidence": 0.042, "confidence_percentage": 4.2 },
      { "label": "Busy signal", "confidence": 0.014, "confidence_percentage": 1.4 }
    ]
  },
  "features": {
    "sample_rate": 16000,
    "waveform_points": [0.12, 0.45, 0.89, ...],
    "rms_energy": { "mean": 0.035, "max": 0.089, "dynamic_range_db": 28.4 },
    "spectral_centroid": { "mean_hz": 446.6, "max_hz": 450.1 },
    "plots": {
      "waveform": "data:image/png;base64,...",
      "stft_spectrogram": "data:image/png;base64,...",
      "mel_spectrogram": "data:image/png;base64,...",
      "mfcc": "data:image/png;base64,..."
    }
  },
  "segments": [
    {
      "segment_index": 0,
      "start_time": 0.0,
      "end_time": 3.0,
      "duration": 3.0,
      "predictions": [...]
    }
  ],
  "transcription": {
    "available": true,
    "text": "Hello world",
    "language": "en",
    "message": "Speech transcribed successfully using local Whisper model."
  },
  "insights": [
    {
      "category": "Dominant Sound Event",
      "type": "classification",
      "title": "Dominant Pattern: Sine wave (81.8% Confidence)",
      "description": "The neural model identified 'Sine wave' as the primary acoustic event..."
    }
  ],
  "message": "Audio analysis completed successfully"
}
```

---

## 6. Privacy & Security Safeguards
1. **Local Offline Inference**: Pretrained models (AST and Whisper) run entirely locally on CPU/GPU. No audio files or speech transcripts are ever transmitted to third-party cloud APIs.
2. **Secure Temporary Storage**: Audio uploads are processed in memory or ephemeral temporary files with automatic deletion in `finally:` blocks.
3. **Magic Byte Verification**: Blocks disguised executable or malicious binary payloads.
4. **No Medical / Emotional Speculation**: Audio insights explicitly state measured acoustic values (Hz, dB, rates) and neural class scores, avoiding unsupported medical or psychological claims.

---

## 7. Known Model Limitations & Common Fixes
- **Audio Overlapping**: AST classifies acoustic events from AudioSet; when multiple loud sounds occur simultaneously (e.g. speech over loud engine noise), confidence scores may be shared between classes. The system automatically flags "Classification Uncertainty" in the Insights panel when top predictions are within 10% of each other.
- **Accents & Background Noise in Speech**: Whisper-tiny is lightweight (150MB) and optimized for CPU execution. In heavily distorted audio, minor transcription inaccuracies may occur.
- **Memory Management**: The backend limits in-memory cached analysis results to 50 jobs with LRU eviction to prevent memory growth.
