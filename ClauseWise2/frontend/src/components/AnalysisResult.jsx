import React from 'react';

function AnalysisResult({ analysisData, onBack }) {
  return (
    <div>
      <h2>Analysis Result</h2>
      <pre>{JSON.stringify(analysisData, null, 2)}</pre>
      <button onClick={onBack}>Back</button>
    </div>
  );
}

export default AnalysisResult;