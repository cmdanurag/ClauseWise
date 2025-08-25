// frontend/src/services/api.js

const API_BASE = "/api/v1"; // Vite proxy will forward this

// Get supported formats
export async function getSupportedFormats() {
  const res = await fetch(`${API_BASE}/documents/supported-formats`);
  if (!res.ok) throw new Error("Failed to fetch supported formats");
  return res.json();
}

// Upload & analyze a document
export async function analyzeDocument(file) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await fetch(`${API_BASE}/documents/analyze`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) throw new Error("Failed to analyze document");
  return res.json();
}

