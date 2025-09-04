// frontend/src/App.jsx
import React, { useState } from "react";
import DocumentUpload from "./components/DocumentUpload";
import AnalysisResult from "./components/AnalysisResult";

function App() {
  const [analysisData, setAnalysisData] = useState(null);

  return (
    <div className="min-h-screen bg-gray-50 flex flex-col items-center p-6">
      <header className="text-center mb-6">
        <h1 className="text-3xl font-bold text-gray-800">ClauseWise</h1>
        <p className="text-gray-500">AI-powered legal document analysis</p>
      </header>

      <main className="w-full">
        {analysisData ? (
          <AnalysisResult analysisData={analysisData} onBack={() => setAnalysisData(null)} />
        ) : (
          <DocumentUpload onUploadSuccess={setAnalysisData} />
        )}
      </main>
    </div>
  );
}

export default App;

