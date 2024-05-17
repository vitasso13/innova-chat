import React from 'react';
import Chatbot from 'react-chatbot-kit'
import './App.css';
import 'react-chatbot-kit/build/main.css'

import ContextProvider from './ContextProvider'
import ContextProviderGemini from './ContextProviderGemini'
import Messanger from './Messanger';
import MessangerGemini from './MessangerGemini';
import config from './config';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                {/* <Chatbot headerText='Innova Bot | Transformers' config={config} actionProvider={ContextProvider} messageParser={Messanger} /> */}
                <Chatbot headerText='Innova Bot | Gemini' config={config} actionProvider={ContextProviderGemini} messageParser={MessangerGemini}/>
            </header>
        </div>
    );
}

export default App;