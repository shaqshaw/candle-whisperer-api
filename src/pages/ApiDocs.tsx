import React from "react";

const ApiDocs = () => (
  <div className="max-w-2xl mx-auto p-8">
    <h1 className="text-3xl font-bold mb-4">Candle Whisperer API Docs</h1>
    <h2 className="text-xl font-semibold mt-6 mb-2">Getting Started</h2>
    <ol className="list-decimal ml-6 mb-6">
      <li className="mb-2">
        <strong>Start the backend server:</strong>
        <pre className="bg-gray-100 p-2 rounded text-sm overflow-x-auto mb-2">
{`cd backend
uvicorn main:app --reload`}
        </pre>
        The API will be available at <code>http://localhost:8000</code>.
      </li>
      <li className="mb-2">
        <strong>Start the frontend app:</strong>
        <pre className="bg-gray-100 p-2 rounded text-sm overflow-x-auto mb-2">
{`npm install
npm run dev`}
        </pre>
        The UI will be available at <code>http://localhost:8080</code> (or the port shown in your terminal).
      </li>
      <li className="mb-2">
        <strong>View these API docs:</strong> Open <code>http://localhost:8080/docs</code> in your browser.
      </li>
    </ol>
    <h2 className="text-xl font-semibold mt-6 mb-2">How to Connect to the API</h2>
    <p className="mb-4">
      You can connect to the backend API using any HTTP client (curl, Postman, your frontend app, etc.).
      The base URL is <code>http://localhost:8000</code>.
    </p>
    <h2 className="text-xl font-semibold mt-6 mb-2">Endpoints</h2>
    <div className="mb-4">
      <strong>POST /predict</strong>
      <pre className="bg-gray-100 p-2 rounded text-sm overflow-x-auto">
{`curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"input_data": "test value"}'`}
      </pre>
      <p>Returns a prediction based on the input data.</p>
    </div>
    <div className="mb-4">
      <strong>GET /trade</strong>
      <pre className="bg-gray-100 p-2 rounded text-sm overflow-x-auto">
{`curl http://localhost:8000/trade`}
      </pre>
      <p>Returns a mock trade object.</p>
    </div>
    <h2 className="text-xl font-semibold mt-6 mb-2">Interactive API Docs</h2>
    <p>
      For interactive API docs and live testing, visit{' '}
      <a href="http://localhost:8000/docs" className="text-blue-600 underline" target="_blank" rel="noopener noreferrer">http://localhost:8000/docs</a>{' '}
      (provided by FastAPI backend).
    </p>
  </div>
);

export default ApiDocs; 