import { createChatBotMessage } from 'react-chatbot-kit';

const config = { 
  botName: "InnovaBot",
  initialMessages: [createChatBotMessage("Olá! Sou o InnovaBot, como posso ajudar você?")],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#ff914d",
    },
    chatButton: {
      backgroundColor: "#3858FF",
    },
  },
}

export default config