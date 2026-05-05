import { useState, useRef, useEffect } from 'react';
import Message from './Message';
import EmptyState from './EmptyState';

const MODEL_OPTIONS = {
  'deepseek/deepseek-v4-flash': 'DeepSeek V4 Flash',
  'deepseek/deepseek-v4-pro': 'DeepSeek V4 Pro',
  'mimo/mimo-v2.5-pro': 'MiMo V2.5 Pro',
};

export default function ChatArea({ messages, loading, onSend, model, onModelChange, sidebarOpen }) {
  const [input, setInput] = useState('');
  const bottomRef = useRef(null);
  const inputRef = useRef(null);

  useEffect(() => { bottomRef.current?.scrollIntoView({ behavior: 'smooth' }); }, [messages, loading]);

  useEffect(() => {
    if (!loading) inputRef.current?.focus();
  }, [loading]);

  const handleSend = () => {
    const q = input.trim();
    if (!q || loading) return;
    setInput('');
    onSend(q);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSend(); }
  };

  const handleInput = (e) => {
    setInput(e.target.value);
    // Auto-resize
    const el = e.target;
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 200) + 'px';
  };

  return (
    <div className="flex-1 flex flex-col min-w-0 bg-white">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto">
        {messages.length === 0 ? (
          <EmptyState onSelect={onSend} />
        ) : (
          <div className="max-w-[768px] mx-auto px-4 md:px-6">
            {messages.map((msg, i) => (
              <Message key={i} message={msg} />
            ))}
            {loading && (
              <div className="flex py-3 animate-fade-in">
                <div className="w-7 h-7 rounded-full flex items-center justify-center shrink-0 text-xs font-semibold mr-3 text-white bg-[#10a37f]">AI</div>
                <div className="flex items-center gap-2">
                  <div className="spinner" />
                  <span className="text-sm text-[#8e8e8e]">思考中…</span>
                </div>
              </div>
            )}
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      {/* Input area */}
      <div className="sticky bottom-0 bg-gradient-to-t from-white via-white to-transparent pt-2 pb-4">
        <div className="max-w-[768px] mx-auto px-4 md:px-6">
          {/* Model selector row */}
          <div className="flex justify-center mb-2">
            <select
              value={model}
              onChange={(e) => onModelChange(e.target.value)}
              className="model-select"
            >
              {Object.entries(MODEL_OPTIONS).map(([k, v]) => (
                <option key={k} value={k}>{v}</option>
              ))}
            </select>
          </div>

          {/* Input box */}
          <div className="relative flex items-end border border-[#d9d9d9] rounded-[28px] bg-white shadow-sm focus-within:border-[#999] focus-within:shadow-[0_0_0_1px_rgba(0,0,0,0.04)] transition-shadow">
            <textarea
              ref={inputRef}
              value={input}
              onChange={handleInput}
              onKeyDown={handleKeyDown}
              placeholder="输入研究问题…"
              rows={1}
              className="chat-input flex-1 bg-transparent px-5 py-3 text-[0.938rem] text-[#0d0d0d] placeholder-[#8e8e8e]"
              disabled={loading}
            />
            <button
              onClick={handleSend}
              disabled={!input.trim() || loading}
              className={`w-9 h-9 rounded-full flex items-center justify-center mr-2 mb-1.5 shrink-0 transition-colors ${
                input.trim() && !loading ? 'bg-[#0d0d0d] text-white hover:bg-[#333]' : 'bg-[#e5e5e5] text-[#8e8e8e]'
              }`}
            >
              {loading ? <div className="spinner" style={{ borderTopColor: '#5d5d5d', borderColor: '#e5e5e5' }} /> : '↑'}
            </button>
          </div>

          <div className="text-center text-[0.68rem] text-[#8e8e8e] mt-2">
            Research Assistant — 基于你的 Zotero 论文库
          </div>
        </div>
      </div>
    </div>
  );
}
