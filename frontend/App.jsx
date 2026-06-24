import React,{ useState } from "react";

function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState("");

  async function generate() {
   const res = await fetch(
  "https://ai-app-compiler-backend-rlka.onrender.com/generate",
  {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          prompt
        })
      }
    );

    const data = await res.json();

    setResult(
      JSON.stringify(data, null, 2)
    );
  }

  return (
    <div>
      <h1>AI App Compiler</h1>

      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <br />

      <button onClick={generate}>
        Generate
      </button>

      <pre>{result}</pre>
    </div>
  );
}

export default App;
