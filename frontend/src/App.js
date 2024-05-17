import React, { useState } from "react";
import axios from "axios";

function App() {
    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState("");

    const API_URL = process.env.REACT_APP_API_URL; 

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(`${API_URL}/ask`, { question });
            setAnswer(response.data.answer);
        } catch (error) {
            console.error("Error fetching answer:", error);
        }
    };

    return (
        <div className="App">
            <h1>Assistente Conversacional</h1>
            <form onSubmit={handleSubmit}>
                <input 
                    type="text" 
                    value={question} 
                    onChange={(e) => setQuestion(e.target.value)} 
                    placeholder="Faça sua pergunta..." 
                />
                <button type="submit">Perguntar</button>
            </form>
            {answer && (
                <div>
                    <h2>Resposta:</h2>
                    <p>{answer}</p>
                </div>
            )}
        </div>
    );
}

export default App;