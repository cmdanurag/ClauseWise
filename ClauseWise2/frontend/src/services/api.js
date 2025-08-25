// frontend/src/services/api.js

const API_BASE = "/api/v1"; // vite proxy forwards this to http://127.0.0.1:8000

// Get supported formats
export async function getSupportedFormats() {
  const res = await fetch(`${API_BASE}/documents/supported-formats`);
  if (!res.ok) throw new Error("Failed to fetch supported formats");
  return res.json();
}

// Upload a document
export async function uploadDocument(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_BASE}/documents/upload`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) throw new Error("Failed to upload document");
  return res.json();
}
