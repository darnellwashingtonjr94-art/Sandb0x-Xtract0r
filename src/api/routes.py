import os
import uuid
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from orchestrator.router import FileRouter
from orchestrator.scheduler import TaskScheduler

router = APIRouter()
scheduler = TaskScheduler()
file_router = FileRouter()

@router.post("/submit")
async def submit_sample(
    file: UploadFile = File(...),
    platform: str = Form("auto")
):
    task_id = f"task_{uuid.uuid4().hex[:8]}"
    upload_dir = "storage/samples"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, f"{task_id}_{file.filename}")
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    detected_platform = file_router.detect_platform(file_path) if platform == "auto" else platform
    scheduler.enqueue(file_path, detected_platform)

    return {
        "task_id": task_id,
        "filename": file.filename,
        "platform": detected_platform,
        "status": "queued"
    }

@router.get("/reports/{task_id}")
def get_report(task_id: str, format: str = "md"):
    ext = "pdf" if format == "pdf" else "md"
    report_path = f"storage/reports/{task_id}_threat_report.{ext}"
    
    if not os.path.exists(report_path):
        raise HTTPException(status_code=404, detail="Report not found or analysis pending.")
    
    return FileResponse(report_path, filename=f"{task_id}_report.{ext}")
