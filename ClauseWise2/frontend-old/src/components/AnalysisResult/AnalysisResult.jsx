import React, { useState } from 'react';
import './AnalysisResult.css';

const AnalysisResult = ({ analysisData, onBack }) => {
  const [activeTab, setActiveTab] = useState('summary');
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [isAsking, setIsAsking] = useState(false);
  const [askError, setAskError] = useState('');

  const handleAskQuestion = async (event) => {
    event.preventDefault();
    
    if (!question.trim()) {
      setAskError('Please enter a question.');
      return;
    }
    
    setIsAsking(true);
    setAskError('');
    setAnswer('');
    
    try {
      const response = await fetch('/api/v1/documents/ask', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          question: question,
          document_context: analysisData.extracted_text,
        }),
      });
      
      if (!response.ok) {
        throw new Error(`Failed to get answer: ${response.statusText}`);
      }
      
      const result = await response.json();
      setAnswer(result.answer.answer);
    } catch (err) {
      setAskError(`Failed to get answer: ${err.message}`);
    } finally {
      setIsAsking(false);
    }
  };

  const handleExplainClause = async (clauseText) => {
    try {
      const response = await fetch('/api/v1/documents/explain-clause', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          clause_text: clauseText,
          context: analysisData.document_type,
        }),
      });
      
      if (!response.ok) {
        throw new Error(`Failed to explain clause: ${response.statusText}`);
      }
      
      const result = await response.json();
      // In a real implementation, you would display this explanation to the user
      alert(result.explanation.explanation);
    } catch (err) {
      alert(`Failed to explain clause: ${err.message}`);
    }
  };

  const handleAssessRisk = async (clauseText) => {
    try {
      const response = await fetch('/api/v1/documents/assess-risk', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          clause_text: clauseText,
          document_type: analysisData.document_type,
        }),
      });
      
      if (!response.ok) {
        throw new Error(`Failed to assess risk: ${response.statusText}`);
      }
      
      const result = await response.json();
      // In a real implementation, you would display this risk assessment to the user
      alert(result.risk_assessment.assessment);
    } catch (err) {
      alert(`Failed to assess risk: ${err.message}`);
    }
  };

  return (
    <div className="analysis-result">
      <div className="header">
        <h2>Document Analysis Results</h2>
        <button onClick={onBack} className="back-button">Upload Another Document</button>
      </div>
      
      <div className="document-info">
        <h3>Document Information</h3>
        <p><strong>File Name:</strong> {analysisData.filename}</p>
        <p><strong>Document Type:</strong> {analysisData.document_type}</p>
        <p><strong>File Type:</strong> {analysisData.file_type}</p>
      </div>
      
      <div className="tabs">
        <button 
          className={activeTab === 'summary' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('summary')}
        >
          Summary
        </button>
        <button 
          className={activeTab === 'clauses' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('clauses')}
        >
          Clause Analysis
        </button>
        <button 
          className={activeTab === 'ask' ? 'tab active' : 'tab'}
          onClick={() => setActiveTab('ask')}
        >
          Ask Questions
        </button>
      </div>
      
      <div className="tab-content">
        {activeTab === 'summary' && (
          <div className="summary-tab">
            <h3>Document Summary</h3>
            <div className="summary-content">
              {analysisData.analysis.analysis}
            </div>
          </div>
        )}
        
        {activeTab === 'clauses' && (
          <div className="clauses-tab">
            <h3>Clause Analysis</h3>
            <p>Click on any clause to get an explanation or risk assessment.</p>
            <div className="clauses-content">
              {/* In a real implementation, you would parse the analysis and display individual clauses */}
              <div className="clause-item">
                <div className="clause-text">
                  {analysisData.extracted_text.substring(0, 200)}...
                </div>
                <div className="clause-actions">
                  <button onClick={() => handleExplainClause(analysisData.extracted_text.substring(0, 200))}>
                    Explain Clause
                  </button>
                  <button onClick={() => handleAssessRisk(analysisData.extracted_text.substring(0, 200))}>
                    Assess Risk
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
        
        {activeTab === 'ask' && (
          <div className="ask-tab">
            <h3>Ask Questions About This Document</h3>
            <form onSubmit={handleAskQuestion} className="ask-form">
              <div className="form-group">
                <label htmlFor="question">Your Question:</label>
                <textarea
                  id="question"
                  value={question}
                  onChange={(e) => setQuestion(e.target.value)}
                  placeholder="Enter your question about the document..."
                  rows="4"
                  disabled={isAsking}
                />
              </div>
              
              {askError && <div className="error-message">{askError}</div>}
              
              <button 
                type="submit" 
                disabled={isAsking || !question.trim()}
                className="ask-button"
              >
                {isAsking ? 'Getting Answer...' : 'Ask Question'}
              </button>
            </form>
            
            {answer && (
              <div className="answer-section">
                <h4>Answer:</h4>
                <div className="answer-content">
                  {answer}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default AnalysisResult;