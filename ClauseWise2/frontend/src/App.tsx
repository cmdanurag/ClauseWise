import React, { useState } from "react";
import axios from "axios";
import DocumentUploader from './components/DocumentUploader';


const App: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [analysis, setAnalysis] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileUpload = (uploadedFile: File) => {
    setFile(uploadedFile);
    setAnalysis("");
    setError(null);
  };

  const handleAnalyze = async () => {
    if (!file) return;

    setLoading(true);
    setAnalysis("");
    setError(null);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const response = await axios.post(
        "http://127.0.0.1:8000/api/v1/documents/upload",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      // Assuming backend returns { data: { text: "..." } }
      setAnalysis(response.data.data.text);
    } catch (err: any) {
      setError(err.response?.data?.detail || "Failed to analyze document.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6 flex flex-col items-center">
      <h1 className="text-3xl font-bold mb-6">ClauseWise - Legal Document Analyzer</h1>

      <DocumentUploader onFileUpload={handleFileUpload} />

      {file && (
        <button
          onClick={handleAnalyze}
          className="mt-4 px-6 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 transition-colors"
        >
          {loading ? "Analyzing..." : "Analyze Document"}
        </button>
      )}

      {error && <p className="mt-4 text-red-600">{error}</p>}

      {analysis && (
        <div className="mt-6 w-full max-w-3xl bg-white p-4 rounded shadow overflow-auto">
          <h2 className="text-xl font-semibold mb-2">Analysis Result:</h2>
          <pre className="whitespace-pre-wrap">{analysis}</pre>
        </div>
      )}
    </div>
  );
};

export default App;
