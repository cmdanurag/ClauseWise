// src/components/document/DocumentUpload.jsx
import React, { useState } from "react";
import { uploadDocument } from "@/services/api";
import { Button } from "@/components/ui/button"; // from shadcn/ui
import { Loader2 } from "lucide-react"; // nice loading icon

function DocumentUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a file.");
      return;
    }

    try {
      setLoading(true);
      const data = await uploadDocument(file); // ⬅️ moved to services layer
      onUploadSuccess(data);
    } catch (err) {
      setError("Upload failed. Try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="flex flex-col items-center gap-4 p-6 border-2 border-dashed rounded-2xl w-full max-w-md mx-auto"
    >
      <input
        type="file"
        accept=".pdf,.docx"
        onChange={handleFileChange}
        className="text-sm"
      />

      {error && <p className="text-red-500 text-sm">{error}</p>}

      <Button
        type="submit"
        disabled={loading}
        className="w-full flex items-center justify-center gap-2"
      >
        {loading && <Loader2 className="h-4 w-4 animate-spin" />}
        {loading ? "Analyzing..." : "Upload & Analyze"}
      </Button>
    </form>
  );
}

export default DocumentUpload;
