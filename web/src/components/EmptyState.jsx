const SUGGESTIONS = [
  { icon: '📄', title: '概览全库', desc: '这些论文分别讲了什么？' },
  { icon: '🔍', title: '知识检索', desc: '根据我的论文库，裂缝网络连通性如何影响渗透率？' },
  { icon: '💡', title: '纯聊天', desc: '帮我头脑风暴一个论文引言结构' },
  { icon: '📊', title: '状态查询', desc: '知识库里有几篇论文？' },
];

export default function EmptyState({ onSelect }) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[70vh] px-4">
      <div className="text-center mb-8">
        <h1 className="text-2xl font-semibold text-[#0d0d0d] mb-2">Research Assistant</h1>
        <p className="text-sm text-[#8e8e8e]">基于你的 Zotero 论文库 + LLM Wiki 知识层</p>
      </div>

      <div className="grid grid-cols-2 gap-3 max-w-[560px] w-full">
        {SUGGESTIONS.map((s, i) => (
          <button key={i}
            onClick={() => onSelect(s.desc)}
            className="text-left p-4 rounded-xl border border-[#e5e5e5] hover:bg-[#f9f9f9] transition-colors group">
            <div className="text-lg mb-1">{s.icon}</div>
            <div className="text-sm font-medium text-[#0d0d0d]">{s.title}</div>
            <div className="text-xs text-[#8e8e8e] mt-0.5 line-clamp-2">{s.desc}</div>
          </button>
        ))}
      </div>
    </div>
  );
}
