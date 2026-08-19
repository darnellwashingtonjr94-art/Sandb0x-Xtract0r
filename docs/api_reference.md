# S@ndb0x-Xtract0r API Reference

## Base URL
`http://localhost:8000/api/v1`

---

### 1. Submit Sample
**Endpoint:** `/submit`  
**Method:** `POST`  
**Content-Type:** `multipart/form-data`

**Parameters:**
* `file` (Required): The binary or application payload to detonate.
* `platform` (Optional): The target execution environment (`windows`, `linux`, `android`, `ios`, `container`, `auto`). Defaults to `auto`.

**Success Response (200 OK):**
```json
{
  "task_id": "task_a1b2c3d4",
  "filename": "malware.exe",
  "platform": "windows",
  "status": "queued"
}
