// frontend/src/App.jsx
import React, { useState } from "react";
import DocumentUpload from "./components/DocumentUpload";
import AnalysisResult from "./components/AnalysisResult";

function App() {
  const [analysisData, setAnalysisData] = useState(null);

  return (
    <div>
      <header>
        <h1>ClauseWise</h1>
        <p>AI-powered legal document analysis</p>
      </header>

      <main>
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
