import React from 'react';

const ContextProviderGemini = ({ createChatBotMessage, setState, children }) => {
  const handleInput = (answer) => {
    const botMessage = createChatBotMessage(answer);

    setState((prev) => ({
      ...prev,
      messages: [...prev.messages, botMessage],
    }));
  };

  return (
    <div>
      {React.Children.map(children, (child) => {
        return React.cloneElement(child, {
          actions: {
            handleInput: handleInput,
          },
        });
      })}
    </div>
  );
};

export default ContextProviderGemini;