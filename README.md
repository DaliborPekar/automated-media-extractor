# automated-media-extractor

A lightweight, self-bootstrapping Command Line Interface (CLI) utility designed to automate the end-to-end extraction and assembly of media streams. This tool features a zero-configuration pipeline that handles dynamic dependency resolution, optimized multi-threaded downloading, and local asset storage.

It is structured specifically to provide a seamless, robust execution environment for non-technical users while retaining enterprise-grade performance.

---

## Key Architecture & Features

* **Self-Bootstrapping Runtime:** The orchestration script automatically detects, downloads, and silently provisions the necessary Python environment and runtime binaries if they are missing from the host system.
* **Concurrent Stream Extraction:** Pre-configured to utilize up to 10 parallel download fragments, maximizing network bandwidth utilizing advanced backend parameters.
* **Asynchronous Progress Tracking:** Features a streamlined, single-line terminal interface that suppresses standard verbose engine clutter in favor of real-time speed and telemetry data.
* **Isolated Local Storage:** Dynamically tracks the script's execution path to automatically construct and target an isolated `/downloads` subdirectory, ensuring portable storage integrity.

---

## Deployment & Usage

### Setup
1. Download the repository source files and place them inside a unified directory on the host machine.
2. Ensure both `Download Video.bat` and `downloader_engine.py` remain adjacent to each other.

### Execution
1. Double-click **`Download Video.bat`**.
2. On initial launch, allow the script a few moments to verify environment variables and fetch dependency updates.
3. Paste the target media URL into the interface prompt (`>>>`) and press **Enter**.
4. The processed, multiplexed `.mp4` file will be compiled directly into the local `downloads/` folder.

---

## Core Dependencies & Acknowledgments

This automation wrapper orchestrates and extends the functionality of the following open-source upstream libraries:

* **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — Used as the primary core media extraction engine.
* **[FFmpeg](https://ffmpeg.org/)** — Utilized as the muxing backend to stitch isolated high-definition video and audio streams seamlessly.
