import { createChatBotMessage } from 'react-chatbot-kit';

const config = { 
  botName: "InnovaBot",
  initialMessages: [createChatBotMessage("Olá! Sou o InnovaBot, como posso ajudar você?")],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#376B7E",
    },
    chatButton: {
      backgroundColor: "#376B7E",
    },
  },
}

export default config