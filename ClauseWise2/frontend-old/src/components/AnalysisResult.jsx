// frontend/src/components/AnalysisResult.jsx
import React from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

function AnalysisResult({ analysisData, onBack }) {
  return (
    <Card className="max-w-3xl mx-auto mt-10 shadow-lg rounded-2xl">
      <CardHeader>
        <CardTitle className="text-xl font-semibold text-center">
          Analysis Result
        </CardTitle>
      </CardHeader>
      <CardContent>
        <pre className="bg-gray-100 p-4 rounded-lg text-sm overflow-auto max-h-[400px]">
          {JSON.stringify(analysisData, null, 2)}
        </pre>
        <div className="flex justify-center mt-4">
          <Button onClick={onBack} variant="outline">
            Back
          </Button>
        </div>
      </CardContent>
    </Card>
  );
}

export default AnalysisResult;

