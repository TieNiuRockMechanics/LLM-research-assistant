import { useState } from 'react';

const GROUP_ORDER = ['wiki_aggregate', 'wiki_paper_page', 'paper_evidence', 'wiki_other'];
const GROUP_TITLES = { wiki_aggregate: '概念与方法', wiki_paper_page: '论文解读', paper_evidence: '原文验证', wiki_other: '补充线索' };
const ROUTE_LABELS = { chat: '直接对话', knowledge: '参考知识库', status: '本地状态' };

function groupKey(item) {
  if (item.type === 'wiki') return item.source_group || item.wiki_layer || 'wiki_other';
  return item.source_group || 'paper_evidence';
}

function simpleMarkdown(text) {
  // Light markdown → HTML for display
  let html = text
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/^### (.+)$/gm, '<h3>$1</h3>')
    .replace(/^## (.+)$/gm, '<h2>$1</h2>')
    .replace(/^# (.+)$/gm, '<h1>$1</h1>')
    .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.+?)\*/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/^- (.+)$/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>\n?)+/g, '<ul>$&</ul>')
    .replace(/\n\n/g, '</p><p>')
    .replace(/\n/g, '<br/>');
  return '<p>' + html + '</p>';
}

export default function Message({ message }) {
  const [showSources, setShowSources] = useState(false);
  const isUser = message.role === 'user';
  const isError = message.error;

  const aiColor = isError ? '#e74c3c'
    : (message.route === 'knowledge' || message.contextCount > 0) ? '#f0a030'
    : '#10a37f';

  return (
    <div className={`flex py-3 animate-fade-in ${isUser ? 'justify-end' : ''}`}>
      {/* Avatar */}
      <div className="w-7 h-7 rounded-full flex items-center justify-center shrink-0 text-xs font-semibold mr-3 text-white"
        style={{ background: isUser ? '#6c5ce7' : aiColor, order: isUser ? 2 : 0, marginLeft: isUser ? '0.75rem' : 0, marginRight: isUser ? 0 : '0.75rem' }}>
        {isUser ? 'U' : 'AI'}
      </div>

      {/* Content */}
      <div className={`min-w-0 ${isUser ? 'text-right' : 'flex-1'}`}>
        {!isUser && !isError && message.route && (
          <div className="flex items-center gap-1.5 mb-1">
            <span className={`w-1.5 h-1.5 rounded-full ${message.route === 'chat' ? 'bg-[#10a37f]' : 'bg-[#f0a030]'}`} />
            <span className="text-xs text-[#8e8e8e]">
              {message.route === 'knowledge' || message.contextCount > 0 ? '已参考本地 Wiki 或论文数据库' : 'DeepSeek 直接回答'}
              {' · '}{ROUTE_LABELS[message.route] || ''}
              {message.contextCount > 0 ? ` · ${message.contextCount} 上下文` : ''}
            </span>
          </div>
        )}

        {isUser ? (
          <div className="inline-block max-w-[85%] bg-[#f4f4f4] rounded-2xl px-4 py-2.5 text-[0.938rem] text-left text-[#0d0d0d]">
            {message.content}
          </div>
        ) : (
          <div className={`message-content ${isError ? 'text-red-600' : ''}`}
            dangerouslySetInnerHTML={{ __html: simpleMarkdown(message.content) }} />
        )}

        {/* Sources */}
        {!isUser && message.sourceItems && message.sourceItems.length > 0 && (
          <div className="mt-2">
            <button onClick={() => setShowSources(!showSources)}
              className="text-xs text-[#8e8e8e] hover:text-[#5d5d5d] transition-colors">
              {showSources ? '收起来源 ▴' : `查看来源 (${message.sourceItems.length}) ▾`}
            </button>
            {showSources && (
              <div className="mt-2 border border-[#e5e5e5] rounded-lg p-3 bg-[#fafafa]">
                {GROUP_ORDER.map(group => {
                  const items = message.sourceItems
                    .map((it, i) => ({ ...it, _idx: i + 1 }))
                    .filter(it => groupKey(it) === group);
                  if (!items.length) return null;
                  return (
                    <div key={group} className="mb-2 last:mb-0">
                      <div className="text-xs font-medium text-[#5d5d5d] mb-1">{GROUP_TITLES[group]}</div>
                      {items.map(it => (
                        <div key={it._idx} className="text-xs text-[#5d5d5d] ml-2 mb-1">
                          <div className="leading-relaxed">{it._idx}. <span className="font-medium">{it.label}</span>
                          {it.heading && <span className="text-[#8e8e8e]"> · {it.heading}</span>}
                          {it.retrieval_method && <span className="text-[#8e8e8e]"> · {it.retrieval_method}</span>}
                          {it.obsidian_uri && (
                            <a href={it.obsidian_uri} target="_blank" rel="noreferrer"
                              className="ml-2 text-[#10a37f] hover:underline">Obsidian</a>
                          )}
                          {it.pdf_uri && (
                            <a href={it.pdf_uri} target="_blank" rel="noreferrer"
                              className="ml-1 text-[#e74c3c] hover:underline font-medium">PDF</a>
                          )}</div>
                          {it.papers_referenced && it.papers_referenced.length > 0 && (
                            <div className="ml-3 mt-0.5">
                              {it.papers_referenced.map((ref, ri) => (
                                <div key={ri} className="text-[#5d5d5d] leading-relaxed">
                                  ↳ <span className="font-medium">{ref.title}</span>
                                  {ref.obsidian_uri && (
                                    <a href={ref.obsidian_uri} target="_blank" rel="noreferrer"
                                      className="ml-2 text-[#10a37f] hover:underline">Obsidian</a>
                                  )}
                                  {ref.pdf_uri && (
                                    <a href={ref.pdf_uri} target="_blank" rel="noreferrer"
                                      className="ml-1 text-[#e74c3c] hover:underline font-medium">PDF</a>
                                  )}
                                </div>
                              ))}
                            </div>
                          )}
                        </div>
                      ))}
                    </div>
                  );
                })}
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
