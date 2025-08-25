import React, { useState } from 'react';
import DocumentUpload from './components/DocumentUpload';
import AnalysisResult from './components/AnalysisResult';

function App() {
  const [analysisData, setAnalysisData] = useState(null);

  const handleUploadSuccess = (data) => {
    setAnalysisData(data);
  };

  const handleBack = () => {
    setAnalysisData(null);
  };

  return (
    <div>
      <header>
        <h1>ClauseWise</h1>
        <p>AI-powered legal document analysis</p>
      </header>

      <main>
        {analysisData ? (
          <AnalysisResult analysisData={analysisData} onBack={handleBack} />
        ) : (
          <DocumentUpload onUploadSuccess={handleUploadSuccess} />
        )}
      </main>
    </div>
  );
}

export default App;