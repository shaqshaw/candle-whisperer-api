import React from "react";
import { Link } from "react-router-dom";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const Index = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-background">
      <Card className="max-w-xl w-full text-center p-0 shadow-lg">
        <CardHeader>
          <CardTitle className="text-3xl md:text-4xl mb-2">
            Deploy Bayesian CRNN Trading Model with Monte Carlo Dropout on Lovable.dev
          </CardTitle>
          <CardDescription className="text-base md:text-lg">
            <strong>Goal:</strong> Build a machine learning API that accepts candlestick pattern image sequences and returns class predictions along with uncertainty, using a Bayesian CRNN model with Monte Carlo Dropout and quantum layers (TFQ).
          </CardDescription>
        </CardHeader>
        <CardContent className="flex flex-col items-center mt-4">
          <Button asChild size="lg" className="px-8 py-3">
            <Link to="/docs">View API Documentation</Link>
          </Button>
        </CardContent>
      </Card>
    </div>
  );
};

export default Index;
