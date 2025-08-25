import React, { useState } from 'react';

function DocumentUpload({ onUploadSuccess }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch('/api/documents/analyze', {
      method: 'POST',
      body: formData,
    });

    if (res.ok) {
      const data = await res.json();
      onUploadSuccess(data);
    } else {
      alert("Upload failed");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="file" accept=".pdf,.docx" onChange={handleFileChange} />
      <button type="submit">Upload & Analyze</button>
    </form>
  );
}

export default DocumentUpload;