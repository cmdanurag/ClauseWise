// frontend/src/components/DocumentUpload.jsx
import React, { useState } from "react";
import { analyzeDocument } from "../services/api";

function DocumentUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    try {
      setLoading(true);
      const data = await analyzeDocument(file);
      onUploadSuccess(data);
    } catch (err) {
      alert(err.message || "Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept=".pdf,.docx" onChange={handleFileChange} />
      <button type="submit" disabled={loading}>
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </button>
    </form>
  );
}

export default DocumentUpload;

