import React from 'react';
import Chatbot from 'react-chatbot-kit'
import './App.css';
import 'react-chatbot-kit/build/main.css'

import ContextProvider from './ContextProvider'
import Messanger from './Messanger';
import config from './config';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <Chatbot config={config} actionProvider={ContextProvider} messageParser={Messanger} />
                <Chatbot config={config} actionProvider={ContextProvider} messageParser={Messanger} />
            </header>
        </div>
    );
}

export default App;