import React from 'react';
import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL; 
const MessangerGemini = ({ children, actions }) => {
  const parse = async (message) => {
    try {
      const response = await axios.post(`${API_URL}/gemini_ask`, { "question": message });
      actions.handleInput(response.data.answer);
    } catch (error) {
      console.error("Error fetching answer:", error);
    }
  }
  
  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          parse: parse,
          actions,
        });
      })}
    </div>
  );
};
  
export default MessangerGemini;