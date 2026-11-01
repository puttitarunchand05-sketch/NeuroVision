# NeuroVision: REST API & WebSocket Protocol Documentation

**NeuroVision: Intelligent Multimodal Pattern Analysis Using Deep Learning**  
*Master of Computer Applications (MCA) Major Project*

---

## 1. API Overview

NeuroVision provides a high-performance RESTful API paired with a real-time WebSocket telemetry channel powered by **FastAPI (ASGI)**. The API orchestrates deep learning inference pipelines across vision, audio, video, and multimodal modalities, with persistence in SQLite via SQLAlchemy.

* **Interactive API Documentation (Swagger UI)**: `http://localhost:8000/docs`
* **Alternative Interactive Documentation (ReDoc)**: `http://localhost:8000/redoc`
* **OpenAPI JSON Schema**: `http://localhost:8000/openapi.json`
* **Real-time WebSocket Bus**: `ws://localhost:8000/ws`

---

## 2. Base Configuration & Environments

* **Development Base URL**: `http://127.0.0.1:8000` or `http://localhost:8000`
* **Default API Prefix**: `/api`
* **Cross-Origin Resource Sharing (CORS)**: Configured in `app/core/config.py` for origins `http://localhost:5173` and `http://127.0.0.1:5173`.

---

## 3. REST API Endpoint Reference

### 3.1. System & Health Endpoints

#### `GET /api/health`
* **Description**: Returns overall system operational status, database connectivity, and backend heartbeat.
* **Query Parameters**: None.
* **Response Status Codes**: `200 OK`, `503 Service Unavailable`.
* **Example Response**:
```json
{
  "status": "online",
  "project": "NeuroVision AI Platform",
  "version": "1.0.0",
  "database": "connected",
  "active_models": 4
}
```

---

### 3.2. Vision Analysis Endpoints

#### `GET /api/vision/status`
* **Description**: Reports availability of MobileNetV2 and SSDLite detector, hardware acceleration device (CPU/CUDA), and class catalogs.
* **Response**: `200 OK`
```json
{
  "success": true,
  "module": "Vision Engine",
  "status": "ready",
  "device": "cpu",
  "classifier": "MobileNetV2 (1000 classes)",
  "detector": "SSDLite MobileNetV3 (80 classes)"
}
```

#### `POST /api/vision/analyze`
* **Description**: Uploads an image, performs classification, object detection localization, and optional Grad-CAM explainability backpropagation.
* **Content-Type**: `multipart/form-data`
* **Form Fields**:
  - `file`: Binary image file (`.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`). Max size: 15 MB.
  - `threshold` (float, optional, default: 0.35): Detection confidence threshold `[0.1 - 0.9]`.
  - `enable_explainability` (bool, optional, default: true): Generate Grad-CAM heatmaps.
* **Response**: `200 OK`
```json
{
  "success": true,
  "filename": "workspace.jpg",
  "classification": {
    "label": "laptop",
    "confidence": 0.9324,
    "top_5": [
      {"label": "laptop", "confidence": 0.9324},
      {"label": "notebook", "confidence": 0.0412},
      {"label": "desktop computer", "confidence": 0.0150}
    ]
  },
  "detections": [
    {
      "label": "laptop",
      "confidence": 0.895,
      "bbox": [0.24, 0.35, 0.72, 0.81]
    }
  ],
  "explainability": {
    "gradcam_available": true,
    "heatmap_overlay": "data:image/jpeg;base64,..."
  },
  "latency_ms": 142.5
}
```

#### `POST /api/vision/detect-frame`
* **Description**: Real-time camera frame detection receiving raw image bytes.
* **Response**: `200 OK` containing detection boxes and inference time.

---

### 3.3. Video Analysis Endpoints

#### `POST /api/video/upload`
* **Description**: Uploads a video file, initiates asynchronous frame extraction, centroid tracking, motion analysis, and annotated video synthesis.
* **Content-Type**: `multipart/form-data`
* **Form Fields**:
  - `file`: Video file (`.mp4`, `.webm`, `.mov`, `.avi`, `.mkv`). Max size: 100 MB.
  - `sample_fps` (float, optional, default: 2.0): Target sampling rate.
  - `threshold` (float, optional, default: 0.35): Detection threshold.
  - `create_annotated` (bool, optional, default: true): Generate annotated video.
* **Response**: `200 OK`
```json
{
  "success": true,
  "job_id": "vid_job_8b91a2fc",
  "status": "queued",
  "filename": "traffic_surveillance.mp4"
}
```

#### `GET /api/video/status/{job_id}`
* **Description**: Polls video analysis progress, current stage, frames processed, and completion percentage.
* **Response**: `200 OK` (`job_id` exists) or `404 Not Found`.
```json
{
  "job_id": "vid_job_8b91a2fc",
  "status": "processing",
  "progress_percent": 65.0,
  "frames_processed": 65,
  "total_frames": 100,
  "current_stage": "Extracting frames & executing SSDLite detection..."
}
```

#### `GET /api/video/results/{job_id}`
* **Description**: Retrieves full frame-by-frame analysis, tracking trajectories, and motion statistics once complete.
* **Response**: `200 OK` or `404 Not Found`.

#### `POST /api/video/cancel/{job_id}`
* **Description**: Signals running video worker thread to stop processing and release temporary file descriptors.

---

### 3.4. Audio Analysis Endpoints

#### `POST /api/audio/analyze`
* **Description**: Uploads an audio file for deep acoustic event classification via AST, Whisper transcription, and Librosa spectral feature extraction.
* **Content-Type**: `multipart/form-data`
* **Form Fields**:
  - `file`: Audio file (`.wav`, `.mp3`, `.flac`, `.ogg`, `.m4a`). Max size: 50 MB.
  - `transcribe` (bool, optional, default: true): Run Whisper speech-to-text.
  - `segment_duration` (float, optional, default: 3.0): Window segmentation length.
* **Response**: `200 OK`
```json
{
  "success": true,
  "filename": "acoustic_guitar.wav",
  "sound_class": "Acoustic Guitar",
  "confidence": 0.9412,
  "transcription": "A soft acoustic melody playing in standard tuning.",
  "features": {
    "sample_rate": 22050,
    "duration_sec": 8.4,
    "spectral_centroid_mean": 1824.5,
    "zero_crossing_rate_mean": 0.0482
  },
  "latency_ms": 285.4
}
```

#### `POST /api/audio/analyze-stream`
* **Description**: Real-time microphone audio chunk processing (accepts 16kHz raw PCM Float32 encoded as WAV blob).
* **Response**: `200 OK` containing top-5 predicted sound classes and live metrics.

---

### 3.5. Multimodal Fusion Endpoints

#### `POST /api/fusion/analyze`
* **Description**: Performs late multimodal fusion by extracting unified cross-modal representations from visual and acoustic inputs.
* **Content-Type**: `multipart/form-data`
* **Form Fields**:
  - `image` (optional): UploadFile.
  - `audio` (optional): UploadFile.
  - `video` (optional): UploadFile.
* *Note: At least one modality file must be provided.*
* **Response**: `200 OK`
```json
{
  "success": true,
  "modalities_present": ["vision", "audio"],
  "fusion_prediction": "Musical Performance",
  "fusion_confidence": 0.928,
  "modality_contributions": {
    "vision": 0.54,
    "audio": 0.46
  },
  "individual_predictions": {
    "vision": {"label": "Electric Guitar", "confidence": 0.912},
    "audio": {"label": "Guitar Strumming", "confidence": 0.935}
  },
  "latency_ms": 380.0
}
```

---

### 3.6. Analytics & History Endpoints

#### `GET /api/analytics/summary`
* **Description**: Returns aggregated metrics, total analyses conducted, modality breakdown, and average processing latency.
* **Response**: `200 OK`

#### `GET /api/analytics/history`
* **Description**: Returns paginated analysis records with optional search filter and date range filtering (`today`, `7d`, `30d`, `all`).
* **Query Parameters**:
  - `page` (int, default: 1)
  - `page_size` (int, default: 20)
  - `search` (string, optional)
  - `analysis_type` (string, optional: `vision`, `audio`, `video`, `multimodal`)
  - `date_range` (string, optional: `today`, `7d`, `30d`, `all`)
* **Response**: `200 OK`

#### `DELETE /api/analytics/history/{record_id}`
* **Description**: Deletes a single analysis record by database ID.
* **Response**: `200 OK` or `404 Not Found`.

---

### 3.7. Explainable AI (XAI) Endpoints

#### `POST /api/xai/image`
* **Description**: Generates class activation maps (Grad-CAM) targeting a specific class index for visual explanation.
* **Response**: `200 OK` containing heatmap matrix and base64 overlay.

#### `POST /api/xai/audio`
* **Description**: Generates Mel-spectrogram saliency map highlighting time-frequency regions responsible for acoustic classification.

---

## 4. File Upload Constraints & Validation

| Modality | Supported Extensions | Content-Type Whitelist | Max Size | Validation Method |
| :--- | :--- | :--- | :--- | :--- |
| **Image** | `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp` | `image/jpeg`, `image/png`, `image/webp`, `image/bmp` | **15 MB** | Magic bytes + PIL / OpenCV decode |
| **Audio** | `.wav`, `.mp3`, `.flac`, `.ogg`, `.m4a` | `audio/wav`, `audio/mpeg`, `audio/flac`, `audio/ogg` | **50 MB** | Magic bytes + Librosa / SoundFile verify |
| **Video** | `.mp4`, `.webm`, `.mov`, `.avi`, `.mkv` | `video/mp4`, `video/webm`, `video/quicktime` | **100 MB** | Container header + OpenCV `VideoCapture` |

*Files failing validation return HTTP 400 with a detailed error message explaining the failure.*

---

## 5. WebSocket Telemetry Protocol (`/ws`)

### 5.1. Connection Handshake
1. Client establishes connection to `ws://localhost:8000/ws`.
2. Server accepts connection and immediately transmits connection acknowledgement:
```json
{
  "event": "connection.established",
  "request_id": null,
  "timestamp": "2026-10-14T12:00:00.000Z",
  "data": {
    "client_id": "ws_client_10a9",
    "heartbeat_interval_seconds": 15,
    "max_frame_size_bytes": 65536
  }
}
```

### 5.2. Ping / Pong Heartbeat
Clients send periodic heartbeats to calculate network latency:
* **Client Request**:
```json
{
  "event": "ping",
  "timestamp": "2026-10-14T12:00:05.100Z"
}
```
* **Server Response**:
```json
{
  "event": "pong",
  "request_id": null,
  "timestamp": "2026-10-14T12:00:05.102Z",
  "data": {
    "client_timestamp": "2026-10-14T12:00:05.100Z",
    "server_timestamp": "2026-10-14T12:00:05.102Z"
  }
}
```

### 5.3. Channel Subscriptions
Clients can selectively subscribe to specific telemetry topics:
```json
{
  "event": "subscribe",
  "data": {
    "topic": "video"
  }
}
```

### 5.4. Thread-Safe Worker Broadcasts
Background analysis threads dispatch updates to connected clients using the thread-safe broadcast bus:
```json
{
  "event": "video.analysis.progress",
  "request_id": "vid_job_8b91a2fc",
  "timestamp": "2026-10-14T12:00:08.500Z",
  "data": {
    "job_id": "vid_job_8b91a2fc",
    "progress_percent": 75.0,
    "current_stage": "Synthesizing annotated tracking video..."
  }
}
```

---

## 6. Error Handling Structure

All REST errors return standard JSON responses:
```json
{
  "detail": "Descriptive human-readable error explanation."
}
```

For WebSocket violations (e.g. malformed JSON or frame exceeding 64KB), a structured error event is returned:
```json
{
  "event": "system.error",
  "request_id": null,
  "timestamp": "2026-10-14T12:00:10.000Z",
  "data": {
    "error_type": "FRAME_TOO_LARGE",
    "message": "Message exceeds maximum size of 65536 bytes (64KB)"
  }
}
```

---

## 7. Synthetic Media Detection Endpoints (Step 20)

### 7.1. Module Overview & Models

#### `GET /api/synthetic-media`
Returns module capabilities, supported media types (JPG, PNG, WEBP, MP4, MOV, WEBM), and size bounds.

#### `GET /api/synthetic-media/models`
Returns forensic model specifications (EfficientNet-B0 backbone, custom weights status, device, parameters count, and explainability layer).

### 7.2. Image & Deepfake Analysis

#### `POST /api/synthetic-media/analyze-image`
* **Content-Type**: `multipart/form-data`
* **Form Parameters**:
  - `file`: Image file (JPG, JPEG, PNG, WEBP) <= 15MB
  - `enable_xai`: `true` (generates Grad-CAM visual heatmap)
  - `colormap`: `"JET"`, `"TURBO"`, or `"VIRIDIS"`
* **Response**:
```json
{
  "success": true,
  "result_category": "Likely AI-generated",
  "category_color": "red",
  "calibrated_probability": 0.8014,
  "confidence_percentage": 80.1,
  "raw_model_score": 0.9412,
  "processing_time_ms": 136.4,
  "breakdown": {
    "deep_cnn_score": 0.9412,
    "spectral_frequency_score": 0.78,
    "noise_residual_score": 0.65,
    "facial_manipulation_score": 0.05,
    "metadata_provenance_score": 0.50
  },
  "spectral_analysis": {
    "checkerboard_artifact_detected": true,
    "high_frequency_ratio": 0.28,
    "spectrum_image_uri": "data:image/png;base64,..."
  },
  "explainable_ai": {
    "method": "Grad-CAM",
    "overlay_image_uri": "data:image/jpeg;base64,...",
    "pure_heatmap_uri": "data:image/png;base64,...",
    "hotspot_regions": [...]
  }
}
```

### 7.3. Video Analysis & Async Jobs

#### `POST /api/synthetic-media/analyze-video`
* **Content-Type**: `multipart/form-data`
* **Form Parameters**:
  - `file`: Video file (MP4, MOV, WEBM) <= 100MB
  - `sample_fps`: Sampling interval (0.5 to 2.0 FPS, default: 1.0)
  - `sync`: `false` (default: background asynchronous processing)
* **Response**:
```json
{
  "success": true,
  "job_id": "3d9a18fa-4e78-45e8-...",
  "status": "queued",
  "polling_endpoint": "/api/synthetic-media/jobs/3d9a18fa-4e78-45e8-..."
}
```

#### `GET /api/synthetic-media/jobs/{job_id}`
Returns processing progress, current stage, and complete aggregated video findings once completed.

### 7.4. Detection History & Result Lookup

#### `GET /api/synthetic-media/history`
Query parameters: `page`, `page_size`, `category`, `search`. Returns historical analysis records saved in SQLite database.

#### `GET /api/synthetic-media/results/{analysis_id}`
Returns full detailed findings for a specific analysis record UUID.

