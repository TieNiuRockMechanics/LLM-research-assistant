import { useState, useEffect, useCallback } from 'react';
import Sidebar from './components/Sidebar';
import ChatArea from './components/ChatArea';
import * as api from './api';

export default function App() {
  const [conversations, setConversations] = useState([]);
  const [activeConv, setActiveConv] = useState(null);
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [knowledgeMode, setKnowledgeMode] = useState('auto');
  const [model, setModel] = useState('deepseek/deepseek-v4-flash');
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const refreshConversations = useCallback(async () => {
    try { setConversations(await api.listConversations()); } catch {}
  }, []);

  useEffect(() => { refreshConversations(); }, [refreshConversations]);

  const newChat = () => { setActiveConv(null); setMessages([]); };

  const selectConversation = async (id) => {
    try {
      const data = await api.getConversation(id);
      setActiveConv(data); setMessages(data.messages || []);
    } catch { refreshConversations(); }
  };

  const deleteConv = async (id) => {
    await api.deleteConversation(id);
    if (activeConv?.id === id) newChat();
    refreshConversations();
  };

  const sendMessage = async (question) => {
    const userMsg = { role: 'user', content: question };
    const msgs = [...messages, userMsg];
    setMessages(msgs); setLoading(true);
    try {
      const data = await api.sendMessage(question, knowledgeMode, model);
      const assistantMsg = {
        role: 'assistant', content: data.answer, route: data.route,
        contextCount: data.context_count, sourceItems: data.source_items,
        references: data.references, retrieval: data.retrieval,
      };
      const updated = [...msgs, assistantMsg];
      setMessages(updated); setLoading(false);
      const convId = activeConv?.id || `conv_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
      if (!activeConv?.id) setActiveConv({ id: convId, title: question.slice(0, 60), messages: updated });
      await api.saveConversation(convId, updated);
      refreshConversations();
    } catch (err) {
      setMessages([...msgs, { role: 'assistant', content: `请求失败：${err.message}`, error: true }]);
      setLoading(false);
    }
  };

  return (
    <div className="flex h-full bg-white">
      <Sidebar open={sidebarOpen} onToggle={() => setSidebarOpen(!sidebarOpen)}
        conversations={conversations} activeId={activeConv?.id}
        onNewChat={newChat} onSelect={selectConversation} onDelete={deleteConv}
        knowledgeMode={knowledgeMode} onKnowledgeModeChange={setKnowledgeMode} />
      <ChatArea messages={messages} loading={loading} onSend={sendMessage}
        model={model} onModelChange={setModel} sidebarOpen={sidebarOpen} />
    </div>
  );
}
