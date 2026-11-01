# NeuroVision — Deep Learning Engine Architecture & Reference Manual

**MCA Major Project: Intelligent Multimodal Pattern Analysis Using Deep Learning**  
**Module: Central AI Engine (Step 9)**

---

## 1. Executive Overview

The **NeuroVision Deep Learning Engine** (`backend/app/ai_engine/`) serves as the central, unified, and modular inference layer for the entire NeuroVision system. It brings together unimodal image classification, real-time object detection, Grad-CAM visual explanations, frame-sampled video tracking, Audio Spectrogram Transformer (AST) acoustic event recognition, Whisper speech recognition, and cross-modal temporal orchestration into a standardized, production-grade AI platform.

---

## 2. Architectural Design

```text
backend/app/ai_engine/
├── __init__.py               # Package entrypoint exporting central singletons & types
├── engine_manager.py         # DeepLearningEngine facade (predict, analyze_multimodal, jobs)
├── model_registry.py         # Catalog of model architectures, input/output contracts, limitations
├── model_loader.py           # Thread-safe lazy loading, model lifecycle & resource cleanup
├── device_manager.py         # Hardware telemetry (CPU cores / CUDA GPU VRAM), safe fallback
├── preprocessing.py          # Unified input validation (image, audio, video) and normalization
├── inference_service.py      # Vision, Audio, and Multimodal cross-modal inference pipelines
├── confidence_utils.py       # Score documentation, probability rankings & ambiguity margins
├── result_formatter.py       # Standardized JSON serialization envelope adhering to Section 11
└── exceptions.py             # Domain-specific typed error hierarchy
```

---

## 3. Registered Models & Capability Matrix

| Model Identifier | Display Name | Modality | Backbone Architecture | Output Classes | Device Requirement | Status |
|---|---|---|---|---|---|---|
| `mobilenet_v2` | MobileNetV2 (ImageNet-1K) | `image_classification` | Inverted Residual CNN | 1,000 ImageNet Classes | CPU / CUDA (512MB RAM) | Ready |
| `ssdlite_mobilenet_v3` | SSDLite MobileNetV3 Large | `object_detection` | SSDLite + MobileNetV3 | 91 MS-COCO Categories | CPU / CUDA (512MB RAM) | Ready |
| `gradcam_mobilenet_v2` | Grad-CAM Explainable AI | `explainable_vision` | Autograd hook on `features.18` | Visual Heatmap Overlay | CPU / CUDA (512MB RAM) | Ready |
| `video_pipeline` | Video Tracking & Motion | `video_analysis` | SSDLite + Centroid Tracker | Tracked trajectories & motion index | CPU / CUDA (1GB RAM) | Ready |
| `ast_audioset` | Audio Spectrogram Transformer | `audio_classification` | Vision Transformer (16x16 audio patches) | 527 AudioSet Classes | CPU / CUDA (1GB RAM) | Ready |
| `whisper_asr` | Whisper Speech-to-Text | `speech_transcription` | Encoder-Decoder Transformer | Natural language text + language code | CPU / CUDA (1GB RAM) | Ready |
| `multimodal_orchestrator`| Cross-Modal Temporal Engine | `multimodal_fusion` | Temporal Event Alignment & Co-occurrence | Aligned cross-modal timeline | CPU / CUDA (1.5GB RAM) | Ready |

---

## 4. Hardware & Device Management

The engine is engineered to run seamlessly on standard Windows development computers:
- **CPU Inference**: Default execution target. Automatically discovers active CPU thread pool, architecture, and system properties without requiring a discrete graphics card.
- **CUDA GPU Acceleration**: When PyTorch detects an active CUDA-capable device (`torch.cuda.is_available()`), models are dispatched to GPU memory. Telemetry reports authentic VRAM allocation, reservation, and device specifications.
- **Graceful Fallback**: If a request specifies a CUDA device that is unavailable or runs out of memory, the engine safely falls back to CPU execution without crashing unrelated services.
- **Resource Cleanup**: Thread-safe invocation of `device_manager.empty_cache()` frees cached memory following intensive tasks.

---

## 5. Standardized Normalized Result Schema

Adheres strictly to the specification contract:

```json
{
  "success": true,
  "request_id": "nv_f4a9b1c208de",
  "modality": "image",
  "model": {
    "id": "mobilenet_v2",
    "name": "MobileNetV2 (ImageNet-1K)",
    "version": "v2",
    "device": "cpu"
  },
  "processing": {
    "duration_ms": 125.4,
    "status": "completed"
  },
  "predictions": [
    {
      "rank": 1,
      "class_id": 611,
      "label": "Jigsaw Puzzle",
      "raw_label": "jigsaw_puzzle",
      "score": 0.8421,
      "percentage": 84.21,
      "score_metadata": {
        "raw_score": 0.8421,
        "normalized_score": 0.8421,
        "score_type": "softmax_normalized_score",
        "is_calibrated": false,
        "interpretation_note": "Model score represents relative ranking confidence across evaluated classes."
      }
    }
  ],
  "detections": [],
  "explanations": [],
  "metadata": {
    "image_dimensions": { "width": 224, "height": 224 },
    "confidence_margin": {
      "top1_score": 0.8421,
      "top2_score": 0.0512,
      "margin": 0.7909,
      "ambiguity_level": "distinct_prediction"
    }
  },
  "warnings": []
}
```

---

## 6. Multimodal Orchestration Capabilities & Limitations

### Implemented Fusion Strategy:
1. **Temporal Event Alignment**: Synchronizes timestamps between sampled visual frames (detected objects, movements, and scenes) and segmented audio intervals (detected acoustic categories, background noises, and spoken speech).
2. **Co-Occurrence Correlation**: Flags when visual subjects (e.g. `Dog`, `Car`, `Person`) co-occur with matching acoustic events (e.g. `Bark`, `Engine`, `Speech`).
3. **Graceful Partial Fallback**: If a video contains no audio track or an audio recording is silent, the engine returns full visual results accompanied by structured warning signals, ensuring resilience.
4. **Honest Architectural Disclosure**: The current system employs **late decision-level temporal alignment** rather than an end-to-end trained joint cross-attention transformer. Scores are preserved without inventing fabricated cross-modal weights.

---

## 7. REST API Endpoints

All engine endpoints are registered under `/api/ai`:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/ai/status` | Returns overall engine status, compute devices, and registered model readiness |
| `GET` | `/api/ai/models` | Lists registered models with input/output requirements and limitations |
| `GET` | `/api/ai/models/{model_id}` | Details for a specific model |
| `POST` | `/api/ai/predict` | Unified inference endpoint accepting multipart file or base64 payload |
| `POST` | `/api/ai/analyze-multimodal`| Cross-modal analysis aligning visual media with acoustic recordings |
| `GET` | `/api/ai/jobs/{job_id}` | Polls progress and result of an asynchronous background job |

---

## 8. Exact Windows Commands to Run

### Run Backend Server:
```powershell
cd "d:\MY PROJECT\neurovision\backend"
& "venv\Scripts\Activate.ps1"
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### Run Frontend Development Server:
```powershell
cd "d:\MY PROJECT\neurovision\frontend"
npm run dev
```

### Run Pytest Test Suite:
```powershell
cd "d:\MY PROJECT\neurovision\backend"
& "venv\Scripts\python.exe" -m pytest tests/ -v
```

### Run Step 9 Verification Script:
```powershell
cd "d:\MY PROJECT\neurovision\backend"
& "venv\Scripts\python.exe" verify_step9.py
```
