export default function Sidebar({ open, onToggle, conversations, activeId, onNewChat, onSelect, onDelete, knowledgeMode, onKnowledgeModeChange }) {
  if (!open) {
    return (
      <div className="flex flex-col items-center pt-3 px-2 bg-[#f9f9f9] border-r border-[#e5e5e5] w-12 shrink-0">
        <button onClick={onToggle} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-[#ececec] text-[#5d5d5d] text-sm" title="展开侧栏">☰</button>
        <button onClick={onNewChat} className="mt-2 w-8 h-8 flex items-center justify-center rounded-lg hover:bg-[#ececec] text-[#5d5d5d]" title="新对话">＋</button>
      </div>
    );
  }

  return (
    <div className="flex flex-col bg-[#f9f9f9] border-r border-[#e5e5e5] w-[260px] shrink-0 h-full">
      {/* Header */}
      <div className="flex items-center justify-between px-3 pt-3 pb-2">
        <button onClick={onToggle} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-[#ececec] text-[#5d5d5d]" title="收起侧栏">☰</button>
        <span className="text-sm font-semibold text-[#0d0d0d]">Research Assistant</span>
        <button onClick={onNewChat} className="w-8 h-8 flex items-center justify-center rounded-lg hover:bg-[#ececec] text-[#5d5d5d] text-lg" title="新对话">＋</button>
      </div>

      {/* New chat button */}
      <div className="px-3 pb-2">
        <button onClick={onNewChat}
          className="w-full text-left text-sm px-3 py-2 rounded-lg border border-[#e5e5e5] bg-white hover:bg-[#ececec] text-[#0d0d0d] transition-colors">
          ＋ 新对话
        </button>
      </div>

      {/* Conversation list */}
      <div className="flex-1 overflow-y-auto px-2">
        <div className="text-xs text-[#8e8e8e] px-2 py-2 font-medium">对话历史</div>
        {conversations.map(c => (
          <div key={c.id}
            onClick={() => onSelect(c.id)}
            className={`group flex items-center px-2 py-2 rounded-lg cursor-pointer text-sm mx-1 transition-colors ${
              c.id === activeId ? 'bg-[#ececec]' : 'hover:bg-[#ececec]'
            }`}>
            <span className="flex-1 truncate text-[#0d0d0d]">{c.title || '未命名对话'}</span>
            <button onClick={(e) => { e.stopPropagation(); onDelete(c.id); }}
              className="w-6 h-6 hidden group-hover:flex items-center justify-center rounded text-[#8e8e8e] hover:text-[#0d0d0d] text-xs shrink-0">
              ✕
            </button>
          </div>
        ))}
        {conversations.length === 0 && (
          <div className="text-xs text-[#8e8e8e] px-3 py-4 text-center">暂无对话历史</div>
        )}
      </div>

      {/* Settings */}
      <div className="px-3 py-3 border-t border-[#e5e5e5]">
        <div className="text-xs text-[#8e8e8e] mb-1.5 font-medium">知识库模式</div>
        <div className="flex gap-1 bg-[#e5e5e5] rounded-lg p-0.5">
          {['auto', 'always', 'never'].map(mode => (
            <button key={mode}
              onClick={() => onKnowledgeModeChange(mode)}
              className={`flex-1 text-xs py-1 rounded-md transition-colors ${
                knowledgeMode === mode ? 'bg-white text-[#0d0d0d] shadow-sm' : 'text-[#5d5d5d] hover:text-[#0d0d0d]'
              }`}>
              {{ auto: '自动', always: '总是参考', never: '不使用' }[mode]}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
